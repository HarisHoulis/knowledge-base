---
domain: system-design
subdomain: replication
concept: primary-backup-replication
title: Lecture 4: Primary-Backup Replication
sources:
  - title: "Lecture 4: Primary-Backup Replication"
    url: "https://www.youtube.com/watch?v=M_teob23ZzY"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-02-18T18:33:12+00:00"
---

# Lecture 4: Primary-Backup Replication

The lecture also emphasizes that replication assumes independent failures between replicas. Correlated failures, such as identical hardware from the same manufacturing batch, can undermine the effectiveness of replication. Hardware errors like bit flips in packets or disk blocks can often be transformed into fail-stop faults via checksums and error-correcting codes, allowing software to stop cleanly rather than produce wrong results. This makes fail-stop a practical abstraction for many real-world failure modes (Lecture 4, 2020).

- Primary-backup replication is designed to handle fail-stop failures, where a machine halts or becomes unreachable.
- Replication cannot protect against bugs in the replicated software or hardware design defects that cause consistent incorrect behavior.
- Independent failures between replicas are a core assumption; correlated failures undermine availability.
- Checksums and error-correcting codes can convert many random hardware corruptions into detectable, fail-stop-like faults.