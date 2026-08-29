---
domain: ai-workflows
subdomain: hybrid-search
concept: hybrid-semantic-lexical-search
title: Implementing Hybrid Semantic + Lexical Search
sources:
  - title: "Implementing Hybrid Semantic + Lexical Search"
    url: "https://kentcdodds.com/blog/implementing-hybrid-semantic-lexical-search"
    date: "2026-03-16"
---

# Implementing Hybrid Semantic + Lexical Search

The article discusses the limitations of semantic search and describes an iterative approach to improving search on kentcdodds.com. The author states that semantic search alone was not good enough, prompting a series of refinements using Cursor and GPT-5.4. Over three rounds of iteration, each pass revealed new shortcomings that the previous design missed, leading to a more robust solution. As indicated by the title, the final approach integrates semantic and lexical search methods to overcome the weaknesses of relying solely on semantic matching. This hybrid strategy leverages both contextual understanding and exact keyword matching to deliver better search results. The process underscores the value of repeated iteration with AI-assisted development tools in refining search functionality.

- Semantic search alone fails to deliver sufficient search quality.
- Iteration with AI tools like Cursor and GPT-5.4 uncovered progressively deeper issues.
- Each of the three rounds contributed new insights that the previous design lacked.
- The solution combines semantic and lexical search for a hybrid approach.