---
domain: ai-workflows
subdomain: model-architecture
concept: million-token-context
title: Why AI Agents Need Million-Token Context (MiniMax M3 & MSA)
sources:
  - title: "Why AI Agents Need Million-Token Context — Thomas Wolf & Olive Song, MiniMax"
    url: "https://www.youtube.com/watch?v=5Cxe5dv2Xlw"
    author: "AI Engineer"
    date: "2026-09-04T13:00:26+00:00"
---

# Why AI Agents Need Million-Token Context (MiniMax M3 & MSA)

In this AI Engineer interview, Hugging Face's Thomas Wolf speaks with Olive Song of MiniMax about the M3 model, an open-source release with roughly 400B total parameters (20B activated) that handles code, images, video, and a 1-million-token context (AI Engineer, 2026). M3 uses a novel architecture called MiniMax Sparse Attention (MSA), which scales context length by combining an index branch that identifies important context blocks with a sparse attention branch that computes over those selected blocks (AI Engineer, 2026).

- MiniMax M3 is an open-source model with approximately 400B total parameters (20B active) and a working 1M-token context.
- MSA (MiniMax Sparse Attention) scales context by using an index branch to select important blocks and a sparse attention branch to compute on them.
- Long context is not only for digesting long documents—it is essential for AI agents that must handle multi-round tool responses and interact with their environment.
- Earlier MiniMax models supported up to 10 million tokens, but M3 is focused on making this capability useful for agent-based workflows.
- Efficient attention remains a key architectural challenge as context windows grow from GPT-2's 1024 tokens to millions.