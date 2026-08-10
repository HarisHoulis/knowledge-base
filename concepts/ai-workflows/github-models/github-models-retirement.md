---
domain: ai-workflows
subdomain: github-models
concept: github-models-retirement
title: GitHub Models is now retired
sources:
  - title: "GitHub Models is now retired"
    url: "https://simonwillison.net/2026/Aug/9/github-models-is-now-retired/#atom-everything"
    date: "2026-08-09"
---

# GitHub Models is now retired

GitHub Models, a tool that provided a unified API and playground across multiple LLM providers, has been retired [1]. Its main advantage was enabling code in GitHub Actions to use the existing GitHub API key to execute prompts, which fit well with GitHub Next's Continuous AI concept [1]. The official reason for the shutdown was not shared, but the author speculates that the rise of coding agent patterns made it prohibitively expensive to offer free or subsidized tokens [1]. The author's personal workflow used GitHub Models to generate folder summaries for a README, and they have since switched to an OpenAI API key with a monthly spending limit, now using GPT-5.6 Luna for that task [1].

- GitHub Models provided a unified API and playground across LLM providers, with deep integration into GitHub Actions via existing API keys.
- The service enabled GitHub Next's Continuous AI concept by simplifying prompt execution in CI/CD workflows.
- The shutdown reason is unannounced, but likely driven by the high costs associated with coding agent usage patterns.
- Users can replace GitHub Models with direct API keys, as the author did by switching to OpenAI's GPT-5.6 Luna with a spending limit.