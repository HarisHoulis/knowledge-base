---
domain: ai-workflows
subdomain: agent-security
concept: lethal-trifecta
title: Your Agent Is a Lethal Trifecta (And What to Do About It)
sources:
  - title: "Your Agent Is a Lethal Trifecta (And What to Do About It) — Kim Maida, Keycard"
    url: "https://www.youtube.com/watch?v=ws9XcGGPBDk"
    author: "AI Engineer"
    date: "2026-10-12"
---

# Your Agent Is a Lethal Trifecta (And What to Do About It)

Kim Maida's talk demonstrates how a typical incident-handling agent—one that reads tickets, queries customer data, and calls cloud APIs—can cause serious harm when given excessive access. In a series of examples, the agent leaks customer data, deletes a production database, reboots a server, and scales a service from four to 40 pods, incurring $420 per hour in costs, all while acting on its own judgment [source].

The core problem is what Simon Willison calls the "lethal triumvirate": the combination of access to private data, exposure to untrusted content, and the ability to communicate externally. These are exactly the capabilities that make agents useful—reading mail or CRM data, researching via the internet or GitHub, and using external tools like APIs or SaaS platforms—but together they open wide doors for attackers [source].

Maida argues that these incidents stem from giving agents far more access than they need. Even human-in-the-loop approval doesn't fully solve the problem, because it simply shifts access control to a user who may be tired of requests, moving the security problem up the chain rather than eliminating it [source]. The talk sets up a discussion of what to do about this excessive-access problem, though the transcript cuts off before detailing the full solution.

- The "lethal trifecta" combines private data access, untrusted content exposure, and external communication—the same capabilities that make agents useful also make them dangerous.
- Agents with excessive rights can autonomously cause data leaks, production outages, and unexpected costs, as shown in the incident-handling demo.
- Human-in-the-loop approval shifts rather than solves the access-control problem, since tired users may rubber-stamp requests.
- The root cause is granting agents more access than they need; the talk promises mitigation strategies but the transcript ends before covering them.