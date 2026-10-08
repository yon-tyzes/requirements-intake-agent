#!/usr/bin/env python3
"""Validate the configuration and assemble paste-ready agent instructions.

Usage:
    python scripts/build.py            # validate, then write dist/
    python scripts/build.py --check    # validate only
    python scripts/build.py --strict   # also fail on unfilled <placeholders>

Outputs:
    dist/instructions.md                 platform-neutral instructions
    dist/glean/<agent-slug>/             Glean agent specification directory
    dist/<agent-slug>-glean.zip          the same directory, ready to import
"""

from __future__ import annotations

import argparse
import json
import re
import secrets
import shutil
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
GLEAN_INSTRUCTION_LIMIT = 32_000
CONFIG_FILES = {
    "agent": "agent.yaml",
    "sections": "intake-sections.yaml",
    "checks": "quality-checks.yaml",
    "topics": "clarifying-topics.yaml",
}
SCHEMA_FILES = {
    "agent": "agent.schema.json",
    "sections": "intake-sections.schema.json",
    "checks": "quality-checks.schema.json",
    "topics": "clarifying-topics.schema.json",
}
PLACEHOLDER = re.compile(r"<[^<>\n]+>")
TOKEN = re.compile(r"\{\{\s*([a-z_.]+)\s*\}\}")
SEVERITY_ORDER = {"blocker": 0, "warning": 1, "note": 2}


class ConfigError(Exception):
    """Raised when configuration is missing or invalid."""


@dataclass
class Config:
    agent: dict[str, Any]
    sections: list[dict[str, Any]]
    checks: list[dict[str, Any]]
    topics: list[dict[str, Any]]


def load_yaml(path: Path) -> Any:
    if not path.is_file():
        raise ConfigError(f"Missing file: {path}")
    with path.open(encoding="utf-8") as handle:
        try:
            return yaml.safe_load(handle)
        except yaml.YAMLError as exc:
            raise ConfigError(f"{path.name}: invalid YAML ({exc})") from exc


def validate(name: str, data: Any, schema_dir: Path) -> list[str]:
    schema = json.loads((schema_dir / SCHEMA_FILES[name]).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        location = "/".join(str(part) for part in error.path) or "(root)"
        errors.append(f"{CONFIG_FILES[name]} at {location}: {error.message}")
    return errors


def unique_ids(name: str, items: list[dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    errors = []
    for item in items:
        if item["id"] in seen:
            errors.append(f"{CONFIG_FILES[name]}: duplicate id '{item['id']}'")
        seen.add(item["id"])
    return errors


def load_config(config_dir: Path, schema_dir: Path = ROOT / "schema") -> Config:
    raw = {key: load_yaml(config_dir / filename) for key, filename in CONFIG_FILES.items()}
    errors: list[str] = []
    for key, data in raw.items():
        errors.extend(validate(key, data, schema_dir))
    if errors:
        raise ConfigError("\n".join(errors))

    config = Config(
        agent=raw["agent"],
        sections=raw["sections"]["sections"],
        checks=raw["checks"]["checks"],
        topics=raw["topics"]["topics"],
    )
    errors.extend(unique_ids("sections", config.sections))
    errors.extend(unique_ids("checks", config.checks))
    errors.extend(unique_ids("topics", config.topics))
    for name, items in (("sections", config.sections), ("checks", config.checks), ("topics", config.topics)):
        if not any(item["enabled"] for item in items):
            errors.append(f"{CONFIG_FILES[name]}: at least one entry must be enabled")
    if errors:
        raise ConfigError("\n".join(errors))
    return config


def find_placeholders(agent: dict[str, Any]) -> list[str]:
    found = []
    for key, value in agent.items():
        if isinstance(value, str) and PLACEHOLDER.search(value):
            found.append(f"agent.yaml: '{key}' still contains a placeholder: {value}")
    return found


def render_sections(sections: list[dict[str, Any]]) -> str:
    lines = []
    number = 0
    for section in sections:
        if not section["enabled"]:
            continue
        number += 1
        flag = "required" if section["required"] else "optional"
        lines.append(f"{number}. **{section['label']}** ({flag}): {section['guidance'].strip()}")
    return "\n".join(lines)


def render_checks(checks: list[dict[str, Any]]) -> str:
    enabled = [check for check in checks if check["enabled"]]
    enabled.sort(key=lambda check: SEVERITY_ORDER[check["severity"]])
    lines = []
    for check in enabled:
        lines.append(
            f"- **{check['label']}** ({check['severity']}). "
            f"Flag when: {check['look_for'].strip()} Fix: {check['fix'].strip()}"
        )
    return "\n".join(lines)


def render_topics(topics: list[dict[str, Any]]) -> str:
    blocks = []
    for topic in topics:
        if not topic["enabled"]:
            continue
        lines = [f"#### {topic['label']}", "", f"Applies when: {topic['applies_when'].strip()}"]
        systems = topic.get("systems") or []
        if systems:
            lines.append(f"Systems in this category: {', '.join(systems)}.")
        lines.append("")
        lines.append("Starter questions:")
        lines.append("")
        lines.extend(f"- {question.strip()}" for question in topic["questions"])
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def render(template: str, config: Config) -> str:
    values: dict[str, str] = {
        "intake_sections": render_sections(config.sections),
        "quality_checks": render_checks(config.checks),
        "clarifying_topics": render_topics(config.topics),
    }
    for key, value in config.agent.items():
        if isinstance(value, (str, int)):
            values[f"agent.{key}"] = " ".join(str(value).split())

    def substitute(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in values:
            raise ConfigError(f"Template uses unknown value '{{{{{key}}}}}'")
        return values[key]

    rendered = TOKEN.sub(substitute, template)
    return rendered.rstrip() + "\n"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def glean_spec(config: Config, agent_id: str) -> dict[str, Any]:
    glean = config.agent.get("glean") or {}
    search: dict[str, Any] = {}
    if glean.get("datasource_instances"):
        search["datasourceInstances"] = list(glean["datasource_instances"])
    if glean.get("search_urls"):
        search["urls"] = list(glean["search_urls"])
    return {
        "id": agent_id,
        "name": config.agent["name"],
        "description": " ".join(config.agent["description"].split()),
        "instructionFile": "instructions.md",
        "gleanSearchConfig": search,
    }


def build_glean(config: Config, instructions: str, out_dir: Path) -> tuple[Path, str, bool]:
    if len(instructions) > GLEAN_INSTRUCTION_LIMIT:
        raise ConfigError(
            f"Instructions are {len(instructions):,} characters; Glean accepts up to "
            f"{GLEAN_INSTRUCTION_LIMIT:,}. Disable sections, checks, or topics, or shorten them."
        )
    configured_id = (config.agent.get("glean") or {}).get("id") or ""
    agent_id = configured_id or secrets.token_hex(16)
    slug = slugify(config.agent["name"])
    agent_dir = out_dir / "glean" / slug
    agent_dir.mkdir(parents=True)
    (agent_dir / "instructions.md").write_text(instructions, encoding="utf-8")
    spec = yaml.safe_dump(glean_spec(config, agent_id), sort_keys=False, allow_unicode=True)
    (agent_dir / "spec.yaml").write_text(spec, encoding="utf-8")

    archive = out_dir / f"{slug}-glean.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(agent_dir.rglob("*")):
            bundle.write(path, path.relative_to(agent_dir.parent))
    return archive, agent_id, not configured_id


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--config", type=Path, default=ROOT / "config", help="configuration directory")
    parser.add_argument("--template", type=Path, default=ROOT / "agent" / "instructions.md")
    parser.add_argument("--out", type=Path, default=ROOT / "dist", help="output directory")
    parser.add_argument("--check", action="store_true", help="validate without writing output")
    parser.add_argument("--strict", action="store_true", help="fail on unfilled <placeholders>")
    args = parser.parse_args(argv)

    try:
        config = load_config(args.config)
        instructions = render(args.template.read_text(encoding="utf-8"), config)
    except ConfigError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    placeholders = find_placeholders(config.agent)
    for message in placeholders:
        print(f"{'error' if args.strict else 'warning'}: {message}", file=sys.stderr)
    if placeholders and args.strict:
        return 1

    print(f"Configuration is valid. Instructions: {len(instructions):,} characters.")
    if args.check:
        return 0

    if args.out.exists():
        shutil.rmtree(args.out)
    args.out.mkdir(parents=True)
    (args.out / "instructions.md").write_text(instructions, encoding="utf-8")
    print(f"Wrote {args.out / 'instructions.md'}")

    try:
        archive, agent_id, generated = build_glean(config, instructions, args.out)
    except ConfigError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"Wrote {archive}")
    if generated:
        print(f"New Glean agent ID: {agent_id}")
        print("Copy it into config/agent.yaml under glean.id so later imports update this agent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
