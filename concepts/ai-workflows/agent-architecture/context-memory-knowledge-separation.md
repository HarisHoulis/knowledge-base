---
domain: ai-workflows
subdomain: agent-architecture
concept: context-memory-knowledge-separation
title: Systemic Approach to Memory, Knowledge, and Context in Agentic AI Architectures
sources:
  - title: "Systemic Approach to Memory, Knowledge, and Context in Agentic AI Architectures"
    url: "https://www.infoq.com/articles/agentic-ai-context-memory-knowledge/"
    author: "Adi Polak"
    date: "2026-11-02"
---

# Systemic Approach to Memory, Knowledge, and Context in Agentic AI Architectures

Adi Polak argues that reliable agentic AI architecture hinges on a context engine that selects, injects, compresses, and expires information before it reaches the model, rather than simply passing everything through. The article distinguishes three concerns: context (what is presented to the model at a given moment), memory (state retained across interactions), and knowledge (curated reference material). Keeping these separate lets each be managed with its own lifecycle and quality controls.

The recommended design uses tiered memory, curated knowledge sources, and explicit token budgeting so that the model receives the most relevant information within its limits. The context engine acts as the gatekeeper, deciding what to include, how to compress it, and when to expire it.

Polak also catalogs common anti-patterns, notably context stuffing (dumping excessive information into the prompt) and stale data loops (reusing outdated information), and pairs each with mitigations. The overall message is that context management should be treated as a systemic engineering concern rather than an ad hoc prompting practice.

- Separate context, memory, and knowledge as distinct architectural concerns
- Use a context engine to select, inject, compress, and expire information before it reaches the model
- Adopt tiered memory, curated knowledge, and token budgeting
- Avoid anti-patterns like context stuffing and stale data loops, and apply explicit mitigations