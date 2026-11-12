---
domain: ai-workflows
subdomain: coding-agents
concept: code-retrieval-benchmarking
title: JioHotstar Benchmarks Knowledge Bases for AI Coding Agents
sources:
  - title: "JioHotstar Benchmarks Knowledge Bases for AI Coding Agents"
    url: "https://www.infoq.com/news/2026/11/jiohotstar-codingagent-retrieval/"
    author: "Leela Kumili"
    date: "2026-11-11"
---

# JioHotstar Benchmarks Knowledge Bases for AI Coding Agents

JioHotstar evaluated six approaches to code retrieval for AI coding agents, using SWE, CodeScale Bench, and an internal question-answering harness as evaluation methods. The study compared how different retrieval strategies perform across task types rather than assuming a single best approach.

The key finding is that structural search performed well on concrete tasks, while semantic retrieval helped with ambiguous requirements. This suggests retrieval tooling should be matched to the nature of the task rather than standardized across all agent workflows.

The results highlight trade-offs in accuracy, token use, and tool design, underscoring the need to align retrieval tools with task types when building knowledge bases for coding agents.

- Six code-retrieval approaches were evaluated using SWE, CodeScale Bench, and an internal QA harness.
- Structural search excelled on concrete tasks; semantic retrieval helped with ambiguous requirements.
- Retrieval choices involve trade-offs in accuracy, token use, and tool design.
- Retrieval tools should be matched to task types rather than applied uniformly.