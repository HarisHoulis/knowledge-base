---
domain: engineering-culture
subdomain: large-scale-migrations
concept: ai-assisted-language-migration
title: GitHub Migrates Copilot Runtime to Rust with AI-Assisted Rewrite
sources:
  - title: "Github Migrates Copilot Runtime to Rust with AI-Assisted Rewrite"
    url: "https://www.infoq.com/news/2026/10/github-copilot-rust-migration/"
    author: "Leela Kumili"
    date: "2026-10-09"
---

# GitHub Migrates Copilot Runtime to Rust with AI-Assisted Rewrite

GitHub migrated more than 800,000 lines of Copilot runtime code from TypeScript and Node.js to Rust in roughly 14.5 weeks, relying on AI-assisted development to drive the rewrite (InfoQ). The effort was incremental rather than a big-bang rewrite, using N-API interoperability to let the new Rust code coexist with the existing Node.js runtime while releases continued to ship.

The migration was broken into 128 pull requests, with automated testing and human review serving as the guardrails for the AI-generated code. This combination of interop, incremental delivery, and review processes allowed the team to keep shipping throughout the transition.

The result is a case study in applying AI-assisted development to a large-scale language migration without halting ongoing product delivery.

- GitHub moved over 800,000 lines of Copilot runtime code from TypeScript/Node.js to Rust in about 14.5 weeks.
- The migration was incremental, using N-API interoperability so Rust and Node.js code could coexist.
- It was delivered through 128 pull requests with automated testing and human review while releases continued.