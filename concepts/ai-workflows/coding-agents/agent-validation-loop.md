---
domain: ai-workflows
subdomain: coding-agents
concept: agent-validation-loop
title: Your AI Agent Starts Every Session Like a New Hire
sources:
  - title: "Your AI Agent Starts Every Session Like a New Hire - Killian Carlsen-Phelan, Sonar"
    url: "https://www.youtube.com/watch?v=8vDzncmzxyg"
    author: "AI Engineer"
    date: "2026-10-30"
---

# Your AI Agent Starts Every Session Like a New Hire

Killian Carlsen-Phelan of Sonar argues that each new coding-agent session in an IDE is like hiring a new employee: the agent doesn't know your design conventions, coding guidelines, or architectural rules, so it must hunt for context by searching the repository—a process that is slow, token-expensive, and unreliable. Worse, any existing problems in the codebase are likely to be reproduced and repeated by the agent, so undetected issues make maintaining code quality nearly impossible.

Sonar's proposed solution is Sonar Vortex, a plugin that connects to whatever coding agent you use. Before the agent writes anything, Vortex supplies project instructions and a map of code relationships—architectural guidelines, approved libraries, and project-specific coding standards—so the agent goes directly to relevant files instead of wasting tokens and overloading context. While the agent works, SonarQube checks its code: quick checks on each edit and a deeper check for serious security issues and cross-file data flows before completion, feeding issues back to the agent to fix and re-check.

Carlsen-Phelan illustrates the need with an example where an agent, despite being told to write its own test suite, introduced a security issue—unclear permissions on a temporary file used to unpack a log—that tests rarely catch and only a senior developer might notice. Such findings otherwise surface at the PR stage, forcing rework, resubmission, and re-checking that wastes time and money. He cites a Sonar survey of over 1,100 developers finding 96% do not fully trust AI-generated code, yet only 48% fully test it before shipping. Vortex is presented as compatible with agents like Claude Code, Codex, and Anti-Gravity.

- Each agent session starts without knowledge of project conventions, forcing costly repository searches that burn tokens and time
- Existing codebase problems are likely to be reproduced by agents, so undetected issues compound
- Sonar Vortex preloads architectural guidelines, approved libraries, and coding standards plus a code-relationship map before coding begins
- SonarQube runs quick checks on edits and deeper security/data-flow checks before completion, looping issues back to the agent
- Sonar's survey of 1,100+ developers: 96% don't fully trust AI code, but only 48% fully test it