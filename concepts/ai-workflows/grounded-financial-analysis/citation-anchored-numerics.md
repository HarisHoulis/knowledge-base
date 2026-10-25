---
domain: ai-workflows
subdomain: grounded-financial-analysis
concept: citation-anchored-numerics
title: Do Not Let Models Invent Numbers: Citation-Anchored Numeric Extraction at Kepler
sources:
  - title: "Do Not Let Models Invent Numbers - Vinoo Ganesh, Kepler"
    url: "https://www.youtube.com/watch?v=dZgA6btnb_s"
    author: "AI Engineer"
    date: "2026-10-25"
---

# Do Not Let Models Invent Numbers: Citation-Anchored Numeric Extraction at Kepler

Vinoo Ganesh, CEO of Kepler, describes an architecture for financial analysis in which the language model never writes numbers itself. Because LLMs are probabilistic machines that perform semantic search rather than truly reading documents, they can pick the wrong source, misread a number's unit or context (e.g. 17 million vs. 17 billion, yen vs. dollars, or a page number), and cannot reliably do arithmetic. Kepler therefore separates three concerns: finding the right source, computing with deterministic human-written code, and post-processing filtering.

- LLMs are probabilistic and don't truly read documents; they do semantic search, so they can surface the wrong source or misread a number's unit and context.
- Models should reference numbers but never generate them; all math (growth rates, margins, multipliers) is done by deterministic human-defined code.
- Kepler pre-processed the full SEC corpus (30M+ documents) into ~20,000 citation anchors—deterministic numeric metrics like revenue, income statements, and balance sheets—so every number is clickable back to its source document.
- A post-processing filter rejects any quote that cannot be verified, making the model structurally incapable of emitting unverified numbers.