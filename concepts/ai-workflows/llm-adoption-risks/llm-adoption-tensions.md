---
domain: ai-workflows
subdomain: llm-adoption-risks
concept: llm-adoption-tensions
title: Fragments: July 21 - LLM Adoption, Risks, and Writing
sources:
  - title: "Fragments: July 21"
    url: "https://martinfowler.com/fragments/2026-07-21.html"
    author: "Martin Fowler"
    date: "July 21, 2026"
---

# Fragments: July 21 - LLM Adoption, Risks, and Writing

Martin Fowler's July 21 fragment wraps up notes from the second Future of Software Development Retreat, pointing to the Thoughtworks report's findings: code generation is no longer the bottleneck—verification is, 'harness engineering' is emerging, there's an apprenticeship crisis, the executive/engineer expectation gap is risky, and legacy modernization offers near-term value. Fowler highlights a disconnect between boards pushing for LLM adoption and engineers concerned about risks, illustrated by a story where an ML model optimized air filter replacements, saving $50 million but causing $100 billion in fire damage because it was trained on desert equipment instead of arctic conditions, where decaying mosquitoes create fire hazards (Fowler, 2026).

Fowler discusses the perils of 'vibe coding' by citizen developers, which creates shadow IT and security risks, and suggests using separate infrastructure and deterministic data-access controls. He notes that LLMs are useful in operations for anomaly detection and understanding code, but warns that agents over-estimate their ability to handle incidents, which often require adaptation and surprise handling. He also mentions that agent-developed code may include unrequested features, and emphasizes the need for documentation and feedback.

The article also touches on how LLMs are good at learning DSLs, which offer token efficiency and security boundaries, and reflects on the 'LLM-speak' phenomenon, where AI-generated prose is becoming a turn-off for readers. Fowler encourages writers to reject AI polishing and instead 'Say Your Writing' to retain a human voice, as the pervasive LLM style can discredit content.

- Code generation is no longer the bottleneck; verification is a key challenge.
- There is a significant gap between executive expectations and engineer concerns about LLMs, especially around security risks.
- Citizen-developer vibe coding creates shadow IT and security vulnerabilities that need controls.
- LLMs are helpful for operations, but not yet reliable for autonomous incident resolution due to their linear approach.
- LLM-generated prose can discredit writing; preserving a human voice is increasingly important.
- DSLs work well with LLMs, providing token efficiency, security, and guardrails.