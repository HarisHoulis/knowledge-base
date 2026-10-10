---
domain: ai-workflows
subdomain: context-engineering
concept: context-graph
title: Why Your Company Needs a Context Graph (and How to Build It)
sources:
  - title: "Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge"
    url: "https://www.youtube.com/watch?v=cSz7aL2nl2U"
    author: "AI Engineer"
    date: "2026-10-09"
---

# Why Your Company Needs a Context Graph (and How to Build It)

Gil Feig, co-founder and CTO of Merge, argues that every company needs a "context graph" — a unified corporate intelligence layer that serves as the "brain" for its AI agents. Rather than delving into graph nodes and edges, he frames the context graph as a collection of components: external data from systems like NetSuite or Jira, structured context from third parties, static documents added deliberately, memories formed gradually through agent use, and skills. He stresses that the focus should be on why the graph is needed and how to structure it at a high level, not on specific technologies.

A central argument is that simply connecting a few MCP servers is insufficient. Using the example of asking "Why was Customer A upset last week?", he shows that a single-customer query can be answered by pulling Zendesk tickets, but broader questions — "Which customers were upset last week?" or "...in the last year?" — require downloading thousands of tickets in real time, causing timeouts. MCP does not fully solve these problems because the underlying API access patterns of platforms like Zendesk and Jira do not support real-time semantic search, and vendors have little incentive to add it since vectorization costs them money and reduces platform visits.

The proposed solution is a synchronization layer: companies must sync a local copy of their data rather than relying on live MCP search for deep or semantic queries. Feig also outlines the rest of his talk's agenda: levels of context and what data and logic belong in the graph, a context selection strategy for picking the most relevant content for agents at any given time, and traceability/origin — knowing where data came from, who requested it, when it appeared, and whether it is up to date.

- A context graph is a company's unified "brain" for AI agents, composed of external system data, structured context, static documents, memories, and skills.
- Connecting a few MCP servers is not enough: real-time API queries cannot handle broad or semantic questions across large datasets like a year of support tickets.
- Platforms like Zendesk and Jira lack semantic query endpoints because vectorization costs them money and reduces visits, so a synchronization layer with a local copy of data is required.
- Key design concerns include context selection (choosing the most relevant content per query) and traceability (origin, requester, timestamp, and freshness of data).