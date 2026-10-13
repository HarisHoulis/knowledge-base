---
domain: ai-workflows
subdomain: llm-tooling
concept: llm-model-integration
title: llm-gemini 0.35 Adds Gemini 4 Argon Support
sources:
  - title: "llm-gemini 0.35"
    url: "https://simonwillison.net/2026/Oct/13/llm-gemini/"
    author: "Simon Willison"
    date: "2026-10-13"
---

# llm-gemini 0.35 Adds Gemini 4 Argon Support

Simon Willison released llm-gemini 0.35, adding support for the new Gemini 4 Argon model, which became available via the Gemini API and Google's $100/month subscription plan. He tested it with his standard pelican-on-a-bicycle SVG prompt at low, medium, and high effort levels, reporting that all three were excellent, consistent with Gemini's track record of producing great SVGs and the fact that Google staff have invested in SVG specifically.

On pricing, Argon launched at $2/million input and $10/million output tokens — the same as GPT-6 Sol, half the price of Claude Opus 5.5, and one-fifth the price of Claude Fable 5.1 and GPT-6 Astra. However, Argon is set to double in price on December 1st, bringing it in line with Opus 5.5.

Willison argues that raw token prices are less meaningful now, since what matters is how many tokens a model consumes to complete a goal within an agentic harness. As a proxy, he cites Artificial Analysis's total benchmark cost figures, where Argon costs $2,407 — close to GLM-5.3 and significantly cheaper than the latest OpenAI, Anthropic, and Meta models. Even after the price doubles, it should remain slightly cheaper than GPT-6 Astra.

- llm-gemini 0.35 adds support for Gemini 4 Argon, available via the Gemini API and Google's $100/month subscription plan.
- Argon launched at $2/million input and $10/million output tokens, but doubles in price on December 1st.
- Willison argues token prices matter less than total tokens consumed to achieve a goal in an agentic harness.
- Artificial Analysis benchmark costs put Argon at $2,407, close to GLM-5.3 and cheaper than the latest OpenAI, Anthropic, and Meta models.