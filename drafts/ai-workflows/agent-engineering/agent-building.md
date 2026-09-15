---
domain: ai-workflows
subdomain: agent-engineering
concept: agent-building
title: Building Vertical Agents: Vercel's Data Science Agent D0 and the AI SDK
sources:
  - title: "How We Solved Agent Building — Andrew Qu, Vercel"
    url: "https://www.youtube.com/watch?v=9dYcwOkpCE8"
    author: "AI Engineer"
    date: "2026-09-14"
---

# Building Vertical Agents: Vercel's Data Science Agent D0 and the AI SDK

Andrew Qu, chief of software at Vercel, describes Vercel's shift from helping people ship websites and web apps to helping them build agents (Qu, Vercel talk). Vercel built the AI SDK so that instead of switching out 300-400 lines of provider-specific code, you switch one line, with the same model interface underlying all providers. They also built tooling for model fallbacks, secure code execution, better pricing when a model is inactive and waiting for responses, and durability and resumability.

The talk frames the goal with a Bill Gates 1980 quote about a computer on every desk and in every home; Qu and Vercel's CTO asked whether instead there could be an agent on every desk (Qu, Vercel talk). Today agents are mainly used for coding and technical workloads, but Qu reports expansion into design, product management, and other verticals. Roughly a year ago, when Sonnet 4 was the state of the art, he surveyed job functions at Vercel — marketing, sales, finance, legal — asking what they hated most about their jobs.

The most compelling use case came from the data team: a lean team facing a growing volume of customer, analytics, metrics, and sales data, and constantly having to drop everything to write queries, run analyses, and return recommendations when someone in marketing or sales asked a question about a customer or product (Qu, Vercel talk). Qu worked with the VP of data on a better way.

The first version was a mega prompt: Qu dumped the Snowflake schema into a system prompt along with a question, had the model generate SQL, and copy-pasted it to run manually. That gave modest confidence that models were not yet good enough but that context engineering and guardrails could improve results. He and the VP of data mapped the data scientist's actual workflow phases — processing the question, exploring the semantic layer and join patterns, executing SQL, retrying when queries failed or were too expensive, and reporting/visualizing — into specific agent workloads, producing a second version called D0.

- Vercel's AI SDK lets you switch model providers with one line of code instead of 300-400 lines of provider-specific code, with a shared model interface across providers.
- Supporting agent infrastructure includes model fallbacks, secure code execution, cheaper pricing while inactive/waiting for responses, and durability and resumability.
- The motivating use case was Vercel's data team, which had to drop everything to write queries and analyses whenever marketing or sales asked about a customer or product.
- The first iteration was a mega prompt: Snowflake schema pasted into a system prompt, model-generated SQL run manually, which suggested context engineering and guardrails could compensate for weak models.
- Mapping the data scientist workflow phases (question, semantic layer and joins, SQL execution, retries, reporting) into distinct agent workloads produced the second version, called D0.