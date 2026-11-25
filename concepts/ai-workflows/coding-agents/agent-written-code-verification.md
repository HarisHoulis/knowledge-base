---
domain: ai-workflows
subdomain: coding-agents
concept: agent-written-code-verification
title: Shipping Millions of Lines of Agent-Written Code
sources:
  - title: "How to Ship Millions of Lines of Agent-Written Code — Jarred Sumner, Anthropic"
    url: "https://www.youtube.com/watch?v=TvsF67C2F54"
    author: "AI Engineer"
    date: "2026-11-24"
---

# Shipping Millions of Lines of Agent-Written Code

Jarred Sumner, author of Bun and engineer at Anthropic, describes merging a multi-million-line PR that adds an ahead-of-time (AOT) precompiler to Bun, which is the JavaScript runtime underlying Claude Code. The motivation was to make Claude Code consume less memory and run faster: for a typical JavaScript app, roughly half of processor time goes to compiling code on demand via JIT, so compiling everything in advance avoids that runtime cost. The project went through five complete rewrites over a little over a month, with earlier versions abandoned because compilation or assembly took too long.

Sumner frames large agent-written projects as limited primarily by how you test the code, more than by any specific development approach: the key question is how to verify the code works and can be trusted. The project succeeded because it could lean on extensive pre-existing test suites — Bun's own tests, WebKit tests, test262, and Cloudflare Workers tests — rather than writing most tests from scratch. A further advantage is the ability to run three versions of a program (JIT, precompiled, and untyped) and check that all three behave the same, plus using Claude to generate code generators for fuzzing different patterns.

He contrasts this with the earlier decision not to rewrite Claude Code in Rust: Bun was easy to port because its tests were written in TypeScript and could run against both the Zig and Rust versions, whereas migrating Claude Code's test suite would mean rewriting the tests and losing trust in them. Instead, making JavaScript faster delivered roughly 4x less memory usage and about 2x faster startup. He also notes TypeScript types are treated as predictions rather than trusted absolutely, and that models are very good at writing compilers.

- Large agent-written projects are limited mainly by testability and verification, not by a particular development workflow
- Reusing existing test suites (Bun, WebKit, test262, Cloudflare Workers) enabled confident release of millions of agent-written lines
- Running JIT, precompiled, and untyped versions and comparing behavior provides a strong correctness signal
- Bun's TypeScript tests made a Rust rewrite feasible; Claude Code's tests would have needed migration, making a rewrite too risky
- The AOT precompiler reduced JavaScript memory usage ~4x and roughly doubled startup speed