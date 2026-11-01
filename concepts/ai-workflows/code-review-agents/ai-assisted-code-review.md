---
domain: ai-workflows
subdomain: code-review-agents
concept: ai-assisted-code-review
title: I Made a Fruit Fly Review My Code
sources:
  - title: "I Made a Fruit Fly Review My Code - Nick Nisi, WorkOS"
    url: "https://www.youtube.com/watch?v=geMAe-PLJF4"
    author: "AI Engineer"
    date: "2026-11-01"
---

# I Made a Fruit Fly Review My Code

Nick Nisi (WorkOS) argues that human code review has become the bottleneck in software development now that AI coding agents (Claude Code, Codex, etc.) write code faster than humans can review it. He notes that CI, linting, and review agents like Graphite and CodeRabbit already handle much of the mechanical checking, so the human reviewer's role is shifting from line-by-line approval toward providing context about why a change matters [source].

To dramatize the point, he runs a demo using the connectome of a male fruit fly brain — 176,000 neurons and roughly 6.3 million connections scanned under an electron microscope — to perform code review. He leaves the neurons untouched except for a small subset used to store memories of good versus bad code, and feeds the code in through the fly's sensilla (treated as its nose) using an AI model to generate about 30 unbiased questions about the code, converting the code into literal 'code smells' that the fly's memory then evaluates [source].

His broader claim is that if humans no longer write the code, requiring a human to review it makes less sense; what matters is whether the change does what is expected. Code review may persist but its purpose will change — less 'only a human can catch this' and more giving context back to the author about the proposed change and why it's important [source].

- Human review is now the bottleneck as AI agents accelerate code writing and PR volume
- CI, linting, and review agents (Graphite, CodeRabbit) already cover much mechanical checking
- The demo feeds code as 'smells' into a fruit fly connectome (176k neurons, ~6.3M connections) to review JavaScript
- Review's purpose is shifting from line-by-line approval to providing context about why a change matters
- The speaker doubts the premise that only a human can catch certain issues