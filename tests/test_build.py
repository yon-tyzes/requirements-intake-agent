"""Tests for scripts/build.py."""

from __future__ import annotations

import importlib.util
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
