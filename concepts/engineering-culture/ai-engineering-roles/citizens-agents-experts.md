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

The article explores the widening gap between what non-technical people can now build with AI over a weekend and the realities of enterprise-grade software. While such apps are genuinely useful, they lack the rigor required for production systems: data protection, dependency resilience, long-term maintainability, audit compliance, scalability, and observability. The author argues that this is not a gap in technology but in understanding what software engineering actually entails, and that experienced engineers become more important rather than less because they provide the judgment needed to decide whether software can be trusted in production (Laycock, martinfowler.com/rachels-ramblings/citizens-agents-experts.html).

The author introduces a framework: "Citizens build, Agents execute, Experts govern." Citizens are non-engineers who use AI to turn ideas into software; agents handle the coding, testing, and refactoring at high speed; and experts provide governance, architecture, security, and operational oversight. This does not mean engineers become obsolete. Instead, their role shifts from manually writing every feature to designing the guardrails, platforms, and feedback loops that allow large numbers of citizen-driven and agent-generated features to be delivered safely (Laycock, martinfowler.com/rachels-ramblings/citizens-agents-experts.html).

Observations from a FOSE conference reinforced that the future of software development centers on design, governance, learning, and judgment rather than coding itself. Humans spend time defining what good looks like, making trade-offs, and reviewing agent output. When agents can generate code quickly, good design matters more, not less. The article concludes that executives and engineers are both correct but looking at different parts of the system: executives see that anyone can build software, while engineers see that someone must live with it. Ultimately, organizations run on trust, not just code, and engineering judgment is the scarce resource that enables creativity to scale safely (Laycock, martinfowler.com/rachels-ramblings/citizens-agents-experts.html).

- AI dramatically increases who can create software, but weekend apps are not the same as enterprise-grade systems that require security, resilience, operability, and compliance.
- The real scarcity is engineering judgment: knowing what good looks like, understanding risks, and deciding whether working software is safe to trust in production.
- The framework 'Citizens build, Agents execute, Experts govern' describes where value moves, not just roles: citizens express ideas, agents execute, and experts create guardrails for safety.
- Experienced engineers become more leveraged, shifting from building features to designing the environment (platforms, practices, feedback loops) that enables safe, rapid creation by others and agents.
- Good design and governance matter more when agents generate large volumes of code, because humans must define quality and make trade-offs.