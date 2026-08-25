---
domain: engineering-culture
subdomain: ai-adoption
concept: llm-adoption-risks
title: Fragments: AI Risks, Agent Operations, and LLM-Speak
sources:
  - title: "Fragments: July 21"
    url: "https://martinfowler.com/fragments/2026-07-21.html"
    author: "Martin Fowler"
    date: "2026-07-21"
---

# Fragments: AI Risks, Agent Operations, and LLM-Speak

Martin Fowler wraps up notes from the second Future of Software Development Retreat, referencing the full Thoughtworks report that highlights five findings: verification is now the bottleneck, 'harness engineering' is emerging, there is an apprenticeship crisis, the executive/engineer expectation gap is a major risk, and legacy modernization offers the clearest near-term value. Fowler then examines the clash between boards pushing LLM adoption and engineers wary of risks, illustrated by a story of an ML model trained on desert equipment applied in the arctic, causing a $100 billion fire loss because of rotting mosquitoes (Fowler, 2026, https://martinfowler.com/fragments/2026-07-21.html).

- Verification is now the bottleneck, not code generation; organizations must build harnesses and feedback loops.
- Vibe-coding by citizen developers creates shadow IT and security risks requiring deterministic controls and separate infrastructure.
- LLMs aid operations by analyzing event streams, but auto-remediation is risky because incident resolution is non-linear.
- DSLs provide a promising pattern for constraining LLM behavior, improving token efficiency and security.
- LLM-generated prose is increasingly repulsive to readers; writers should read their work aloud to retain a human voice.