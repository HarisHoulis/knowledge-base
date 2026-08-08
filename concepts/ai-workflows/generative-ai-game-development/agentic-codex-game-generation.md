---
domain: ai-workflows
subdomain: generative-ai-game-development
concept: agentic-codex-game-generation
title: Moonlight & Mayhem (Raccoon Heist by Codex + GPT-5.6 Sol Ultra)
sources:
  - title: "Moonlight & Mayhem (Raccoon Heist by Codex + GPT-5.6 Sol Ultra)"
    url: "https://simonwillison.net/2026/Aug/7/moonlight-mayhem/"
    author: "Simon Willison"
    date: "2026-08-07"
---

# Moonlight & Mayhem (Raccoon Heist by Codex + GPT-5.6 Sol Ultra)

Simon Willison tested the same game-generation prompt with Codex Desktop running GPT-5.6 Sol Ultra, which aggressively uses sub-agents. The result was a much better game called Moonlight & Mayhem, where the player controls raccoons robbing a museum and rescuing crewmates to steal a golden sardine. This contrasted with an earlier simpler game produced by a different model that involved a single raccoon collecting coins in a backyard (source: https://simonwillison.net/2026/Aug/7/moonlight-mayhem/).

Despite the improved outcome, the one-shot prompt yielded a visual bug: each raccoon had an enormous spherical eyeball floating overhead. Codex reviewed screenshots during development but failed to spot this issue. Willison corrected it by prompting 'Why do the raccoons have huge black spheres on them?' followed by 'Fix it', which resolved the problem. He shared the full Codex transcript in the repository to showcase the workflow (source: https://simonwillison.net/2026/Aug/7/moonlight-mayhem/).

The entire session took 52 minutes, and Willison included an AgentsView cost estimate illustrating what it would cost at full API prices versus his monthly Codex subscription. The article highlights the strengths and limitations of AI coding agents in creative game development, including the importance of prompt iteration and bug-fixing loops.

- Codex with GPT-5.6 Sol Ultra produced a richer, more heist-themed game than a prior attempt, with multi-raccoon team mechanics.
- The one-shot prompt had a major visual bug (giant eyeball spheres) that went unnoticed by Codex during development.
- Simple follow-up prompts successfully fixed the bug, demonstrating the value of iterative correction.
- The full transcript was shared, and the session cost estimate was provided to show API pricing versus subscription.
- AI coding agents can generate impressive creative artifacts but still require human oversight for visual quality control.