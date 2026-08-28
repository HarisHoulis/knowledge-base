---
domain: engineering-culture
subdomain: ai-augmented-engineering
concept: citizens-agents-experts
title: Citizens Build, Agents Execute, Experts Govern
sources:
  - title: "Citizens Build, Agents Execute, Experts Govern"
    url: "https://martinfowler.com/rachels-ramblings/citizens-agents-experts.html"
    author: "Rachel Laycock"
---

# Citizens Build, Agents Execute, Experts Govern

The article explores the widening gap between what non-engineers build with AI and what enterprise software engineering entails. Laycock observes that AI has dramatically increased the number of people who can turn ideas into working software, but building a weekend app is very different from introducing software into a highly regulated production environment. The key distinction lies in questions about data protection, dependency failures, maintainability, auditability, scalability, and operational visibility—questions that don't arise in demos unless experienced engineers are in the room (Laycock, "Citizens Build, Agents Execute, Experts Govern").

Laycock introduces the framework "Citizens build, agents execute, experts govern" to describe where value is moving. Citizens (non-engineers) express ideas through software, agents handle execution by writing code and iterating quickly, and experts provide governance through design judgment, architecture, security, resilience, operability, compliance, and cost management. Rather than making experienced engineers less important, AI makes them more leveraged—they shift from building features to creating the environment, guardrails, and feedback loops that allow many features to be built safely by others and by agents. The article emphasizes that software's purpose is to run safely in production, and that organizations run on trust, not code (Laycock, "Citizens Build, Agents Execute, Experts Govern").

- AI allows non-engineers to build software, but enterprise production software requires far more than features: security, resilience, operability, compliance, and maintainability.
- Experienced engineers provide critical judgment: knowing what good design looks like, understanding risks, and deciding whether software can be trusted in production.
- The future organization will see citizens building, agents executing, and experts governing—engineers move from writing every feature to designing guardrails and platforms that enable safe, fast development.
- Software exists to run in production and solve problems safely; as Laycock states, 'Organisations don't run on code. They run on trust.'