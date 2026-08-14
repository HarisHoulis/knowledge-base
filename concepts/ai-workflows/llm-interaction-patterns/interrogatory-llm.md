---
domain: ai-workflows
subdomain: llm-interaction-patterns
concept: interrogatory-llm
title: Interrogatory LLM
sources:
  - title: "Bliki: Interrogatory LLM"
    url: "https://martinfowler.com/bliki/InterrogatoryLLM.html"
    author: "Martin Fowler"
---

# Interrogatory LLM

When an LLM needs extensive context for complex tasks, that context is usually written by humans. Martin Fowler describes an alternative: prompt the LLM to interview a human, asking questions until it has enough information to generate the context report itself. This report can then be used in another session, possibly with a different model, to perform the actual task (Fowler).

A key practice from Harper Reed's workflow is that the LLM should ask only one question at a time, which Fowler found necessary to reinforce repeatedly. The interrogatory approach can also be applied to document review: an LLM can interview a human expert to verify a specification's accuracy, offering an easier alternative to asking the expert to read and review the document directly (Fowler).

Fowler notes the technique is broader still. For people who struggle with writing, an LLM interview can extract knowledge that would otherwise remain unwritten, even if the resulting text has identifiable AI style. This is preferable to losing the information entirely due to writing difficulty (Fowler).

- Use an LLM to interview a human as a way to generate context for another LLM session.
- The LLM should ask one question at a time, and often needs reminders to stick to that.
- Interrogatory LLMs can validate existing documents by interviewing human experts.
- The technique helps people who find writing hard to share their knowledge.
- The resulting text may have an AI 'tang,' but having information is better than not having it.