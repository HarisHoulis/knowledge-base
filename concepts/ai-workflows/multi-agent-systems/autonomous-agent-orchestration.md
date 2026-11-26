---
domain: ai-workflows
subdomain: multi-agent-systems
concept: autonomous-agent-orchestration
title: 1,000 Claude Agents Formalizing Fermat's Last Theorem
sources:
  - title: "1,000 Claude Agents Formalized Fermat's Last Theorem — Lance Martin, Anthropic"
    url: "https://www.youtube.com/watch?v=wrfbI5eyLAI"
    author: "AI Engineer"
    date: "2026-11-25"
---

# 1,000 Claude Agents Formalizing Fermat's Last Theorem

Lance Martin of Anthropic describes an experiment scaling from roughly a dozen agents to 1,000 Claude agents to formalize Fermat's Last Theorem in Lean. The earlier September result relied on a specialized orchestration platform, human confirmation, and significant researcher support; the new test asked whether a large agent team could autonomously develop the formalization without a specialized environment or human intervention in the solution process.

- Scaling from ~12 to 1,000 agents was framed as a test of autonomous formalization without specialized tooling or human intervention
- Each agent ran in its own sandbox with limited network access, able to reach only Git and a SQL database
- The lead agent autonomously created database tables for announcements, role assignment, subtasks, notes, and completion tracking within minutes
- Real-time monitoring watched every tool call for boundary violations, with offline checks of all agents every 10 minutes