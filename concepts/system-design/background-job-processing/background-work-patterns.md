---
domain: system-design
subdomain: background-job-processing
concept: background-work-patterns
title: Background Work: From Cron Jobs to Distributed Systems
sources:
  - title: "Background Work: From Cron Jobs to Distributed Systems"
    url: "https://blog.bytebytego.com/p/background-work-from-cron-jobs-to"
    author: "ByteByteGo"
    date: "2026-08-27"
---

# Background Work: From Cron Jobs to Distributed Systems

The article opens with a photo-upload example where resizing, scanning, CDN distribution, and metadata updates all occur in the request path, causing a poor user experience. Moving such extra work outside the request path—triggered by user actions, time, external systems, or work volume—is called background work. Normal request-response fails when time limits are enforced by infrastructure, third-party latency sets capacity, heavy work starves other requests, or work has nobody waiting on it (ByteByteGo, 2026).

The article then examines cron jobs. A cron job guarantees only that a command starts at a specified time, not that it completes successfully. Daylight-saving transitions and missed schedules create ambiguity, and adding a second server introduces the need for distributed locks or leader election. However, locks with TTL can cause duplicate execution due to paused workers, and consensus-based leader election still doesn't solve the 'launch started but not recorded' crash window. Thus, no arrangement of scheduled scripts achieves both "runs on machine death" and "runs exactly once" (ByteByteGo, 2026).

The solution is to separate the scheduler from the executor. The scheduler determines when work starts and enqueues it; workers pick it up. This introduces distinct roles: broker, scheduler, and job system. The transactional outbox pattern solves the dual-write problem by writing business rows and job rows in the same database transaction, with a relay publishing to the queue. However, leases used for recovery cause duplicate delivery—at-most-once and at-least-once are possible, but exactly-once end-to-end is not achievable because a slow worker is indistinguishable from a dead one (ByteByteGo, 2026).

- Background work decouples execution from the request path, improving UX and resilience for long-running or triggered tasks.
- Cron jobs provide a 'started' guarantee only, not completion; distributed cron with locks/leader election still cannot ensure exactly-once execution.
- A clean architecture separates scheduler (when to start), broker (message transport), and worker pool (execution), with a job store for tracking state.
- The transactional outbox pattern avoids dual-write failures but guarantees at-least-once delivery, leading to occasional duplicates.
- Exactly-once delivery is impossible end-to-end because the system cannot distinguish slow workers from crashed ones.