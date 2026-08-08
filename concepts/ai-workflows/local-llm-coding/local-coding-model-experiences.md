---
domain: ai-workflows
subdomain: local-llm-coding
concept: local-coding-model-experiences
title: Experiences with local models for coding
sources:
  - title: "Experiences with local models for coding"
    url: "https://martinfowler.com/articles/exploring-gen-ai/local-models-for-coding-experiences.html"
    author: "Martin Fowler"
    date: "Jul 30"
---

# Experiences with local models for coding

Martin Fowler recounts his hands-on evaluation of locally run small language models for agentic coding, using an M3 Max (48GB) and M5 Pro (64GB). He frames viability through a funnel of increasing difficulty: fitting into RAM, achieving reasonable speed, handling tool calling, producing functionally correct code, managing longer contexts, and tackling larger tasks with acceptable code quality. His manual and automated tests used JavaScript/TypeScript tasks, revealing that task choice—such as amount of code search, file count, and instruction specificity—significantly impacts success [1].

Results were inconsistent: Gemma 4 26B succeeded manually but failed 3/3 times in automated one-shot evals, while Qwen3.6 35B MoE succeeded 2/2 in one task but failed 5/7 times in another. Surprisingly, running the same model on the 64GB machine improved outcomes versus 48GB, a mystery Fowler cannot explain. In day-to-day use, Qwen3.6 35B handled small defined changes, Bash/Python scripts, and website content well, but struggled with complex game logic. Fowler notes that smaller models force more careful code review, which he views positively as a 'detox' from over-reliance on stronger models [1].

His current default setup is qwen3.6-35b-a3b (4BIT quantization), with reasoning off and max context window, using OpenCode or Pi as harnesses, primarily for small tasks often pre-planned by a larger model. Overall, he concludes that local agentic coding is far from the capabilities of bigger models, but the experience has improved his intuition for when to use them [1].

- Local models require a structured viability funnel: RAM, speed, tool calling, functional correctness, context handling, task complexity, and code quality.
- Task characteristics (code search, file count, instruction specificity, tech stack) matter more than raw model capability.
- Results were inconsistent across manual and automated evaluations; Qwen3.6 35B MoE was the most practical for day-to-day small tasks.
- Running on 64GB RAM yielded better outcomes than 48GB with the same model, though the reason remains unclear.
- Smaller models encourage more attentive code review, which Fowler sees as a benefit despite their limitations.