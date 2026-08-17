---
domain: ai-workflows
subdomain: llm-interaction
concept: interrogatory-llm
title: Bliki: Interrogatory LLM
sources:
  - title: "Bliki: Interrogatory LLM"
    url: "https://martinfowler.com/bliki/InterrogatoryLLM.html"
    author: "Martin Fowler"
  - title: "My LLM Codegen Workflow ATM"
    url: "https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/"
    author: "Harper Reed"
    date: "2025-02-16"
---

# Bliki: Interrogatory LLM

Martin Fowler describes the concept of an "interrogatory LLM" as a technique where an LLM asks a human a series of questions to gather the context needed for a complex task. Instead of a human writing extensive markdown context documents, the LLM can interview the human, asking one question at a time, and then produce a context report for a subsequent session or model to execute the task. This approach was inspired by Harper Reed's LLM codegen workflow, which emphasizes asking only one question at a time to keep the interaction focused (Fowler, n.d.; Reed, 2025).

The technique can also be used for document review: an LLM is given a specification and then interviews a human expert to determine if the document is accurate. This offers an alternative to having the expert read and review the document, which many people find difficult. Fowler notes that this can be more fruitful, especially for poorly written documents, and that multiple interrogatory LLMs can be chained to build and then review documents with different experts (Fowler, n.d.).

Beyond LLM context generation, Fowler sees broader applicability. He identifies as a "natural writer," but acknowledges that many people find writing very hard. For those individuals, being interviewed by an LLM to extract information into a usable form may be easier than writing a document themselves. While the resulting AI-flavored text might be less pleasing to skilled writers, it is preferable to missing information entirely (Fowler, n.d.).

- An interrogatory LLM gathers context by interviewing a human, asking one question at a time, then creates a context report for another LLM session.
- This technique can be used to build context documents and also to review existing documents by having the LLM interview an expert about the document's accuracy.
- The approach is especially useful for people who find writing difficult, allowing them to share knowledge through conversation rather than written documentation.
- The concept is inspired by Harper Reed's LLM codegen workflow, which emphasizes one-at-a-time questioning to maintain focus.