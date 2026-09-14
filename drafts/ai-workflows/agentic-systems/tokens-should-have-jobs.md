---
domain: ai-workflows
subdomain: agentic-systems
concept: tokens-should-have-jobs
title: Tokens Should Have Jobs: Specialized Token Roles in Agentic Systems
sources:
  - title: "Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic"
    url: "https://www.youtube.com/watch?v=PXj0p_mW9nI"
    author: "AI Engineer (Katelyn Lesse & Angela Jiang)"
    date: "2026-09-14"
---

# Tokens Should Have Jobs: Specialized Token Roles in Agentic Systems

Katelyn Lesse and Angela Jiang propose that agentic systems should stop treating all tokens as fungible. The common lever for improving outcomes is increasing the token budget or using more expensive tokens, but that assumes every token is doing the same job: execution. They ask what happens if some tokens are given different jobs instead (AI Engineer, 2026).

They describe three strategies. In advising, an executor can call an adviser for guidance, such as a sales agent flagging overdue follow-ups or stalled deals. In grading, a grader evaluates the executor against a rubric and the executor iterates until it meets the criteria; an example is a customer-service agent deciding refunds. In dreaming, a dreamer inspects the executor's work and transcripts, writes findings to memory, and the executor picks up that memory for the next round; an example is a recruiting agent that improves fit over time (AI Engineer, 2026).

To make the ideas concrete, they created a bench of financial-analysis tasks intended to replicate how an expert human financial analyst would perform. The provided transcript ends before reporting the experiment results (AI Engineer, 2026).

- Instead of treating tokens as fungible, assign tokens distinct jobs such as executor, adviser, grader, or dreamer.
- Advising: an executor can call an adviser for guidance; useful for sales agents tracking overdue follow-ups or stalled deals.
- Grading: a grader uses a rubric to evaluate executor output and drive iteration; example: customer-service refund decisions.
- Dreaming: a dreamer inspects executor transcripts and writes learnings to memory for the next execution round; example: recruiting fit.
- They built a financial-analysis bench to compare agent strategies against expert human analyst performance, though the excerpt does not include results.