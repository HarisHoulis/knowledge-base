---
domain: ai-workflows
subdomain: context-engineering
concept: minimal-agent-context
title: Stop Burning Your Context Cash
sources:
  - title: "Stop Burning Your Context Cash"
    url: "https://www.youtube.com/watch?v=7cUEIh4jMrQ"
    author: "Kent C. Dodds"
    date: "2026-08-13T15:28:10+00:00"
---

# Stop Burning Your Context Cash

Kent Dodds argues that large agent instruction files like agents.md or CLAUDE.md consume valuable context without improving agent usefulness. He notes that Claude Code has removed 80% of its system prompt for advanced models, and workflows must adapt as models improve (Dodds, 2026). He emphasizes that many previous context-engineering best practices have become myths, and developers need to continuously revisit their agent configuration as models evolve.

A central problem is conflict between the system prompt, auto-loaded skills, and user requests. Specific, auto-loaded skills can contradict the system prompt or user instructions, forcing the agent to reconcile conflicting guidance. Dodds recommends keeping skills general and loading them on demand rather than auto-loading them. He also advises against stating obvious facts the agent can infer from the repo, and instead using progressive disclosure to surface details only when relevant.

The talk compares this to React optimization advice where premature optimizations waste effort. Just as useMemo and useCallback were often overused, huge agent documentation files can be counterproductive. Dodds suggests that understanding how harnesses and models work will help developers adapt their workflows and avoid burning context dollars on instructions that are no longer needed.

- Oversized agents.md or CLAUDE.md files waste context and can make agents less effective.
- Claude Code recently removed 80% of its system prompt for advanced models, showing that workflows must adapt to model improvements.
- Auto-loaded skills with specific instructions often conflict with system or user prompts; load them on demand instead.
- Avoid stating what the agent can infer from the repository, and use progressive disclosure heavily.
- Previous context-engineering best practices can become myths as models improve; regularly reevaluate your setup.