---
domain: ai-workflows
subdomain: context-engineering
concept: context-engineering
title: Context Engineering in 2026
sources:
  - title: "Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI"
    url: "https://www.youtube.com/watch?v=WP3hjUXd918"
    author: "AI Engineer"
    date: "2026-08-17T16:26:35+00:00"
---

# Context Engineering in 2026

The video, presented by Louis-François Bouchard, Omar Solano, and Samridhi Vaid of Towards AI, discusses the challenges and solutions for context engineering in AI agents, particularly in the context of an AI tutor. The speakers identify two core problems: the finite context window, which degrades model performance and increases cost as it fills, and the stateless nature of models, which requires external mechanisms for continuity. They share their experiments to improve their AI tutor, focusing on compaction, memory retrieval, and grounding responses in course content. The talk emphasizes that context engineering in 2026 is not just about prompt design but managing the entire context lifecycle, including retrieval, summarization, and session handling. The team open-sourced their AI tutor and experiments, providing a practical resource for the community [1].

- Context windows are finite: piling tokens degrades results and increases cost.
- Models are stateless; memory and compaction are essential for long, coherent interactions.
- Effective context engineering involves grounding responses in user-specific content (e.g., course materials).
- The Towards AI team open-sourced their AI tutor and experiments to share best practices.