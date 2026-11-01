---
domain: ai-workflows
subdomain: agent-ready-documentation
concept: agent-first-docs
title: Designing Documentation and APIs for AI Agent Readers
sources:
  - title: "Most of Your Docs Readers Are Now AI Agents - Hahnbee Lee, Mintlify & Lincoln Murr, Coinbase"
    url: "https://www.youtube.com/watch?v=YX4Z4XqZ9Vo"
    author: "AI Engineer"
    date: "2026-11-01"
---

# Designing Documentation and APIs for AI Agent Readers

Hahnbee Lee (co-founder/CTO of Mintlify) and Lincoln Murr (head of AI products at Coinbase) discuss how AI agents are becoming primary consumers of developer documentation and financial APIs. Lee notes that Mintlify was founded in 2022, before GPT-3, when documentation prioritized design and interface; agents, however, don't see or care about a site's visual design or branding. Instead, page size and context-window footprint become critical, and content accuracy is paramount because an agent that hits even a slight problem will simply stop rather than try to fix it, potentially switching to a competitor's product.

Lee argues that coding agents have accelerated engineering productivity so much that the rest of an organization must use AI to keep pace, making automation to prevent documentation from going stale especially important. He is still working out how to judge the quality of AI-written text.

Murr frames Coinbase's response around two questions: what new products can be built specifically for agents, and which core parts of the business (trading, money management) must be exposed to agents so people keep using Coinbase. The approach is to make the entire business available through APIs rather than relying on browser interaction, since authentication and security are problematic for financial tasks—you don't want to give an agent unlimited access to an account, so safeguards and limits are needed. He compares this shift to the web-to-mobile transition, predicting that in ten years people may rarely look at their accounts directly because agents will handle everything.

- Agents don't perceive design or branding, so documentation priorities shift toward small page size (context-window efficiency) and strict content accuracy.
- Agents encountering even minor documentation errors tend to stop rather than self-correct, risking loss of the user to another product.
- Automation to keep docs from going stale is essential as engineering productivity outpaces the rest of the organization.
- Coinbase is exposing its full business via APIs for agents, with safeguards and limits instead of granting agents unlimited account access.
- The web-to-mobile transition is used as the analogy for the coming mobile-to-agent shift in how people manage money.