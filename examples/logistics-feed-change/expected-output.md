# Sample output

The response the agent should produce for [input.md](input.md), using the default configuration with `intake_tool` set to "Request Portal" and `external_party` set to "partner". Use it as a reference when you test changes to the instructions.

Related prior work assumes the search found one matching intake. The link is a placeholder.

---

## 1. Intake draft

**Request summary** `[SOURCE]`
Bayline Home Goods wants the ShipStatus file sent more often than once a night and wants failure reason codes added, so store teams can contact customers the same day. Target date is in question: April 13 or the first week of April.

**Business need** `[SOURCE]`
Bayline stores tell customers a delivery is in transit after it was delivered or failed, because the status file arrives once a night.

**Desired outcome and success measure** `[INFERRED]` from Email 1
Bayline sees current delivery status during the day and can call customers about failed deliveries the same day. `[MISSING]` success measure.

**Summary of source communications** `[SOURCE]`
See part 6.

**In scope** `[SOURCE]`

- Increase ShipStatus file frequency for Bayline. Proposed: every 2 hours (Marcus, Email 2).
- Add delivery failure reason codes from DispatchHub to the ShipStatus file.

**Out of scope** `[INFERRED]` from requester notes

- Customer tracking page. Marked "don't think we change," so this needs confirmation.

**Products, files, and data elements**

- ShipStatus file `[SOURCE]`
- Failure reason codes, possibly 14 `[SOURCE]` (unconfirmed)
- Field names and positions for the new reason code `[MISSING]`

**External parties and contacts** `[SOURCE]`

- Bayline Home Goods: Priya Natarajan (business contact), Tom (developer, last name `[MISSING]`)

**Impacted systems and applications** `[SOURCE]`

- FeedRunner job (sends ShipStatus nightly)
- DispatchHub (source of reason codes)

**Impacted teams and stakeholders** `[SOURCE]`

- Operations team (owns FeedRunner)
- Dispatch team (owns reason codes)
- Internal QA
- Six other partners that receive the same file `[INFERRED]` from requester notes

**Testing**
Internal `[SOURCE]`: QA regression test for the six other partners on the ShipStatus file. Test types beyond regression, environment, and tester names `[MISSING]`.
External `[SOURCE]`: Bayline tests in their test environment. Tester: Tom. Needs a sample file. Scenarios and sign-off owner `[MISSING]`.

**Dates and milestones** `[CONFLICT]`

- Email 1: live before April 13 (spring promotion start).
- Requester notes: Priya said "first week of April" on a call.
- Testing window `[MISSING]`.

**Dependencies** `[INFERRED]`

- Dispatch team confirms the reason code list. Owner and date `[MISSING]`.
- Kestrel provides a sample file to Bayline. Owner and date `[MISSING]`.

**Assumptions** `[INFERRED]`

- A 2-hour schedule is feasible for FeedRunner. Not yet confirmed by operations.
- The other six partners can receive the file on the new schedule, or the change applies to Bayline only. Not stated.

**Risks and blockers** `[INFERRED]`

- Changing a shared file affects six other partners.
- Date conflict could shorten the build and test window by a week.

## 2. Quality flags

| Check | Finding | Section | Fix |
| --- | --- | --- | --- |
| Dates conflict | April 13 in Email 1, first week of April on a call | Dates and milestones | Confirm the date with Priya in writing |
| Dates missing | No testing window | Dates and milestones | Ask for test start and end dates |
| Vague action | "Update the system so we get statuses faster" | Request summary | Confirm the target frequency and which system changes |
| Data elements not listed | Reason code count and field layout unknown | Products, files, and data elements | Ask dispatch for the code list and agree on a field layout |
| Dependency without an owner | Sample file and code list have no owner or date | Dependencies | Name an owner and due date for each |
| Unconfirmed assumption | 2-hour schedule not confirmed by operations | Assumptions | Ask operations to confirm |
| Outcome has no measure | No measure of "faster" or of fewer wrong calls | Desired outcome | Ask Bayline how they will judge success |

## 3. Missing information

1. Which date is fixed: April 13 or the first week of April?
2. Does the frequency change apply only to Bayline or to all seven partners on the ShipStatus file?
3. What is the full list of failure reason codes, and where in the file will they go?
4. Who on the operations team confirms FeedRunner can run every 2 hours?
5. When does internal testing start and end, and who on QA owns it?
6. Is the customer tracking page out of scope?
7. What is Tom's full name and email?

## 4. Clarifying questions

**Batch jobs, mainframe, and scheduled reporting**

- Can FeedRunner run every 2 hours without overlapping the next run? (Internal)
- What is the rollback plan if a daytime run fails? (Internal)

**Data feeds and integrations**

- Will the reason code be a new field at the end of the ShipStatus record or replace an existing field? (Internal)
- Does Bayline need a code-to-description table, or only the codes? (partner)
- How should Bayline handle a status that changes between two runs? (partner)

**Internal testing**

- Which QA environment holds copies of all seven partner feeds? (Internal)
- Do the regression tests cover the file layout change and the schedule change? (Internal)

**External and partner testing**

- Which scenarios will Tom run: delivered, failed with each reason code, and late status changes? (partner)
- Who at Bayline signs off before go-live? (partner)

Skipped: Customer and partner-facing platforms, Servicing and post-transaction platforms, Application code and services, Reporting and analytics, Access and compliance. None are mentioned. Confirm the tracking page exclusion to close the first one.

## 5. Related prior work

- **[Harborline partner feed frequency change](https://example.com/intakes/placeholder)**: moved a partner file from nightly to every 4 hours on FeedRunner. It recorded an operations capacity review and a 3-week parallel run, which this request does not mention yet.

## 6. Source summary

1. Email from Priya Natarajan, Bayline Home Goods, February 3.
2. Email from Marcus Webb, Kestrel Freight, February 4.
3. Requester notes from Marcus Webb, undated.

**Email 1 (Priya, February 3)**

- Stores give customers outdated delivery status.
- Asks for faster status updates and failure reason codes.
- Wants it live before April 13.
- Developer Tom needs a sample file.

**Email 2 (Marcus, February 4)**

- ShipStatus runs nightly at 2 a.m.
- Proposes every 2 hours.
- Reason codes exist in DispatchHub but are not in the file.

**Requester notes**

- FeedRunner owned by operations.
- About 14 reason codes, unconfirmed.
- Date given on a call differs from the email.
- Six other partners receive the same file.

7 of 15 sections ready, 8 need answers, 2 blockers remain.
