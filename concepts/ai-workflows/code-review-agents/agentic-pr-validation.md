---
domain: ai-workflows
subdomain: code-review-agents
concept: agentic-pr-validation
title: AI Writes More PRs. Who Validates Them?
sources:
  - title: "AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar"
    url: "https://www.youtube.com/watch?v=uuwDWRbxoYo"
    author: "AI Engineer"
    date: "2026-10-09"
---

# AI Writes More PRs. Who Validates Them?

Ali-Reza Adl-Tabatabai, co-founder of Guitar.ai (acquired by Sonar), argues that the centralized review phase — CI plus code review — is the critical path for delivering changes to production, and that AI is making this bottleneck worse. Because AI generates more and larger PRs, each potentially containing defects, development-cycle costs shift right: teams must either slow down for careful human review or auto-approve and risk production incidents, both of which reduce developer satisfaction and productivity (Adl-Tabatabai, 2026).

His proposed answer is an agent-based validation approach, originally built at Guitar.ai and now part of Sonar. The agent fully automates validation steps so that PRs become "green" and ready to merge, or are merged automatically. It inspects PRs and adds inline notes and comments, but aims to be noise-free by publishing only real, important issues. Teams can customize inspection rules, add their own checks, run automated workflows, and configure the system to block merges when concerns remain unresolved (Adl-Tabatabai, 2026).

The agent also analyzes CI failures and summarizes root causes, with particular strength at detecting flaky tests; users can set rules to automatically restart unstable tests, a popular feature. It can automatically fix code review issues and CI errors, either on request or by looping until all issues in a PR are resolved and the PR is green. Finally, rules and conditions can govern when agents automatically approve and merge green PRs (Adl-Tabatabai, 2026).

Adl-Tabatabai reports a clear trajectory toward fully automated PRs. Users first receive checks, become satisfied, and begin to trust the accuracy of results; then they grant the agent authority to block PRs; then they adopt auto-fix to move PRs to green; and finally they set up rules for automatic approval and merge as trust grows (Adl-Tabatabai, 2026).

- AI increases PR volume and size, shifting cost and risk into the centralized review phase (CI plus code review), which is already the critical path to production.
- Sonar's agent-based validation automates inspection, adds noise-free inline comments, analyzes CI failures, and detects flaky tests.
- The agent can auto-fix code review issues and CI errors, looping until a PR is green, and can block merges on unresolved concerns.
- Rules can enable automatic approval and merging of green PRs, and users show a trajectory from trusting checks to granting block authority to full auto-merge.