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

Kent C. Dodds discusses how AI agents' context windows are being wasted by overly large and overly specific agents.md or CLAUDE.md files. He notes that as frontier models improve, harnesses like Claude Code have begun removing large portions of system prompts, making many previously useful instructions redundant or even harmful. The key is to avoid stating the obvious — the agent can infer a lot from the repository itself — and instead rely on progressive disclosure, where detailed instructions are loaded only when needed. Dodds also warns about conflicting instructions between system prompts, skills, and user prompts, which force the model to reconcile contradictory guidance and burn context tokens. He emphasizes that context engineering best practices are not durable; they evolve as models and harnesses change, so developers must continuously revisit their agent configuration.

- Avoid filling agents.md with obvious instructions; the model can already infer from the repo.
- Use progressive disclosure to load detailed instructions on demand instead of auto-loading them.
- Beware of conflicting instructions between system prompts, skills, and user prompts.
- Context engineering best practices change as models improve; revisit your workflow regularly.
- Large auto-loaded skills and docs waste context and can make agents less useful.