---
domain: ai-workflows
subdomain: self-hosted-inference
concept: self-hosted-open-models
title: How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models
sources:
  - title: "How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models - David Abitbol, Revolut"
    url: "https://www.youtube.com/watch?v=Ok6QdZHCcI8"
    author: "AI Engineer"
    date: "2026-10-29"
---

# How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models

David Abitbol, who manages AI operations at Revolut, describes how the digital bank moved from budget-constrained commercial AI coding tools to self-hosted open-source models to give its ~2,000 engineers effectively unlimited tokens at a fraction of the cost. Revolut first rolled out Gemini in January 2025, which improved execution time ~10% and coding time ~20% by removing Stack Overflow and documentation lookups, but early Claude Code adoption had limited impact and costs were unpredictable, with engineers spending thousands per month for little return.

Around April 2026 Revolut began self-hosting open models, favoring GLM for programming. The shift produced roughly 60% improvement in coding time and 70% in execution time. Abitbol notes the impact on execution time exceeded that on coding time, suggesting the real engineering bottleneck is not writing code but overhead like email, Jira, and Confluence—and unlimited tokens remove the incentive to ration usage for only the hardest tasks.

Operationally, supporting 2,000 engineers on GLM (an ~800B-parameter model) requires about 56 B200 GPUs. Abitbol cites empirical latency targets: under 3 seconds to first token (Slack complaints spike past 5 seconds) and ~200 tokens/second for interactivity, with throughput rising to ~800 TPS off-peak after 5pm. Self-hosting yields an average token cost of ~30 cents per million—about one-tenth of Anthropic/OpenAI spend—with stable bills. He cautions that simply loading weights onto a GPU yields terrible performance; workload behavior depends heavily on inference configuration and demand patterns.

Commercial models like Codex remain an exception for the best frontier capability, but open source is now a priority at Revolut with favorable economics.

- Self-hosting GLM on ~56 B200s for 2,000 engineers cut token costs to ~30 cents per million, about 1/10 of Anthropic/OpenAI spend
- Latency targets are empirical: <3s to first token (5s triggers complaints) and ~200 tokens/sec for interactivity, ~800 TPS off-peak
- Execution-time gains outpaced coding-time gains, showing non-coding overhead (email, Jira, Confluence) is the real bottleneck
- Unlimited tokens change engineer behavior—no need to ration usage for only the hardest tasks
- Naively loading model weights onto GPUs performs poorly; inference configuration and demand patterns matter greatly