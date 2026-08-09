---
domain: engineering-culture
subdomain: ai-and-software-practice
concept: fragments-may-27
title: Fragments: May 27
sources:
  - title: "Fragments: May 27"
    url: "https://martinfowler.com/fragments/2026-05-27.html"
    author: "Martin Fowler"
    date: "2026-05-27"
---

# Fragments: May 27

Martin Fowler's 'Fragments: May 27' covers the evolving practice of LLM-augmented programming. He highlights Ian Johnson's three-month series on restructuring a legacy codebase, where the key move was first building characterization tests, adding static analysis, and introducing the right architectural patterns before letting an AI agent work more autonomously. Johnson's experience shifted from being 'in-the-loop' (approving every AI action) to 'on-the-loop' (curating patterns and reviewing output), a change enabled by the safety harness he had built. Fowler draws on this to emphasize that a solid engineering foundation is a prerequisite for safely leveraging AI agents in production.

- AI-agent autonomy in coding works best after establishing characterization tests, static analysis, and sound architecture; this shifts the developer's role from writer to curator.
- Human-AI collaboration should move from 'in-the-loop' micro-management to 'on-the-loop' strategic review, enabled by automated safety nets.
- Agentic coding increases decision density and cognitive load; keep agent tasks small, automate everything possible, and avoid parallelizing human attention.
- Closing open-source repositories is not an effective defense against LLM-augmented attackers; secure-by-design and remediation investment are more important.
- AI is already affecting graduate job markets: employment rates for the most AI-exposed fields fell 6.6%, versus 1.5% for the least exposed, according to Economist survey analysis cited by Fowler.