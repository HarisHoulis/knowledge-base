---
domain: ai-workflows
subdomain: llm-context-elicitation
concept: interrogatory-llm
title: Interrogatory LLM
sources:
  - title: "Bliki: Interrogatory LLM"
    url: "https://martinfowler.com/bliki/InterrogatoryLLM.html"
    author: "Martin Fowler"
---

# Interrogatory LLM

Interrogatory LLM is a technique where an LLM interviews a human to gather the context needed for a complex task, instead of requiring a human to write that context directly. The LLM asks all the questions it needs, accepts information from the user, and may consult other sources; then it creates a context report for another session or model to execute the next step. Fowler notes that Harper Reed's blog describes this approach and emphasizes asking only one question at a time, though the LLM often needs reminders of this constraint.

A second application is using an interrogatory LLM to review an existing document, such as a software specification, by interviewing a human expert to check its accuracy. This can be more fruitful than asking the expert to read and review the document directly, especially if the document is poorly written. Both uses can be combined: one LLM builds a document, and other interrogatory LLMs review it with different experts.

Fowler also observes that the technique extends beyond LLM-specific tasks. For people who find writing difficult, being interviewed by an LLM can be an easier way to capture knowledge in a form others can consume, even though the result may carry the 'tang of AI-writing' that some dislike. This is better than losing the information due to rushed writing or no writing at all.

- An interrogatory LLM gathers context by interviewing a human, asking one question at a time, and then produces a context report for a subsequent LLM session.
- The technique can build context from scratch or review an existing document by having the LLM interview a human expert for accuracy.
- Multiple interrogatory LLMs can be chained: one to create a document, others to review it with different experts.
- The approach is useful beyond LLM workflows, offering a way for people who find writing hard to share knowledge through conversation.