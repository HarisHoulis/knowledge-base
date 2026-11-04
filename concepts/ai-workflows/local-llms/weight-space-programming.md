---
domain: ai-workflows
subdomain: local-llms
concept: weight-space-programming
title: Qwen 3.8 27B on a Laptop Can Interpret Model Weights
sources:
  - title: "Qwen 3.8 27B on my laptop can interpret model weights, too"
    url: "https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/"
    author: "Simon Willison"
    date: "2026-11-03"
---

# Qwen 3.8 27B on a Laptop Can Interpret Model Weights

Simon Willison tests a paper by Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab that coins the term "Weight-Space Programming" for LLMs analyzing and modifying raw neural network weights. The paper reports that GPT-6 Astra can identify what a network was trained to do from raw weights alone, write small game-playing networks from scratch, and fix reasoning loops in Qwen3.5-0.8B by editing 0.016% of its weights, raising MATH-500 from 7.9% to 48.1% (per the source).

Willison separates two claims: what models can do with raw weights without tools, and what they can do with code to update other models. He cites Matthew Honnibal calling the paper misleading for conflating these, and Sean Goedecke deconstructing the Qwen weight-edit example as steps a human ML researcher would take. Willison focuses on the no-tools question.

He reproduces the paper's experiment using self-contained prompts from the RikiyaT/lm_understand-logs repo, which feed raw weights of networks trained on 10x10 grid versions of Breakout, Pong, Pac-Man, and Freeway and ask the model to identify the game without tools. Running Qwen 3.8 27B (17GB GGUF) locally via LM Studio and the llm-lmstudio plugin, he got correct identifications for Pac-Man (46m, 43,506 reasoning tokens, 72% confidence), Pong (1h 5m, 75%), and Breakout (52m, 88%), but it failed on the more obscure Freeway, guessing Pac-Man-like.

Willison finds the result impressive but pushes back on hype, noting the reasoning traces are nearly incomprehensible and that an experienced human with a notepad could likely do the same. He is not ready to declare source code obsolete or accept a future of machines editing their own weights in incomprehensible ways.

- Weight-Space Programming: LLMs reading and editing raw model weights without training loops, per the Takehi et al. paper
- A 17GB Qwen 3.8 27B running locally identified Pac-Man, Pong, and Breakout from raw weights alone, but failed on Freeway
- Local runs took 46 minutes to over an hour and tens of thousands of reasoning tokens each
- Critics (Honnibal, Goedecke) argue the paper conflates no-tools weight reading with code-assisted weight editing
- Willison cautions against overhyping the results as the end of source code