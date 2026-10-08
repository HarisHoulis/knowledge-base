---
domain: system-design
subdomain: distributed-databases
concept: spanner-omni-ga
title: Spanner Omni Reaches GA, Replacing Google's Atomic Clocks and File System with Software
sources:
  - title: "Spanner Omni Reaches GA, Replacing Google's Atomic Clocks and File System with Software"
    url: "https://www.infoq.com/news/2026/10/spanner-omni-deploy-anywhere-ga/"
    author: "Steef-Jan Wiggers"
    date: "2026-10-07"
---

# Spanner Omni Reaches GA, Replacing Google's Atomic Clocks and File System with Software

Google has made Spanner Omni generally available, allowing its distributed SQL database to run on-premises, across clouds, or even on a laptop (Wiggers, 2026). Achieving this portability required re-architecting two core dependencies of the original Spanner: Colossus, Google's distributed file system, was replaced with a Colossus-like abstraction layer, and TrueTime, the GPS- and atomic-clock-based time synchronization service, was replaced with software-based time synchronization (Wiggers, 2026).

These substitutions are significant because TrueTime and Colossus were foundational to Spanner's original design guarantees. By moving time synchronization into software, Spanner Omni trades the tight, hardware-backed clock uncertainty bounds of Google's datacenters for a purely software approach, which has implications for how the system reasons about transaction ordering and consistency (Wiggers, 2026).

Notably, Spanner Omni ships without an availability SLA, and practitioners are reportedly pricing the move in terms of tail latency and operational toil (Wiggers, 2026). This suggests that while the deployment flexibility is real, teams adopting it outside Google's infrastructure should expect to absorb additional operational burden and latency variability compared to the managed cloud service.

- Spanner Omni is now GA, enabling Spanner to run on-premises, across clouds, or on a laptop.
- Colossus was replaced with a Colossus-like abstraction layer, and TrueTime with software-based time synchronization.
- There is no availability SLA for Spanner Omni.
- Practitioners are weighing the move in terms of tail latency and operational toil.