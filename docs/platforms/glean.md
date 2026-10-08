# Deploying on Glean

Glean suits this agent because it already indexes your documents and respects each user's permissions. The related-work step uses Glean's company search directly.

There are two ways to set it up. Both start with `make build`.

## Before you start

- Confirm that completed intakes are indexed in Glean, and note the folder or datasource they live in.
- Confirm that requesters can see those intakes. The agent searches as the person running it, so it cannot find documents that person cannot open.
- Ask your Glean admin whether agent creation is open to you and which models your instance allows.

## Option A: Agent Builder

Best for a first pilot.

1. Run `make build`.
2. In Glean, open the Agent Library and select **Create agent**.
3. Switch to manual editing and add a single step that takes the user's message as input and responds.
4. Paste the contents of `dist/instructions.md` into that step's instructions.
5. Restrict the step's company search to the folder or datasource that holds completed intakes.
6. Name the agent to match `name` in `config/agent.yaml` and save it as a draft.
7. Run the sample in `examples/logistics-feed-change/input.md` and compare the result with `expected-output.md`.

Glean's builder can also split the work across several steps. A useful split, once the single step works:

| Step | Job |
| --- | --- |
| 1 | Steps 1 to 5 of the instructions: sources, summaries, request type, sections, quality checks |
| 2 | Company search for related intakes |
| 3 | Clarifying questions and final output |

Splitting makes each step easier to test, at the cost of more setup.

## Option B: Import the specification package

Best once the agent is stable and you want it under version control.

`make build` writes `dist/<agent-name>-glean.zip`. The archive holds one folder with `spec.yaml` and `instructions.md`, which follows the Glean agent specification format. Your Glean developer can send it to the agent import endpoint in the Glean Client API.

The build sets these `spec.yaml` fields from `config/agent.yaml`:

| Field | Source |
| --- | --- |
| `id` | `glean.id`, or a new ID on first build |
| `name`, `description` | `name`, `description` |
| `instructionFile` | always `instructions.md` |
| `gleanSearchConfig` | `glean.search_urls` and `glean.datasource_instances`; empty means search everything the user can see |

On the first build, copy the printed ID into `glean.id`. Later imports with the same ID update the agent instead of creating a copy.

Glean caps instruction files at 32,000 characters. The build stops with a message if your configuration goes over.

Check field names against the current specification in Glean's developer documentation before your first import. The format is new and may change.

## Costs

Agent usage is normally part of your Glean license. Ask your admin whether your plan meters agent runs or premium models.

## Updating

Edit `config/`, run `make build`, and either paste the new instructions into the step or reimport the package. Rerun your evaluation set before you publish the change.
