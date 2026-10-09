---
domain: ai-workflows
subdomain: agent-memory
concept: adaptive-agent-memory
title: Giving AI Agents Memory That Learns
sources:
  - title: "Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain"
    url: "https://www.youtube.com/watch?v=KGFyOtl5ktI"
    author: "AI Engineer"
    date: "2026-10-08"
---

# Giving AI Agents Memory That Learns

Jake Broekhuizen, who leads the lab team at LangChain, argues that the central challenge for agent developers is giving agents memory that lets them improve with each run. He illustrates this with a financial-sector agent that drifted from an advisory tone into directive language ("you should actually cancel a few subscriptions"), violating regulatory tone guidelines. Fixing such failures manually—analyzing logs, editing context, checking for regressions—doesn't scale, so the system around the agent should become an environment where it continuously learns from its interactions.

Broekhuizen distinguishes observability from memory. Agents generate traces that record tools used, reasoning, and artifacts, and observability is a critical foundation for reliable agents. But the real challenge comes after the trace is saved: if the future context the agent references never changes, a faulty skill or instruction will cause today's error to persist in future runs. The goal is to transform a trace from a simple log into a signal source—agents that can be observed tell you what happened, while adaptive agents change and direct themselves during subsequent runs.

He defines memory as persistent context the agent references to manage future launches; a trace, transcript, or log only becomes memory when a lesson becomes persistent context for future runs. He borrows a taxonomy from cognitive science with three categories: semantic memory (what the agent knows—facts and preferences), episodic memory (what the agent experienced firsthand—learned patterns, past interactions, examples), and procedural memory (how the agent should behave—instructions, skills, rules). Procedural memory is where most noticeable results come from: in the financial example, the tone fix came from giving the agent a rule to follow when interacting with users, not from new facts or banned words.

- Memory is persistent context an agent references in future runs; a trace only becomes memory when its lesson is made persistent.
- Observability tells you what happened, but adaptive agents must change their own behavior in subsequent runs to avoid repeating errors.
- Memory can be categorized as semantic (facts/preferences), episodic (past interactions/patterns), and procedural (instructions/skills/rules).
- Procedural memory drives the most noticeable behavioral fixes, such as enforcing tone rules in a regulated financial agent.
- Manual log analysis and context editing to fix agent behavior does not scale, motivating self-improving agent environments.