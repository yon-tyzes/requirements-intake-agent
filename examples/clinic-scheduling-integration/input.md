# Sample input

This is the raw material a requester pasted into the agent. The clinic group, vendor, people, and systems are fictional.

Fernwood Health Partners runs six outpatient clinics. Patients book online through Slatebook, a booking page on the Fernwood website. Front desk staff schedule visits in Quillpath, a scheduling system from Harrowgate Health Software.

---

**Email 1**

From: Dana Okafor, Practice Operations, Fernwood Health Partners
To: Luis Ferreira, IT Applications
Date: Monday, June 8

Luis,

Front desk staff at all six clinics are still re-keying online bookings from Slatebook into Quillpath every morning. Last month we had 31 double bookings because a slot still showed as open online after someone had booked it by phone. Patients show up and wait, and staff have to reschedule them.

Can we get Slatebook and Quillpath talking to each other, so online bookings go straight into Quillpath and the online calendar only shows slots that are really open? I'd like this live by September 1, before flu shot season gets busy.

Someone should test it before it goes live.

Dana

---

**Email 2**

From: Renee Albright, Harrowgate Health Software
To: Luis Ferreira
Date: Thursday, June 11

Hi Luis,

Quillpath has an appointments API that accepts bookings and returns open slots. Slatebook would need to call it. Our integration team's next opening is the week of August 17, and a connection like this usually takes four to six weeks, including testing in our sandbox. We need a signed data sharing addendum before we can issue API credentials.

Renee

---

**Meeting notes (Luis), June 12, call with Dana**

- Dana confirmed 6 clinics, all on Slatebook
- Patients can also cancel online, cancellations should free the slot in Quillpath too
- Phone bookings stay as they are
- Vendor timeline puts go-live mid to late Sept at the earliest, Dana still wants Sept 1
- Slatebook is managed by our web team (contact TBD)
- Need to check with the privacy officer about the addendum
- Testing in the Harrowgate sandbox
