---
domain: ai-workflows
subdomain: llm-evaluation
concept: three-gulfs-framework
title: Evals for AI Engineers: The Three Gulfs of LLM Application Development
sources:
  - title: "Evals for AI Engineers"
    url: "https://blog.bytebytego.com/p/evals-for-ai-engineers"
    author: "ByteByteGo (excerpt from Shreya Shankar and Hamel Husain)"
    date: "2026-11-18"
---

# Evals for AI Engineers: The Three Gulfs of LLM Application Development

Shreya Shankar and Hamel Husain argue that building AI products is dominated by evaluation, which they frame through the "Three Gulfs" model adapted from Shankar et al. (2025) and inspired by Norman (1988). The first gulf, comprehension, lies between the developer and the data: without characterizing real inputs (forwards, quoted threads, multilingual signatures) and the model's actual output patterns at scale, you design against an imagined task. The second, specification, lies between intent and instructions—natural-language prompts like "extract the sender's name and summarize" leave format, scope, and edge cases unstated, so the model guesses. The third, generalization, lies between the data and the model: even with clear specs, LLMs fail inconsistently, e.g. returning a name mentioned in the body instead of the header.

The framework is diagnostic: when debugging, teams can classify a failure as a specification problem (fixable with better instructions or agent design) or a generalization problem (measurable via automated evals). The authors note the gulfs apply across domains—support chatbots, code assistants, personal stylists—and that the stakes differ by application: programmers can self-specify and debug, while a styling app's users cannot easily detect generalization failures, requiring more rigorous evaluation.

To bridge the gulfs, they propose an iterative Analyze-Measure-Improve lifecycle. Analyze means reading traces and consulting users/domain experts to catalog failure modes; Measure means quantifying the generalization issues that remain after specification fixes; Improve closes the loop. Evaluation is framed not as a one-time check but as an ongoing process where requirements emerge only after inspecting real outputs.

- The Three Gulfs—comprehension (developer vs. data), specification (intent vs. instructions), and generalization (data vs. model)—give teams a shared vocabulary for diagnosing LLM application failures.
- Evaluation is iterative, not one-time: requirements become clear only after inspecting real inputs and outputs, so trace-reading and expert input drive discovery of failure modes.
- Distinguish specification failures (fixable with clearer prompts/agent logic) from generalization failures (measured with automated evals) to choose the right remedy.
- Evaluation rigor should scale with stakes: applications where users can't catch mistakes themselves need more rigorous processes.