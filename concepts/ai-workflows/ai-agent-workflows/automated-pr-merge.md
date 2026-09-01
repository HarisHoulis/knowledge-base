---
domain: ai-workflows
subdomain: ai-agent-workflows
concept: automated-pr-merge
title: Forget "read the code," I don't even merge PRs myself
sources:
  - title: "Forget "read the code," I don't even merge PRs myself"
    url: "https://www.youtube.com/watch?v=lfSnYGdtbqE"
    author: "Kent C. Dodds"
    date: "2026-07-30T11:46:10+00:00"
---

# Forget "read the code," I don't even merge PRs myself

In this video, Kent C. Dodds challenges the common practice of reading all code before merging, framing it as a spectrum of risk tolerance, agentic loop maturity, and AI reviewer capability. He argues that the industry is moving toward producing far more code than any human can manually review, so engineers should optimize for systems that reduce human involvement in routine changes.

Dodds details his own workflow where AI agents generate pull requests and iterate with review bots until they pass all checks. The agent then merges the PR, deletes the branch, and monitors the production deployment, sending a summary via Discord with relevant links for optional human review. This shifts the engineer's role from reading code to reviewing systems and exceptions.

He also notes that some changes are flagged as medium risk or high impact, prompting human attention before merging. This approach reflects a broader trend toward "factory engineer" principles where automation handles routine tasks, allowing humans to focus on durable skills and edge cases (Dodds, 2026).

- Reading code is not binary; it's a spectrum based on risk, agentic loop quality, and AI reviewer effectiveness.
- AI agents can autonomously open, review, merge, and deploy PRs, freeing humans from the loop.
- Automated workflows should provide concise summaries and selective escalation for high-risk changes.
- The shift is toward producing and merging more code with less manual review, emphasizing system-level oversight.