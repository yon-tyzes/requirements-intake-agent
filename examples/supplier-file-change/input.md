# Sample input

This is the raw material a requester pasted into the agent. The manufacturer, supplier, people, and systems are fictional.

Corliss Pump Works builds industrial pumps. Ardent Castings supplies pump housings and sends an advance ship notice file before each shipment. Corliss imports the file into Receivo, its receiving system.

---

**Email 1**

From: Hanne Lindqvist, EDI Coordinator, Ardent Castings
To: Ardent customer contacts
Date: Tuesday, May 12

Dear customer,

On August 3, Ardent Castings will move all customers to version 3 of our advance ship notice file. Version 3 adds new fields and changes some existing ones. The layout document is attached. Version 2 files stop on August 3.

We can send test files from July 6. Please contact your account representative with any questions.

Regards,
Hanne Lindqvist

---

**Email 2**

From: Mateo Ruiz, Supply Chain, Corliss Pump Works
To: Sana Qureshi, IT Integration
Date: Wednesday, May 13

Sana,

See below. Ardent sends us about 40 shipments a week, and the receiving team relies on that file to check in castings at the dock. If it breaks, receiving falls back to paper packing slips and we lose a day. I didn't get the attachment, can you ask them for it? We need to be ready by August 3.

Mateo

---

**Meeting notes (Mateo), May 15, call with Sana**

- File lands in the SFTP folder nightly, Receivo imports it at 5 a.m.
- Sana's team owns the import mapping
- No layout doc yet, Ardent rep hasn't replied
- Sana thinks Pellworth ERP also reads receipt data from Receivo for invoice matching
- Sana's team can test the import once we have a test file
- Only Ardent uses this mapping, other suppliers have their own
