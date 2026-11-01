---
domain: system-design
subdomain: distributed-systems-testing
concept: protocol-io-separation
title: Separating Protocol Logic from I/O for Deterministic Tests
sources:
  - title: "Separate Protocol Logic from I/O for Deterministic Tests • Somtochi Onyekwere • Bug Bash EU 2026"
    url: "https://www.youtube.com/watch?v=DhmcJK2nCK0"
    author: "GOTO Conferences"
    date: "2026-10-30"
---

# Separating Protocol Logic from I/O for Deterministic Tests

Somtochi Onyekwere (Fly.io) describes the difficulty of testing distributed protocols: they involve coordination across many nodes, message loss, reordering, timeouts, and node failures, and integration testing at scale (e.g. thousands of containers) is impractical and non-reproducible. While working on a new broadcast protocol for Corrosion, an open-source SQLite replication system used at Fly.io, the team wanted the protocol to be easy to test, deterministic, reusable, and simple.

- Distributed protocols are hard to test because of message loss, reordering, timeouts, and node failures, and large-scale integration tests are impractical and non-reproducible.
- The protocol is modeled as a state machine that receives events (message received, node joined/left, timer fired) and returns an output basket of actions instead of performing I/O itself.
- The protocol has no access to sockets or the clock, making it mostly pure functions that are simpler, reusable, and easy to test.
- The caller decides how messages and timers are actually sent, so mechanisms can be swapped out.