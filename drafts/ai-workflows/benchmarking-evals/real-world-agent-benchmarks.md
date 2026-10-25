---
domain: ai-workflows
subdomain: benchmarking-evals
concept: real-world-agent-benchmarks
title: Why Frontier Models Fail as Buy-Side Analysts: Building Real-World Benchmarks
sources:
  - title: "Why Frontier Models Fail as Buy-Side Analysts - Janie Gu, Google DeepMind & Suyeol Yun, LinqAlpha"
    url: "https://www.youtube.com/watch?v=aVbRSIQO2dE"
    author: "AI Engineer"
    date: "2026-10-25"
---

# Why Frontier Models Fail as Buy-Side Analysts: Building Real-World Benchmarks

Janie Gu (Google DeepMind/Kaggle) and Suyeol Yun (LinqAlpha) discuss the state of AI benchmarking and introduce Mandate Bench, a benchmark evaluating how well models perform as securities investment analysts. Kaggle, home to 31 million ML enthusiasts and 15 years of competitions, became part of Google DeepMind in February 2026 and is repositioning as GDM's public benchmarking platform, aiming to be an open, neutral testing ground and the industry standard for benchmarks.

Gu argues benchmarks are fundamentally broken for three reasons: relevance, cost, and verification. Most public benchmarks test synthetic puzzles, academic trivia, or random math problems that don't resemble production agent work. Running a 500-task multi-pass agent benchmark across 16 frontier models can cost tens of thousands of dollars per run, and must be repeated as new models ship weekly. Verification is the most underestimated problem: differing supporting software, tool-calling conventions, and input serialization produce different scores for the same model on the same benchmark, reflecting infrastructure rather than model quality.

To diagnose these issues, Kaggle spent two months recreating and running 65 industry benchmarks step by step, uncovering a variety of problems (including cases where the evaluated model found something it shouldn't have). The talk frames benchmarks as the mechanism that steers model development: when you don't measure what you need, models become worse at the tasks they were designed for. The Mandate Bench case study with LinqAlpha applies this to buy-side analyst workflows, where frontier models reportedly fall short.

- Kaggle became part of Google DeepMind in February 2026 and is becoming GDM's public benchmarking platform, leveraging 15 years of competition rigor (private test sets, leak detection, fraud fighting).
- Three failure modes of modern benchmarks: irrelevance (synthetic puzzles vs. production work), high compute cost (tens of thousands of dollars per multi-model run), and inconsistent verification across implementations.
- Verification differences—tool-calling conventions, supporting software, input serialization—cause score variance that reflects infrastructure, not model quality.
- Kaggle recreated and ran 65 industry benchmarks over two months to diagnose problems and design needed infrastructure.
- Mandate Bench evaluates models as securities investment analysts, a case study built with partner LinqAlpha.