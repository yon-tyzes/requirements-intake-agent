# Sample input

This is the raw material a requester pasted into the agent. The company, partner, people, and systems are fictional.

Kestrel Freight is a regional carrier. Bayline Home Goods is a retail partner that receives shipment updates from Kestrel.

---

**Email 1**

From: Priya Natarajan, Bayline Home Goods
To: Marcus Webb, Kestrel Freight
Date: Tuesday, February 3

Hi Marcus,

Our stores keep calling customers to say a delivery is "in transit" when it was already delivered or failed. We think the status file you send us is too slow. Can you update the system so we get statuses faster? Ideally we'd also get the reason code when a delivery fails so our team can call the customer the same day.

We'd like this live before our spring promotion starts April 13. Our developer, Tom, will need a sample file to test with.

Thanks,
Priya

---

**Email 2**

From: Marcus Webb
To: Priya Natarajan
Date: Wednesday, February 4

Thanks Priya. Today the ShipStatus file goes out once a night at 2 a.m. I'll talk to our team about every 2 hours. We have reason codes in DispatchHub, they just aren't in the file. I'll get an intake started.

---

**Requester notes (Marcus)**

- Partner wants faster ShipStatus file + failure reason codes
- Night batch is the FeedRunner job, ops team owns it
- Reason codes live in DispatchHub, maybe 14 codes? Need to check with dispatch
- Priya said April 13 on email but on the call she said "first week of April"
- Test with Bayline in their test env, Tom is their dev
- Our QA should regression test the other 6 partners on the same file
- Don't think we change the customer tracking page
