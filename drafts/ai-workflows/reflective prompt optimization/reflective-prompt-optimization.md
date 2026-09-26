---
domain: ai-workflows
subdomain: reflective prompt optimization
concept: reflective-prompt-optimization
title: Beating RL With Reflection: GEPA and Optimize Anything
sources:
  - title: "Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA"
    url: "https://www.youtube.com/watch?v=OA-Mc60Rboo"
    author: "Lakshya A. Agrawal (AI Engineer)"
    date: "2026-09-26"
---

# Beating RL With Reflection: GEPA and Optimize Anything

Lakshya A. Agrawal argues that the standard route to teaching AI new tasks — weight updates through gradient descent in pre-training, supervised fine-tuning, or reinforcement learning — is sample-inefficient: it demands trillions of tokens for pre-training, tens of thousands of labeled examples for post-training, and hundreds of thousands of iterations for RL in areas like math and programming. Most teams lack that data and compute, and modern problems are limited by sample usage in two ways: subject-specific knowledge resources are scarce, and iterations are expensive because LLM workflows, agent deployments, and task metrics are slow or costly — agents can now run for hours, making real-time learning impractical ("Beating RL With Reflection: GEPA and Optimize Anything").

He critiques the dominant paradigm of RL with verified rewards: given a task, a model performs n parallel rollouts, receives a single reward, and an algorithm such as GRPO converts that scalar into gradients. That discards most of the information produced in each iteration — chains of thought, tool calls to the environment, environment responses, and error messages that carry diagnostic value. The first key idea of the talk is therefore reflective optimization in text space: instead of a zero-or-one reward signal, a language model or agent analyzes the entire execution process to understand what worked and what didn't, potentially drawing on all intermediate results and even making further tool calls such as searching a company knowledge base, manuals, or tutorials.

The second key idea is to update the prompt rather than the weights. Because a single natural-language change can produce a large behavioral shift — changing "Create a one-line resume" to "Create a 10-line resume" is his example — while achieving a comparable update through gradients would require thousands of tiny sequential updates, prompts are a high-leverage optimization target. Building on this, GEPA performs reflective optimization of agent prompts using an evolutionary cycle plus Pareto-based candidate selection, described as reinforcement learning in text space where feedback is text rather than only a reward point, allowing domain-specific learning.

Empirically, the speaker claims GEPA in a single reflection cycle using only three data points already achieves twice the efficiency of GRPO after 25,000 iterations, and that a few more GEPA steps widen the gap by another twofold. The optimization is self-driven by the Qwen 8B model with no external teacher experts, and GEPA's feedback provides a detailed problem specification — an understanding of input data, the purpose and context of the pipeline stage, and key observations — rather than vague motivational prompt hints ("Beating RL With Reflection: GEPA and Optimize Anything").

- Weight-update methods (pre-training, SFT, RL) are sample-hungry; most teams lack the data and compute, and current AI problems are bottlenecked by sample efficiency and expensive iterations.
- RL with verified rewards such as GRPO collapses each rollout into a single scalar reward, throwing away rich diagnostic signal in chains of thought, tool calls, environment responses, and error messages.
- GEPA proposes reflective optimization in text space: an LLM or agent reviews the whole execution trace and can issue extra tool calls (knowledge bases, manuals, tutorials) to reason about what worked.
- Optimizing the prompt rather than the weights is high-leverage — one natural-language substitution can cause a behavioral shift that would otherwise take thousands of small gradient steps.
- GEPA combines an evolutionary cycle with Pareto-based candidate selection and reportedly matches/exceeds GRPO efficiency: one reflection cycle with three data points beat GRPO's 25,000 iterations by 2x, widening to 4x with a few more steps, using self-optimization by a Qwen 8B model with no external teachers.