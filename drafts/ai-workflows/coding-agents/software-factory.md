---
domain: ai-workflows
subdomain: coding-agents
concept: software-factory
title: Harness Engineering: How to Build a Software Factory
sources:
  - title: "Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl"
    url: "https://www.youtube.com/watch?v=X6l4lpA0_NY"
    author: "AI Engineer"
    date: "2026-10-06"
---

# Harness Engineering: How to Build a Software Factory

Dru Knox, Head of Product and Design at Tessl, argues that "harness engineering" is a new discipline in agent development: the practice of building a software factory, defined as any agent-based system where all of the end product delivered to users is created by agents, while the software development teams focus on building and improving that factory itself. In this model, each team member effectively becomes a developer of internal tools [1].

The factory is assessed against three pillars, in order. Autonomy is how much human intervention is needed to get the right result — how often people must fix code or tell the agent how to build. Automation is how freely agents can be let to work — how much you must verify or build trust in a decision before you make it. These are related but distinct: an agent can solve tasks correctly the first time (high autonomy) yet still be manually reviewed line by line (low automation), and Knox argues you must build autonomy before moving to automation. Quality — how good the product is for users, measured with familiar signals like user analytics, test quality and coverage — is the third pillar and is maintained while the other two improve [1].

The claimed benefit of a software factory is quality rather than raw speed. Knox notes the initial assumption that factories mainly ship features faster, with a short-term slowdown justified by ROI, but argues that as agents improve, the backlog effectively disappears: teams gain time for test-quality work and architectural refactoring that they previously never had time for. He acknowledges possible minimal quality degradation during the transition, but expects better code quality to emerge, along with a significant change in how teams collaborate [1].

The talk targets practitioners already using coding agents who run multiple sessions in parallel and find that agents handle simple and medium-complexity tasks correctly — that is the point at which harness engineering becomes relevant. Knox states that the techniques are not exclusive to Tessl and work with any stack, though he indicates Tessl's product simplifies them [1].

- A software factory is defined as an agent-based system where the entire user-facing product is produced by agents, and dev teams focus on improving the factory's autonomy, automation, and quality.
- The three pillars, in order, are autonomy (human correction needed), automation (how freely agents can work without verification), and quality (product quality, measured like usual analytics and test metrics); autonomy must be built before automation.
- The primary expected benefit is improved quality, not just speed: the backlog nearly disappears, freeing time for test quality and architectural refactoring.
- It is a prerequisite to already use coding agents across multiple parallel sessions on tasks that agents solve correctly — this is not a starting point for teams new to coding agents.