---
domain: ai-workflows
subdomain: local-llms
concept: muse-glimmer-evaluation
title: Introducing Muse Glimmer
sources:
  - title: "Introducing Muse Glimmer"
    url: "https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/"
    author: "Simon Willison"
    date: "2026-08-10"
---

# Introducing Muse Glimmer

Simon Willison introduces Muse Glimmer, a local LLM optimized for end-to-end agentic task completion, reliable tool use, and multi-step reasoning. He highlights the model's strong performance on benchmarks like DeepSearch QA, MCP-Atlas, τ-Bench, and SWE-Bench, and notes that it is available in an 18.16 GB version via LM Studio, making it suitable for machines with 32 GB of RAM or more (Willison, 2026).

- Muse Glimmer excels at agentic tasks, tool use, and multi-step reasoning, according to its creators.
- Willison tested the model with LM Studio and his llm-coding-agent plugin on a fresh Datasette checkout, producing a long transcript of tool calls in response to the prompt 'how does auth work?'.
- The model is a vision LLM; Willison asked it to describe a photograph of pelicans and received a detailed, accurate visual description.
- The 18.16 GB model size leaves ample RAM for other applications on 32 GB+ systems, which Willison finds practical.
- He applied a patch to llm-lmstudio for compatibility with LLM 0.32 to run the coding agent test.