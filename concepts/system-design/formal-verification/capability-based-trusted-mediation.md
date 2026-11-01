---
domain: system-design
subdomain: formal-verification
concept: capability-based-trusted-mediation
title: Verifying Code That Calls Code You Can't Trust
sources:
  - title: "Verifying Code That Calls Code You Can't Trust • Sophia Drossopoulou • Bug Bash EU 2026"
    url: "https://www.youtube.com/watch?v=iXD6NvG8k7A"
    author: "GOTO Conferences"
    date: "2026-10-21"
---

# Verifying Code That Calls Code You Can't Trust

Sophia Drossopoulou's Bug Bash EU 2026 talk addresses the problem of open systems, where trusted internal code is tightly intertwined with untrusted external code whose behavior may be unknown or adversarial. Programmers must reason about the potential effects of calls to external code even when that code cannot be inspected or trusted.

The proposed approach is defensive: internal code restricts the effects of external calls by ensuring those effects can only be caused through access to certain capabilities. This combines capability-based access control with effect specification so that verification can account for untrusted callees via trusted mediation rather than full inspection of external code.

The talk's original title frames the work as specification and verification of robust open systems, bringing formal verification, programming languages, and security together around the challenge of trusting code you cannot see.

- Open systems mix trusted internal code with untrusted, potentially adversarial external code
- Callers must account for effects of external calls even when callee code cannot be inspected
- Defensive internal code limits external effects by gating them behind specific capabilities
- Trusted mediation plus effect specification enables verification of such systems