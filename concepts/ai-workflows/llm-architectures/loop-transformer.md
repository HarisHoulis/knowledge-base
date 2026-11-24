---
domain: ai-workflows
subdomain: llm-architectures
concept: loop-transformer
title: GLM-5.4 and the Rise of Loop Transformers
sources:
  - title: "GLM-5.4: Toward Generalized Coding with Our First Loop Transformer"
    url: "https://simonwillison.net/2026/Nov/23/glm-54/"
    author: "Simon Willison"
    date: "2026-11-23"
---

# GLM-5.4 and the Rise of Loop Transformers

GLM-5.4 from Z.ai is described as the company's first Loop Transformer, an architecture where a group of weight-shared layers runs for multiple iterations, refining hidden states from the previous pass. This yields a deeper effective network without increasing parameter count (z.ai blog, via Simon Willison).

This is the second looped-transformer mention in a week: Thinking Machines Lab's Inkling 2 Mini (Nov 20) runs its middle layers three times per token, letting the model apply more reasoning and reach answers with fewer tokens, especially on agentic coding tasks.

GLM-5.4 is not yet available as open weights. Willison accessed it via the Z.ai Coding Plan subscription, discovering that the coding plan and regular API share the same OpenAI-compatible Responses API at https://api.z.ai/api/v1, so the coding-plan key worked there. He built an llm-glm plugin before realizing llm-zai already existed; he shipped his only because llm-zai lacks support for the new model.

On the pelican-riding-a-bicycle benchmark, GLM-5.4's outputs at low, high, and max effort resemble those of GLM-5.3, and both are now much more comparable to OpenAI and Anthropic models than the distinctive earlier GLM 5.1 and 5.2 generations—a stark style transition between 5.2 and 5.3.

- Loop Transformers run weight-shared layer groups for multiple iterations, deepening the network without adding parameters
- Thinking Machines' Inkling 2 Mini uses the same approach, running middle layers three times per token for better reasoning with fewer tokens
- GLM-5.4 is not yet open weights; it's accessible via Z.ai's Coding Plan, whose key works with the shared OpenAI-compatible Responses API
- GLM-5.3 and 5.4 pelican outputs are more comparable to OpenAI/Anthropic models than the distinctive 5.1/5.2 generations