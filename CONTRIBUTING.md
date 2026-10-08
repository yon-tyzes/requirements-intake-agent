# Contributing

Thanks for helping improve this project. Contributions of every size are welcome, from a typo fix to a new platform guide.

## Before you start

- **Never include real data.** No project names, people, systems, emails, or intake content from your organization in issues, examples, or tests. Use fictional examples like the one in `examples/`.
- For anything larger than a small fix, open an issue first so we can agree on the approach.

## Ways to help

- Report output problems: describe the input pattern (in fictional terms) and what the agent got wrong.
- Suggest quality checks or clarifying questions that would apply to most organizations.
- Add a setup guide for another platform.
- Add a fictional example from a different domain.

## Development setup

```sh
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
make install-dev
make test
```

## Making a change

1. Fork the repository and create a branch from `main`.
2. Make your change. Keep each pull request to one purpose.
3. Run the full check:

   ```sh
   make lint test check
   ```

4. Update `CHANGELOG.md` under **Unreleased**.
5. Open a pull request and fill in the template.

### Changing the instructions

Changes to `agent/instructions.md` affect every user. In the pull request, describe:

- the failure you saw, using a fictional input
- the output before and after your change
- any case in `examples/` that changed as a result

### Changing configuration keys

Renaming or removing a key breaks existing configurations. Update the schema, the build script, the tests, and `docs/customizing.md` together, and note the change under **Changed** in the changelog.

## Style

- Python: formatted and linted with Ruff (`make lint`).
- Markdown: one sentence per idea, plain words, short paragraphs.
- YAML: two-space indent, lowercase-with-dashes IDs.

## Code of conduct

This project follows the [Code of Conduct](CODE_OF_CONDUCT.md). By taking part, you agree to follow it.
