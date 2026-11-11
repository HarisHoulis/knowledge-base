---
domain: ai-workflows
subdomain: agentic-engineering
concept: agentic-ai-operating-model
title: Fragments: November 10 — Scaling Agents, Token Costs, and Context Quality
sources:
  - title: "Fragments: November 10"
    url: "https://martinfowler.com/fragments/2026-11-10.html"
    author: "Martin Fowler"
---

# Fragments: November 10 — Scaling Agents, Token Costs, and Context Quality

Fowler's November 2026 fragments center on the shift of agentic AI from pilot to operating model. Drawing on the Thoughtworks Technology Radar, he notes that a small, co-located team can make almost anything work with agents, but scaling to hundreds of people surfaces a second layer of problems: shared context between teams, token bills, increased review demands, what agents are allowed to reach and change, and ownership of the shared harness. He frames the enterprise questions as shared context, token cost, cognitive load, security, and platform building — distinct but interdependent — while insisting these tools should serve humans (martinfowler.com).

On economics, Fowler relays Ben Thompson's analysis that bipartisan opposition to new data centers will constrain token supply, raising token costs and benefiting owners of existing data centers; Fowler adds that incumbents may quietly lobby for regulation that blocks new competitors. He also cites Hadley Wickham's finding that per-token API pricing does not appear significantly subsidized, though subscription plans are (with training costs excluded from the analysis).

On research, he highlights "Weight-Space Programming" work suggesting models can infer what a network was trained to do from raw weights and write small game-playing networks from scratch, plus Simon Willison's follow-up examining whether an LLM can identify which game four simple networks were trained to play from weights alone. He also covers Houck et al's CAFE(S) framework for assessing the quality of assembled agent context, including "context smells," and Cindy Sridharan's observation that roughly 70% of her token spend now goes to verifying patches versus 20-30% to creating them — a pattern echoed in enterprise use of guardrails and evals.

- Scaling agents from a small team to an enterprise surfaces shared context, token cost, cognitive load, security, and platform-building problems that must be addressed together
- Opposition to new data centers may raise token costs and benefit owners of existing capacity; incumbents may even favor regulation that blocks new entrants
- Per-token API pricing appears largely unsubsidized, though subscription plans are, per Hadley Wickham's analysis
- Research on reading and editing model weights (Weight-Space Programming) suggests models can infer and reproduce network behavior from weights alone
- Verification dominates agent token spend — roughly 70% verifying versus 20-30% generating patches, per Cindy Sridharan