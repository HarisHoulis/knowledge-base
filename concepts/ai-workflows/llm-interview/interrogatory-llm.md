---
domain: ai-workflows
subdomain: llm-interview
concept: interrogatory-llm
title: Interrogatory LLM
sources:
  - title: "Bliki: Interrogatory LLM"
    url: "https://martinfowler.com/bliki/InterrogatoryLLM.html"
    author: "Martin Fowler"
---

# Interrogatory LLM

The article introduces the concept of an 'interrogatory LLM' as a way to gather context for complex LLM tasks. Instead of having a human write extensive context documents, an LLM can interview a human by asking targeted questions, then compile a context report for use in another session with perhaps a different model. This approach was inspired by Harper Reed's workflow, which notably insists on asking only one question at a time to improve the quality of information gathered (Fowler, n.d.).

The technique can also be applied to document review. For example, a software specification can be validated by having an LLM interview a human expert to determine if the document is accurate, rather than requiring the expert to read and review the entire document. This is often easier for people, especially if the document is poorly written. Both use cases can be combined: one interrogatory LLM builds a document, and other interrogatory LLMs review it with various experts.

Beyond LLM-specific contexts, the approach is broadly useful for knowledge capture. Many people find writing difficult, but they may find it easier to be interviewed by an LLM and have it produce the document. While the output may have an AI-generated style that some might dislike, it is preferable to having no documentation at all, or to having rushed and incomplete writing.

- An interrogatory LLM interviews a human to gather context for another LLM task, replacing manual context writing.
- Asking one question at a time improves the quality of the elicited information, as noted by Harper Reed.
- The technique can validate documents by interviewing domain experts, offering an alternative to traditional document review.
- It helps people who struggle with writing by converting tacit knowledge into documents through conversation.