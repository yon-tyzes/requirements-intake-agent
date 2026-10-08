# Sample output

The response the agent should produce for [input.md](input.md), using the default configuration with `intake_tool` set to "Request Portal" and `external_party` set to "vendor". Use it as a reference when you test changes to the instructions.

Related prior work assumes the search found nothing.

---

## 1. Readiness

Readiness: Blocked. Type: Compliance-driven (source). 7 of 15 sections ready, 8 need answers, 2 blockers.

Type `[SOURCE]` from Email 1: Owen says the field is needed because of Ordinance 2026-14. Change to existing also fits, as a secondary type, because the Permitry application already exists.

## 2. Intake draft

**Request summary** `[SOURCE]`
The Department of Building and Land Use wants a tree removal question added to the residential building permit application in Permitry, with the answer shown in CaseLedger, by July 1, when Ordinance 2026-14 takes effect.

**Business need**
Ordinance 2026-14, adopted by Council and effective July 1, is the stated reason for the change. `[SOURCE]`
What the ordinance requires of applicants or the department `[MISSING]`.

**Desired outcome and success measure** `[MISSING]`

**Summary of source communications** `[SOURCE]`
See part 7.

**In scope** `[SOURCE]`

- New tree removal question on the residential building permit application in Permitry.
- Show the answer in CaseLedger so reviewers can see it.

**Out of scope** `[MISSING]`
The source does not say whether commercial or other permit applications are excluded.

**Products, services, files, and data elements**

- Residential building permit application `[SOURCE]`
- Proposed fields: tree removal yes or no, and number of trees `[SOURCE]` (Gloria wrote "probably")
- Field wording and rules required by the ordinance `[MISSING]`

**External parties and contacts**

- Tallgrass Civic Systems, hosts Permitry `[SOURCE]`. Contact `[MISSING]`.

**Impacted systems and applications** `[SOURCE]`

- Permitry (changes: new question on the residential application)
- CaseLedger (shows the answer to reviewers)

**Impacted teams and stakeholders**

- Department of Building and Land Use, Owen Marsh `[SOURCE]`
- Permit Services, Gloria Vance, and the permit techs who test `[SOURCE]`
- IT Service Desk, Ken Ito `[SOURCE]`
- Tallgrass Civic Systems `[SOURCE]`
- Planning reviewers `[INFERRED]` from requester notes. Gloria has not confirmed they use the answer.

**Testing**
Internal `[SOURCE]`: permit techs test in Permitry staging before July 1. Named testers, test types, and scenarios `[MISSING]`.
External `[MISSING]`: whether Tallgrass tests, and who signs off.

**Dates and milestones**

- Ordinance 2026-14 takes effect July 1. `[SOURCE]`
- Tallgrass needs 6 weeks notice for form changes. `[SOURCE]`
- Testing window `[MISSING]`.

**Dependencies**

- Tallgrass makes the form change, with 6 weeks notice `[SOURCE]`. To meet July 1, the request must reach Tallgrass by May 20 `[INFERRED]`. Owner `[MISSING]`.

**Assumptions**

- Tallgrass makes the change. Gloria wrote "I assume." `[SOURCE]`
- A yes or no question with a tree count meets the ordinance. Not checked against the ordinance text. `[INFERRED]` from Email 2

**Risks and blockers** `[INFERRED]` from requester notes

- If the field wording changes after the ordinance text is checked, the 6-week notice period may push the change past July 1.

## 3. Quality flags

| Check | Finding | Section | Fix |
| --- | --- | --- | --- |
| Solution without an outcome | The request names a new field but not what the ordinance requires or how the answer will be used | Business need; Desired outcome and success measure | Ask what the ordinance requires and what should be true after July 1 |
| Dates missing | No testing window | Dates and milestones | Ask for test start and end dates in Permitry staging |
| Internal and external testing not separated | The draft does not say whether Tallgrass tests or who signs off | Testing | Ask whether Tallgrass tests and who signs off on each side |
| External contact missing | No named contact at Tallgrass | External parties and contacts | Ask for the Tallgrass account contact and technical contact |
| Dependency without an owner | Nobody owns sending the change request to Tallgrass | Dependencies | Name an owner and send the request by May 20 |
| Unconfirmed assumption | Tallgrass making the change is assumed | Assumptions | Ask Ken to confirm with Tallgrass |
| No scope boundary | Commercial and other permit applications are not addressed | Out of scope | Ask which permit applications are excluded |

## 4. Missing information

1. What does Ordinance 2026-14 require applicants or the department to do?
2. What should be true after July 1, and how will the department know the change works?
3. When does testing in Permitry staging start and end?
4. Who sends the form change request to Tallgrass, and can it go out by May 20?
5. Which permit techs test, and which test types and scenarios apply?
6. Are commercial and other permit applications out of scope?
7. What field wording and rules does the ordinance require?
8. Who is the contact at Tallgrass, and does Tallgrass test the change?

## 5. Clarifying questions

**Customer and partner-facing systems**

- Is the tree removal question required on every residential application? (Internal)
- What happens to residential applications submitted before July 1 and still under review? (Internal)
- Should the question include help text that names the ordinance? (Internal)

**Data feeds and integrations**

- How will the answer reach CaseLedger: through an existing connection from Permitry, or a new one? (vendor)

**Reporting, dashboards, and analytics**

- Does any permit report need to include the tree removal answer? (Internal)

**Access, privacy, and compliance**

- Who checks the question wording against the ordinance text before release? (Internal)

**Internal testing**

- Which scenarios will the permit techs test: yes with a tree count, no, and a missing answer? (Internal)
- Does the testing window fit before July 1, given the 6-week notice? (Internal)

**External and partner testing**

- Does Tallgrass test the change in Permitry staging, and who signs off? (vendor)

Skipped: Fulfillment, servicing, and downstream systems; Scheduled jobs, legacy systems, and batch processing; Application code and services. None are mentioned.

## 6. Related prior work

No related intakes found.

## 7. Source summary

1. Email from Owen Marsh, Department of Building and Land Use, March 2.
2. Email from Gloria Vance, Permit Services, March 3.
3. Requester notes from Gloria Vance, undated.

**Email 1 (Owen, March 2)**

- Council adopted Ordinance 2026-14. It takes effect July 1.
- Because of it, asks for a new field on the residential building permit application asking whether the project removes trees.
- Asks Gloria to request the change from IT.

**Email 2 (Gloria, March 3)**

- Asks Ken to add a tree removal question to the residential application in Permitry.
- Suggests a yes or no answer with a box for the number of trees.
- Assumes Tallgrass makes the change.
- Wants the answer shown in CaseLedger for reviewers.

**Requester notes**

- Ordinance takes effect July 1.
- Residential building permits. Commercial not mentioned in the summary Owen sent.
- Tallgrass needs 6 weeks notice for form changes.
- Unsure whether planning reviewers use the answer.
- Permit techs can test in Permitry staging before July 1.

Review the checklist before you submit.
