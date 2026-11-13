---
domain: ai-workflows
subdomain: agent-explainability
concept: decision-token-interpretability
title: Opening the Black Box: Critical Explainability for AI Agent Tool Selection with Kiji Inspector
sources:
  - title: "Presentation: Opening the Black Box: Critical Explainability for AI Agent Tool Selection with Kiji Inspector"
    url: "https://www.infoq.com/presentations/explainable-ai-llm-agent-decisions/"
    author: "Hannes Hapke"
    date: "2026-11-12"
---

# Opening the Black Box: Critical Explainability for AI Agent Tool Selection with Kiji Inspector

Hannes Hapke presents Dataiku's open-source Kiji Inspector, a tool for explaining why AI agents select particular tools. Rather than relying on chain-of-thought narratives, which the talk characterizes as superficial, Kiji Inspector applies Sparse Autoencoders (SAEs) directly to decision tokens to expose the underlying factors driving tool selection.

The approach combines causal ablation with layer activation extraction performed through patched vLLM engines, allowing engineers to probe model internals at the point of decision. The presentation frames these techniques as part of production monitoring workflows aimed at software architects and senior engineering leaders who need visibility into agent behavior.

- Kiji Inspector is Dataiku's open-source tool for explaining AI agent tool selection
- It applies Sparse Autoencoders (SAEs) directly to decision tokens instead of relying on chain-of-thought narratives
- Causal ablation and layer activation extraction via patched vLLM engines are core techniques
- The work targets production monitoring workflows for architects and engineering leaders