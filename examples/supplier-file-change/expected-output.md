# Sample output

The response the agent should produce for [input.md](input.md), using the default configuration with `intake_tool` set to "Request Portal" and `external_party` set to "supplier". Use it as a reference when you test changes to the instructions.

Related prior work assumes the search found nothing.

---

## 1. Readiness

Readiness: Needs answers. Type: Data or report (inferred). 10 of 15 sections ready, 5 need answers, 0 blockers.

Type `[INFERRED]` from Email 1: the request changes how an inbound data file is read. Change to existing also fits, as a secondary type, because the Receivo import already exists.

## 2. Intake draft

**Request summary** `[SOURCE]`
Ardent Castings moves its advance ship notice file to version 3 on August 3. Corliss Pump Works needs the Receivo import updated to read version 3 by that date.

**Business need** `[SOURCE]`
The receiving team uses the Ardent file to check in castings at the dock, about 40 shipments a week. Version 2 files stop on August 3. If the import breaks, receiving falls back to paper packing slips and loses a day.

**Desired outcome and success measure** `[INFERRED]` from Email 2
Receivo imports version 3 files from August 3, and receiving checks in Ardent shipments without paper packing slips. `[MISSING]` success measure.

**Summary of source communications** `[SOURCE]`
See part 7.

**In scope** `[SOURCE]`

- Update the Receivo import mapping for the Ardent advance ship notice file to version 3.

**Out of scope** `[INFERRED]` from meeting notes

- Import mappings for other suppliers. Only Ardent uses this mapping.

**Products, services, files, and data elements**

- Ardent advance ship notice file, version 3 `[SOURCE]`
- Added and changed fields `[MISSING]`. The layout document was not received.

**External parties and contacts**

- Ardent Castings, supplier of pump housings: Hanne Lindqvist, EDI Coordinator `[SOURCE]`
- Ardent account representative for Corliss: name `[MISSING]`

**Impacted systems and applications**

- Receivo (import mapping changes; imports the file at 5 a.m.) `[SOURCE]`
- SFTP folder where the file lands nightly `[SOURCE]`
- Pellworth ERP (may read receipt data from Receivo for invoice matching) `[SOURCE]`, unconfirmed

**Impacted teams and stakeholders** `[SOURCE]`

- Receiving team (checks in castings using the file)
- IT Integration, Sana Qureshi (owns the import mapping and tests it)
- Supply Chain, Mateo Ruiz (raised the request with IT)

**Testing**
Internal `[SOURCE]`: Sana's team tests the Receivo import once a test file arrives. Test types, environment, and scenarios `[MISSING]`.
External `[MISSING]`: Ardent sends test files from July 6. Whether Ardent takes part in testing, and who signs off on each side, is not stated.

**Dates and milestones**

- Version 3 starts and version 2 stops on August 3. `[SOURCE]`
- Ardent test files available from July 6. `[SOURCE]`
- Testing window July 6 to August 3. `[INFERRED]` from Email 1

**Dependencies**

- Ardent sends the version 3 layout document. Sana to ask for it `[SOURCE]`. Due date `[MISSING]`.
- Ardent sends test files from July 6. Owner: Ardent `[SOURCE]`.

**Assumptions** `[SOURCE]`

- Pellworth ERP reads receipt data from Receivo for invoice matching. Sana "thinks" so. Not confirmed.

**Risks and blockers**

- Version 2 files stop on August 3. A late mapping change stops the import, and receiving falls back to paper packing slips. Raised in Email 2. `[SOURCE]`
- Without the layout document, mapping work cannot start, and the testing window is four weeks at most. `[INFERRED]` from Email 1 and meeting notes

## 3. Quality flags

| Check | Finding | Section | Fix |
| --- | --- | --- | --- |
| Data elements not listed | Version 3 layout document not received; added and changed fields unknown | Products, services, files, and data elements | Get the layout document from Ardent and map each changed field |
| Internal and external testing not separated | The draft does not say whether Ardent takes part in testing or who signs off | Testing | Ask Ardent whether they test with Corliss, and who signs off on each side |
| Dependency without an owner | The layout document has no due date | Dependencies | Set a due date for the layout document |
| Unconfirmed assumption | Pellworth ERP reading receipt data from Receivo is not confirmed | Assumptions | Ask Sana's team to confirm |
| Outcome has no measure | No measure of success after August 3 | Desired outcome and success measure | Ask how receiving will judge success one month after the change |

## 4. Missing information

1. Which fields does version 3 add or change? Can Ardent resend the layout document?
2. When is the layout document due?
3. Which test types, environment, and scenarios will Sana's team use?
4. Does Ardent take part in testing, and who signs off on each side?
5. Who is the Ardent account representative for Corliss?
6. How will receiving judge success one month after the change?

## 5. Clarifying questions

**Scheduled jobs, legacy systems, and batch processing**

- Do the nightly file arrival or the 5 a.m. Receivo import change with version 3? (Internal)
- What is the plan if the first version 3 file fails to import, given that version 2 files stop on August 3? (Internal)

**Data feeds and integrations**

- Which fields does version 3 add, remove, or redefine compared with version 2? (supplier)
- Can Ardent send a version 3 test file before July 6? (supplier)
- How are rejected records in the Ardent file reported in Receivo, and to whom? (Internal)

**Fulfillment, servicing, and downstream systems**

- Does invoice matching in Pellworth ERP use any field that changes in version 3? (Internal)

**Reporting, dashboards, and analytics**

- Does any receiving report read fields from the Ardent file? (Internal)

**Internal testing**

- Which test environment holds a copy of the Receivo import? (Internal)
- Does the receiving team check test receipts before August 3? (Internal)

**External and partner testing**

- Do Ardent's test files reflect real upcoming shipments, or sample data? (supplier)
- Who at Ardent confirms that Corliss can read version 3 files before August 3? (supplier)

Skipped: Customer and partner-facing systems; Application code and services; Access, privacy, and compliance. None are mentioned.

## 6. Related prior work

No related intakes found.

## 7. Source summary

1. Email from Hanne Lindqvist, Ardent Castings, May 12.
2. Email from Mateo Ruiz, Corliss Pump Works, May 13.
3. Meeting notes from Mateo Ruiz, May 15.

**Email 1 (Hanne, May 12)**

- Ardent moves all customers to version 3 of its advance ship notice file on August 3.
- Version 3 adds new fields and changes some existing ones.
- Version 2 files stop on August 3.
- Test files available from July 6.
- Layout document said to be attached.

**Email 2 (Mateo, May 13)**

- About 40 Ardent shipments a week.
- Receiving uses the file to check in castings. If it breaks, receiving falls back to paper packing slips and loses a day.
- The attachment did not arrive. Asks Sana to request it.
- Needs to be ready by August 3.

**Meeting notes (Mateo, May 15)**

- File lands in the SFTP folder nightly. Receivo imports it at 5 a.m.
- Sana's team owns the import mapping.
- No layout document yet. The Ardent representative has not replied.
- Pellworth ERP may read receipt data from Receivo for invoice matching.
- Sana's team can test once a test file arrives.
- Only Ardent uses this mapping.

Review the checklist before you submit.
