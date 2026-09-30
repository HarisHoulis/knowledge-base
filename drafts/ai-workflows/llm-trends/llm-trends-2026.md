---
domain: ai-workflows
subdomain: llm-trends
concept: llm-trends-2026
title: 2026 in LLMs (so far)
sources:
  - title: "2026 in LLMs (so far)"
    url: "https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/"
    author: "Simon Willison"
    date: "2026-09-27"
---

# 2026 in LLMs (so far)

Simon Willison's annotated keynote traces 2026 as the year coding agents crossed from "often make mistakes" to reliable daily use. The trigger was November 2025's Claude Opus 4.5 and GPT-5.1: individually incremental releases, but paired with their coding agent harnesses (Claude Code, Codex) they made something that previously didn't work start working. December holiday tinkering let developers discover how much more these combinations could do, and by January many were putting them into production (Willison, 2026).

The year's dominant artifact was OpenClaw, first committed in November 2025 under the name "Warelay" and renamed repeatedly (CLAWDIS, CLAWDBOT, Moltbot) before reaching OpenClaw with 8,300 commits in under two months — over 100,000 today. Willison calls it "the most vibe-coded piece of software in existence" and the founder of a category (Claws, now rebranded "personal agents"). Bay Area Apple stores sold out of Mac Minis as people bought them to host their Claws. MoltBook, a social network for agents, blew up in a week and was forgotten the next, then acquired by Meta a month later (Willison, 2026).

In February, StrongDM described a "Software Factory" (Dan Shapiro's "Dark Factory") with two rules in force since July 2025: code must not be written by humans, and code must not be reviewed by humans. Willison notes they were living six months ahead of everyone else, exploring how to be confident in quality without reading the code. Tokenmaxxing — Meta, Microsoft, and Uber pushing AI adoption metrics — spiked and collapsed within months once it became clear agents are expensive; Willison argues AI hit product market fit in 2026 primarily through coding agents. He also describes "Deep Blue" (AI-induced engineer ennui), his own "AI mania" and its cure via building a Python JavaScript interpreter and a Python WebAssembly runtime, plus the Claude Mythos model withheld to security researchers as plausibly too dangerous, given how good agents had become at finding bugs (Willison, 2026).

- Claude Opus 4.5 and GPT-5.1 (Nov 2025) plus their agent harnesses moved coding agents from error-prone to reliable enough for daily work.
- OpenClaw went from first commit to a software category in months (8,300 commits by January, 100k+ now), spawning a "Claw" ecosystem and real consumer demand, including install parties in China.
- StrongDM's Software Factory rules — no human-written code, no human code review — foreshadowed a year of debate about verifying agent output.
- Tokenmaxxing rose and fell as agent usage proved expensive; Willison credits coding agents with AI reaching product market fit in 2026.
- Agent security and sandboxing dominated conference sessions (~40 of 277), though the predicted "Challenger disaster" had not materialized.