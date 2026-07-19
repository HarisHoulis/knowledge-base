---
domain: system-design
subdomain: fault-tolerance
concept: primary-backup-replication
title: Lecture 4: Primary-Backup Replication
sources:
  - title: "Lecture 4: Primary-Backup Replication"
    url: "https://www.youtube.com/watch?v=M_teob23ZzY"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-02-18T18:33:12+00:00"
---

# Lecture 4: Primary-Backup Replication

The lecture introduces primary-backup replication as a technique for achieving fault tolerance in distributed systems. It focuses on handling fail-stop failures, where a server stops executing due to hardware issues or crashes, but does not produce incorrect results. The key insight is that replication can only mask fail-stop faults, not software bugs or hardware design defects, since those would cause both replicas to produce the same incorrect outputs. Additionally, replication assumes independent failures; correlated failures (e.g., identical hardware with manufacturing defects) diminish its effectiveness. The talk sets the stage for discussing VMware FT's approach to implementing this pattern.

- Primary-backup replication is used to tolerate fail-stop failures, where a server ceases execution without producing erroneous results.
- It cannot protect against software bugs or hardware design defects, as these affect all replicas equally.
- The technique relies on failure independence between replicas; correlated failures (e.g., same batch of hardware) undermine its guarantees.
- Fail-stop failures can arise from power loss, network cuts, or hardware errors detectable by checksums or error-correcting codes.