---
domain: ai-workflows
subdomain: agent-orchestration
concept: orchestrating-coding-agents
title: Orchestras, Not Factories: How the Fastest Builders Work
sources:
  - title: "Orchestras, Not Factories: How the Fastest Builders Work — Charlie Holtz, Conductor"
    url: "https://www.youtube.com/watch?v=TRfzFJCJ7ZE"
    author: "AI Engineer"
    date: "2026-09-27"
---

# Orchestras, Not Factories: How the Fastest Builders Work

Charlie Holtz, co-founder of Conductor, opens by describing Conductor as a desktop application for managing a team of programmers (coding agents) simultaneously — one interface to manage what would otherwise be a bunch of terminal windows for cloud code and coding agents (source). Building Conductor gave him close-up visibility into how the best developers work, which he distills into principles for becoming the fastest developer in your organization.

Principle one is to stay on the front lines: try the latest tools practically the day they come out (Ultra Code, Slash Go, etc.). Staying on the cutting edge lets builders come up with new ideas about what to actually build — his own company was building a different app called Chorus when they became such advanced Cloud Code users (as of February of the prior year) that they cloned their repository five times, opened up working trees, and built Conductor as an internal tool from that workflow. He argues you can no longer rely on information trickling down through your social graph, because things are moving too fast — you'll always be three to six months behind. Unless you're building a startup, you should be the person in your company who always knows the latest workflows (source).

Principle two guards against over-optimization, which he calls "midwig-meming" — spending all your time on your workflow rather than the actual work. The heuristic Conductor uses internally is "don't beat the market": ask why a given workflow isn't the default, and if it works for everyone, wait for Anthropic or OpenAI to build it into the standard harness rather than optimizing for it yourself. It's framed like the efficient market hypothesis — without real alpha, you shouldn't optimize your workflow too much. True alpha means information about your users or codebase that the models may not know about; Conductor, as a chat application needing to render very long chats quickly, invests heavily in optimizing React queries and is willing to make sacrifices elsewhere in the codebase because that is its alpha. Otherwise, he warns, don't be the person with a great Emacs setup who doesn't get the job done (source).

Principle three, cut off in the transcript, is to create clutter-free zones — Conductor's term for a part of the codebase or application that requires very strict human review (source).

- Conductor is a desktop app that manages a team of coding agents simultaneously through one interface instead of many terminal windows.
- Stay on the front lines: adopt new tools the day they ship, since relying on your social graph for workflow information leaves you three to six months behind.
- Avoid "midwig-meming" — over-investing in workflow rather than work. Use the "don't beat the market" heuristic: if a workflow isn't the default and you lack real alpha, let the model providers build it in.
- Reserve deep optimization for where you have alpha — unique information about your users or codebase that the models don't have (e.g. Conductor optimizing React queries for rendering long chats).
- Create "junk-free zones": parts of a codebase or application that require very strict human review.