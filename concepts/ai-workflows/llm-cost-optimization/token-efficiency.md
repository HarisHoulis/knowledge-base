---
domain: ai-workflows
subdomain: llm-cost-optimization
concept: token-efficiency
title: How to Actually Tokenmaxx and Save Millions
sources:
  - title: "How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival"
    url: "https://www.youtube.com/watch?v=8g1N_a3h9H0"
    author: "AI Engineer"
    date: "2026-10-14"
---

# How to Actually Tokenmaxx and Save Millions

Alvin Pane, head of the intelligent agents department at Outrival, argues that "token maxing" — burning the most tokens as a badge of honor — is a strange indicator of success for real products. Tokens are not the work itself; they are what you pay to get the job done. At Outrival, which processes billions of tokens per day for digital workers handling tasks via phone, text, and email, every extra query translates into huge delays and millions of dollars in costs. He reframes token maxing as extracting the most intelligence from the least amount of tokens possible.

The first step is observation: you can't fix what you can't measure. He recommends a shared model client so each attempt becomes part of a trace combining model calls, tools, and retries into a single task, recording prompt version, model settings, token usage, latency, and cost — with OpenTelemetry as a good framework. This telemetry enables a production benchmark. He warns that naive optimization hits a wall: swapping in a cheaper model caused an 18% disagreement rate with the expensive production baseline, but that summary figure hides the model's own variability. Running an "AA test" or "ceiling test" — running the expensive working model three times on the same input — revealed it contradicted itself about 7% of the time, i.e. only ~93% self-consistency. Demanding perfection from a cheap model that the existing expensive system couldn't achieve is therefore misguided; the ceiling test provides a measurable baseline.

With that baseline, three technical levers work in sequence. First, caching — structuring prompts to maximize prefix cache usage reduces task execution cost. Second, reducing prompt size: the Harbor Byte intent-classification prompt grew to almost 5000 tokens as developers kept adding rules and hard-coded transcripts, since no one wants to delete a line and break a working system. Automating this turns prompting into a search task: with a framework like DSPy, you define an interface contract (input data, output schema, evaluation function) and pass it to an optimizer like Jeppa, which treats the prompt as a search space, matches historical marks, and uses error feedback to correct instructions. This removed almost all long examples, replacing them with compact rules, yielding a 51% reduction in instruction tokens while maintaining the same functionality — an instant increase in margin. The third lever is directly reducing the size of the model.

- Token maxing (burning the most tokens) is a poor success indicator; the goal should be extracting the most intelligence from the fewest tokens.
- Instrument everything: use a shared model client and OpenTelemetry to trace prompt version, model settings, token usage, latency, and cost per task.
- Run a "ceiling test" (AA test) to measure the working model's self-consistency (~93% in their case) before judging a cheaper candidate model's 18% disagreement rate.
- Apply three levers in sequence: prefix caching, prompt-size reduction via automated search (e.g. DSPy/Jeppa), and model-size reduction.
- Automated prompt optimization cut instruction tokens by 51% while maintaining functionality, directly improving margin.