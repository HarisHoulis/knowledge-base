---
domain: engineering-culture
subdomain: ai-engineering-roles
concept: citizens-agents-experts
title: Citizens Build, Agents Execute, Experts Govern
sources:
  - title: "Citizens Build, Agents Execute, Experts Govern"
    url: "https://martinfowler.com/rachels-ramblings/citizens-agents-experts.html"
    author: "Rachel Laycock"
---

# Citizens Build, Agents Execute, Experts Govern

Rachel Laycock observes a growing gap between what non-technical people think software engineering is and what experienced engineers know it takes to run software reliably in production. She acknowledges that AI has enabled more people to build real, useful applications over a weekend—and that this is genuinely exciting—but she stresses that such an app is very different from enterprise software that handles customer data, depends on external systems, must survive audits, scale to millions of users, and alert operators before customers notice failures. These concerns only surface in the build process when an experienced engineer is in the room (Laycock, martinfowler.com/rachels-ramblings/citizens-agents-experts.html).

Laycock argues that experienced engineers become more important, not less, because they carry engineering judgment: knowing what good design looks like, understanding trade-offs, and deciding whether something that works today can be trusted in production tomorrow. At the FOSE gathering, teams spent their time designing specifications, letting agents work overnight, and reviewing results—with humans focusing on what good looked like rather than writing code themselves. This led Laycock to coin the phrase: "Citizens build. Agents execute. Experts govern." She clarifies this is not just about roles but about where value is moving: AI gives more people creative power, agents execute the code, but expertise is needed to govern whether that code deserves to exist in an enterprise system.

The future software organization, she proposes, is not one where everyone becomes a software engineer, nor one where engineers disappear. It is one where almost anyone can create software, agents increasingly handle execution, and engineers design the guardrails, platforms, engineering practices, and feedback loops that allow all that creativity to scale safely. Both executives and engineers are right in different ways: the executive sees that anyone can build software, while the engineer sees that somebody has to live with it, and the two views are simply different parts of the same challenge.

- Building a weekend app with AI is not the same as shipping and operating enterprise-grade software, which requires security, resilience, auditability, scalability, monitoring, and long-term maintainability.
- Software engineering value is shifting from writing code to exercising engineering judgment: defining what good looks like, assessing risks, and deciding whether software can be trusted in production.
- AI agents can generate code, tests, and features at unprecedented speed, but this makes good design and governance more important, not less.
- The model "Citizens build, agents execute, experts govern" captures a future organization where broad AI-enabled creativity is made safe by experienced engineers who design guardrails and feedback loops.
- Executives and engineers appear to describe different futures because they focus on different parts of the same system: creation versus operational trust.