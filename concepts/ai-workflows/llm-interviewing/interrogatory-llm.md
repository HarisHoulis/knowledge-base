---
domain: ai-workflows
subdomain: llm-interviewing
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

Martin Fowler describes a pattern where an LLM interviews a human to gather context needed for another LLM session, rather than having the human write a lengthy context document. The LLM asks questions one at a time, collects information, identifies external sources to consult, and then produces a context report. This approach is inspired by Harper Reed's blog post, which emphasizes asking only one question at a time—something Fowler notes requires frequent reminders.

The technique can also be used for document review: give the LLM a specification or domain document, and have it interview a human expert to verify accuracy. This can be more effective than asking the expert to read and review the document, especially if the document is not well-written. Both use cases can be combined—building a document with one interrogatory LLM and reviewing it with others.

Beyond LLM-specific tasks, Fowler suggests this could help people who struggle with writing to externalize their knowledge. For those who find writing very hard, an LLM interview may be easier than composing a document, even if the resulting text has an AI flavor. The value of capturing information outweighs stylistic concerns.

- Use an LLM to interview a human to generate context for another LLM session.
- Instruct the LLM to ask one question at a time to avoid overwhelming the user.
- Apply the same technique to review existing documents by interviewing a human expert.
- Helps non-writers convert their knowledge into a consumable form, replacing or augmenting traditional document writing.