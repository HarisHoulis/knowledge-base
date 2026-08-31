---
domain: ai-workflows
subdomain: agent-context-management
concept: progressive-disclosure
title: Stop Burning Your Context Cash
sources:
  - title: "Stop Burning Your Context Cash"
    url: "https://www.youtube.com/watch?v=7cUEIh4jMrQ"
    author: "Kent C. Dodds"
    date: "2026-08-13T15:28:10+00:00"
---

# Stop Burning Your Context Cash

Kent C. Dodds argues that large agent instruction files like CLAUDE.md often waste context window space without improving agent performance. He points to Claude Code removing 80% of its system prompt for advanced models as evidence that many previous context engineering best practices have become myths (Dodds, 2026). He emphasizes that workflows must constantly evolve as models improve, and what was useful for older models may no longer be helpful for frontier models.

A key problem he identifies is conflicting instructions: system prompts, auto-loaded skills, and user requests can contradict each other, forcing the agent to reconcile opposing directives. To avoid this, he advises keeping instructions general and broadly applicable rather than overly specific, especially when they are loaded every time. Since users generally control their own agent files (e.g., CLAUDE.md) but not the system prompt, they need to be mindful of these clashes.

He highlights modern best practices from Claude Code, including avoiding stating the obvious and using progressive disclosure heavily. Dodds has used progressive disclosure for over nine months with good results, and he compares the over-optimization of agent instructions to unnecessary React optimizations like useMemo and useCallback. The main takeaway is to continuously re-evaluate and simplify agent instructions as models and harnesses change (Dodds, 2026).

- Large agent instruction files can consume context budget without adding real utility; keep them lean.
- Context engineering best practices change rapidly as models improve; old advice can become myths.
- Avoid conflicting instructions across system prompt, skills, and user requests by making auto-loaded guidance general.
- Use progressive disclosure instead of stating obvious information the agent can infer from the codebase.
- Regularly update your agent configuration (e.g., CLAUDE.md) to match current model capabilities.