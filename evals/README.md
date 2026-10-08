# Evaluating the agent

Test the agent on past requests before anyone relies on it. The method below replays real intakes with no help from the requester and compares the agent's draft with what the analysts actually ended up needing.

## 1. Build a golden set

Pick 10 to 20 completed intakes. For each one you need:

- **The raw material** the requester started with: emails, notes, attachments.
- **The final intake** as approved, after all follow-up.
- **The follow-up record**: questions analysts asked after the intake was submitted, and any scope changes during requirements.

Mix easy and hard cases. Include at least two requests that changed scope during requirements, two with an outside party testing, and one that turned out to be a duplicate.

Record each case in a copy of [`golden-set-template.csv`](golden-set-template.csv). Store the set where only the evaluation team can see it. It contains real project data, so keep it out of this repository.

## 2. Run the agent cold

For each case, paste only the raw material into the agent. Do not add context, answer its questions, or correct it. This shows what the agent does alone, which is the condition that matters most in daily use.

Save every response with the date, the configuration version, and the model the platform used.

## 3. Score each response

Score with [`rubric.md`](rubric.md). Two reviewers should score the first five cases independently, then compare scores and agree on how to apply the rubric before splitting the rest.

Record scores in [`scoring-sheet-template.csv`](scoring-sheet-template.csv).

## 4. Decide

Suggested release thresholds:

| Measure | Threshold |
| --- | --- |
| Fabricated facts | 0 across the whole set |
| Gap recall | At least 70 percent of real follow-up questions caught |
| Section accuracy | Average of 1.5 or higher out of 2 |
| Related work | A relevant match in at least half the cases that had one |

A single fabricated fact blocks release. Fix the instructions, then rerun the full set.

## 5. Rerun after every change

Any change to `agent/instructions.md` or `config/` can fix one case and break another. Rerun the golden set, compare totals with the previous run, and note the result in your change record.

## Pilot

After the golden set passes, run a pilot with two or three requesters for three to four weeks. Ask analysts to rate each incoming intake on the same rubric. Compare follow-up rounds per intake against the period before the pilot.
