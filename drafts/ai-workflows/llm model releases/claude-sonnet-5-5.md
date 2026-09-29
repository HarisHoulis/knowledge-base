---
domain: ai-workflows
subdomain: llm model releases
concept: claude-sonnet-5-5
title: Claude Sonnet 5.5
sources:
  - title: "Claude Sonnet 5.5"
    url: "https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/"
    author: "Simon Willison"
    date: "2026-09-28"
  - title: "Opus 5.5, Sol and Luna"
    url: "https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/"
    author: "Simon Willison"
    date: "2026-09-22"
---

# Claude Sonnet 5.5

Simon Willison tests Anthropic's newly released Claude Sonnet 5.5 using his standard pelican-riding-a-bicycle benchmark. Sonnet 5.5 reproduced the same failure seen in Opus 5.5 at "max" thinking effort: the model reasoned for 128,000 tokens (costing $1.28) before running out of tokens and failing to produce an SVG. At "xhigh" thinking effort it succeeded, producing a pelican in 41 seconds at a cost of 5.74 cents.

Willison reports that Sonnet 5.5 appears to be almost as good as Opus 5.5 on some coding tasks, including the viral 3D animation tricks being shared around.

The most notable aspect of the release, per Willison, is that Sonnet 5.5 now powers the free tier on claude.ai. Since OpenAI's ChatGPT free tier uses Luna 5.6, he concludes Anthropic currently has the much more capable free offering. Running his 3D pelican WebGL prompt against that free tier produced a "solid effort" page.

Anthropic's announcement restates that Haiku 5.5 will be available "in the coming weeks", and Willison hopes it will be price-competitive with GPT-6 Luna.

- Sonnet 5.5 repeats Opus 5.5's "max" thinking-effort bug: 128,000 tokens (~$1.28) burned before failing to produce an SVG.
- At "xhigh" effort it succeeded on the pelican test in 41 seconds for 5.74 cents.
- It is reportedly almost as good as Opus 5.5 on some coding tasks, including viral 3D animation tricks.
- Sonnet 5.5 now backs the free claude.ai tier, which Willison rates as more capable than ChatGPT's free tier running Luna 5.6.
- Haiku 5.5 is promised "in the coming weeks", with hopes it will be price-competitive with GPT-6 Luna.