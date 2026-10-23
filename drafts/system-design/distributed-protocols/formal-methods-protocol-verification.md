---
domain: system-design
subdomain: distributed-protocols
concept: formal-methods-protocol-verification
title: Formal Methods and AI for Reliable Database Protocols
sources:
  - title: "Formal Methods & AI for Reliable Databases • Anatoliy Bilenko & Alberto Carretero • Bug Bash EU 2026"
    url: "https://www.youtube.com/watch?v=ds9np_fgI-U"
    author: "GOTO Conferences"
    date: "2026-10-23"
---

# Formal Methods and AI for Reliable Database Protocols

Anatoliy Bilenko and Alberto Carretero of Canonical describe the toolchain they use to design and verify distributed database protocols for Dqlite. Writing a protocol's happy path is easy, but failures—lost, duplicated, or corrupted messages, process crashes, and Byzantine faults—explode the state space and make correctness hard to reason about. They argue for a shared formal language, starting with finite state machines, so distributed teams can communicate about protocols precisely rather than through ad-hoc abstractions or diagrams.

The talk frames protocol development as a long-term social problem as well as a technical one: designs drift from code, implicit assumptions are lost when engineers leave, and distributed teams think in incompatible representations. Formal specifications keep assumptions explicit and durable across the decades-long life of such systems.

Their verification suite combines formal specification and verification, TLA+, Antithesis, Jepsen, global state reconstruction, and model-based and property-based testing. The speakers position these as complementary techniques for defining, designing, and ensuring the correctness of protocols rather than a single silver bullet.

- The happy path of a protocol is easy; correctness problems emerge from failures, crashes, and Byzantine faults that multiply states.
- Formal methods give distributed teams a shared, explicit language (starting with state machines) for protocol design.
- Design-code drift and engineer turnover make implicit assumptions dangerous in long-lived systems.
- Canonical's toolchain spans TLA+, Antithesis, Jepsen, global state reconstruction, and model- and property-based testing.