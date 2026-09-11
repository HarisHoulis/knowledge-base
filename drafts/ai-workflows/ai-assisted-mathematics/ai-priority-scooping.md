---
domain: ai-workflows
subdomain: ai-assisted-mathematics
concept: ai-priority-scooping
title: Some thoughts on the Navier–Stokes Millennium Prize Problem
sources:
  - title: "Some thoughts on the Navier–Stokes Millennium Prize Problem"
    url: "https://simonwillison.net/2026/Sep/8/on-navier-stokes/"
    author: "Simon Willison"
    date: "2026-09-08"
  - title: "On the Navier–Stokes Millennium Prize Problem"
    url: "https://openai.com/index/navier-stokes-solution/"
    author: "OpenAI"
  - title: "Statement on the Navier–Stokes collaboration"
    url: "https://cims.nyu.edu/~tristanb/statement.pdf"
    author: "Tristan Buckmaster"
---

# Some thoughts on the Navier–Stokes Millennium Prize Problem

OpenAI used an unreleased model to produce a resolution to the Navier–Stokes existence and smoothness problem, one of the seven Millennium Prize Problems carrying a $1,000,000 prize since May 24, 2000. OpenAI says its agents arrived at the resolution on September 5, about 88 hours after the first agents were launched, with Lean formalization and verification taking an additional 17 hours via GPT-6 Astra. Across all attempted problems the agents sent 4.9 million messages and used about 300 billion output tokens; for Navier–Stokes specifically, 2.7 million messages and approximately 130 billion output tokens (roughly $15,000,000 at public API prices for GPT-6 Astra).

The result is overshadowed by accusations from Tristan Buckmaster, an NYU mathematics professor collaborating with Levent Alpöge, an Anthropic employee. They worked on the problem for almost a year using Claude and Codex (mainly GPT-5.6 Sol), with a breakthrough on August 15. Buckmaster reports that OpenAI launched its effort on September 1 after hearing rumors, and that when he asked whether the model had been trained on or had access to their Codex sessions, he was told the model did not look up user data, but his repeated question about training went unanswered. OpenAI offered to wait for Tristan to publish or to have him author a paper about their result, but said Levent would not be invited as a co-author due to OpenAI's competitive relationship with his employer.

OpenAI states it reached out after completing its project and Lean verification to offer a concurrent release and recognize priority in a joint announcement, that researchers and agents did not see the pair's work until public release, and that no specific user data was accessed. It adds: "While unlikely, we cannot rule out that de-identified data derived from their usage of our products helped improve our models," noting the proofs differ significantly and even the precise results proved differ in the Euler case (forced vs unforced).

Willison interprets this as OpenAI hearing that some Millennium Prize problems had been solved with LLMs and seizing an opportunity to demonstrate its latest model without weighing the optics of scooping a team that had used OpenAI's own models for the better part of a year. He compares it to computer security, citing Anil Madhavapeddy's observation that just a rumor of a bug is enough to find an exploit, and asks whether knowing an unpublished solution exists could now trigger millions of dollars in LLM spending to get there first—while also highlighting the opacity of what "used to improve model performance" actually means.

- OpenAI's unreleased model resolved the Navier–Stokes Millennium Prize problem, with Lean formalization via GPT-6 Astra; the effort took ~88 hours plus 17 hours of verification and consumed ~130B output tokens for this problem alone.
- Tristan Buckmaster (NYU) and Levent Alpöge (Anthropic) spent nearly a year on related work using Claude, Codex, and GPT-5.6 Sol, reaching a breakthrough on August 15; OpenAI began its effort September 1 after rumors and produced its result September 5.
- OpenAI denies accessing specific user data but cannot rule out that de-identified data from the pair's product usage helped improve its models; Buckmaster's question about model training went unanswered.
- OpenAI offered a concurrent release and to recognize priority, but excluded Alpöge as co-author because of his employer Anthropic.
- Willison argues that merely knowing an unpublished solution exists may now trigger massive LLM spending to claim priority first, mirroring how a rumored security bug is enough to find an exploit.