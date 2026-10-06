---
domain: ai-workflows
subdomain: llm-evaluation
concept: saturated-benchmark-svg-test
title: Mistral Large 4 and the armadillo-in-fishnet-tights benchmark
sources:
  - title: "Mistral Large 4"
    url: "https://simonwillison.net/2026/Oct/6/hn-49982139/"
    author: "Simon Willison"
    date: "2026-10-06"
  - title: "Mistral Large 4 (Hacker News discussion)"
    url: "https://news.ycombinator.com/item?id=49977979"
    author: "Hacker News"
    date: "2026-10-06"
  - title: "Rendered SVG outputs (gist)"
    url: "https://gist.github.com/simonw/18c9f7fc3b3705cf88514cb9170ec246"
    author: "Simon Willison"
    date: "2026-10-06"
---

# Mistral Large 4 and the armadillo-in-fishnet-tights benchmark

This post is Simon Willison's comment on a Hacker News thread about Mistral Large 4. It opens with a quoted HN comment from wren6991 arguing that standard benchmarks are saturated, illustrated with the joke that "Frontier models are tested with an armadillo in fishnet tights jaywalking on Mars."

Willison takes the joke literally, running the same prompt — "Generate an SVG of an armadillo in fishnet tights jaywalking on Mars" — against four frontier models using his `llm` command-line tool: `claude-opus-5.5`, `gpt-6.1-sol`, `gemini-3.8-flash` and `mistral/mistral-large-4`. No model was given special configuration; he notes these are the "default reasoning levels for each".

The post provides no qualitative comparison of the resulting SVGs. It links out to a markdown SVG renderer tool pointed at a gist containing the outputs, leaving the evaluation to the reader.

- A HN commenter claims frontier-model benchmarks are saturated, using an absurd hypothetical prompt as the illustration.
- Willison runs that exact prompt — an SVG of an armadillo in fishnet tights jaywalking on Mars — across four models via the `llm` CLI.
- Models tested: claude-opus-5.5, gpt-6.1-sol, gemini-3.8-flash and mistral/mistral-large-4, all at their default reasoning levels.
- The post presents no verdict on the outputs; results are linked via a markdown SVG renderer pointed at a GitHub gist.