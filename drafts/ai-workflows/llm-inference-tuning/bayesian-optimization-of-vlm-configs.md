---
domain: ai-workflows
subdomain: llm-inference-tuning
concept: bayesian-optimization-of-vlm-configs
title: Stop Shipping LLM Settings That Only Win on Paper
sources:
  - title: "Stop Shipping LLM Settings That Only Win on Paper - Rohan Pandey & Balaji Varadarajan, DigitalOcean"
    url: "https://www.youtube.com/watch?v=cWrYEBlWpcY"
    author: "AI Engineer"
    date: "2026-11-12"
---

# Stop Shipping LLM Settings That Only Win on Paper

Rohan Pandey and Balaji Varadarajan (DigitalOcean) demo an optimization agent that automatically finds the best VLM service configuration for a given model, replacing manual trial-and-error over serving recipes. The goal is to cut the time engineers spend hand-searching for optimal recipes and parameters by running the search in the background.

The agent uses Bayesian Optimization, implemented via Optuna, to minimize the search space and converge faster. Optuna takes the initial recipe (a YAML config with workload modes such as chat-short, chat-long, RAG, and batch-classify, each with its own output-token settings), evaluates each trial, scores it, mutates the recipe, and loops until the configured number of attempts completes. Runs are launched with a tuner.py script that takes a study title, the initial YAML, target hardware, and attempt count, and typically take several hours.

Results are reported as an HTML report identifying the best attempt plus an optimized YAML recipe. For GPT-OSS 120B, the agent found 256 an optimal setting and delivered a 17.5% improvement in useful tokens generated versus the initial configuration; for DeepSeek R1 Distill, token throughput doubled and time to first token was nearly halved after nine attempts.

- Bayesian Optimization via Optuna automates search over VLM serving recipes instead of manual tuning
- The tuner takes an initial YAML recipe, hardware spec, and attempt count, and runs for hours in the background
- GPT-OSS 120B saw a 17.5% gain in useful tokens generated over the baseline recipe
- DeepSeek R1 Distill doubled token throughput and nearly halved time to first token
- Output is an HTML report of all trials plus an optimized YAML recipe