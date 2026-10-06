---
domain: ai-workflows
subdomain: llm-context-handling
concept: lost-in-the-middle
title: The LLM Blindspot: Why Models Forget What’s in the Middle of Your Prompt
sources:
  - title: "The LLM Blindspot: Why Models Forget What’s in the Middle of Your Prompt"
    url: "https://blog.bytebytego.com/p/the-llm-blindspot-why-models-forget"
    author: "ByteByteGo"
    date: "2026-10-05"
---

# The LLM Blindspot: Why Models Forget What’s in the Middle of Your Prompt

LLMs can fail to use information that is present in the prompt, especially when it appears in the middle of long input. The article calls this the “lost in the middle” effect or LLM blind spot. A coding assistant might ignore a clearly stated retention rule—such as keeping audit logs for 37 days—and generate code that deletes them after 30 days because the rule was buried mid-prompt (ByteByteGo).

The effect is demonstrated by moving the same supporting fact to different positions while keeping the question fixed. Performance tends to be strongest near the beginning, associated with primacy bias, and near the end, associated with recency bias, producing a U-shaped accuracy curve; middle positions tend to be weaker (ByteByteGo).

Transformer attention and causal masking help explain asymmetries. Early tokens can influence later representations through multiple layers, while tokens near the end are closer to the question and answer. However, permission to attend does not guarantee high attention weight, and when generating an answer, full causal attention can access all earlier prompt positions, including the middle (ByteByteGo).

Larger context windows increase capacity but do not guarantee uniform reliability. The article distinguishes maximum context size from effective context size, which depends on the task and is illustrated by RULER benchmark findings of degradation as input length increases. Mitigations include prompt optimization, pruning unnecessary context, and retrieval-augmented generation to reduce how much searching the model must do inside the prompt (ByteByteGo).

- LLMs often show lower accuracy for information placed in the middle of a long prompt, producing a U-shaped accuracy curve with primacy and recency advantages (ByteByteGo).
- The problem is not simply missing or truncated information: the evidence can be present in the input but still fail to influence the answer due to positional effects (ByteByteGo).
- Transformer attention, causal masking, and proximity to the question help explain why beginnings and ends tend to have advantages, but the explanation is not as simple as one token accumulating all attention (ByteByteGo).
- Larger context windows do not solve the issue because maximum context size is different from effective context size, which varies by task (ByteByteGo).
- Mitigation strategies include clearer prompt organization, pruning unnecessary context, and retrieval-augmented generation to supply a smaller set of relevant evidence (ByteByteGo).