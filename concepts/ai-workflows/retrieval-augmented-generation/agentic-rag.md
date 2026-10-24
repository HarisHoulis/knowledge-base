---
domain: ai-workflows
subdomain: retrieval-augmented-generation
concept: agentic-rag
title: RAG vs Agentic RAG
sources:
  - title: "EP230: RAG vs Agentic RAG"
    url: "https://blog.bytebytego.com/p/ep230-rag-vs-agentic-rag"
    author: "ByteByteGo"
    date: "2026-10-24"
---

# RAG vs Agentic RAG

Retrieval-Augmented Generation (RAG) combines information retrieval with an LLM to generate answers: a user asks a question, the retrieval system fetches relevant information from a knowledge base, the application adds that information to the prompt, and the LLM uses that context to generate an answer. RAG usually follows a predefined retrieval process, and the quality of its results depends on the accuracy of the retrieved context.

Agentic RAG follows a different approach. Instead of retrieving once, an agent can repeatedly fetch and evaluate information until it has enough evidence to generate an answer. An agent selects the right tools based on the task; those tools can search documents, APIs, databases, or the web. The fetched evidence is then checked for sufficiency, and if it is not sufficient, the agent can adjust its search or choose a different tool. Once sufficient evidence is achieved, the LLM uses that context to generate an answer.

The contrast is essentially single-shot, predefined retrieval versus an iterative, tool-selecting loop that validates evidence before answering. The article presents both as high-level patterns without prescribing when to use each.

- RAG performs a predefined retrieval step and feeds the retrieved context into the LLM prompt; result quality depends on retrieval accuracy.
- Agentic RAG lets an agent select tools (documents, APIs, databases, web) and repeatedly fetch and evaluate evidence until it is sufficient.
- The agent can adjust its search or switch tools when evidence is judged insufficient, then generate the answer once enough context is gathered.