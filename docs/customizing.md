# Customizing

All organization-specific content lives in `config/`. Edit those files, run `make build`, and use the files in `dist/`. Leave `agent/instructions.md` alone unless you want to change how the agent works.

## `agent.yaml`

| Key | What to set |
| --- | --- |
| `name` | The name people see. Keep it plain: "Intake Assistant" over a persona name. |
| `intake_tool` | The form or system where intakes are submitted. |
| `requester_role` | The role that runs the agent, as your teams say it. |
| `analyst_role` | The role that reads the output. |
| `external_party` | What you call the outside organizations that send requests. |
| `prior_intake_location` | Where completed intakes live. Name the library, project, or folder. |
| `max_related_intakes` | How many matches to return. Three is usually enough. |
| `data_handling` | Your rule for personal and account data. Ask your privacy or security team for the wording. |

## `intake-sections.yaml`

Match your intake form. Use the same labels and order as the form so requesters can paste each section without hunting for the field.

- Set `required: false` for fields your form treats as optional.
- Set `enabled: false` to hide a section without losing its text.
- Write `guidance` as an instruction to a new team member: what belongs here, and what does not.

## `quality-checks.yaml`

Start with the defaults. After your first evaluation run, look at the reviewer notes:

- If analysts keep asking the same question the agent missed, add a check for it.
- If a check produces noise, tighten `look_for` or lower its `severity`.

Severity controls order in the output. Blockers are things that stop requirements work. Warnings slow it down. Notes are nice to have.

## `clarifying-topics.yaml`

This file has the largest effect on output quality.

1. **List your systems.** Add the real names of your platforms, jobs, feeds, and applications under `systems` for each topic. The agent uses them to recognize which topics a request touches.
2. **Rewrite the questions in your language.** Replace generic questions with the ones your best analysts actually ask.
3. **Add topics** for system categories that are specific to your organization.

Keep each topic to three to six questions. The agent adapts them to the request; a long list produces long, generic output.

## Checking your changes

```sh
make check    # validates every file against its schema
make build    # writes dist/instructions.md and the Glean package
make strict   # fails if any <placeholder> is still unfilled
```

Then rerun your evaluation set. See [evals/README.md](../evals/README.md).
