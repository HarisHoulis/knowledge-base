---
domain: ai-workflows
subdomain: data-curation
concept: data-centric-training
title: Training Krea 2: What matters in generative model training
sources:
  - title: "Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai"
    url: "https://www.youtube.com/watch?v=-tviRdpmHvs"
    author: "AI Engineer"
    date: "2026-08-18T14:00:06+00:00"
---

# Training Krea 2: What matters in generative model training

In the talk, Sangwu Lee explains that Krea 2 deliberately trades the consistency of production image models for stylistic diversity and faster generation. Production models achieve reliable outputs by rendering an 'average person' centered in the frame, but Krea 2 aims to let studios explore visual ideas, prioritizing range over uniformity (AI Engineer, 2026).

Lee emphasizes that data is 'basically everything' once the architecture is fixed. The talk details specific data pitfalls: captions for paintings photographed on walls omit the frame and wall, causing the model to learn those as part of the image; they refuse AI-generated training images to avoid inheriting another model's aesthetic; and deduplication spans hashing across 2–10 billion images followed by embedding-based near-duplicate detection (AI Engineer, 2026).

To scale data quality, they distill large vision-language model judgments into cheap classifiers capable of sweeping a billion images, use sparse autoencoders as unsupervised taggers for watermarks and border artifacts, and check world-knowledge coverage against Wikipedia concepts ranked by PageRank. The training pipeline itself borrows wholesale from LLMs, and thirty to forty in-house filters are applied (AI Engineer, 2026).

- Data quality is the dominant factor once architecture and model are fixed; Krea 2 prioritizes diversity over production consistency.
- AI-generated images are explicitly excluded from training to avoid sticky aesthetics inherited from other models.
- Deduplication is two-stage: hash-based exact de-dup, then embedding-based near-dup detection at billion-image scale.
- Large VLM judgments are distilled into cheap classifiers for scalable filtering; sparse autoencoders serve as unsupervised taggers.
- World knowledge coverage is assessed using Wikipedia concepts ranked by PageRank, alongside 30–40 in-house filters.