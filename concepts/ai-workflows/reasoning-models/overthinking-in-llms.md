---
domain: ai-workflows
subdomain: reasoning-models
concept: overthinking-in-llms
title: Why Thinking More Can Make an LLM Dumb
sources:
  - title: "Why Thinking More Can Make an LLM Dumb"
    url: "https://blog.bytebytego.com/p/why-thinking-more-can-make-an-llm"
    author: "ByteByteGo"
    date: "2026-11-17"
---

# Why Thinking More Can Make an LLM Dumb

LLMs generate text token by token, conditioning each new token on the original prompt plus everything already written, so early output strongly shapes later reasoning. A chain of thought can help—working out that a $100 item raised then cut by 20% ends at $96 requires writing down the intermediate $120—but the same mechanism can also entrench a wrong interpretation. Reasoning models like OpenAI's o1 are trained to produce such intermediate 'thinking tokens' before answering, often kept private and shown only as a summary.

Extra compute can be spent at training time or at inference time ('test-time scaling'). Within a single attempt, each step can build on the last (tracing a buggy loop through a small example), while generating several independent attempts helps mainly when those attempts make different mistakes. DeepSeek's R1-Zero showed reinforcement learning can teach this behavior: using Group Relative Policy Optimization (GRPO), the model generates a group of attempts, scores them against verifiable answers (math keys, code tests), and is nudged toward attempts that beat their peers—no separate critic model needed. The team observed an 'aha moment' where the model spontaneously abandoned a messy approach and reconsidered its steps.

Overthinking has two failure modes. The benign one: asked '2 + 3', a model produced thirteen solutions to the same question, because a correctness checker scores a short correct answer and a long correct answer identically—knowing when to stop is a separate skill. The harmful one: given a timetable showing 9:00 with a note that trains usually run 10 minutes late, a model may reason its way to 9:10, drifting from reporting the schedule to predicting departure. Each sentence is sensible, but the accumulated context pulls the final answer away from the task, making the model appear dumb.

- Autoregressive generation means early tokens shape later reasoning, so a chain of thought can either catch errors or entrench them.
- Test-time scaling helps most when a single attempt follows a promising idea long enough to verify it; independent attempts help when they fail differently.
- GRPO trains reasoning by scoring a group of attempts against verifiable answers and favoring those that outperform their peers, without a critic model.
- Correctness-only rewards don't teach stopping: a model may keep re-solving an already-correct answer because length is unpenalized.
- Extra reasoning can introduce plausible but off-task assumptions, turning a correct first answer into a wrong final one.