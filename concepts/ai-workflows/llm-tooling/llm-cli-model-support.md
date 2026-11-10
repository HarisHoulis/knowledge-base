---
domain: ai-workflows
subdomain: llm-tooling
concept: llm-cli-model-support
title: llm-anthropic 0.31 Adds Fable 5.2 and Mythos 5.2
sources:
  - title: "llm-anthropic 0.31"
    url: "https://simonwillison.net/2026/Nov/9/llm-anthropic/"
    author: "Simon Willison"
    date: "2026-11-09"
---

# llm-anthropic 0.31 Adds Fable 5.2 and Mythos 5.2

Simon Willison released llm-anthropic 0.31, adding Anthropic's newly released Fable 5.2 and Mythos 5.2 models to the `llm` CLI. Users can install the tool, set an Anthropic API key, and run prompts against the new models, e.g. `llm -m claude-fable-5.2 "Generate an SVG of a pelican riding a bicycle"` (Simon Willison, 2026-11-09).

He tested the pelican prompt at all five reasoning levels: low, medium, high, xhigh, and max. The best result came from `xhigh`. At `max`, the model failed to return an image at all, exhausting its tokens after spending 128,000 on reasoning.

That failure mirrors a bug previously seen with Opus 5.5, but it is new for the Fable series: both Fable 5 and Fable 5.1 returned max-effort pelicans without issue.

- llm-anthropic 0.31 adds Fable 5.2 and Mythos 5.2, usable via `llm -m claude-fable-5.2`
- The best pelican SVG came from the `xhigh` reasoning level
- At `max` effort, Fable 5.2 ran out of tokens after 128,000 reasoning tokens and returned no image
- This over-thinking failure matches an earlier Opus 5.5 bug but is new for the Fable series