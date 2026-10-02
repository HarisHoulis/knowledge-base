---
domain: ai-workflows
subdomain: AI coding and code-review agents
concept: agent-search-for-code-review
title: Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa
sources:
  - title: "Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa"
    url: "https://www.youtube.com/watch?v=cKhpeEBnT1o"
    author: "AI Engineer"
    date: "2026-10-02T15:30:31+00:00"
---

# Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa

Jakub Hojsan of Exa describes building semantic search for coding and code-review agents. Coding agents do not need the “10 blue links” of traditional web search; they need contextual highlights passed directly to the LLM. The core problem is the LLM knowledge cutoff: models are typically about six months behind from cutoff date to release date, creating a blind spot for recent changelogs, PRs, and repository changes (AI Engineer, 2026).

Hojsan gives the example of a CUDA vector-storage PR made after the GPT 5.5 cutoff date. Without web search, a model may see an error or diff and assume a removed parameter is a simple cleanup, when the change actually requires refactoring dependencies. Search lets the agent view the repository, critical changelog changes, and explain the migration in detail. Exa does not return the entire GitHub page; an interpretation step reduces the page to what the language model needs, giving roughly 500 characters instead of 100,000 (AI Engineer, 2026).

Adding a search tool to an agent is not enough. Hojsan argues it is a two-step process: instruct the agent when to use web search, then perform the search. For example, Claude Code may deny that Sonnet 4.6 or 4.7 exists even with a web search tool, because the model does not know to request a version that exists. A code-review agent rule should say that when a diff raises a dependency or version, inspect the source code to verify and base the review on what is found (AI Engineer, 2026).

Exa provides transparency: users get a full trace of what was searched, the exact queries, exact sources, and key points passed into the model, which can feed telemetry. Native web search tools in OpenAI or Anthropic are described as black boxes that synthesize information, may take up to 10 seconds, and return sources with no content. Exa’s effective highlights aim to give the model exactly what it needs (AI Engineer, 2026).

- LLM knowledge cutoffs leave roughly a six-month blind spot, so recent repository changes and PRs are unavailable to coding agents without external search.
- Search for coding agents should return contextual highlights, not full pages or blue links, reducing context from about 100,000 characters to about 500.
- Adding a web search tool is insufficient; agents also need rules instructing when to search, such as checking source when a diff changes a dependency or version.
- Exa offers transparency via a full trace of queries, sources, and key points passed to the model, unlike black-box native web search tools.