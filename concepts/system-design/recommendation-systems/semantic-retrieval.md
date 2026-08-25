---
domain: system-design
subdomain: recommendation-systems
concept: semantic-retrieval
title: How to Fight Clickbait: Meta, LinkedIn & YouTube Case Studies
sources:
  - title: "How to Fight Clickbait: Meta, LinkedIn & YouTube Case Studies"
    url: "https://blog.bytebytego.com/p/how-to-fight-clickbait-meta-linkedin"
    author: "ByteByteGo"
    date: "Mon, 10 Aug 2026 15:30:49 GMT"
---

# How to Fight Clickbait: Meta, LinkedIn & YouTube Case Studies

The article explains that engagement-based retrieval rewards clickbait, because optimization for interaction counts surfaces content that maximizes clicks regardless of value. To counter this, LinkedIn, Meta, and YouTube have shifted toward semantic retrieval, where content and users are matched by meaning using embeddings. According to ByteByteGo (2026), LinkedIn consolidated five retrieval systems into a single fine-tuned LLaMA-3 dual-encoder, using prompt templates to convert structured features like view counts and profiles into text that the model can process. The approach improved cold-start performance but required careful representation of numerical data, as raw counts performed poorly while bucketed percentages improved accuracy by roughly fifteen percent [1].

Meta, by contrast, kept a multi-stage funnel of over a thousand specialized models, with a lightweight two-tower model for early ranking and a heavier late-stage model that predicts multiple user actions combined into a single score. This design allows independent control over objectives such as engagement, diversity, and integrity, but adds operational complexity. YouTube's PLUM system takes a generative approach: it assigns each video a Semantic ID and adapts a language model to generate the next video's identifier via beam search, eliminating the need for a separate index. PLUM improved long-tail coverage and increased panel click-through on Shorts by 4.96 percent, though it must keep the rate of invalid generated IDs below five percent [5].

The cold-start problem is alleviated because language models can infer interests from sparse profiles, as seen in LinkedIn's gains among new and low-connection members. However, this also risks stereotyping users. The designs trade off consolidation versus specialization, compute cost, and the choice between generative and index-based retrieval, with the model often being the easier part and the surrounding data representation requiring the most effort.

- Engagement-based retrieval rewards clickbait; semantic retrieval matches by meaning to reduce bait.
- LinkedIn consolidated five retrieval systems into a single LLaMA-3 dual-encoder with text prompts, improving cold-start performance.
- Meta uses a multi-stage funnel of many specialized models, balancing engagement and integrity with operational complexity.
- YouTube's PLUM generates Semantic IDs for videos, treating retrieval as a generation task and boosting long-tail coverage.
- Semantic retrieval helps cold start but may stereotype users; tradeoffs include consolidation vs specialization and compute costs.