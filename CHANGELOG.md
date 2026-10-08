# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Configuration changes that rename or remove keys are breaking changes and bump the major version.

## [Unreleased]

## [1.0.0] - 2026-10-08

### Added

- Seven-step agent instructions with source tagging and a no-fabrication rule.
- Readiness verdict at the top of every output: `Ready to submit`, `Needs answers`, or `Blocked`, with the request type and section and blocker counts.
- Request type classification step, configured in `config/request-types.yaml` with its own schema. Each type lists the sections and topics to check closely, and the build fails on an unknown ID.
- Optional `example` for each intake section, rendered after its guidance.
- Configuration files for intake sections, quality checks, clarifying-question topics, and request types, each with a JSON Schema.
- Industry-neutral topic names, questions, and section labels, plus a role names by industry table in `docs/customizing.md`.
- Review checklist for requesters in `docs/review-checklist.md`. Every output ends by pointing to it.
- Accepted inputs section in the README and `docs/how-it-works.md`.
- Build script that validates configuration, renders paste-ready instructions, and packages a Glean agent specification.
- Setup guides for Glean, Microsoft Copilot Studio, and custom applications.
- Four worked examples with fictional input and expected output: logistics, healthcare, public sector, and manufacturing, indexed in `examples/README.md`.
- Evaluation method, scoring rubric with a readiness verdict measure, CSV templates, and an embedded-instruction test case in `evals/cases/`.
- Tests that check the build, the request types, the output format, and the consistency of every example.
- Continuous integration.

[Unreleased]: https://github.com/yon-tyzes/requirements-intake-agent/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/yon-tyzes/requirements-intake-agent/releases/tag/v1.0.0
