---
domain: ai-workflows
subdomain: agentic-development
concept: ai-pr-automation
title: Forget "read the code," I don't even merge PRs myself
sources:
  - title: "Forget "read the code," I don't even merge PRs myself"
    url: "https://www.youtube.com/watch?v=lfSnYGdtbqE"
    author: "Kent C. Dodds"
    date: "2026-07-30T11:46:10+00:00"
---

# Forget "read the code," I don't even merge PRs myself

Kent C. Dodds discusses how he has largely moved away from reading code line-by-line and even from manually merging pull requests. He frames the decision to read code as a spectrum based on risk tolerance and the quality of one's 'agentic loop' and AI reviewers. Rather than reviewing every change, he focuses on reviewing systems and understanding the product, while AI agents handle the generated pull requests and iterate with review bots. The agent can merge branches, delete them, watch deployments, and test in production, then send Discord messages with summaries and relevant links. However, for changes with medium risk or broad impact, the agent flags them for human attention, and there remain cases where reading the code is necessary. Dodds emphasizes that the industry is moving toward producing far more code than can be manually reviewed, encouraging a 'factory engineer' mindset with minimal human interaction while still maintaining oversight through systems.

- Reading code is a spectrum: humans can skip line-by-line review when risk is low and AI review is strong.
- AI agents can manage the full PR lifecycle: generating PRs, iterating with review bots, merging, and deploying.
- Humans shift from code review to system review and product understanding.
- High-risk or broad-impact changes still require human oversight.
- The goal is to minimize human bottlenecks by turning the agentic loop into a reusable skill.