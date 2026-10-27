---
domain: ai-workflows
subdomain: agent-security
concept: agent-fleet-monitoring
title: 300 Agents, 60 People: Securing an Internal Agent Fleet
sources:
  - title: "300 Agents, 60 People: How We Secured Our Own AI Agents - Aiden Sochowski, Runlayer"
    url: "https://www.youtube.com/watch?v=BgLdvF7Qkh8"
    author: "AI Engineer"
    date: "2026-10-27"
---

# 300 Agents, 60 People: Securing an Internal Agent Fleet

Aiden Sochowski, a founding engineer at Runlayer, describes how his roughly 50-60 person company runs over 300 agents daily and how it went about securing them. He notes that in most companies people have little visibility into the MCP clients and agents running locally on their machines, authenticating against random product agents and MCP servers, so nothing really counts. Runlayer's response was to deploy a gateway and centralize logging of every session and tool call to a synchronizer, which surfaced how many agents actually exist and how they are distributed by topic and risk.

He stresses that not all agents are equal: some carry too many tools, giving them a much larger blast radius, and they connect systems built for a different era with different classes of data. Agents can increase the risk of mixing such data far more than the deliberate API integrations of the past. A colleague's visualization maps teams as galaxies, each agent as a planet representing a launch, and drills into the MCP servers accessed and actions performed.

Every tool call is treated as an attack surface: a chance to read hostile data, take destructive actions, or steal data. His concrete example is an attacker emailing a company asking for a list of current leads; a naive agent with excessive permissions could list them on a calendar and leak the data. Getting each user to independently embrace all the tools an agent can use is complicated, and defining policies in an agent gateway is hard because blocking a tool is context-dependent — sometimes it is safe.

One mitigation he mentions is a trained classifier model that thoroughly checks every email read for embedded instructions, though nothing is 100% accurate or effective.

- A 50-60 person company can run 300+ agents daily, far outnumbering the people who manage them.
- Centralized gateway logging of every session and tool call reveals agent inventory, topics, and risk levels.
- Agents with excessive tools have a larger blast radius and raise data-mixing risk beyond traditional API integrations.
- Every tool call is an attack surface for prompt injection, destructive actions, or data theft.
- Gateway policies are hard because blocking a tool is context-dependent; classifier-based checks on inputs like email are only partially effective.