---
domain: engineering-culture
subdomain: ai-native-engineering
concept: ai-native-engineering-velocity
title: How Software Engineering Is Changing: A Tale of Two Eras
sources:
  - title: "How software engineering is changing: a tale of two eras"
    url: "https://newsletter.pragmaticengineer.com/p/how-software-engineering-is-changing"
    author: "Gergely Orosz (guest essay by Neil Kakkar)"
    date: "2026-11-03"
---

# How Software Engineering Is Changing: A Tale of Two Eras

Neil Kakkar, a software engineer with nine years of experience across Bloomberg, PostHog, and the AI-native startup Tano, compares his output and working style across these workplaces. At Bloomberg he shipped the fewest pull requests (PRs); at PostHog, a fast-moving pre-AI startup, he shipped 2.4x as many; at Tano, founded after AI agents emerged, he ships roughly 11x more PRs than at PostHog, or about 200+ per month versus 8-20 previously. He attributes the jump primarily to AI tooling, particularly Claude Code Desktop, which can build entire features end to end with little hand-holding.

The shift removes old constraints and introduces new ones. At Tano, engineers work independently, with one person owning a feature across design, frontend, and backend, eliminating the communication overhead that slowed multi-person efforts at PostHog. Human code reviews are optional and usually replaced by an automated review agent running in CI, with a stronger on-demand agent for risky changes. The team accepts that things will break and fixes forward quickly; Kakkar notes a currency-handling bug where an agent assumed every currency has 100 minor units, and a blocking Postgres migration that stalled ingestion, both caught and fixed fast. The revert rate is reportedly 6x lower than before, and median time to merge is under an hour.

New constraints include context switching across 3-5 concurrent workstreams, agents that take 1-2 hours per feature run, loss of shared context, less focus on design, and worries about AI plan limits. Product management responsibilities also merge into engineering: Tano has no product managers, and engineers set direction with context from the CEO and CTO. Kakkar argues that everyone must be onboard with AI to realize the benefits, that encouraging experimentation matters, and that many existing technologies and processes crack under the change.

- AI-native workflows enabled roughly an 11x increase in PR output at Tano versus a pre-AI PostHog baseline, with agents building full features end to end.
- Removing mandatory human code review and communication overhead lets one engineer own a feature across design, frontend, and backend, but trades off against more breakage fixed forward.
- Automated review agents in CI catch many issues, yet domain-specific mistakes (e.g., currency minor units) and risky migrations still slip through and require fast remediation.
- New bottlenecks replace old ones: context switching across 3-5 parallel agent runs, agents taking 1-2 hours per feature, lost shared context, and AI plan limits.
- Engineering and product roles merge at small AI-native companies; Tano has no product managers, and engineers set direction with context from leadership.