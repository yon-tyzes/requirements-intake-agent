# Requirements Intake Agent

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)

Agent instructions and configuration that turn rough project requests into a complete intake an analyst can act on. Requesters paste emails and notes; the agent returns a structured draft, flags gaps, writes clarifying questions, and links related past work.

Runs on Glean, Microsoft Copilot Studio, or any assistant that accepts custom instructions.

## The problem it addresses

Requirements work slows down when intakes arrive incomplete. A request names a fix but not the outcome. Testing is marked "yes" with no tester. Two emails give different dates. Analysts find the gaps one follow-up at a time, and scope shifts while requirements are already underway.

This agent moves gap-finding to the moment the request is written down.

## What you get back

For every request, the agent returns six parts:

1. **Intake draft**, section by section, ready to paste into your intake form. Every entry carries a tag: `[SOURCE]`, `[INFERRED]`, `[PRIOR]`, `[MISSING]`, or `[CONFLICT]`.
2. **Quality flags**, such as vague actions, unnamed systems, missing dates, and testing with no owner.
3. **Missing information**, as numbered questions for the requester.
4. **Clarifying questions** an analyst would ask, grouped by system category and marked internal or external.
5. **Related prior work**: similar completed intakes, with links and the details they recorded that this request lacks.
6. **Source summary** of each email and note.

See a full worked example in [`examples/logistics-feed-change`](examples/logistics-feed-change).

## Quick start

Requires Python 3.10 or later.

```sh
git clone <this repository>
cd requirements-intake-agent
make install       # installs PyYAML and jsonschema
```

1. Edit the four files in [`config/`](config) to match your intake form, your systems, and your team's language. Start with [`agent.yaml`](config/agent.yaml).
2. Build:

   ```sh
   make build
   ```

3. Use the output:
   - `dist/instructions.md`: paste into your platform's agent instructions.
   - `dist/<agent-name>-glean.zip`: a Glean agent specification package for import.
4. Test it on 10 to 20 past intakes before anyone relies on it. See [`evals/`](evals).

Without Python, you can still use the agent: copy [`agent/instructions.md`](agent/instructions.md) and replace each `{{...}}` placeholder by hand using the YAML files.

## Repository layout

```text
agent/instructions.md          instruction logic, with placeholders
config/
  agent.yaml                   names, roles, data rules, platform settings
  intake-sections.yaml         sections of your intake form
  quality-checks.yaml          checks the agent runs on its own draft
  clarifying-topics.yaml       system categories and starter questions
schema/                        JSON Schema for each config file
scripts/build.py               validates config and renders dist/
docs/
  how-it-works.md              the six steps and the reasoning behind them
  customizing.md               how to fit the config to your organization
  platforms/                   setup for Glean and other platforms
examples/                      fictional input with expected output
evals/                         evaluation method, rubric, and templates
tests/                         tests for the build script
```

## Documentation

- [How it works](docs/how-it-works.md)
- [Customizing](docs/customizing.md)
- [Deploying on Glean](docs/platforms/glean.md)
- [Other platforms and cost sizing](docs/platforms/other-platforms.md)
- [Evaluating the agent](evals/README.md)

## Limitations

- **A person reviews every draft.** The agent drafts and asks; it does not confirm facts or submit intakes.
- **Related work depends on search.** The agent can only find completed intakes that your platform indexes and the user can open.
- **Output is copy and paste.** Most intake tools do not accept writes from an assistant.
- **Results vary by model.** Rerun your evaluation set when the platform changes models.

## Contributing

Issues and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first. Please never include real project data, names, or system details from your organization in an issue or pull request.

## License

[MIT](LICENSE). If you use this in published work, see [CITATION.cff](CITATION.cff).
