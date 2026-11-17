---
domain: ai-workflows
subdomain: legal-ai-agents
concept: rules-plus-rag-legal-redlining
title: Uber's Legal AI Agent Cuts Contract Review Time by 20% with Rules and RAG
sources:
  - title: "Uber's Legal AI Agent Cuts Contract Review Time by 20% with Rules and RAG"
    url: "https://www.infoq.com/news/2026/11/uber-legal-redlining-agent/"
    author: "Leela Kumili"
    date: "2026-11-16"
---

# Uber's Legal AI Agent Cuts Contract Review Time by 20% with Rules and RAG

Uber built a Legal Redlining Agent that reviews contract changes directly in Microsoft Word, combining retrieval-augmented generation (RAG), historical lawyer feedback, and deterministic policy rules (InfoQ). The system is assembled with LangGraph, OpenSearch, and Redis, and Uber reports more than 20% lower average contract review time alongside 91% accuracy in AI-generated decisions.

The design pairs generative retrieval with hard-coded policy rules rather than relying on the model alone, and it feeds prior lawyer feedback back into the loop to improve decisions over time. Uber is now exploring agentic harnesses, skills, legal ontologies, and knowledge graphs as next steps.

- Combines RAG, historical lawyer feedback, and deterministic policy rules rather than relying on the LLM alone
- Built on LangGraph, OpenSearch, and Redis, operating inside Microsoft Word
- Reports >20% reduction in average contract review time and 91% decision accuracy
- Future work includes agentic harnesses, skills, legal ontologies, and knowledge graphs