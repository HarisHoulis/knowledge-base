---
domain: ai-workflows
subdomain: automated-ai-research
concept: agent-speedrun-benchmark
title: Automated AI Research: Racing Codex and Claude Code Against Human Researchers on Speedruns
sources:
  - title: "We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect"
    url: "https://www.youtube.com/watch?v=oVsEddfhdxc"
    author: "AI Engineer"
    date: "2026-09-26"
---

# Automated AI Research: Racing Codex and Claude Code Against Human Researchers on Speedruns

A researcher at Prime Intellect describes work benchmarking whether AI agents can do AI research autonomously, motivated by claims from large labs about "recursive self-improvement" — models training other models without human intervention — for which there is no independent benchmark, particularly none from smaller labs [1]. The speaker argues this matters beyond AI itself, since a significant portion of scientific research in coming years will be conducted with AI tools, so understanding how models conduct research is important [1].

The chosen testbed is the nanoGPT speedrun. It began with Karpathy's project training GPT-2 from scratch in about 90 minutes, where reaching the GPT-2 validation loss counts as roughly GPT-2-level performance; the community's "modded nanoGPT," led by Kyler Jordan, cut that to 45 minutes and eventually to under 2 minutes over about two years [1]. Speedruns were selected as an environment because they are fast, give a clear reward signal (positive when a model breaks the previous record, zero or negative on failure), have clear testable rules, and — as in the newer "optimizer speedrun" released a few months prior, which restricts changes to optimizer parameters — behave more like research: finding the best method rather than minimizing wall-clock time [1].

Prime Intellect released two agents onto their cluster, Codex and Claude Code, and iterated in versions V1, V2 and V3, where each version simply means stopping and restarting the agent [1]. V3 came a day or two before the release, after the agents stopped producing the best results, and was instructed to beat all human records from the previous few weeks across any task [1]. A separate "novelty" direction required breaking records only through new ideas, which proved more difficult for the models [1]. The agent harness itself was deliberately simple — the speaker notes it could have been replaced with a /goal command [1].

- Recursive self-improvement (models training models without humans) is widely discussed but lacks independent benchmarks, especially from smaller labs [1].
- The nanoGPT speedrun was chosen as the testbed: GPT-2 validation loss in minimal time, with community work reducing the run from ~90 minutes to under 2 minutes over ~2 years [1].
- Speedruns offer a fast, rule-bound environment with a clear reward signal (positive only for beating the previous record), making them useful for training and for testable discoveries [1].
- The newer optimizer speedrun constrains changes to optimizer parameters only, shifting the task from program optimization toward genuine method research [1].
- Prime Intellect ran Codex and Claude Code agents on their cluster in restart-based versions (V1–V3), with a harder novelty-only track requiring records to be broken via new ideas [1].