---
domain: ai-workflows
subdomain: LLM cost optimization
concept: model-routing-harness
title: Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI
sources:
  - title: "Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI"
    url: "https://www.youtube.com/watch?v=48YUYDjwfYY"
    author: "AI Engineer"
    date: "2026-10-02T20:00:14+00:00"
---

# Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI

In this talk, Laura (co-founder and president of Cast AI, the company behind Kimchi) and Zilvinas (who leads the Kimchi platform) frame rising LLM token costs as a business problem. They cite two news stories: a company in India that spent $500 million on Anthropic in one month, and Uber's CTO saying the company used up its entire annual Anthropic budget in four months. Companies have responded by restricting token use, which developers experience as a severe limit, but Kimchi argues managers should instead make tokens effectively unlimited and inexpensive. Kimchi uses proprietary models for complex cases and open source for everything else.

The core argument is that cost per token is not the same as cost per task. Laura points to a university study comparing models at the same quality: Gemini 3 looked inexpensive at $3.5 per million tokens, but completing the task cost $705, while Minimax 2.7 cost $1.5 per million tokens and $148 for the task. Because models differ in both token price and task cost, Kimchi built a programming agent with an automated token optimization system that chooses the right model for the task at the right time based on the outcome.

After three months of internal use across Cast AI's roughly 300 employees—two-thirds of them developers—Kimchi reports 2.5x savings on cloud services. During that period, token usage increased 1.5x while cloud costs decreased 1.5x, meaning the agent can be treated as effectively unlimited relative to token growth. The harness also changed model selection over time, shifting heavily around June 12; Kimi 2.6 became the most popular choice by June 3, and Minimax 3 won on June 21. Laura argues humans would not continuously adapt to new models, but an autonomous code-writing agent obsessed with token value will, so managers should focus on providing optimal token value for the same result.

- Token costs have become a major business problem, with reported examples of massive Anthropic spending; rationing tokens is framed as the wrong response.
- Kimchi argues managers should make tokens unlimited and inexpensive, using an automated harness to pick the optimal model per task.
- Cost per token alone is misleading: the same task can cost $705 on Gemini 3 versus $148 on Minimax 2.7 at comparable quality.
- Cast AI reports 2.5x cloud cost savings over three months while token usage rose 1.5x and cloud costs fell 1.5x.
- The harness autonomously shifts model selection over time—e.g., toward Kimi 2.6 and later Minimax 3—without requiring humans to manually adapt.