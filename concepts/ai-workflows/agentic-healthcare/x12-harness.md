---
domain: ai-workflows
subdomain: agentic-healthcare
concept: x12-harness
title: Healthcare's Agent Bytecode: X12 as the Harness for AI Agents
sources:
  - title: "Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay"
    url: "https://www.youtube.com/watch?v=UyyOoJmuATU"
    author: "AI Engineer"
    date: "2026-08-19"
---

# Healthcare's Agent Bytecode: X12 as the Harness for AI Agents

Vasant Kearney argues that payer systems—phone lines, web portals, and X12 feeds—often contradict each other, and none represents ground truth [1]. He proposes treating X12 not as a file format but as a harness: a strict rule system that confines AI agents productively, similar to how a programming language confines code [1]. Every stage of the claim lifecycle maps to an X12 transaction, such as the 270 for eligibility checks, the 999 for syntax acknowledgment, and the 835 for payment records [1]. Thus, an agent making a phone call or driving a portal is effectively emitting the same transaction through another route, and everything can be normalized into an internal representation that is held as correct only until downstream evidence says otherwise [1].

Two constraints accompany this approach: enterprise memory must reside in a database rather than on local disk, to ensure logical separation, and a stronger model cannot simply be swapped in because better benchmark performance does not guarantee better integration within an existing system [1]. Kearney describes this posture as being 'AI pilled and AI skeptical at once'—embracing AI's potential while remaining critical of assumptions [1].

- X12 should be treated as a harness or contract, not ground truth; payer surfaces can agree on the wrong answer.
- Every claim lifecycle stage has an X12 transaction (e.g., 270, 999, 835), providing a unified abstraction for agent actions.
- Phone calls and portal interactions are equivalent to X12 transactions and can be normalized into a single internal representation.
- Enterprise memory must live in a database, not on local disk, to support logical separation.
- A better model on benchmarks is not automatically better when embedded in a system built around the previous model.