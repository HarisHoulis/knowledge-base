---
domain: ai-workflows
subdomain: managed-agents
concept: claude-managed-agents
title: Building a Research Agent with Claude Managed Agents
sources:
  - title: "Build a Research Agent with Claude Managed Agents (Part 2 of 4)"
    url: "https://www.youtube.com/watch?v=FGftGOzfohc"
    author: "AI Engineer"
    date: "2026-10-12"
---

# Building a Research Agent with Claude Managed Agents

This workshop demonstrates using Claude Managed Agents (CMA) to build a research agent, starting with a simple chat interface and extending it into a multi-agent ecosystem. The presenter shows how to create an agent via a system request where Claude generates a name, description, and model choice, then configures an environment as a sandbox template with configurable access controls and package installation. The agent runs in the cloud, with the platform managing infrastructure, hosting, hardware, sandbox management, scaling, and event log storage, so developers only need to start a session, send events, and receive events back.

The workshop roadmap includes extending the agent to delegate tasks to sub-agents, giving it skills such as fetching SEC filings for individual tickers and analyzing specific forms, and performing asynchronous time-consuming agent tasks. It culminates in a map-reduce interface where a main agent delegates to many agents, plus a deployment API for scheduling recurring jobs at a given frequency for continuously updated long-term analysis. The session store was refactored between iterations to abstract and separate storage mechanisms into different components, virtualizing interfaces at the event level rather than tying them tightly to session mechanics.

- Claude Managed Agents handle infrastructure, hosting, sandbox management, scaling, and event log storage, letting developers focus on product logic
- Agents are created via a system request that generates name, description, and model, then configured with an environment sandbox template and toolkit access
- The workshop extends a basic chat agent into a multi-agent ecosystem with sub-agent delegation, custom skills like SEC filing retrieval, and map-reduce orchestration
- A deployment API enables scheduled recurring sessions for long-term analysis that stays continuously updated
- Session store design evolved to abstract storage mechanisms into separate components, virtualizing interfaces at the event level