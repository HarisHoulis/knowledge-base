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

Background work refers to moving operations outside the request path to improve user experience and system resilience. The article explains why normal request-response fails for long-running tasks, third-party dependencies, heavy computations, and work with no waiting client. It then explores strategies from simple cron jobs to distributed systems, highlighting trade-offs in guarantees. Cron jobs provide a basic scheduling guarantee but don't ensure completion or success. Running cron on multiple servers introduces distributed locking and leader election, but no arrangement can guarantee exactly-once execution. The article introduces schedulers, queues, and workers, and explains the transactional outbox pattern to solve the dual-write problem. It concludes with delivery semantics: at-most-once, at-least-once, and the impossibility of exactly-once end-to-end.

- Background work decouples execution from the request path, improving user experience and allowing long-running or deferred tasks.
- Cron jobs only guarantee that a command is started at the scheduled time, not that it completes successfully.
- Distributed locks and leader election reduce the risk of duplicate executions but cannot eliminate it; jobs must be designed idempotent.
- The transactional outbox pattern ensures that database writes and queue enqueues are atomic, preventing silent message loss.
- At-least-once delivery is the common practical guarantee; exactly-once is not achievable end-to-end due to the separate work and acknowledgement operations.