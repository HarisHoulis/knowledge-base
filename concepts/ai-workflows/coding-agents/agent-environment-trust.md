---
domain: ai-workflows
subdomain: coding-agents
concept: agent-environment-trust
title: All Code Is Slop (Except Mine): Building Trust in Agent Environments
sources:
  - title: "All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI"
    url: "https://www.youtube.com/watch?v=O_zcc6Xl12g"
    author: "AI Engineer"
    date: "2026-11-14"
---

# All Code Is Slop (Except Mine): Building Trust in Agent Environments

Lauren Tan ("Potato") of SpaceXSI argues that the core challenge of agentic software development is maintaining or improving code quality while dramatically increasing productivity, and that this ultimately comes down to trust—not blind trust, but investing in the agent's environment so agents reliably do the right thing. After half a year of investment, she reached a point where she could send 3,000 pull requests to production, many while sleeping. She frames the goal as a "software factory," though she prefers to reduce it to trust built through environment design.

She presents an inverted pyramid of where to spend time on agent environments. The first two levels are deterministic and based on your own code: good API design, architecture, refactoring, linters, type systems, compilers, and testing—used together to restrict agent actions and force correctness by default. Above that sit verification (runtime and formal) for detecting errors and checking invariants, and finally descriptive instructions like rules, skills, and agents.md files, which require judgment. Her guidance is to convert fixes into deterministic checks rather than adding lines to rules files, since code is easier to reproduce and inspires more trust.

Because the codebase is the largest input to agents, she likens it to a garden: agents copy whatever patterns they see, so workarounds, anti-patterns, obsolete code, and technical debt spread like weeds. Engineers now act as gardeners tending hundreds or thousands of agents, with code arriving as a near-continuous flow rather than a few pull requests a day. She illustrates with Dune, a Next.js-like framework for Electron apps built for Grokbot, which encodes lessons as linting rules—for example, disallowing useEffect in product code because it requires subtlety that agents handle poorly, allowing it only inside the Dune API. Another pattern is conveying context through directory structure to prevent agents from importing main-thread code into the rendering thread.

- Trust in agents comes from investing in their environment, not blind faith; it took about half a year to reach thousands of merge requests, many issued while sleeping.
- Prioritize deterministic constraints—API design, architecture, linters, type systems, compilers, tests—over prose rules in agents.md, since code-based checks are reproducible and inspire more trust.
- Treat the codebase as a garden: agents imitate existing patterns, so anti-patterns and tech debt spread like weeds and must be cleaned up.
- Encode hard-won lessons as lint rules and framework limitations (e.g., banning useEffect in product code in Dune) rather than relying on code review.
- Use directory structure to convey context and prevent agent mistakes such as importing main-thread code into the rendering thread.