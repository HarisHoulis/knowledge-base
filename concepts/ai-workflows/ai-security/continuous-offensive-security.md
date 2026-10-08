---
domain: ai-workflows
subdomain: ai-security
concept: continuous-offensive-security
title: AI Hackers Are Faster Than Your Pen Test
sources:
  - title: "AI Hackers Are Faster Than Your Pen Test — Eli Cohen, Snyk"
    url: "https://www.youtube.com/watch?v=f3o0-9Dlw3E"
    author: "AI Engineer"
    date: "2026-10-07"
---

# AI Hackers Are Faster Than Your Pen Test

Eli Cohen, field CTO at Snyk, argues that AI coding agents have fundamentally changed the security landscape: developers now generate 218% more lines of code per day, and over 85% of developers use coding agents, yet 62% of LLM-generated results are unsafe or corrupted (AI Engineer, 2026). This means dangerous code reaches production faster than ever while the security backlog grows harder to fix.

Attackers are exploiting the same AI tools. Cohen cites an operating model that identified over 600 vulnerabilities to breach 600 firewalls across 55 countries, with the average successful AI attack taking 24–34 minutes and the fastest just 4 minutes (AI Engineer, 2026). Additionally, 43% of MCP servers have vulnerabilities, and attackers can bundle low-severity issues into critical ones.

Traditional security approaches cannot keep pace. Static code scanning (SAST) is cheap and easy to run on every code change but misses runtime issues like authorization and configuration flaws, which require dynamic application security testing (DAST) (AI Engineer, 2026). Cohen's talk introduces continuous offensive security as a way for defenders to use AI-driven offensive techniques to keep up with AI-powered attackers.

- AI coding agents generate 218% more code per day, and 62% of LLM-generated results are unsafe or corrupted, flooding production with vulnerabilities.
- AI-powered attacks succeed in an average of 24–34 minutes, with the fastest at 4 minutes, and 43% of MCP servers contain vulnerabilities.
- Static code scanning (SAST) misses runtime issues like authorization and configuration flaws, requiring dynamic application security testing (DAST).
- Continuous offensive security proposes using AI offensive techniques defensively to match the speed of AI attackers.