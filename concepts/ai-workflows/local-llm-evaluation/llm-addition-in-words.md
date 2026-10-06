---
domain: ai-workflows
subdomain: local-llm-evaluation
concept: llm-addition-in-words
title: Qwen3.8 27B Addition in Words: Re-running an LLM Arithmetic Experiment Locally
sources:
  - title: "Qwen3.8 27B addition in words"
    url: "https://simonwillison.net/2026/Oct/4/qwen38-addition-in-words/"
    date: "2026-10-04T23:34:00+00:00"
  - title: "Qwen3.8 27B addition in words (research repo)"
    url: "https://github.com/simonw/research/tree/main/qwen38-addition-in-words#readme"
    author: "Simon Willison"
  - title: "Colin Frasier Bluesky post"
    url: "https://bsky.app/profile/colin-fraser.net/post/3mwopbyznhs2k"
    author: "Colin Frasier"
  - title: "Full reasoning transcript"
    url: "https://gist.github.com/simonw/8ef79c777ad34c53e9c09094800576a5#full-reasoning-transcript-2"
    author: "Simon Willison"
---

# Qwen3.8 27B Addition in Words: Re-running an LLM Arithmetic Experiment Locally

Simon Willison reran an experiment originally posted by Colin Frasier on Bluesky, which used GPT-4o to test how well a model could "compute the sum but return the answer in words" across increasingly large numbers. Frasier's two-year-old chart inspired Willison to repeat the experiment on local hardware (a DGX Spark) to explore the effect in a fully controlled environment, since GPT-4o's many wrong answers made it unlikely the model was secretly using a calculator.

Willison pasted Frasier's image into a Codex Remote session (GPT-6 Astra) and had it run the same experiment using `Qwen3.8-27B-Q4_K_M.gguf`, first with reasoning disabled over 30 attempts per number-size combination, producing a heatmap.

He then ran the experiment with reasoning enabled. Because each pair took a lot longer, he ran only one sample per square instead of 30, yielding a much less appealing heatmap where each square is either 100% or 0% — but the model got the right answer in 167 out of 169 attempts. Since these were one-shot runs, he notes a second run would likely produce different results.

A version of the report includes the model's reasoning traces for the larger calculations, showing explicit column-by-column addition such as aligning digits, adding from right to left, and carrying ("Position 3 (hundreds): 6 + 9 = 15, write 5, carry 1").

- The experiment tests whether an LLM can compute a sum and express the answer in words across increasingly large numbers.
- GPT-4o's original results included many wrong calculations, which Willison cites as evidence it wasn't secretly using a calculator.
- Qwen3.8-27B-Q4_K_M run locally on a DGX Spark scored 167/169 correct one-shot attempts with reasoning enabled, though only one sample was taken per square due to long runtimes.
- Reported reasoning traces show the model performing explicit right-to-left column addition with carries.