---
domain: ai-workflows
subdomain: ai-safety-evaluations
concept: third-party-cyber-evals
title: Third-party cyber evaluations involving OpenAI models
sources:
  - title: "Third-party cyber evaluations involving OpenAI models"
    url: "https://simonwillison.net/2026/Aug/5/third-party-cyber-evaluations/#atom-everything"
    author: "Simon Willison"
    date: "2026-08-05"
---

# Third-party cyber evaluations involving OpenAI models

OpenAI's third-party cyber evaluations, intended to be isolated from the internet, suffered misconfigurations that allowed models to access the public internet. One test by Irregular involved a Capture-the-Flag-style challenge where the fictional target's name coincidentally matched a real domain. Because the environment was mistakenly connected to the internet, the model exploited the real website, mistaking it for part of the simulated environment. This incident highlights the risks of misconfigured evaluation environments. Irregular also hosted a misconfigured environment for Anthropic, as detailed in Anthropic's own write-up, indicating a recurring issue in third-party cybersecurity testing.

- Testing-environment misconfigurations allowed OpenAI models to access the public internet during cyber evaluations.
- A fictional CTF target name coinciding with a real domain caused the model to exploit the actual website.
- Irregular, an external testing partner, was behind the misconfiguration and also featured in Anthropic's incident write-up.
- These incidents underscore the importance of isolating evaluation environments to prevent accidental cyberattacks.