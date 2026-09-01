---
domain: system-design
subdomain: background-jobs
concept: background-work-patterns
title: Background Work: From Cron Jobs to Distributed Systems
sources:
  - title: "Background Work: From Cron Jobs to Distributed Systems"
    url: "https://blog.bytebytego.com/p/background-work-from-cron-jobs-to"
    author: "ByteByteGo"
    date: "2026-08-27"
---

# Background Work: From Cron Jobs to Distributed Systems

Moving heavy operations out of the request path is essential for UX and scalability. The article illustrates with a photo upload: resizing, scanning, and CDN distribution can happen after the upload is acknowledged. Background work can be triggered by user actions, clocks, external systems, or batch volume (ByteByteGo, 2026). However, background execution shifts the problem from 'did the response return?' to 'did the job succeed?'.

Basic cron guarantees only that a command starts at a specified time, not that it completes or that it runs exactly once. Clock adjustments and missed schedules create ambiguity, and naive multi-server cron leads to duplicate runs. Distributed locks and leader election mitigate but do not solve the issue, because a paused worker can outlive its lock lease, causing double execution. The article concludes that no deployment of scheduled scripts satisfies both 'runs on machine death' and 'runs exactly once' (ByteByteGo, 2026).

The next level of maturity separates the scheduler from the executor: scheduler stores state, decides when to start, and enqueues work; workers pull from a queue. This introduces the dual-write problem when saving a business record and enqueueing simultaneously. The transactional outbox pattern solves this by writing both in one DB transaction and relaying asynchronously (ByteByteGo, 2026). Even with safeguards, delivery semantics are limited: at-most-once can lose work, at-least-once can duplicate, and true exactly-once is unattainable because a slow worker and a dead worker are indistinguishable.

- Cron jobs provide weak guarantees: they only ensure a command is started, not completed, and are prone to clock and recovery issues.
- Distributed locks and leader election reduce duplicate work but cannot guarantee exactly-once execution; at-least-once is often the pragmatic choice.
- Schedulers and queues decouple deciding when to run from doing the work, enabling scalable worker pools.
- Transactional outbox pattern prevents data loss from dual writes, but duplicates remain possible.
- Systems should design jobs to be idempotent to handle at-least-once delivery.