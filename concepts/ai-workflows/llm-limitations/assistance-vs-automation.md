---
domain: ai-workflows
subdomain: llm-limitations
concept: assistance-vs-automation
title: I Love You So Much: Why AI Is Superhuman at Some Tasks and Useless at Others
sources:
  - title: "I love you so jevving much — Diogo Almeida, TypeSafe AI"
    url: "https://www.youtube.com/watch?v=Cyt3LU8TyNc"
    author: "AI Engineer"
    date: "2026-11-15"
---

# I Love You So Much: Why AI Is Superhuman at Some Tasks and Useless at Others

Diogo Almeida, a co-author of InstructGPT, ChatGPT, and RLHF, argues that the AI industry is split into two cults: one that points to benchmarks showing models outperforming humans and claims AGI is perpetually three months away, and another that observes the rest of the world—especially outside San Francisco—has barely changed despite AI being genuinely transformative. He insists both views see the same facts, and that experts owe a simple explanation for why AI is superhumanly good at some tasks (e.g., deep research, millennium-style math problems) yet worthless at others that seem far easier (e.g., accounting).

His answer is a distinction between tasks that inherently require a person and tasks that require automation. Models excel where pleasing a human is the goal—deep research produces well-written output, but if correctness is mandatory you would still choose a human. Conversely, automation tasks demand an abstraction detached from the process: a decision is made, then execution returns to code, the language of automation. AI consistently fails at these, producing recurring high-profile failures such as self-driving services.

Almeida, despite co-authoring RLHF, calls it part of the problem: because of RLHF, all modern models require a human in the loop whenever a task is not trivially verifiable and independently performable, since the human-feedback objective was literally trained into them. He summarizes the state of affairs as 100% of modern language models being optimized for assistance rather than automation, and argues there is a better way.

- AI is uneven: superhuman at human-centric tasks like deep research but unreliable at seemingly simpler automation tasks like accounting or self-driving
- Pleasing a person is not the same as getting the job done; automation requires decisions abstracted from the process and handed back to code
- RLHF is framed as part of the problem: it bakes in a human-in-the-loop requirement for any non-trivially-verifiable task
- The industry splits into a benchmark-driven AGI-hype cult and a reality-driven skepticism, and experts should reconcile them with a simple explanation
- Modern language models are optimized for assistance, not automation