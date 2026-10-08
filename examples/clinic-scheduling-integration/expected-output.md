# Sample output

The response the agent should produce for [input.md](input.md), using the default configuration with `intake_tool` set to "Request Portal" and `external_party` set to "vendor". Use it as a reference when you test changes to the instructions.

Related prior work assumes the search found nothing.

---

## 1. Readiness

Readiness: Blocked. Type: New capability (inferred). 9 of 15 sections ready, 6 need answers, 3 blockers.

Type `[INFERRED]` from Email 1: bookings are re-keyed by hand today, so a connection between Slatebook and Quillpath does not exist yet.

## 2. Intake draft

**Request summary** `[SOURCE]`
Fernwood Health Partners wants online bookings in Slatebook to go straight into Quillpath, and Slatebook to show only open Quillpath slots, at all six clinics. Target date is in question: September 1 requested, mid to late September at the earliest on the vendor timeline.

**Business need** `[SOURCE]`
Front desk staff re-key online bookings into Quillpath every morning. Slots stay open online after phone bookings, which caused 31 double bookings last month. Patients wait and staff reschedule them.

**Desired outcome and success measure** `[INFERRED]` from Email 1
Online bookings and cancellations reach Quillpath without re-keying, and Slatebook shows only open slots. `[MISSING]` success measure.

**Summary of source communications** `[SOURCE]`
See part 7.

**In scope** `[SOURCE]`

- Online bookings from Slatebook go into Quillpath.
- Slatebook shows only open slots from Quillpath.
- Online cancellations free the slot in Quillpath (meeting notes).
- All six clinics.

**Out of scope** `[SOURCE]`

- Phone bookings stay as they are (meeting notes).

**Products, services, files, and data elements**

- Online appointment booking and cancellation `[SOURCE]`
- Quillpath appointments API `[SOURCE]`
- Fields sent with each booking and cancellation `[MISSING]`

**External parties and contacts** `[SOURCE]`

- Harrowgate Health Software, vendor of Quillpath: Renee Albright

**Impacted systems and applications** `[SOURCE]`

- Slatebook (changes: calls the Quillpath appointments API)
- Quillpath (accepts bookings and returns open slots)

**Impacted teams and stakeholders**

- Front desk staff at six clinics `[SOURCE]`
- Practice operations, Dana Okafor `[SOURCE]`
- IT applications, Luis Ferreira `[SOURCE]`
- Web team, manages Slatebook `[SOURCE]`. Contact `[MISSING]`.
- Harrowgate integration team `[SOURCE]`
- Privacy officer, for the addendum `[SOURCE]`

**Testing**
Internal `[SOURCE]`: Email 1 says someone should test before go-live. Tester, team, test types, and scenarios `[MISSING]`.
External `[SOURCE]`: Testing in the Harrowgate sandbox. Harrowgate tester and sign-off owner `[MISSING]`.

**Dates and milestones** `[CONFLICT]`

- Email 1: live by September 1, before flu shot season.
- Email 2 and meeting notes: integration team starts the week of August 17 and needs four to six weeks, so go-live is mid to late September at the earliest.
- Testing window `[MISSING]`.

**Dependencies** `[SOURCE]`

- Signed data sharing addendum before Harrowgate issues API credentials. Owner and date `[MISSING]`.
- Harrowgate integration team availability, from the week of August 17. Owner: Harrowgate.

**Assumptions** `[INFERRED]` from Email 2

- Slatebook can call the Quillpath appointments API. The web team has not confirmed this.

**Risks and blockers**

- The vendor timeline puts go-live after September 1. Raised in the meeting notes. `[SOURCE]`
- Privacy review of the addendum could delay API credentials and the start of work. `[INFERRED]` from meeting notes

## 3. Quality flags

| Check | Finding | Section | Fix |
| --- | --- | --- | --- |
| Dates conflict | September 1 (Email 1) falls before the earliest vendor finish in mid to late September (Email 2, meeting notes) | Dates and milestones | Agree on a date that fits the vendor timeline, or ask Harrowgate for an earlier start |
| Dates missing | No testing window | Dates and milestones | Ask for test start and end dates in the Harrowgate sandbox |
| Testing has no owner | "Someone should test it"; no tester, team, or test type named | Testing | Name the internal tester, the test types, and the environment |
| Data elements not listed | Booking and cancellation fields are not listed | Products, services, files, and data elements | Ask Harrowgate for the API field list and map the Slatebook fields to it |
| Dependency without an owner | Data sharing addendum has no owner or due date | Dependencies | Name an owner and a due date for the signed addendum |
| Unconfirmed assumption | The web team has not confirmed that Slatebook can call the API | Assumptions | Ask the web team to confirm |
| Outcome has no measure | No target for double bookings after go-live | Desired outcome and success measure | Ask what double booking count would count as success |

## 4. Missing information

1. Which go-live date is current: September 1, or a date that fits the Harrowgate timeline?
2. Who tests internally, which test types apply, and when does testing start and end?
3. Who owns the data sharing addendum, and when will it be signed?
4. Which fields does Slatebook send to Quillpath for a booking and a cancellation?
5. Who on the web team manages Slatebook?
6. Who at Harrowgate supports testing, and who signs off?
7. What double booking count after go-live would count as success?

## 5. Clarifying questions

**Customer and partner-facing systems**

- Which Slatebook pages change for patients? (Internal)
- What happens to online bookings made before go-live that were already re-keyed into Quillpath? (Internal)

**Application code and services**

- Does Slatebook call the Quillpath appointments API directly, or through a service the web team builds? (Internal)
- What logging will show a booking that did not reach Quillpath? (Internal)

**Data feeds and integrations**

- Which fields does the Quillpath appointments API require for a booking and for a cancellation? (vendor)
- How current is the list of open slots that the API returns? (vendor)
- How are rejected bookings reported, and to whom? (vendor)

**Access, privacy, and compliance**

- Which patient data does each booking send to Harrowgate, and does the privacy officer review it before the addendum is signed? (Internal)

**Internal testing**

- Which front desk staff test, and at which clinics? (Internal)
- Do the test scenarios cover a phone booking and an online booking for the same slot? (Internal)

**External and partner testing**

- Who at Harrowgate supports testing in the sandbox, and who signs off? (vendor)
- Can the Slatebook test environment reach the Harrowgate sandbox? (vendor)

Skipped: Fulfillment, servicing, and downstream systems; Scheduled jobs, legacy systems, and batch processing; Reporting, dashboards, and analytics. None are mentioned.

## 6. Related prior work

No related intakes found.

## 7. Source summary

1. Email from Dana Okafor, Fernwood Health Partners, June 8.
2. Email from Renee Albright, Harrowgate Health Software, June 11.
3. Meeting notes from Luis Ferreira, June 12.

**Email 1 (Dana, June 8)**

- Front desk staff at six clinics re-key online bookings into Quillpath every morning.
- 31 double bookings last month.
- Asks for online bookings to go straight into Quillpath and for Slatebook to show only open slots.
- Wants it live by September 1.
- Says someone should test before go-live.

**Email 2 (Renee, June 11)**

- Quillpath has an appointments API that accepts bookings and returns open slots.
- Integration team's next opening is the week of August 17. Work takes four to six weeks, including sandbox testing.
- A signed data sharing addendum is needed before API credentials.

**Meeting notes (Luis, June 12)**

- Six clinics, all on Slatebook.
- Online cancellations should free the slot in Quillpath.
- Phone bookings stay as they are.
- Vendor timeline puts go-live mid to late September at the earliest.
- Web team manages Slatebook. Contact not yet known.
- Privacy officer to be consulted about the addendum.

Review the checklist before you submit.
