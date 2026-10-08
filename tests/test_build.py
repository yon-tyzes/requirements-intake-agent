"""Tests for scripts/build.py."""

from __future__ import annotations

import importlib.util
import re
import shutil
import sys
import zipfile
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("build", ROOT / "scripts" / "build.py")
build = importlib.util.module_from_spec(SPEC)
sys.modules["build"] = build
SPEC.loader.exec_module(build)

OUTPUT_PARTS = [
    "Readiness",
    "Intake draft",
    "Quality flags",
    "Missing information",
    "Clarifying questions",
    "Related prior work",
    "Source summary",
]
READINESS = re.compile(
    r"^Readiness: (Ready to submit|Needs answers|Blocked)\. Type: .+? \((?:source|inferred)\)\. "
    r"(\d+) of (\d+) sections ready, (\d+) need answers, (\d+) blockers\.$",
    flags=re.MULTILINE,
)


@pytest.fixture()
def config_dir(tmp_path: Path) -> Path:
    target = tmp_path / "config"
    shutil.copytree(ROOT / "config", target)
    return target


def edit(path: Path, change) -> None:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    change(data)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def render_default(config_dir: Path) -> str:
    config = build.load_config(config_dir)
    template = (ROOT / "agent" / "instructions.md").read_text(encoding="utf-8")
    return build.render(template, config)


def test_default_config_is_valid() -> None:
    build.load_config(ROOT / "config")


def test_render_resolves_every_token(config_dir: Path) -> None:
    rendered = render_default(config_dir)
    assert "{{" not in rendered and "}}" not in rendered


def test_render_includes_enabled_entries(config_dir: Path) -> None:
    config = build.load_config(config_dir)
    rendered = render_default(config_dir)
    for section in config.sections:
        assert section["label"] in rendered
    for check in config.checks:
        assert check["label"] in rendered
    for topic in config.topics:
        assert topic["label"] in rendered


def test_disabled_entries_are_left_out(config_dir: Path) -> None:
    edit(config_dir / "intake-sections.yaml", lambda d: d["sections"][-1].update(enabled=False))
    label = yaml.safe_load((config_dir / "intake-sections.yaml").read_text())["sections"][-1]["label"]
    assert f"**{label}**" not in render_default(config_dir)


def test_request_types_load() -> None:
    config = build.load_config(ROOT / "config")
    ids = [request_type["id"] for request_type in config.types]
    assert ids == [
        "new-capability",
        "change-existing",
        "defect",
        "data-or-report",
        "compliance-driven",
        "retirement",
    ]


def test_unknown_extra_attention_id_fails(config_dir: Path) -> None:
    edit(config_dir / "request-types.yaml", lambda d: d["types"][0]["extra_attention"].append("no-such-id"))
    with pytest.raises(build.ConfigError, match="unknown extra_attention id 'no-such-id'"):
        build.load_config(config_dir)


def test_disabled_request_type_is_left_out(config_dir: Path) -> None:
    edit(config_dir / "request-types.yaml", lambda d: d["types"][-1].update(enabled=False))
    label = yaml.safe_load((config_dir / "request-types.yaml").read_text())["types"][-1]["label"]
    assert f"**{label}**" not in render_default(config_dir)


def test_request_types_token_resolves(config_dir: Path) -> None:
    rendered = render_default(config_dir)
    assert "{{request_types}}" not in rendered
    assert "- **Change to existing**: " in rendered
    assert "Look closely at: Impacted systems and applications" in rendered


def test_no_enabled_request_types_skips_step(config_dir: Path) -> None:
    edit(config_dir / "request-types.yaml", lambda d: [t.update(enabled=False) for t in d["types"]])
    assert "No request types are configured. Skip this step" in render_default(config_dir)


def test_section_example_is_rendered(config_dir: Path) -> None:
    def set_example(data):
        data["sections"][0]["example"] = "Add a field to the order form by June 1."

    edit(config_dir / "intake-sections.yaml", set_example)
    assert ' Example: "Add a field to the order form by June 1".' in render_default(config_dir)


def test_section_without_example_has_no_example_text(config_dir: Path) -> None:
    edit(config_dir / "intake-sections.yaml", lambda d: [s.pop("example", None) for s in d["sections"]])
    assert "Example: " not in build.render_sections(build.load_config(config_dir).sections)


def test_output_has_seven_parts_in_order(config_dir: Path) -> None:
    rendered = render_default(config_dir)
    positions = [rendered.index(f"### {number}. {name}") for number, name in enumerate(OUTPUT_PARTS, 1)]
    assert positions == sorted(positions)
    assert rendered.rstrip().endswith('"Review the checklist before you submit."')


@pytest.mark.parametrize(
    "example", sorted(p.parent.name for p in (ROOT / "examples").glob("*/expected-output.md"))
)
def test_example_output_is_consistent(example: str) -> None:
    text = (ROOT / "examples" / example / "expected-output.md").read_text(encoding="utf-8")
    headings = re.findall(r"^## (\d)\. (.+)$", text, flags=re.MULTILINE)
    assert headings == [(str(number), name) for number, name in enumerate(OUTPUT_PARTS, 1)]
    assert text.rstrip().endswith("Review the checklist before you submit.")

    match = READINESS.search(text)
    assert match, "missing or malformed Readiness line"
    verdict, ready, total, need, blockers = match.group(1), *map(int, match.group(2, 3, 4, 5))
    sections = [s for s in build.load_config(ROOT / "config").sections if s["enabled"]]
    assert total == len(sections)
    assert ready + need == total

    draft = text.split("## 2. Intake draft")[1].split("## 3. Quality flags")[0]
    bodies = re.split(r"^\*\*(.+?)\*\*", draft, flags=re.MULTILINE)[1:]
    found = {bodies[i]: bodies[i + 1] for i in range(0, len(bodies), 2)}
    assert list(found) == [s["label"] for s in sections]
    needing = [label for label, body in found.items() if "[MISSING]" in body or "[CONFLICT]" in body]
    assert len(needing) == need

    blocker_labels = {
        c["label"] for c in build.load_config(ROOT / "config").checks if c["severity"] == "blocker"
    }
    flags = text.split("## 3. Quality flags")[1].split("## 4.")[0]
    rows = [line.split("|")[1].strip() for line in flags.splitlines() if line.startswith("| ")][1:]
    assert sum(row in blocker_labels for row in rows) == blockers

    expected = "Blocked" if blockers else "Needs answers" if need else "Ready to submit"
    assert verdict == expected


def test_topic_systems_are_listed(config_dir: Path) -> None:
    edit(config_dir / "clarifying-topics.yaml", lambda d: d["topics"][0].update(systems=["Alpha", "Beta"]))
    assert "Systems in this category: Alpha, Beta." in render_default(config_dir)


def test_checks_are_ordered_by_severity(config_dir: Path) -> None:
    config = build.load_config(config_dir)
    rendered = build.render_checks(config.checks)
    severities = [line.split("(")[1].split(")")[0] for line in rendered.splitlines()]
    ranks = [build.SEVERITY_ORDER[s] for s in severities]
    assert ranks == sorted(ranks)


def test_duplicate_ids_fail(config_dir: Path) -> None:
    def duplicate(data):
        data["checks"].append(dict(data["checks"][0]))

    edit(config_dir / "quality-checks.yaml", duplicate)
    with pytest.raises(build.ConfigError, match="duplicate id"):
        build.load_config(config_dir)


def test_schema_errors_name_the_file(config_dir: Path) -> None:
    edit(config_dir / "quality-checks.yaml", lambda d: d["checks"][0].update(severity="urgent"))
    with pytest.raises(build.ConfigError, match="quality-checks.yaml"):
        build.load_config(config_dir)


def test_all_disabled_fails(config_dir: Path) -> None:
    edit(config_dir / "clarifying-topics.yaml", lambda d: [t.update(enabled=False) for t in d["topics"]])
    with pytest.raises(build.ConfigError, match="at least one entry"):
        build.load_config(config_dir)


def test_unknown_template_token_fails(config_dir: Path) -> None:
    config = build.load_config(config_dir)
    with pytest.raises(build.ConfigError, match="unknown value"):
        build.render("{{agent.nonexistent}}", config)


def test_placeholders_are_reported() -> None:
    assert build.find_placeholders({"intake_tool": "<your intake tool>"})
    assert not build.find_placeholders({"intake_tool": "Request Portal"})


def test_strict_mode_fails_on_placeholders(tmp_path: Path) -> None:
    assert build.main(["--strict", "--check", "--out", str(tmp_path / "dist")]) == 1


def test_glean_package(config_dir: Path, tmp_path: Path) -> None:
    out = tmp_path / "dist"
    assert build.main(["--config", str(config_dir), "--out", str(out)]) == 0
    archive = next(out.glob("*-glean.zip"))
    with zipfile.ZipFile(archive) as bundle:
        names = bundle.namelist()
        top_level = {name.split("/")[0] for name in names}
        assert len(top_level) == 1
        folder = top_level.pop()
        assert f"{folder}/spec.yaml" in names
        assert f"{folder}/instructions.md" in names
        spec = yaml.safe_load(bundle.read(f"{folder}/spec.yaml"))
    assert len(spec["id"]) == 32
    assert spec["instructionFile"] == "instructions.md"
    assert spec["gleanSearchConfig"] == {}


def test_glean_search_scope(config_dir: Path) -> None:
    edit(
        config_dir / "agent.yaml",
        lambda d: d["glean"].update(search_urls=["https://example.com/intakes"], id="a" * 32),
    )
    config = build.load_config(config_dir)
    spec = build.glean_spec(config, config.agent["glean"]["id"])
    assert spec["gleanSearchConfig"] == {"urls": ["https://example.com/intakes"]}


def test_glean_length_limit(config_dir: Path, tmp_path: Path) -> None:
    config = build.load_config(config_dir)
    with pytest.raises(build.ConfigError, match="Glean accepts"):
        build.build_glean(config, "x" * (build.GLEAN_INSTRUCTION_LIMIT + 1), tmp_path)
