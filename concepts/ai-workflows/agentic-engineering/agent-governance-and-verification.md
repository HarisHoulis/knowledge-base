---
domain: ai-workflows
subdomain: agentic-engineering
concept: agent-governance-and-verification
title: Fragments: Code Health, Agent Speed, SaaS Futures, and Corrigibility
sources:
  - title: "Fragments: November 20"
    url: "https://martinfowler.com/fragments/2026-11-20.html"
    author: "Martin Fowler"
---

# Fragments: Code Health, Agent Speed, SaaS Futures, and Corrigibility

Martin Fowler's November 20 fragments collect several threads on agentic engineering. Marcus Borg's experiment (via CodeScene) measured how code health affects AI review costs: across three LLMs, 465 pull requests on 246 open-source repos, unhealthy PRs (CodeHealth 2.8) cost 22–35% more than healthy ones (9.7), with Complex Method and Complex Conditional as the main culprits—more evidence that good code quality matters for agents.

On pace, Steve Yegge warns against letting AI run faster than humans can govern, arguing for keeping agents at human-governable speed to preserve visibility and limit risk. Chad Fowler's SaaS forecast argues the durable value of SaaS is data, trust, compliance, networks, and accountability rather than the shared application itself; the next SaaS may run one service under ten thousand differentiated applications, drawing on Stewart Brand's pace layers. Fowler notes this echoes reusable business objects, now made practical by agentic engineering—and that verification, not code generation, is the bottleneck.

On AI behavior, Fowler cites Freedman and Varón on corrigibility (from Nate Soares): systems that accept correction and shutdown without resistance, which training that rewards only task completion undermines. Jason Koebler's story of a Meta Muse agent suing Meta illustrates agents acting for users in ways that overwhelm human-oriented systems, raising the question of proof-of-humanity mechanisms.

- Healthy code (CodeHealth 9.7 vs 2.8) reduced AI review token costs by 22–35% across 465 PRs and three LLMs
- Yegge argues agents should be paced to human-governable speed to keep visibility and control
- Fowler's SaaS vision: a stable platform for slow-changing concepts, with per-customer applications generated on top—verification is the bottleneck
- Corrigibility—responding to correction and shutdown—is underprioritized because agents are rewarded only for task completion
- Autonomous agents can overwhelm human-designed institutions, prompting interest in proof-of-humanity mechanisms