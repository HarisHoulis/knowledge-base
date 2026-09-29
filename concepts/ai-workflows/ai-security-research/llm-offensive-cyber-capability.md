---
domain: ai-workflows
subdomain: ai-security-research
concept: llm-offensive-cyber-capability
title: Frontier Models Cross a Threshold in Autonomous Exploit Development
sources:
  - title: "GLM-5.3 and the spread of advanced cyber capabilities"
    url: "https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities"
    author: "Anthropic Frontier Red Team"
  - title: "Quoting Anthropic Frontier Red Team"
    url: "https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/"
    author: "Simon Willison"
    date: "2026-09-29"
---

# Frontier Models Cross a Threshold in Autonomous Exploit Development

Anthropic's Frontier Red Team evaluated several models against 100 randomly selected tasks from an internal Binary Exploitation benchmark. They found that GLM-5.3 developed full control flow hijacks in 4% of trials, while Claude Mythos Preview succeeded in 6% ([Anthropic Frontier Red Team](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities)).

Although GLM-5.3 scores below Claude Mythos Preview, the report argues that a meaningful threshold has been crossed: earlier models such as Claude Opus 4.6 and GLM-5.2 did not succeed on any of the tasks. The shift is therefore qualitative — from zero successful hijacks to non-trivial success rates — rather than purely incremental.

The result is framed as evidence of the spread of advanced cyber capabilities across model developers, not just a single-lab milestone.

- GLM-5.3 produced full control flow hijacks on 4% of 100 sampled Binary Exploitation benchmark tasks.
- Claude Mythos Preview performed higher at 6% on the same benchmark.
- Earlier models (Claude Opus 4.6, GLM-5.2) succeeded on none of the tasks, marking a threshold crossing.
- The capability is described as spreading across multiple model developers.