---
domain: ai-workflows
subdomain: llm-interrogation
concept: interrogatory-llm
title: Interrogatory LLM
sources:
  - title: "Bliki: Interrogatory LLM"
    url: "https://martinfowler.com/bliki/InterrogatoryLLM.html"
    author: "Martin Fowler"
  - title: "My LLM Codegen Workflow ATM"
    url: "https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/"
    author: "Harper Reed"
    date: "2025-02-16"
---

# Interrogatory LLM

When an LLM needs to perform a complex task, it usually requires a large amount of context. A human can write this context, but an alternative is to have the LLM interview a human to gather the needed information. The LLM asks questions, takes answers, consults other sources if necessary, and produces a context report for a subsequent session to carry out the next step. This approach is described by Harper Reed, who emphasizes asking only one question at a time, a detail that may need repeated reminders.

- Use an LLM to interview a human to generate context documents for complex tasks.
- The LLM should ask one question at a time to gather information effectively.
- An interrogatory LLM can also review a document by interviewing a human expert instead of having the expert read the document.
- The technique can be used both to build context and to assess existing documents with multiple experts.
- This method may help people who struggle with writing to get knowledge out of their heads into usable form, even if the result has an AI-generated style.