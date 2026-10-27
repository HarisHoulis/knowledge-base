---
domain: system-design
subdomain: ai-sre-oncall
concept: ai-incident-investigation
title: AI SRE: What It Is, How It Changes On-Call, and Whether It Works
sources:
  - title: "AI SRE: what is it, how could it change on-call – and does it work?"
    url: "https://newsletter.pragmaticengineer.com/p/ai-sre"
    author: "Gergely Orosz"
    date: "2026-10-27"
---

# AI SRE: What It Is, How It Changes On-Call, and Whether It Works

AI SRE tooling is gaining traction as a way to speed up incident investigation, driven by rising deploy frequency from AI coding agents. Using the reliability formula I = C x P (incident rate = change rate x failure probability), the article notes that PR frequency has roughly doubled in a year at many companies, and Rootly data shows pages are up, with outside-business-hours pages nearly doubling. This makes investing in better on-call tooling a natural response.

The term "AI SRE" is used reluctantly by vendors (Rootly, incident.io, ResolveAI) since SREs do far more than handle alerts, but no better name has stuck. In practice, these tools focus on the investigation phase: inspecting alerts, dashboards, runbooks, and logs/observability data. Agents typically fan out subagents, interact with engineers in Slack incident channels, and take steering instructions. A key tension is trust: effective agents need broad access to telemetry, logs, and source code, which pushes larger companies to build in-house tools rather than grant vendors that access.

Vendors differ on remediation: incident.io hands incident context to engineers' own coding agents, ResolveAI writes simple PRs itself and delegates larger changes, and Rootly aims for autonomous PR merging with a verifier agent, though all current PRs require human approval. All three vendors rebuilt their investigation agents at least once; ResolveAI went from a scripted workflow (2024) to a single agent with a knowledge graph (2025), which suffered context rot, self-confirmation, and lack of memory, to a multi-agent system (2026) with independent Investigator, Verifier, and Communicator roles.

Accuracy work includes adversarial verification agents, mixing models, evals, and backtesting, though measuring accuracy is highly company- and team-specific. Speed and cost tradeoffs are managed via model routing, lean prompts, and cache hit rate tracking. Fully autonomous stage demos remain unrealistic, but AI triaging pager calls and silencing unimportant ones is becoming common. On-call engineers should expect fewer but harder pages, a new category of AI-related outages, and deskilling risk, making incident response simulations worth considering.

- Incident rate rises with deploy frequency (I = C x P); AI agents have roughly doubled PR frequency, and pages are up, especially outside business hours.
- AI SRE tools mainly accelerate incident investigation in Slack, fanning out subagents and pulling telemetry, logs, and deploy data.
- Broad data access requirements create a trust barrier, pushing mid-size and larger companies to build in-house investigation agents.
- Vendors rebuilt investigation agents multiple times; ResolveAI moved to a multi-agent Investigator/Verifier/Communicator design to counter context rot and self-confirmation.
- Fully autonomous remediation isn't real yet, but AI pager triage is growing; expect fewer but harder pages and deskilling risk for on-call engineers.