# Other platforms

The instructions in `dist/instructions.md` are plain Markdown with no platform-specific syntax. Any assistant that accepts custom instructions and can search your documents can run them.

## Microsoft Copilot Studio

1. Create an agent and paste `dist/instructions.md` into its instructions.
2. Add the library that holds completed intakes as a knowledge source.
3. Test with the sample in `examples/`.

Copilot Studio limits instruction length. If the build output is too long, move the clarifying topics into a knowledge file and replace the `{{clarifying_topics}}` block in `agent/instructions.md` with a line telling the agent to use that file.

## A chat assistant with no company search

Paste `dist/instructions.md` as the system prompt or project instructions. Steps 1 to 4 and 6 work as written. Step 5 will report "No related intakes found" unless the user also pastes past intakes into the conversation.

This setup works for a quick trial. It is not a substitute for the related-work step in daily use.

## Your own application

Call a model API with `dist/instructions.md` as the system prompt and the requester's material as the user message. Add a retrieval step that searches your intake store and passes the top matches into the request.

### Sizing

One run typically uses:

| Part | Approximate size |
| --- | --- |
| Instructions | 3,500 to 4,500 tokens |
| Pasted source material | 2,000 to 15,000 tokens |
| Retrieved prior intakes | 3,000 to 6,000 tokens |
| Response | 2,000 to 4,000 tokens |

Multiply by your provider's current per-token prices and your expected monthly volume. For most teams the model cost is small next to the time spent on follow-up rounds. Security review, data handling approval, and hosting are the larger costs.

### Things to build in

- Log the configuration version and model with every response, so you can trace a bad result.
- Do not store raw source material in logs unless your data policy allows it.
- Rerun the evaluation set when you change models.
