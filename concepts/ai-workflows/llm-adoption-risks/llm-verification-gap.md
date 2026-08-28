---
domain: ai-workflows
subdomain: llm-adoption-risks
concept: llm-verification-gap
title: Fragments: July 21
sources:
  - title: "Fragments: July 21"
    url: "https://martinfowler.com/fragments/2026-07-21.html"
    author: "Martin Fowler"
    date: "2026-07-21"
---

# Fragments: July 21

In this retreat wrap-up, Martin Fowler highlights the second Future of Software Development Retreat's key findings: code generation is no longer the bottleneck, verification is; 'harness engineering' is emerging; there's an apprenticeship crisis; the executive/engineer expectation gap is risky; and legacy modernization is the clearest near-term value pool ([Thoughtworks report](https://www.thoughtworks.com/content/dam/thoughtworks/documents/report/tw_future_of_software_engineering_europe_2026.pdf)). A cautionary tale about an ML model trained on desert equipment but used in the arctic led to a $100 billion fire loss due to decaying mosquitoes, emphasizing the need for context awareness and rapid feedback sensors.

The gap between engineers and boards is a central concern. Boards push LLMs for productivity while underestimating security risks. Vibe-coded citizen developer apps create shadow IT and amplify risks, requiring deterministic controls and separate infrastructure to tame the 'lethal trifecta' ([lethal trifecta](https://martinfowler.com/articles/agentic-ai-security.html#lethal-trifecta)). Some companies run board-level threat modeling sessions, and involving legal departments can help because they see LLM failures. Kelsey Hightower's observation is cited: 'The less busy work you have the less appealing these AI tools are'.

Many acknowledge an AI bubble, similar to the dotcom era, but note a difference: less excitement about building new things and more wariness. Cost-cutting drives board adoption, but token costs may temper enthusiasm. In operations, LLMs help with anomaly detection and incident understanding, but agents overestimated for incident resolution; they inject unrequested features and require careful documentation and human feedback.

A Stanford law professors' experiment found LLM answers to student questions preferred over human peers (75.33% win rate) but rarely harmful. DSLs are praised for making LLMs more reliable, token-efficient, and security-bound ([LLM and DSLs](https://martinfowler.com/articles/llm-and-dsls.html)). Finally, Fowler warns about 'LLM-speak' permeating writing, causing visceral reactions; he now encourages writers to reject AI polishing and use 'Say Your Writing' to preserve authentic voice.

- The bottleneck in AI-assisted development has shifted from code generation to verification, especially for security and context appropriateness.
- Executive/engineer expectation gaps and unmanaged citizen development are bigger risks than technical limitations.
- LLMs are useful for operations (anomaly detection, incident understanding) but overhyped for autonomous remediation; agents need human-in-the-loop and careful oversight.
- DSLs are a promising pattern for making LLM outputs secure, token-efficient, and reliable.
- AI-generated prose is increasingly discrediting writing; writers should prioritize authentic human voice and read their work aloud.