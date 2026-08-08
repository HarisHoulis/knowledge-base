---
domain: system-design
subdomain: llm-search-architecture
concept: llm-integration-depth
title: Why DoorDash, Instacart, and Uber Eats Integrated LLMs Into Search Three Different Ways
sources:
  - title: "Why DoorDash, Instacart, and Uber Eats Integrated LLMs Into Search Three Different Ways"
    url: "https://blog.bytebytego.com/p/why-doordash-instacart-and-uber-eats"
    author: "ByteByteGo"
    date: "2026-07-28"
---

# Why DoorDash, Instacart, and Uber Eats Integrated LLMs Into Search Three Different Ways

Food delivery search platforms face similar intent-understanding challenges: synonyms, typos, shorthand, language mixing, ambiguity, long-tail queries, and hard constraints. ByteByteGo compares how DoorDash, Instacart, and Uber Eats each rebuilt search with LLMs, and shows that the depth of LLM integration into the runtime—not the model choice—is the key architectural decision (ByteByteGo, 2026).

- DoorDash uses LLMs offline to enrich a knowledge graph and parse queries into graph-linked chunks, keeping the runtime mostly classical and using constrained RAG to limit outputs to known taxonomy concepts.
- Instacart splits head vs. tail queries: offline RAG-and-cache serves popular queries, while a fine-tuned Llama-3-8B handles cold-start tail queries in real time, improving query rewrite coverage from 50% to over 95% and halving tail-query complaints.
- Uber Eats fine-tunes a Qwen LLM as the embedding backbone of a two-tower retrieval system, serving every query and document vector with optimizations like Matryoshka Representation Learning and scalar quantization to cut latency and storage costs.
- Each company's position on the integration spectrum was determined by its existing infrastructure, illustrating that the question 'where should the LLM sit?' matters more than which LLM to pick.