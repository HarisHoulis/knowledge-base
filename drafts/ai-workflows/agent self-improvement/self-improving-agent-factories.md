---
domain: ai-workflows
subdomain: agent self-improvement
concept: self-improving-agent-factories
title: Building Self-Improving Agent Software Factories
sources:
  - title: "Building Self-Improving Agent Software Factories — Suraj Gupta, Warp"
    url: "https://www.youtube.com/watch?v=TN3mj92oZ8I"
    author: "AI Engineer"
    date: "2026-09-27"
---

# Building Self-Improving Agent Software Factories

Warp's lead of harness development describes how the company moved from building a state-of-the-art agent development environment (starting as a modern terminal, now a cloud agent platform with roughly a million active users) toward helping teams create software factories (source). The talk frames self-improvement as agents improving over time with humans removed from the loop, and software factories as a shift from individual agents to automations that take work from triage all the way to production (source). The gap the speaker targets is that little has been said about how factories themselves improve, become better, more efficient and faster — which he expects to matter more as engineers move from building products to building and supporting factories (source).

The talk covers three concrete ways agent factories improve: skills, persistent memory, and model routing (source). Skills give agents procedural memory — for example, a triage agent taught exactly how to reproduce problems. Because skills go obsolete as people give feedback and agents learn from their own launches and trajectories, Warp deployed an outer loop agent: the inner loop agent applies the skill (e.g. triage), while the outer loop agent watches its work and improves the skill by detecting errors and incorporating user feedback (source).

In Warp's open-sourced client repository, the factory is fully functional: a GitHub workflow triggers a triage agent when a request is created, to determine missing information, duplicates, or whether the request should be developed (source). The outer loop agent analyzes the triage agent's decisions and collects feedback signals such as likes/dislikes, user comments, and comments from Warp employees, then synthesizes the iteration and updates the inner loop skill (source). Improvements are made by editing the skill and opening a pull request, so changes are tracked through Git — giving full transparency and human review so the outer agent cannot silently degrade the triage agent (source).

Persistent memory addresses what skills don't cover: when a sentinel agent finds a problem, gathers context and fixes it, a similar future problem may not be traced to the same root cause, and even when it is, many tokens are spent (source). The transcript is truncated before the model routing section is developed (source).

- Self-improvement and software factories are usually discussed separately; the talk's contribution is combining them so factories themselves improve over time.
- Three improvement levers: skills (procedural memory), persistent memory, and model routing.
- An outer loop agent watches the inner loop agent, collects error signals and user feedback, and rewrites the inner loop skill.
- Skill updates are landed as pull requests, giving Git-tracked transparency and human review before adoption.
- Persistent memory matters because recurring problems otherwise require the agent to re-derive root causes at high token cost.