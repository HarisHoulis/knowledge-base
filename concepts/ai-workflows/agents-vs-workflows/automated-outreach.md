---
domain: ai-workflows
subdomain: agents-vs-workflows
concept: automated-outreach
title: How I automate my own job at Hugging Face using agents
sources:
  - title: "How I automate my own job at Hugging Face using agents — Niels Rogge, Hugging Face"
    url: "https://www.youtube.com/watch?v=FLUoowDJg4I"
    author: "AI Engineer"
    date: "2026-08-20T15:30:35+00:00"
---

# How I automate my own job at Hugging Face using agents

Niels Rogge, a machine learning engineer at Hugging Face, automated his job of convincing researchers to publish model weights on the Hugging Face Hub instead of obscure storage like Dropbox or Zenodo. He built two versions of the automation: a deterministic workflow for initial outreach and a fully autonomous agent loop for follow-up. The first is a nightly cron job on GitHub Actions that models each step of his manual process with a language model call per step, including tracing for cost and latency, and deliberately avoids an agent framework because the prevailing advice was to use agents only when necessary. The second is a recently built autonomous system whose main tool is bash, with one CLI, one skill, and a sandbox, fanned out so that each GitHub issue runs in its own container. Rogge notes that recipients are not told an agent wrote to them because the messages are identical to what he would send, and disclosing a bot tends to result in unread and closed issues (source).

- Automation should be built twice: first as a deterministic workflow, then as an autonomous agent loop if the problem truly requires it.
- Deterministic workflows with tracing (prompts, cost, latency) are sufficient for many tasks and can run on free cron infrastructure.
- For autonomous loops, keeping the tool surface minimal — bash, one CLI, one skill, one sandbox — reduces complexity and failure modes.
- Fanning out each issue to its own container provides isolation and scalability for parallel follow-up.
- Whether to disclose that a message is bot-generated is a practical decision; in this case, concealment improves response rates.