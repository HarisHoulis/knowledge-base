---
domain: ai-workflows
subdomain: enterprise-rag-platforms
concept: unstructured-data-platform
title: Bridgewater's Vault: Turning 100 Million Documents Into an Investment Edge
sources:
  - title: "How Bridgewater Turned 100 Million Documents Into an Edge - Sam Green & Aaron Linsky, Bridgewater"
    url: "https://www.youtube.com/watch?v=CLve4Nx_RwI"
    author: "AI Engineer"
    date: "2026-10-24"
---

# Bridgewater's Vault: Turning 100 Million Documents Into an Investment Edge

Bridgewater Associates built Vault, an internal data platform that indexes, organizes, and prepares unstructured external and internal data—news, research transcripts, policy documents, memos, and meeting transcripts—for use by both investors and AI agents. The platform now holds over 100 million documents, with thousands added daily from 135 external sources, all aligned to Bridgewater's internal ontology via refinements like countries, concepts, markets, and the time period described in each document. The team found no off-the-shelf data provider that gave them the control needed to maintain their data advantage, so they built their own.

The talk centers on three lessons. First, people and agents have very different needs from a data platform, so solutions for each must be built separately. Second, the greatest impact comes when a single tool can meet both sets of needs simultaneously. Third, real success comes when agents become proactive participants in the investment process rather than reactive tools for people.

A concrete example illustrates the gap: a generic chat agent asked about AI infrastructure investment and the South Korean won found 15 sources but used only one or two, relied on a note from July 2026 when the question was asked in October, and admitted it could not establish a market consensus. Connected to Vault, the same question caused the agent to scope its search to October 1–8 and surface a much broader set of 52 documents, demonstrating how ontology-aware, time-bounded retrieval changes answer quality.

- People and agents need different things from a data platform, so build separate solutions—but aim for a single tool that serves both.
- Vault holds 100M+ documents from 135 external sources plus internal data, enriched with ontology refinements like country, concept, market, and time period.
- Generic web-search agents fail on investment questions due to stale sources and thin evidence; ontology-aware retrieval scoped to a time window surfaced 52 documents versus 15.
- The end goal is agents as proactive participants in the investment process, not just reactive query tools.