---
domain: ai-workflows
subdomain: llm-knowledge-capture
concept: interrogatory-llm
title: Interrogatory LLM
sources:
  - title: "Bliki: Interrogatory LLM"
    url: "https://martinfowler.com/bliki/InterrogatoryLLM.html"
    author: "Martin Fowler"
---

# Interrogatory LLM

When complex tasks require LLMs to have substantial context, the usual approach is to have a human write that context. However, an alternative is to use the LLM itself to generate the context by interrogating a human expert. The LLM asks the questions necessary to gather all relevant information, consults external sources when needed, and produces a context report for downstream LLM sessions (Fowler). Harper Reed's workflow emphasizes asking only one question at a time, a constraint that often needs reinforcement (Fowler).

This interrogation technique can also invert the typical review process. Instead of having a human expert read a document to check it, an LLM can interview the expert to verify the document's accuracy. This is especially useful when documents are not well-written or when experts find reading and reviewing difficult (Fowler). Combining both uses, one interrogatory LLM can build a document while others interview different experts to review it.

Beyond context creation for LLM use, the technique addresses a broader challenge: many people find writing hard. For those who naturally think by writing, this is not an issue, but for others, extracting knowledge from their heads into a human-readable form is painful. An LLM interview can serve as an alternative, even if the output has the characteristic AI style; it is better to have the information captured imperfectly than to lose it entirely due to writing difficulties (Fowler).

- Use an LLM to interview a human to generate rich context reports for other LLM sessions.
- Instruct the LLM to ask only one question at a time to avoid overwhelming the interviewee.
- Interrogatory LLMs can review documents by interviewing human experts, offering an alternative to traditional document review.
- Multiple interrogatory LLMs can be chained to build and then validate context with different experts.
- The technique helps non-writers externalize knowledge through conversation instead of writing.