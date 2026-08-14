---
domain: system-design
subdomain: recommendation-systems
concept: semantic-retrieval
title: How to Fight Clickbait: Meta, LinkedIn & YouTube Case Studies
sources:
  - title: "How to Fight Clickbait: Meta, LinkedIn & YouTube Case Studies"
    url: "https://blog.bytebytego.com/p/how-to-fight-clickbait-meta-linkedin"
    author: "ByteByteGo"
    date: "2026-08-10"
---

# How to Fight Clickbait: Meta, LinkedIn & YouTube Case Studies

The article examines how social media platforms are combating engagement bait by shifting feed retrieval from behavioral signals to semantic understanding. For years, retrieval relied on engagement as a cheap proxy for relevance, but this proved easily gameable by content designed to maximize clicks and replies. Traditional demotions and heuristics treated symptoms, not the root cause. The durable fix involves using embeddings to match users and posts by meaning, a technique enabled by dual-encoder models and nearest-neighbor search. (ByteByteGo, 2026)

Three major platforms have adopted semantic retrieval with distinct architectures. LinkedIn consolidated five separate retrieval systems into a single fine-tuned LLaMA-3 dual encoder, using a prompt library to convert structured features into text. This model serves the entire feed at sub-50ms latency and improved retrieval accuracy by ~15% after converting raw popularity counts into ranked percentage buckets. Meta took the opposite approach, retaining a multi-stage funnel of over a thousand specialized models, where retrieval, early-stage ranking, and late-stage ranking each apply increasingly expensive models, and a value model balances positive and negative engagement signals. YouTube removed the search index altogether with its PLUM system, assigning each video a Semantic ID and treating retrieval as a generative task from a language model, decoding candidate video IDs directly. (ByteByteGo, 2026)

The three designs highlight key tradeoffs. Consolidation simplifies maintenance and aligns retrieval with ranking, but complicates rollback and loses independent control per objective. Specialization offers modularity and redundancy at the cost of operational complexity. Generative retrieval eliminates large embedding tables and improves long-tail coverage, but introduces a failure mode where generated IDs may not map to real content (kept below 5% after fine-tuning). All three approaches benefit cold-start scenarios by leveraging pretrained associations, though they risk stereotyping sparse profiles. LinkedIn reported gains concentrated among new and low-connection members, demonstrating the cold-start advantage. (ByteByteGo, 2026)

- Engagement-based retrieval is vulnerable to clickbait; semantic retrieval uses embeddings to match content by meaning instead of interaction history.
- LinkedIn consolidated retrieval into a single LLaMA-3-based dual encoder, while Meta kept a multi-stage funnel of specialized models.
- YouTube's PLUM uses generative retrieval with Semantic IDs, treating retrieval as a token-generation task rather than a search over an index.
- Semantic retrieval improves cold-start performance by inferring interests from profiles, but may over-stereotype users with sparse history.