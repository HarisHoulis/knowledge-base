---
domain: ai-workflows
subdomain: agentic-search
concept: versioned-search
title: Version-Controlled Search: The Web as It Was
sources:
  - title: "Version-Controlled Search: The Web as It Was — Ryan Ahern, Exa"
    url: "https://www.youtube.com/watch?v=vS2IA9pq0Q4"
    author: "AI Engineer"
    date: "2026-10-19"
---

# Version-Controlled Search: The Web as It Was

Ryan Ahern, a development engineer at Exa, presents Exa's versioned search feature and argues that agent-based web search is displacing traditional keyword search. He notes that many users no longer search directly but instead ask agents like ChatGPT or Claude to search for them, and that agents search differently from humans: they are verbose, describe what they want in detail, and run many searches to understand a space before responding.

- Agents search differently from humans: they issue many detailed queries rather than a few keywords and give up less easily
- Exa runs its own crawling infrastructure, database, embedding model, and search architecture to serve agent queries
- Financial users (hedge funds, asset managers, insurers, VCs) need the latest unstructured web information for alpha and risk decisions
- Exa emphasizes search quality so agents need fewer tool calls, reducing cost and improving trajectory success
- Exa released a new benchmark intended to measure search engine performance separately from the agent or model invoking it