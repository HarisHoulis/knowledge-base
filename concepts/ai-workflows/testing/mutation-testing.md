---
domain: ai-workflows
subdomain: testing
concept: mutation-testing
title: Mutation Testing Is AWESOME
sources:
  - title: "Mutation testing is AWESOME"
    url: "https://www.youtube.com/shorts/djSbndoByr8"
    author: "Matt Pocock"
    date: "2026-10-14"
---

# Mutation Testing Is AWESOME

Matt Pocock introduces mutation testing as a way to improve an AI agent's test suite. The core idea is to introduce controlled bugs into the code and observe whether the existing tests catch them, which reveals weak spots in test coverage [source].

He points to Stryker.js as the tool for doing this in TypeScript projects, and frames the practice as especially valuable when working with AI agents that generate tests, since it provides a concrete signal of whether those tests actually verify behavior [source].

- Mutation testing introduces controlled bugs to check whether tests catch them
- It exposes weak tests that pass despite broken code
- Stryker.js is the recommended tool for TypeScript
- Useful for validating test suites produced by AI agents