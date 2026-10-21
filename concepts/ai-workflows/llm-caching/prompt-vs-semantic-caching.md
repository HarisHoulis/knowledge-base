---
domain: ai-workflows
subdomain: llm-caching
concept: prompt-vs-semantic-caching
title: LLM Prompt Caching Versus Semantic Caching
sources:
  - title: "LLM Prompt Caching Versus Semantic Caching"
    url: "https://blog.bytebytego.com/p/llm-prompt-caching-versus-semantic"
    author: "ByteByteGo"
    date: "2026-10-21"
---

# LLM Prompt Caching Versus Semantic Caching

LLM requests cost money because input text is tokenized and processed, and inputs often include far more than the user's question—system instructions, examples, documentation, and prior conversation can make a 10-word question part of a request with thousands of input tokens. ByteByteGo identifies two distinct caching opportunities: reusing already-processed input (prompt caching) and reusing previously generated answers (semantic caching).

Prompt caching exploits the transformer's prefill stage, where the model computes KV states for input tokens. Because a causal model's token representations depend only on preceding tokens, a shared prefix—such as support instructions plus a product manual—can be cached and reused across requests with different suffixes. The shared content must sit at the beginning and be byte-for-byte identical; even a timestamp or request ID at the front can defeat reuse. Savings are real but not free: Anthropic's standard cache-read rate is 1/10th the normal input rate, with cache writes costing 1.25x (5-minute) or 2x (1-hour), so a write plus a read costs $1.35 instead of $2 for a $1 prefix. Output token charges remain unchanged.

Semantic caching sits in the application layer: an embedding model converts the incoming question to a vector, which is compared against stored question embeddings, and a sufficiently similar cached answer is returned without calling the LLM. The hard part is the similarity threshold—strict thresholds reject legitimate paraphrases, loose ones risk wrong answers. Near-identical questions can hinge on a single critical word (cancelling before vs. after shipping), and numbers, negation, dates, product editions, and eligibility conditions cause similar failures. A similarity score is not a probability of correctness, so teams need labeled evaluation sets covering paraphrases and near-matches, plus measurement of both hit rate and answer appropriateness.

Checking only the question is insufficient: answers to questions like "What is my order status?" depend on the customer and current state, and pronouns depend on conversation context. The two techniques are complementary—prompt caching reduces input-processing cost and latency, while semantic caching can eliminate the LLM call entirely on a hit, though misses cost more due to embedding and lookup overhead.

- Prompt caching reuses KV states for an identical shared prefix placed at the start of the request; any change in wording, order, or a leading timestamp breaks the match.
- Prompt caching discounts input processing but not output generation, and cache writes cost a premium (1.25x for 5-minute, 2x for 1-hour on Anthropic), so savings require repeated reads.
- Semantic caching returns a stored answer when an embedding similarity score exceeds a threshold, avoiding LLM input and output charges on a hit but adding cost on a miss.
- Threshold tuning is the core difficulty: near-matches differing by negation, numbers, dates, or product tier can produce confidently wrong cached answers, and similarity scores are not correctness probabilities.
- Question similarity alone is insufficient—answers may depend on user-specific state, conversation context, or requested language, so evaluation and possibly a verifier are needed.