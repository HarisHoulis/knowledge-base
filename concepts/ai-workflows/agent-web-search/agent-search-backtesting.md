---
domain: ai-workflows
subdomain: agent-web-search
concept: agent-search-backtesting
title: Backtest Your Agent Against Yesterday's Web
sources:
  - title: "Backtest Your Agent Against Yesterday's Web — Ryan Ahern, Exa"
    url: "https://www.youtube.com/watch?v=L4dUFimVDKU"
    author: "AI Engineer"
    date: "2026-10-19"
---

# Backtest Your Agent Against Yesterday's Web

Ryan Ahern, a full-stack engineer at Exa, argues that AI agents now search the web far more often than humans because they can issue many queries, browse many pages, and keep iterating until they find the answer, whereas people typically type a few keywords and stop at the first page. He frames Exa as the search layer behind large coding and agent applications, citing Cursor fetching documentation and Gamma pulling financial figures as examples, and notes adoption among hedge funds, sovereign wealth funds, asset managers, and VCs seeking information before it hits the press.

Exa positions itself as a research lab building its own generative benchmark rather than relying on existing ones, because published benchmarks get trained on by search providers and labs. Ahern frames the design tradeoff as a triangle of quality, cost, and latency, and argues that a search provider's value over asking a model directly is access to up-to-date information.

The talk's core proposal is to apply version control to agent search: backtest an agent against a snapshot of yesterday's web so you can measure how changes to the agent affect results. The transcript is heavily garbled and repetitive, so the practical exercise and prize mentioned are not recoverable in detail.

- AI agents search the web more often and more persistently than humans, issuing many queries and browsing many pages before answering.
- Exa supplies search to major coding and agent applications and to finance customers such as hedge funds, sovereign wealth funds, asset managers, and VCs.
- Exa builds its own generative benchmark because public benchmarks get trained on by search providers and labs.
- Search design is framed as a quality/cost/latency tradeoff, with up-to-date information as the main reason to use a search provider over a model's built-in knowledge.
- The talk advocates version-controlling agent search so you can backtest against yesterday's web.