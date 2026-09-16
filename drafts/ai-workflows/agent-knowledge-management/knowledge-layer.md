---
domain: ai-workflows
subdomain: agent-knowledge-management
concept: knowledge-layer
title: Pinecone 2.0 and the Knowledge Layer for AI Agents
sources:
  - title: "Pinecone 2.0 — Edo Liberty, Pinecone"
    url: "https://www.youtube.com/watch?v=IN-rb-9WmiY"
    author: "AI Engineer"
    date: "2026-09-16"
---

# Pinecone 2.0 and the Knowledge Layer for AI Agents

Edo Liberty opens with the psychological concept of theory of mind — our capacity to model what other people know, believe, and how they act — to argue that we misjudge what our AI agents actually know. He illustrates the mismatch with a Yahoo Answers anecdote: users asked questions like "am I fat?" of a Q&A product that could have no way of knowing, a silly example of failing to model a system's information boundaries. He contends we make the same mistake with AI today, in a subtler but equally fundamental way.

Liberty categorizes knowledge into three kinds. General knowledge is what lives in the public domain and what LLMs are trained on — explaining legal terms, improving Rust code, exploring product use cases — and models are already very good at it. Specific knowledge is private to a company (a codebase's implementation details, a particular customer's contract), and this is the problem RAG, search, and vector databases like Pinecone solved long ago, though he notes there is still work to do.

The third kind is tribal knowledge: the general knowledge inside a company that a seasoned employee has and a new hire does not — how things are done, processes, who is in charge of what, guiding principles. It is not general knowledge because it is company-specific, and it is not a specific piece of knowledge because you cannot simply retrieve it from one document; it is the sum total of many things.

Given this, Liberty argues agents in big companies today should be modeled like a new hire: brilliant, tool-equipped, held to high expectations, but largely clueless about goals, culture, priorities, and processes, forced to read documents and start most tasks from scratch each session. What they need is not to be smarter or to have better tools, but a knowledge layer. At minimum, that layer must be persistent — company knowledge, processes, capabilities, and goals, built once or rarely, accessible to all agents in the company — and it must be highly specialized, so an agent handling HR practices looks different from one optimizing kernels in a codebase.

- Agents in enterprises should be thought of as new hires: capable and tool-rich but clueless about the company's goals, culture, priorities, and processes.
- Knowledge splits into three kinds: general (public, model-trained), specific (private, solved by RAG/search/vector DBs), and tribal (company-wide know-how that cannot be retrieved from any single document).
- The proposed knowledge layer must be persistent — built once or rarely and shared across all agents in a company.
- The knowledge layer must be highly specialized to the agent's domain, e.g. HR practices versus codebase kernel optimization.