---
domain: ai-workflows
subdomain: eval-quality
concept: adversarial-user-simulator
title: Build Evals That Actually Matter - Nick Ung, Lyft
sources:
  - title: "Build Evals That Actually Matter - Nick Ung, Lyft"
    url: "https://www.youtube.com/watch?v=3z2uT5aDx_Y"
    author: "AI Engineer"
    date: "2026-07-19T12:15:06+00:00"
---

# Build Evals That Actually Matter - Nick Ung, Lyft

In this talk, Nick Ung from Lyft addresses the common problem of offline evals that pass with high accuracy but fail in production due to unrealistic test sets. He emphasizes that using off-the-shelf LLMs to simulate customer interactions leads to evaluations that don't capture the messy, emotional, or off-topic conversations real users have. Lyft built an adversarial user simulator by fine-tuning an LLM on actual rider and driver transcripts, enabling it to role-play frustrated, confused, and adversarial users at the same distribution as production. This simulator found regressions that simpler synthetic datasets missed for months. The talk also covers the complete eval lifecycle at Lyft, including harness primitives for writing benchmarks in 20 lines, calibrating LLM-judge rubrics against human labels to match inter-rater agreement, routing failed production traces back into the offline test set, and a continual-learning loop that feeds improvements into prompts, harness, and the model. The system supports Lyft's multi-agent platform that resolves roughly a third of all customer issues, processing millions of conversations monthly (Lyft, 2026).

- Offline evals often fail in production because the synthetic test set does not reflect the real distribution of user behaviors, especially frustration or off-topic queries.
- Lyft developed an adversarial user simulator fine-tuned on actual transcripts to generate realistic, challenging test cases that surface regressions missed by standard evals.
- The eval pipeline includes lightweight harness primitives for easy benchmark creation, LLM-judge calibration against human labels, and automated feedback loops from production failures to improve the test set and model.
- This approach enabled Lyft's AI agents to handle about one-third of all customer issues reliably at scale.
- The continual-learning loop ensures that the eval system evolves with production data, maintaining high relevance and trustworthiness.