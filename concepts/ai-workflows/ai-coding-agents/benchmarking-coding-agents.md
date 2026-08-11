---
domain: ai-workflows
subdomain: ai-coding-agents
concept: benchmarking-coding-agents
title: Benchmarking Coding Agents on New vs Legacy Codebases
sources:
  - title: "Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs"
    url: "https://www.youtube.com/watch?v=7vn4WpqNpck"
    author: "AI Engineer"
    date: "2026-08-08T19:00:06+00:00"
---

# Benchmarking Coding Agents on New vs Legacy Codebases

In this talk, Denys Linkov from Wisedocs describes the company's challenges scaling an AI pipeline that processes complex medical claims (PDFs over 10,000 pages). Facing slow customer delivery, complicated updates, and an unappealing legacy codebase spanning more than 10 repos, they decided to refactor over six months. Linkov frames technical debt like financial debt: it compounds in unexpected ways, and the ROI from shipping features must outweigh the added complexity. He observes that while AI tools have sped up coding, product quality and reliability have not necessarily improved, citing degraded uptime at leading companies.

Linkov details the evaluation process for AI pipeline orchestrators. Over two months, a team of three assessed five open-source projects against 17 criteria, building proof-of-concepts to validate results. He notes that with modern tooling—such as deep research and agentic workflows—this evaluation could be done 90% faster, with sub-agents handling each criterion and automating POC generation. The talk is framed around comparing coding-agent effectiveness on new versus legacy codebases, using the refactor as a real-world testbed.

Key takeaways include the importance of treating technical debt with rigorous ROI analysis, the potential for AI agents to accelerate both code changes and infrastructure evaluation, and the need to watch product quality as shipping velocity increases.

- Technical debt should be analyzed like financial debt, ensuring the ROI of new features outweighs added complexity.
- Wisedocs chose to refactor a legacy multi-repo AI pipeline to improve throughput and maintainability.
- Evaluating five orchestrators took two months with 17 criteria; agentic workflows could reduce this effort by ~90%.
- Faster code shipping via AI does not guarantee better product quality or reliability.