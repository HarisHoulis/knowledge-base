---
domain: ai-workflows
subdomain: agentic-search
concept: grep-vs-embeddings
title: Grep or Embeddings? Agentic Search Over Company Documents
sources:
  - title: "Grep or Embeddings? Agentic Search Over Company Documents — George He, LlamaIndex"
    url: "https://www.youtube.com/watch?v=X4w2Pkz5tDY"
    author: "AI Engineer"
    date: "2026-10-07"
---

# Grep or Embeddings? Agentic Search Over Company Documents

George He, head of development at LlamaIndex, contrasts two approaches to giving agents document context: local file search (grep, read, glob) versus pre-indexed embeddings/vector search. He notes that models have become much better at orchestrating tools and browsing local file systems, but still face problems of local search and context management for large, complex datasets. The talk frames the choice as depending on data scale and the effort one is willing to invest in maintaining a search or data management system.

Claude Code is presented as the canonical grep-style approach: Anthropic used the local file system with grep, read, and glob rather than pre-indexing. He cites a tweet from Boris, the creator of Claude Code, noting that Claude Code experimented with a vector database but abandoned it, for reasons including not just performance but practical scaling and maintenance. Keeping a pre-indexed vector pointer up to date is hard, especially when code changes constantly. This works well because code is usually small, semi-structured, full of clues about imports and tests, naturally hierarchical, and already on disk locally.

Enterprise document datasets break these assumptions. They contain images, PDFs, and PowerPoints with no folder structure that can simply be grepped, are hard to keep up to date, and operate at a completely different scale. Security and access control matter much more, formats are not standardized (complex PDFs, schematics, production diagrams), and the data can no longer be run locally. He mentions MCP servers, Claude MD, skills, and instruction files as ways to track hierarchy and tell the agent how to look at the data, but the main takeaway is that the right choice comes down to the scale of the data and the maintenance effort you are willing to accept.

- Two orchestration approaches: grep-style local file search/execution versus embeddings-based pre-indexing/pre-extraction.
- Claude Code abandoned a vector database in favor of grep/read/glob because code is small, semi-structured, hierarchical, and already local, and pre-indexed vectors are hard to keep current.
- Enterprise datasets (images, PDFs, PowerPoints) lack greppable folder structure, have non-standardized formats, stricter security needs, and scale beyond local execution.
- MCP servers, Claude MD, skills, and instruction files are options for tracking hierarchy and guiding agent access to data.
- The decision ultimately depends on data scale and how much effort you will invest in maintaining the search/data management system.