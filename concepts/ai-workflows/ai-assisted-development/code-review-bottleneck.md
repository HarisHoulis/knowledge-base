---
domain: ai-workflows
subdomain: ai-assisted-development
concept: code-review-bottleneck
title: AI Writes Code Faster Than Your Team Can Review It
sources:
  - title: "AI Writes Code Faster Than Your Team Can Review It - Andrew Norrish, Sourcegraph"
    url: "https://www.youtube.com/watch?v=-X3yXTwGs9A"
    author: "AI Engineer"
    date: "2026-11-02"
---

# AI Writes Code Faster Than Your Team Can Review It

Andrew Norrish, Director of Field Engineering at Sourcegraph, describes a recurring pattern among large enterprise customers: agent-based AI development dramatically increases development speed and codebase growth, and organizations allocate large budgets for AI tools while expecting developers to use them to justify the spend. Historically the first question on any AI roadmap was how many workers it would save, but at a recent Sourcegraph customer advisory board that question was not raised at all, signaling a shift in thinking.

The consequence is that code review has become the bottleneck. Where the constraint used to be human developer throughput, it is now the speed at which humans can review AI-written code. AI writes significantly more code, so pull request volume and PR size have both increased, and AI-generated PRs often lack the organizational and large-codebase context needed for industrial-grade quality. Increasingly such code reaches production without human review, and missed critical bugs are only a matter of time.

SREs bear much of the fallout: they are asked to resolve a growing number of incidents in code they may never have seen, without the context needed to track problems, so incidents become more frequent, longer to resolve, and more expensive. Hiring more SREs is a temporary fix that is getting costlier as incident growth outpaces hiring. Norrish also notes verification as a new bottleneck: distrust of AI code forces developers to spend more time testing it, while organizations expect review to confirm compliance with standards and regulations. AI still hallucinates, though it is improving.

- The development bottleneck has shifted from writing code to human review of AI-generated code
- AI increases both PR volume and PR size, and AI PRs often lack large-codebase and organizational context
- AI-written code increasingly reaches production without human review, raising the risk of missed critical bugs
- SREs face more incidents in unfamiliar code without context, making incidents costlier and harder to resolve
- Distrust of AI output makes verification and compliance review an additional bottleneck