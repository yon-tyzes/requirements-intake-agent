# Scoring rubric

Score each response against the final approved intake and the follow-up record for that case.

## Section accuracy

Score each enabled section 0, 1, or 2. Report the average.

| Score | Meaning |
| --- | --- |
| 2 | Matches the final intake, or correctly marked `[MISSING]` where the source lacked it |
| 1 | Partly right: incomplete, too general, or tagged incorrectly |
| 0 | Wrong, or filled when it should have been `[MISSING]` |

## Fabricated facts

Count every name, system, date, number, file, owner, or contact that appears in the response but not in the source material or a linked prior intake. Any count above zero fails the case.

Wrong tags do not count as fabrication. A fact tagged `[SOURCE]` that is only inferred is a section accuracy issue.

## Gap recall

List the questions analysts asked after the original intake was submitted. Count how many the agent raised in Missing information, Quality flags, or Clarifying questions.

Gap recall = questions caught / questions asked

A question counts as caught when the agent asked about the same fact, even in different words.

## Question quality

Score the Missing information and Clarifying questions parts together.

| Score | Meaning |
| --- | --- |
| 2 | Specific to this request, names the system or item, and nothing a reviewer would delete |
| 1 | Useful but includes generic or repeated questions |
| 0 | Mostly generic, or misses the main gap |

## Readiness verdict

Score the Readiness line correct or incorrect against the reviewer's judgment.

| Score | Meaning |
| --- | --- |
| Correct | The verdict matches what the reviewer would give: `Ready to submit`, `Needs answers`, or `Blocked` |
| Incorrect | Any other verdict, or a verdict whose counts do not match the intake draft and the quality flags |

Report the share of cases scored correct.

## Related work

| Score | Meaning |
| --- | --- |
| 2 | Found the most relevant prior intake and named a useful missing detail |
| 1 | Found a related intake but the suggestion adds little |
| 0 | Missed an obvious match, or described an intake it did not retrieve |
| n/a | No related intake exists |

## Reviewer notes

Write one line on the biggest problem in each response. Patterns across these notes usually point to the instruction to change.
