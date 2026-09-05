---
domain: ai-workflows
subdomain: multi-agent-systems
concept: agent-network-effects
title: Agents' Next Frontier: Agent-to-Agent and Network Effects
sources:
  - title: "Agents' next frontier: agent-to-agent and network effects — Jean-Denis Greze, Town"
    url: "https://www.youtube.com/watch?v=REascnFlq_8"
    author: "AI Engineer"
    date: "2026-09-03"
---

# Agents' Next Frontier: Agent-to-Agent and Network Effects

In this talk, Jean-Denis Greze, CTO of Town and former CTO of Plaid, reframes LLM-based systems as fundamentally a search problem: success depends on getting the right information into the context window before the model acts. He traces the evolution from manual context filling, to RAG, to agent-based search where agents use tools to explore content, emphasizing that the core challenge remains placing correct information in the context window (Greze, 2026).

Greze argues that a multi-agent world should be seen as an approximation of a single ideal agent with access to all relevant data. Such an agent would be extremely powerful but is impossible due to privacy and security constraints—no user would grant one agent unrestricted access to everything (including email, corporate data, and government records). Therefore, the real test of any multi-agent system is how well it approximates that ideal while respecting boundaries.

He then introduces five strategies for achieving context-rich agent interactions, starting with the first: closed access to everything within a trusted zone. Examples include a family agent with access to both spouses' emails, or an HR agent that can access all internal HR systems just like a typical HR employee. This strategy relies on creating agents that operate within defined trust boundaries to pull relevant data into the context window as needed.

- LLM systems are search tasks: the key is getting the right data into the context window before the model responds.
- Agent-based search is the latest evolution, following manual prompting and RAG, but still solves the same context problem.
- A multi-agent system should be evaluated by how closely it approximates a hypothetical single agent with universal access.
- Privacy and security make universal access impossible, so trusted-zone agents with full access to a defined area are the first strategy.
- A trusted-zone agent (e.g., a joint household agent or HR agent) can pool relevant data to produce better results than isolated agents.