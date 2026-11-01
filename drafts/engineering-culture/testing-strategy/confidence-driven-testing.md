---
domain: engineering-culture
subdomain: testing-strategy
concept: confidence-driven-testing
title: From Unit Tests to Synthetic Canaries at Netflix
sources:
  - title: "From Unit Tests to Synthetic Canaries at Netflix • William Schor • Bug Bash EU 2026"
    url: "https://www.youtube.com/watch?v=gINXSCYTC0A"
    author: "GOTO Conferences"
    date: "2026-10-26"
---

# From Unit Tests to Synthetic Canaries at Netflix

William Schor, who works on Netflix's key-value team serving Cassandra databases and front-ends, describes the team's evolving approach to testing and how they tried to generalize it across the company, including for the online data warehouse group. He opens by questioning why we test at all: tests help you reflect on code structure, express external intent, and fix an interface like a specification — but he argues none of these is the main reason. The real reason is confidence, so you can move forward and deploy. He points to code freezes during critical periods as evidence that companies value proven, running code over forced releases.

- The primary purpose of testing is confidence to deploy, not just reflection, intent expression, or specification
- Code freezes at companies like Netflix show that proven production behavior is trusted more than untested new releases
- Tests written alongside code can inherit the same false assumptions, so they don't guarantee independent verification
- The talk frames testing in terms of 'epistemological distance' between writing code and testing it, aiming to bring production-level confidence into earlier stages