---
domain: ai-workflows
subdomain: agent-architecture
concept: decision-models-vs-llms
title: Your Agent Doesn't Need an LLM for Every Decision
sources:
  - title: "Your Agent Doesn't Need an LLM for Every Decision - Raymond Weitekamp, OpenProse"
    url: "https://www.youtube.com/watch?v=hFNbPmzzcEs"
    author: "AI Engineer"
    date: "2026-11-10"
---

# Your Agent Doesn't Need an LLM for Every Decision

Raymond Weitekamp argues that not every step in an agent's reasoning needs a generative LLM. Drawing on Kahneman's System 1/System 2 framing, he points to a new class of 'decision models' (also called System 1 models, or 'zero-step classifiers') that only rank, choose, and select among options rather than generating free text. He notes that TypeSafe's recently released Jev popularized this idea, and that while some argue such models make judgments rather than decisions—leaving the actual decision to your code—the terminology matters less than the underlying capability.

- Decision models rank/select among options instead of generating unconstrained text, contrasting with LLMs
- Framed as System 1 (fast, intuitive) vs System 2 (slow, deliberate) reasoning from Kahneman
- Positioned as a balancing 'yin and yang' force to generative AI's divergence
- Builds on prior work on recursive language models (RLM) by Alex Singh and Omar at MIT