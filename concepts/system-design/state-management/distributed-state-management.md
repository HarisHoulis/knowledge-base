---
domain: system-design
subdomain: state-management
concept: distributed-state-management
title: Why State Is the Hardest Thing in Software Design
sources:
  - title: "Why State is the Hardest Thing in Software Design"
    url: "https://blog.bytebytego.com/p/why-state-is-the-hardest-thing-in"
    author: "ByteByteGo"
    date: "2026-10-01"
---

# Why State Is the Hardest Thing in Software Design

State is the information a system retains that affects its functionality, from logged-in users to pending background tasks to database records (ByteByteGo). State makes an operation depend on something beyond its immediate inputs: a ticket-number function called twice with the same input returns different results because retained state changed in between. In design discussions the focus is narrower than variables in memory — it is the information that must remain available across requests, across workers, or across failures. This is why a server can use memory heavily and still be called stateless: no state needs to cross a certain boundary.

"Make the application stateless" does not mean the absence of state. It means making individual application instances replaceable while putting important state in backing services such as databases (ByteByteGo). A load balancer distributes requests across instances, each instance can fetch what it needs — for example, a session identifier supplied in the request is used to pull session details from a shared store — so instances can be added, replaced, and redeployed without transferring information between them, while still creating orders, updating documents, and changing database records.

The article sorts state into categories with different storage implications: session state (login info, temporary preferences, multi-step workflow progress, often expiring); application state (an auction's highest bid, job status, inventory, feature settings); persistent state (documents, account records, uploads, surviving process restarts and typically stored in databases or object storage); derived state (caches, search indexes, daily totals, rebuilt from a source of truth and prone to staleness); and ephemeral state (request buffers, typing indicators, connection data). Lifetime and loss tolerance are separate decisions — a seat reservation expiring in five minutes may still need to survive a server restart, and durably stored records can still be deliberately deleted the next day.

Storage choice depends on who needs the information, how fast, and what happens if it disappears, with options ranging from application memory and browser/mobile storage through shared key-value stores, databases, object storage, and persistent volumes (ByteByteGo). A shared store is not automatically durable and a durable file is not automatically accessible from another machine. Sticky sessions keep requests near in-memory state and let existing applications work unchanged, but they skew traffic distribution, don't automatically rebalance existing sessions onto new instances, and lose session data when the pinned instance fails — so deployments must drain or transfer sessions. Moving state to shared storage adds network round trips, serialization, and latency that compounds across sequential reads, and moving state means catching up with concurrent updates and transferring ownership without losing or double-applying operations. Correct concurrent updates remain the hardest part: in the classic example, two purchases both read stock as one and both write zero, approving two purchases for one item because reading, deciding, and writing were separate steps. The fix is a conditional update performed as one indivisible operation, plus constraints, locks, or transaction isolation that protects the business rule — and clear ownership, such as an inventory service that is the sole authority for inventory changes.

- "Make the application stateless" means making application instances replaceable while keeping important state in shared backing services — not eliminating state entirely.
- State categories — session, application, persistent, derived, and ephemeral — differ in storage and durability needs, and useful lifetime is a separate decision from loss tolerance.
- A shared store is not automatically durable and a durable volume is not automatically accessible from another machine; likewise, multiple copies of a value require clear rules about which one is authoritative.
- Sticky sessions preserve locality and avoid moving state, but uneven traffic, limited rebalancing, and total loss of in-memory session data on instance failure are the costs.
- Concurrency bugs like the two-purchases-for-one-item case come from splitting read, decide, and write; they require an indivisible conditional update, plus constraints, locks, or appropriate isolation, ideally under single-service ownership of the data.