---
domain: ai-workflows
subdomain: agentic-development
concept: production-readiness-caution
title: Why Good Developers Are Wary of Agentic Development
sources:
  - title: "Why are good developers so wary of agentic development?"
    url: "https://martinfowler.com/rachels-ramblings/good-devs-wary.html"
    author: "Rachel Laycock"
---

# Why Good Developers Are Wary of Agentic Development

Rachel Laycock observes that many experienced developers hesitate to go "all in" on coding agents, and argues this caution is not mere nostalgia or job anxiety but a well-founded concern about production readiness. Thoughtworkers have long prioritized building the right thing and building it right, championing practices like continuous integration, pairing, automated testing, and continuous delivery. Early coding agents made it easy to produce code that no one would want near production, and even improved tools leave experienced developers asking whether behavior is correct, boundaries are right, the system can evolve, and what happens when something fails [martinfowler.com/rachels-ramblings/good-devs-wary.html].

The deeper question is trust: nearly every production system today was built by hand by people we could trust, while agent-built systems have not yet been lived with. Laycock values the judgment senior technologists bring—challenging premises, recognizing patterns from past failures, spotting organizational problems hidden in technical ones—and sees that judgment as exactly what hesitant developers are trying to protect. They are not refusing assistants; they are reluctant to take their hands off the wheel without confidence in the guardrails.

A week-long experiment where agents wrote all the code reinforced this. The team spent roughly two-thirds of their time at the whiteboard working out the domain, boundaries, and plans, and one-third building the harness of tests, contracts, architecture checks, and pipeline. The application ran, but the build was frequently red—undermining the reassurance continuous integration was meant to provide. Laycock connects this to DORA's 2025 finding that AI adoption raises throughput but lowers delivery stability, and to open questions about TDD, test strategy, batch size, and how CI handles larger units of work.

She closes with a skiing analogy, sharpened by Martin Fowler: unlike a groomed slope, agentic development is uncharted backcountry where we don't yet know which skills matter. Built is not the same as working in production. Leaders must distinguish useful concerns from resistance and create room for experimentation, while developers must bring their experience into experiments and be willing to test their assumptions.

- Experienced developers' wariness stems from knowing that built is not the same as working in production, not from fear of job loss or love of coding.
- In an all-agent experiment, teams spent about two-thirds of time at the whiteboard on domain and boundaries and one-third on the test/architecture harness, yet the build was frequently red.
- DORA's 2025 research links AI adoption to higher throughput but lower delivery stability, echoing the problems continuous delivery and DevOps were created to solve.
- Open questions remain around TDD's role, test strategy, design up front, and batch size as teams move from stories to epics.
- Leaders should distinguish legitimate concerns from reluctance and fund real experimentation; developers should bring their judgment and be ready to revise assumptions.