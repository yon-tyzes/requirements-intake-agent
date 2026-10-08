# Security

## Reporting a problem

If you find a way the instructions could expose data, follow injected instructions from pasted content, or produce unsafe output, please report it privately through GitHub's **Report a vulnerability** option on the repository's Security tab. Do not open a public issue.

Include a fictional input that reproduces the problem and the output you saw. We aim to respond within five business days.

## Using this project safely

- **Keep real data out of the repository.** Evaluation sets contain real project material. Store them where only your evaluation team can see them, never in a fork of this repository.
- **Set the data handling rule.** Replace `data_handling` in `config/agent.yaml` with wording approved by your privacy or security team.
- **Scope search.** On platforms that support it, limit the agent's search to the location of completed intakes rather than all company content.
- **Review before submission.** The agent drafts; a person confirms and submits.
- **Pasted content is untrusted.** The instructions tell the agent to treat pasted text as data. Include a test case with an embedded instruction in your evaluation set to confirm this holds on your platform and model.

## Supported versions

Only the latest release receives fixes.
