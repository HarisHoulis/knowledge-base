---
domain: ai-workflows
subdomain: automated-pr-review
concept: agentic-pr-merging
title: Forget "read the code," I don't even merge PRs myself
sources:
  - title: "Forget "read the code," I don't even merge PRs myself"
    url: "https://www.youtube.com/watch?v=lfSnYGdtbqE"
    author: "Kent C. Dodds"
    date: "2026-07-30T11:46:10+00:00"
---

# Forget "read the code," I don't even merge PRs myself

Kent C. Dodds argues that the practice of reading every line of code before merging is becoming obsolete. Instead, he describes a spectrum of code-reading intensity based on risk tolerance and the maturity of one's agentic loop and AI reviewers. He notes the industry is moving toward producing far more code than humans can reasonably review, aligning with the "factory engineer" concept where human interaction is minimized (Dodds, 2026).

The core problem, he explains, is that if you're not reading code, you become a babysitter for AI agents that open pull requests. To avoid being a bottleneck, he recommends using PRs for projects you care about, but letting the AI agent drive the entire lifecycle: opening the PR, iterating with review bots, merging, deleting the branch, and watching the production deployment. The human receives a summary via Discord with links to relevant details (Dodds, 2026).

This approach is not a blanket policy; exceptions exist for medium- or high-risk changes that impact many areas. In those cases, the agent flags the PR for human review. The key takeaway is to turn the human-in-the-loop review process into a skill that the agent can execute, freeing the human to focus on exceptions and system-level understanding rather than reading every line (Dodds, 2026).

- Reading code is a risk-based spectrum, not an all-or-nothing practice.
- AI agents can fully automate the PR lifecycle—from opening to merging to deploying—with humans only reviewing high-risk exceptions.
- The "factory engineer" mindset prioritizes minimal human interaction and maximum AI autonomy.
- Using PRs for important projects is still worthwhile, but the human should not be the bottleneck; summaries and links allow on-demand deep dives.
- The trend is toward producing more code than humans can ever review, making agentic loops and AI reviewers critical.