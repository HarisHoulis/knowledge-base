---
domain: ai-workflows
subdomain: context-engineering
concept: progressive-disclosure
title: Stop Burning Your Context Cash
sources:
  - title: "Stop Burning Your Context Cash"
    url: "https://www.youtube.com/watch?v=7cUEIh4jMrQ"
    author: "Kent C. Dodds"
    date: "2026-08-13T15:28:10+00:00"
---

# Stop Burning Your Context Cash

Kent C. Dodds argues that overly large agent instruction files, such as AGENTS.md or CLAUDE.md, waste valuable context window space and can make agents less effective. As frontier models improve, harnesses like Claude Code have already removed large portions of their system prompts to focus on essential guidance. He points out that prior context-engineering best practices can quickly become myths as models and harnesses evolve, so developers must continuously re-evaluate their workflows and simplify them when possible (Kent C. Dodds, "Stop Burning Your Context Cash", 2026).

A central problem is when system prompts, auto-loaded skills, and user requests conflict, forcing the agent to reconcile contradictory instructions. Dodds advises against very large or auto-loaded instruction sets; instead, he recommends keeping system-level guidance general and loading specialized skills on demand. He highlights progressive disclosure as a key technique—provide high-level direction that points to deeper documentation only when needed. This reduces token overhead and avoids burning 'context dollars' on information the agent doesn't need for every task (Kent C. Dodds, "Stop Burning Your Context Cash", 2026).

- Avoid bloated agent instruction files that consume context without adding real utility.
- Best practices for context engineering can become outdated quickly as models and harnesses improve.
- Conflicting instructions between system prompts, skills, and user requests hurt agent performance.
- Use progressive disclosure to keep context lean and load details on demand.
- Regularly review and simplify workflows to match current model capabilities.