---
domain: system-design
subdomain: ai-assisted-analytics
concept: determinism-split-ai-data-interface
title: AI Changes the Data Interface, Not the Query Engine
sources:
  - title: "AI Changes the Data Interface, Not the Query Engine"
    url: "https://www.infoq.com/articles/ai-changes-data-interface/"
    author: "Peihao Yuan"
    date: "2026-10-22"
---

# AI Changes the Data Interface, Not the Query Engine

Peihao Yuan argues that AI's role in analytics is at the interface layer—translating intent into constrained SQL or Python—while the query engine remains responsible for deterministic, reproducible computation. In the described disaster-recovery analytics workflow, an AI agent generates constrained queries, DuckDB computes reproducible facts from Parquet files, and the agent then interprets those results for the user.

The article frames this as a "determinism split": the agent handles ambiguity and natural-language interpretation, but the facts themselves come from an engine whose outputs can be replayed. This makes analyses replayable, since the same constrained query over the same Parquet data yields the same result regardless of the agent's involvement.

Yuan also offers four signals for deciding whether an embedded engine like DuckDB is sufficient or whether a managed lakehouse is justified, positioning engine choice as an architectural decision separate from the AI interface layer.

- AI belongs at the data interface (generating constrained SQL/Python and interpreting results), not in the query engine itself
- DuckDB over Parquet provides deterministic, reproducible facts that make analyses replayable
- The "determinism split" separates agent-driven interpretation from engine-driven computation
- Four signals help decide between an embedded engine and a managed lakehouse