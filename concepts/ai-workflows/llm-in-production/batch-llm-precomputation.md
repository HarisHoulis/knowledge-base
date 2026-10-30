---
domain: ai-workflows
subdomain: llm-in-production
concept: batch-llm-precomputation
title: DoorDash Cuts Grocery Reorder Latency from 16 to 2 Seconds with AI Agents
sources:
  - title: "DoorDash Cuts Grocery Reorder Latency from 16 to 2 Seconds with AI Agents"
    url: "https://www.infoq.com/news/2026/10/doordash-ai-grocery-reorder/"
    author: "Leela Kumili"
    date: "2026-10-30"
---

# DoorDash Cuts Grocery Reorder Latency from 16 to 2 Seconds with AI Agents

DoorDash reduced grocery reorder latency from 16 seconds to 2 seconds by precomputing recurring purchase needs with batch LLM inference rather than calling models in the live request path. Deterministic validation checks the model output, and live catalog resolution keeps product selections current at request time.

The design also uses an editable shopping interface so users can adjust the precomputed list without triggering unnecessary model calls. According to the company, shopping list views doubled and the flow's order rate increased by roughly 34%.

- Batch LLM inference plus deterministic validation cut reorder latency from 16s to 2s
- Live catalog resolution keeps precomputed selections current
- An editable interface avoids extra model calls during interaction
- Reported results: 2x shopping list views and ~34% higher order rate