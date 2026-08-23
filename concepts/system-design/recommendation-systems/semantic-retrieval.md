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

Social media feeds have long used engagement signals as a cheap proxy for relevance, but this proxy is easily gamed by clickbait that optimizes for clicks and replies rather than value. The article argues that a durable fix requires changing the retrieval stage from behavioral matching to semantic matching, where content is retrieved by meaning rather than interaction history. Three platforms illustrate different approaches to this semantic retrieval shift (ByteByteGo, 2026).

LinkedIn consolidated five parallel retrieval systems into a single language-model retriever based on LLaMA-3, using a prompt library to convert structured profile and post features into text. This unified model improved retrieval accuracy by roughly 15% and was especially effective for new users with sparse history, demonstrating the cold-start benefit of pretrained associations. Meta, in contrast, retained a multi-stage funnel comprising over a thousand specialized models, where each stage narrows candidates and balances objectives like engagement, diversity, and integrity (ByteByteGo, 2026).

YouTube went further by removing the search index entirely with its PLUM system, which assigns videos Semantic IDs and uses a Gemini-based language model to generate the ID of the next video a user will watch. This generative retrieval approach surfaced more long-tail content, lifted Shorts click-through by 4.96%, and shifted parameters from embedding tables into the network itself. However, it introduces a failure mode where generated IDs may not map to a real video, kept below 5% after fine-tuning. Each design carries tradeoffs in consolidation, specialization, compute cost, and rollback complexity (ByteByteGo, 2026).

- Engagement signals are a manipulable proxy for relevance, leading to clickbait promotion.
- Semantic retrieval via dual-encoder embeddings matches users and content by meaning.
- LinkedIn unified five systems into one LLaMA-3-based retriever, improving accuracy and cold start.
- Meta uses a funnel of many specialized models to trade off multiple objectives.
- YouTube's PLUM uses generative retrieval with Semantic IDs, boosting long-tail coverage and click-through.