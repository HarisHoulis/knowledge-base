---
domain: ai-workflows
subdomain: embeddings
concept: open-weights-embedding-models
title: Open Weights Matter for Embedding Models
sources:
  - title: "My comment on EmbeddingGemma 2"
    url: "https://news.ycombinator.com/item?id=49980487#49983751"
    author: "Simon Willison"
    date: "2026-10-06"
  - title: "EmbeddingGemma 2"
    url: "https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/"
  - title: "GPT-4 API general availability"
    url: "https://openai.com/index/gpt-4-api-general-availability/"
    author: "OpenAI"
    date: "2024-04"
---

# Open Weights Matter for Embedding Models

Simon Willison welcomes the fact that EmbeddingGemma 2 is released under the Apache 2.0 license, arguing that closed, proprietary, hosted-only models are a poor fit for embeddings specifically (HN comment, 2026-10-06). His reasoning is that most embedding applications involve computing thousands or millions of embedding vectors and storing them for later comparison, which creates a lock-in risk.

If a vendor discontinues a proprietary embedding model, users are left with stale stored vectors and must pay to re-calculate millions of existing embeddings against a replacement model. He notes that OpenAI offered in April 2024 to cover the financial cost of re-embedding content with its new models, but says that is not something that can be relied on from every provider.

Crucially, Willison states he does not want to host the model himself. He would rather pay a provider for a hosted embedding model while knowing that, if the provider stops hosting it, he can run the open weights version himself or find another vendor to do so.

- EmbeddingGemma 2's Apache 2.0 license is valuable because embedding workloads store millions of vectors for later comparison.
- Proprietary hosted-only embedding models create lock-in: if the vendor retires the model, users must pay to re-embed all stored vectors.
- OpenAI's April 2024 offer to cover re-embedding costs for new models is cited as an exception that cannot be assumed from all providers.
- The desired arrangement is paying for a hosted model while retaining the ability to fall back to self-hosting open weights or switch vendors.