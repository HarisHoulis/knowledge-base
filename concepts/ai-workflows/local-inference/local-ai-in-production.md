---
domain: ai-workflows
subdomain: local-inference
concept: local-ai-in-production
title: What Runs Where? Local AI in Production
sources:
  - title: "What Runs Where? Local AI in Production — Ahmad Osman, Osmantic"
    url: "https://www.youtube.com/watch?v=GKSQYbELDzw"
    author: "AI Engineer"
    date: "2026-11-21"
---

# What Runs Where? Local AI in Production

Ahmad Osman (Osmantic) traces the trajectory of local AI from 2023 to the present, arguing that the field is in its "90s Linux phase" — ecosystem and infrastructure investment is finally accelerating, with new inference engines and models optimized for specific chips and workflows. He frames open source AI as an optimization problem and local AI as a user-experience problem, both of which must be solved in parallel. A joint launch with Nvidia produced an optimized rendering engine for RTX Spark, demonstrated by a game built entirely locally with no cloud.

Osman challenges assumptions about cloud superiority: in a Hugging Face collaboration demo, a 27B-parameter local model ran at 51 tokens/second versus 34 tokens/second for a cloud model, with similar response quality. He argues that agent workloads are increasingly bottlenecked by waiting on shell commands and tool execution rather than tokens per second, which makes even a single RTX 3090 practically useful.

He highlights shifting usage data: since February 2026 agents have generated more tokens than humans on OpenRouter, and long-task horizons are doubling roughly every four months. Open source models have closed much of the gap on the Artificial Analysis Intelligence Index (13 to 51 points since January 2025), though he notes that benchmark results conflict — one index shows a closed model ahead while Terminal Bench shows open models ahead — concluding that evaluation itself is an unresolved problem.

- Local AI is framed as a user-experience problem while open source AI is an optimization problem; both need parallel investment
- A local 27B model hit 51 tokens/sec versus 34 tokens/sec for a cloud model in a side-by-side demo
- Agent workloads are limited more by tool-execution latency than tokens per second, making modest local hardware (e.g., a single RTX 3090) practically valuable
- Agents have out-generated humans in tokens since February 2026, and task horizons are doubling about every four months
- Conflicting benchmarks (e.g., HELLE Diamond vs Terminal Bench) show that model evaluation remains an open problem