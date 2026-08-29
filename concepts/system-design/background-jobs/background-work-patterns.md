---
domain: system-design
subdomain: background-jobs
concept: background-work-patterns
title: Background Work: From Cron Jobs to Distributed Systems
sources:
  - title: "Background Work: From Cron Jobs to Distributed Systems"
    url: "https://blog.bytebytego.com/p/background-work-from-cron-jobs-to"
    author: "ByteByteGo"
    date: "Thu, 27 Aug 2026 15:31:25 GMT"
---

# Background Work: From Cron Jobs to Distributed Systems

Background work separates execution from the request path, enabling long-running or asynchronous tasks like image resizing, email sending, and nighty reports. The article explains why the normal request-response model breaks down for such tasks: infrastructure-enforced time limits, third-party latency, heavy computation starving other requests, and work that has no client waiting for it. Moving work to the background improves user experience and decouples producers from consumers, but introduces new failure modes (ByteByteGo, 2026).

Starting with a single-machine cron job, the article highlights that cron only guarantees that a command starts at a scheduled time, not that it finishes successfully. Clock changes can trigger duplicate or skipped runs, and missed schedules are silently ignored. When scaling cron to multiple servers, issues like the lock TTL problem and leader election arise. A lock with an expiration can cause two machines to process the same job if a holder pauses, and even consensus-based leader election cannot guarantee exactly-once execution if the leader crashes mid-launch (ByteByteGo, 2026).

The solution is to separate the scheduler from the workers: a scheduler determines when work starts, a broker transports messages, and a job system tracks lifecycle and retries. Queues and job stores differ in how much state they keep; job stores are needed for debugging customer issues. The transactional outbox pattern solves the dual-write problem by writing a business row and a job row in the same database transaction, with a relay publishing to the queue. However, this guarantees at-least-once delivery, not exactly-once, because a worker can crash between performing work and acknowledging it. The article concludes that exactly-once end-to-end is not achievable (ByteByteGo, 2026).

- Background work moves time-consuming or asynchronous tasks out of the request path to improve user experience and resilience.
- Basic cron jobs provide no guarantees about completion, success, or duplicate execution, and are fragile across multi-server setups.
- Distributed locks and leader election introduce trade-offs; pausing workers can lead to duplicate work.
- Separating scheduler, broker, and job system allows independent scaling and better state tracking.
- The transactional outbox pattern solves dual-write consistency but yields at-least-once delivery; exactly-once is not achievable end-to-end.