---
domain: ai-workflows
subdomain: agent-identity
concept: tethered-agents
title: Tethered: Our Agents Are Us — Shu Fang, Two Sigma
sources:
  - title: "Tethered: Our Agents Are Us — Shu Fang, Two Sigma"
    url: "https://www.youtube.com/watch?v=wCIYViPd4SU"
    author: "AI Engineer"
    date: "2026-09-03T14:30:21+00:00"
---

# Tethered: Our Agents Are Us — Shu Fang, Two Sigma

The talk also highlights two major dangers. First, internal threat: when both a person and their agent share the exact same identity, it becomes hard to audit and attribute actions to a human or an agent, which is critical in a regulated industry. Second, LLMs require external network access for web search and current data, which creates a vulnerability surface. Fang frames agents as 'tethered'—connected to and indistinguishable from the user—which raises practical and security challenges that organizations must address.

- Two Sigma gives every employee a cloud agent that can be used from mobile, Slack, or browser but runs remotely on infrastructure.
- Running agents under separate machine identities is unviable due to permission sync, licensing, and multi-identity data conflicts; agents run under the same user identity.
- Existing Kubernetes per-user namespaces and identity sidecars are repurposed to run agents on behalf of users.
- Identity sharing creates audit and attribution challenges: it is hard to tell whether an action was performed by a human or an agent.
- Agents need external network access for current information, which introduces security vulnerabilities.