---
domain: ai-workflows
subdomain: agent-architecture
concept: harness-engineering
title: Harness Engineering: Building the Production Cage for Powerful Domain Agents
sources:
  - title: "Harness Engineering: Building the Production Cage for Powerful Domain Agents — Mike Chambers, AWS"
    url: "https://www.youtube.com/watch?v=gxVZ_1tuuq4"
    author: "Mike Chambers (AI Engineer)"
    date: "2026-09-14"
---

# Harness Engineering: Building the Production Cage for Powerful Domain Agents

Mike Chambers, a senior AI specialist developer advocate at AWS, argues that there are two distinct categories of agents: the agents we use (tools like Claude Code, Cursor and Kiro, plus general productivity agents) and the agents we build. He says these are quite separate concerns even though they chain together — you might build an agent that someone else uses. The distinction drives how much care you should apply: token maxing and similar optimizations are fine for agents you use, but for agents you build "think about it carefully" and put it together in a way that works for the audience who will use it.

He offers a working definition of a harness: take an agent, remove the model part from it, and everything that is left is the harness. He grounds this in the dictionary definition of a harness — "a set of straps and fastenings used to control an animal" — noting that if you swap the animal for a model, the metaphor holds up well. He also points to existing writing on the topic, including an article from LangChain and a piece on martinfowler.com on harness engineering for coding agents, as better elaborations than the bare dictionary definition.

Chambers' own background frames the talk: he worked in 2023 with a colleague and Andrew Ng on a generative AI with LLMs course approaching half a million enrollments, built an MCP Lambda handler in 2025 that is still downloaded around 35,000 times a month, and in 2026 AWS is a founding member of an agent-focused foundation under the Linux Foundation. He notes he had reread the session abstract and realized he promised live coding, which he intends to deliver in the session.

The transcript is truncated mid-sentence during his explanation of harnesses in the context of an agent that we use, so the full walkthrough of harness engineering practice is not captured in the source.

- Agents split into two categories — agents we use (Claude Code, Cursor, Kiro, productivity agents) and agents we build — and they should be treated differently; token maxing is fine for the former but not automatically for the latter.
- A harness is defined as the agent minus the model: whatever remains is the harness.
- The dictionary definition of a harness ('straps and fastenings used to control an animal') maps onto controlling a model.
- Prior art referenced includes a LangChain article and a martinfowler.com article on harness engineering for coding agents.