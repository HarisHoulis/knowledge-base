---
domain: ai-workflows
subdomain: agent-memory
concept: memory-promotion
title: How to Decide What Your AI Agent Should Remember
sources:
  - title: "How to Decide What Your AI Agent Should Remember - Wojciech Pluta, Oracle"
    url: "https://www.youtube.com/watch?v=qq2Hm4XNRgI"
    author: "AI Engineer"
    date: "2026-10-30"
---

# How to Decide What Your AI Agent Should Remember

Wojciech Pluta (Oracle) argues that the AI stack has stabilized around models, infrastructure, and a harness (the code around the model), with the data layer now the main source of competitive advantage because it belongs to you. He frames RAG as a read path: search tells an agent what to retrieve, but not what should persist after an interaction. Memory, by contrast, is the write path — when an agent sees something worth saving, it should elevate that content to a record it can reuse later.

- RAG is the read path; memory is the write path — search alone doesn't decide what to keep after an interaction.
- Memory promotion is a pipeline: classify the candidate's meaning, compare it against existing records, check the evidence required for that type, then accept, reject, or route to human review.
- The data layer, not models or infrastructure, is where competitive advantage lives because it belongs to you.