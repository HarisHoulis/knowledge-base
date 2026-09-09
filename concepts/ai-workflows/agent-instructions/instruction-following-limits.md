---
domain: ai-workflows
subdomain: agent-instructions
concept: instruction-following-limits
title: How long can your skills be before your agent forgets what you told it?
sources:
  - title: "How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI"
    url: "https://www.youtube.com/watch?v=XzJD1bvXKjs"
    author: "Laurie Voss, Arize AI"
    date: "2026-09-09"
---

# How long can your skills be before your agent forgets what you told it?

Laurie Voss of Arize AI investigates how many instructions an AI agent can reliably follow before it begins to forget or ignore them. He references a claim from the AI Engineer conference that agents can follow up to 200 instructions, a figure rooted in the IFEval benchmark. IFEval measures instruction density—the number of simultaneous rules—against accuracy, using simple tasks such as requiring exact keywords in a generated report. Voss argues this is an upper-bound proxy: if a model cannot track 200 simple keyword constraints, it will likely perform even worse on more complex real-world instructions (Laurie Voss, Arize AI, via AI Engineer, 2026).

Voss reran the original benchmark on the few models from the original test set that were still available via API: GPT-4.1, Claude Sonnet 4, and Gemini 2.5 Pro. He highlights that models are retired quickly, and notes that the practical instruction-following limit has changed by an order of magnitude since the original 200-instruction figure. The talk aims to help developers understand the real constraints on skill-file complexity and what workflow changes are needed as a result, though the transcript cuts off before presenting the full numeric results.

- The '200 instructions' figure comes from IFEval, which tests how many simultaneous keyword constraints a model can satisfy.
- Simple keyword constraints provide an upper-bound estimate; more complex instructions are likely followed even less reliably.
- The speaker reran the original benchmark on the surviving API models from the original set, highlighting how quickly models are retired.
- The practical instruction-following limit has reportedly changed by an order of magnitude compared to the original figure.