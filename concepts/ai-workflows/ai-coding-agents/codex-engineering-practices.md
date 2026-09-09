---
domain: ai-workflows
subdomain: ai-coding-agents
concept: codex-engineering-practices
title: Building Codex: OpenAI's Coding Agent and Its Engineering Lessons
sources:
  - title: "Building Codex with Tibo Sottiaux"
    url: "https://newsletter.pragmaticengineer.com/p/building-codex-with-tibo-sottiaux"
    author: "Gergely Orosz"
    date: "Wed, 09 Sep 2026 15:57:24 GMT"
---

# Building Codex: OpenAI's Coding Agent and Its Engineering Lessons

The interview covers how AI agents are changing software engineering practices: code reviews may shift toward pre-code intent discussions, maintenance tasks like dependency upgrades can be done in hours, and re-architecting code can take days instead of years. Sottiaux notes that code quality, abstractions, and test suites still heavily influence how easy these changes are. He also shares a personal shift away from long "in the zone" coding sessions toward using agents to gather data and make faster, better-informed decisions (Gergely Orosz, "Building Codex with Tibo Sottiaux").

- Codex was deliberately built in Rust for performance, security, and scalability, even though AI models were then weaker at writing Rust; this avoided a costly rewrite later.
- Codex is open source, which builds trust and community but also means other tools sometimes copy its features before Codex ships them.
- Codex supports models from multiple providers, partly because open source makes it easy to fork and connect to other models; Sottiaux believes competition makes the product better.
- At OpenAI, Codex is deeply integrated into internal tools and documents, making it a go-to resource for onboarding and everyday questions.
- AI agents are making maintenance and re-architecture dramatically cheaper in time, but quality code and tests remain critical for ease of change.