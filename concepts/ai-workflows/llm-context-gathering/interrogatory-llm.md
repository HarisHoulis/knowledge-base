---
domain: ai-workflows
subdomain: llm-context-gathering
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

Martin Fowler describes an approach where an LLM interviews a human to gather context needed for complex tasks, rather than having the human write that context manually. The LLM asks questions one at a time to build a context report that can be used by another LLM session. Fowler credits Harper Reed's blog for this pattern, emphasizing Reed's insistence on single-question prompts to keep the process focused.

This technique can also be used to review existing documents: an LLM interviews a human expert to verify accuracy, offering an alternative to having the expert read the document directly. Both use cases can be combined—one LLM builds a document, others review it with different experts. Fowler notes the broader applicability for knowledge capture, especially for people who find writing difficult, since an LLM interview can extract information that would otherwise remain unwritten.

- Use an LLM to interrogate a human to generate context for another LLM session.
- Ask one question at a time to keep the process coherent.
- Apply the same pattern to review documents via expert interviews.
- Useful for capturing knowledge from people who struggle with writing.