---
domain: ai-workflows
subdomain: context-engineering
concept: context-is-the-next-frontier
title: Building Agents Is Trivial Now, Context Is the Next Frontier
sources:
  - title: "Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked"
    url: "https://www.youtube.com/watch?v=HvMyYLTfvhg"
    author: "Jeff Ng"
    date: "2026-08-21"
---

# Building Agents Is Trivial Now, Context Is the Next Frontier

Jeff Ng, founding engineer at Unblocked, argues that the infrastructure and tooling for building AI agents have matured so quickly that the mechanical act of constructing an agent has become trivial. He notes that six months ago, building an agent required a dedicated team and roughly a quarter of work, but now cloud providers like Cloudflare, Vercel, and AWS, combined with frameworks like Flu, have abstracted away much of the complexity. Defining an agent today is largely a matter of choosing a model, writing instructions, exposing tools and skills, and specifying a sandbox location.

However, Ng emphasizes that despite this ease of construction, agents still "confidently get things wrong." He walks through the supporting systems that were previously necessary—checkpoint and state persistence, sandbox infrastructure, and observability—calling them "taxes" that do not improve an agent's underlying capabilities. With modern primitives, teams can focus on the core agent logic instead of these operational concerns.

The real challenge, he argues, is context. Ng demonstrates a Linear issue enrichment agent he built that fetches tickets, searches code, and proposes next steps. In one example, the agent analyzed a degradation in an agentic QA pipeline and recommended re-enabling async dispatch—a plausible suggestion that was actually wrong, as that change had already caused an outage. This illustrates that the next frontier in AI engineering is not building agents, but providing them with the right context to make correct decisions.

- Agent development has shifted from building custom infrastructure to composing cloud primitives and framework abstractions.
- State persistence, sandboxes, and observability are necessary operational 'taxes' that do not enhance agent intelligence.
- Defining an agent now boils down to model selection, instructions, tools/skills, and sandbox configuration.
- The primary failure mode of agents is confidently wrong outputs due to insufficient or misleading context.
- Context engineering—not agent construction—is the next major challenge in AI workflows.