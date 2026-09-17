---
domain: ai-workflows
subdomain: agentic-search
concept: bm25-agentic-search
title: The Unreasonable Effectiveness of BM25 for Agentic Search
sources:
  - title: "The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev"
    url: "https://www.youtube.com/watch?v=fZH97QHHYjY"
    author: "AI Engineer"
    date: "2026-09-16T13:30:32+00:00"
---

# The Unreasonable Effectiveness of BM25 for Agentic Search

Bergum defines agentic search as search inside an agent loop: an agent has an information need while trying to complete a task, such as coding or deep research. He argues a good agentic search system needs three things: a capable model that can use tools and formulate queries, a harness that exposes retrieval and search functions to the model—whether through tool calling or code mode—and an efficient retrieval engine that can search potentially billion-scale document sets (Bergum, 2026).

BM25 stands for Best Match 25, named because experiment number 25 was best among a series of retrieval experiments. It is a lexical scoring function: given a query and document, it calculates a score from the interaction between query terms and document terms, hoping that score proxies relevance. BM25 itself has not changed; it is a roughly 30-year-old scoring function, and much work has gone into accelerating top-k retrieval with it (Bergum, 2026).

The comeback is driven less by the scoring function than by a more powerful user. LLMs have broad general knowledge about entities, companies, and dates, and by using that implicit parametric knowledge they become very good at search. Historically BM25 was a baseline in information retrieval research, with fancier neural methods compared against it; now BM25 is more relevant because agents can use it effectively (Bergum, 2026).

Evaluation is also shifting. Instead of humans scanning 10 blue links and computing metrics from a single-shot query, agents can type out many more queries than a human. Bergum highlights BrowseComp Plus, a deep research benchmark with about 830 riddle-like questions. The harness gives the model a simple search tool that accepts a query string and returns snippets, over a corpus of roughly 100,000 web documents, with end-to-end accuracy checked against golden reference answers (Bergum, 2026).

- Agentic search is search inside an agent loop; a good system needs a capable tool-using model, a harness exposing retrieval, and an efficient retrieval engine.
- BM25 stands for Best Match 25 and remains the same lexical scoring function; its resurgence comes from LLM agents acting as more capable users.
- LLMs' parametric knowledge of entities, companies, and dates helps them formulate queries, making BM25 more relevant.
- Agentic evaluation moves away from single-shot, 10-blue-links search because agents can issue many queries.
- BrowseComp Plus is a deep research benchmark with ~830 riddle-like questions, a simple search tool over ~100k documents, and end-to-end accuracy against golden answers.