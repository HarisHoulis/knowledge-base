---
domain: ai-workflows
subdomain: llm-evaluation
concept: gpt-6-astra
title: GPT-6 Astra: OpenAI's New Model Pricing and Benchmarks
sources:
  - title: "GPT‑6 Astra"
    url: "https://simonwillison.net/2026/Sep/3/gpt6-astra/"
    author: "Simon Willison"
    date: "2026-09-03"
  - title: "Artificial Analysis tweet"
    url: "https://twitter.com/ArtificialAnlys/status/2095595489031000350"
    author: "Artificial Analysis"
    date: "2026-09-03"
  - title: "ARC-AGI 3"
    url: "https://arcprize.org/arc-agi/3"
    date: "2026-03"
  - title: "ARC-AGI blog on Astra"
    url: "https://arcprize.org/blog/astra"
---

# GPT-6 Astra: OpenAI's New Model Pricing and Benchmarks

OpenAI's GPT-6 Astra is priced at $10/million input and $50/million output, matching Claude Fable 5 and 5.1, and appears positioned as a direct competitor to Fable. According to OpenAI's self-reported benchmarks, Astra scores higher than Fable on most measures, including a 99.9% score on the ARC-AGI 3 benchmark (released in March) when using OpenAI's custom 'Provider Adapter harness' for $19K, though the default ARC-AGI harness scored 62.7% for $26K. The Provider Adapter harness preserves opaque reasoning state between requests and uses compaction for longer conversations, enabling reuse of prior work (source: https://simonwillison.net/2026/Sep/3/gpt6-astra/).

Astra demonstrates particular strength in security tasks, scoring 100% on ExploitBench (vs. GPT-5.6 Sol's 78.5%), 42.4% on ExploitGym (vs. Sol's 30.3%), and 99.2% within four attempts on SRE-Bench binary reverse engineering (vs. Sol's 68.7%). It also improves long-context performance, achieving 100% on OpenAI's eight-needle benchmark at 256K–512K tokens and 96.3% at 512K–1M tokens. However, third-party evaluations from Artificial Analysis indicate Astra still trails Claude Fable 5.1 on their Intelligence Index, scoring 61 (equal to GPT-5.6 Sol, 5 points lower than Fable 5.1 max with fallback, and trailing Meta's Muse Spark 1.3). On their Coding Agent Index, Astra leads the cost efficiency frontier, costing about the same as GPT-5.6 Sol at max effort while scoring 2 points higher, and being less than half the cost of Claude Fable 5 per task for the same score (source: https://twitter.com/ArtificialAnlys/status/2095595489031000350).

- GPT-6 Astra is priced at $10/$50 per million input/output tokens, matching Claude Fable 5/5.1.
- Astra scores 99.9% on ARC-AGI 3 only with OpenAI's custom Provider Adapter harness; default harness gives 62.7%.
- Astra excels at security tasks (100% ExploitBench) and long-context retrieval up to 1M tokens.
- Third-party Intelligence Index still places Astra below Claude Fable 5.1 and Meta's Muse Spark 1.3.
- On the Coding Agent Index, Astra matches GPT-5.6 Sol in cost and outperforms it by 2 points.