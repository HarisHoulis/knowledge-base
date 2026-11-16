---
domain: ai-workflows
subdomain: agent-skills
concept: skill-evaluation
title: Evaluating Agent Skills: Measuring What a SKILL.md Actually Adds
sources:
  - title: "Your SKILL.md Is 70% Stuff the Model Already Knows - Nikolay Petrov, Intel"
    url: "https://www.youtube.com/watch?v=yzx4IuEh_tU"
    author: "AI Engineer"
    date: "2026-11-11"
---

# Evaluating Agent Skills: Measuring What a SKILL.md Actually Adds

Mykola Petrov (Intel) argues that many agent skills are largely redundant, since much of a SKILL.md contains knowledge the model already has. He distinguishes skills that teach genuinely new knowledge or capabilities from management/process skills that add no new information but enforce a repeatable flow of actions, noting both types are useful and that some skills have hundreds of GitHub stars. Rather than relying on intuition about whether a skill works, he proposes a deterministic evaluation approach.

The core method is an A/B comparison: run a set of tasks without the skill loaded and again with the skill added to context, then compare outcomes such as how many tasks were solved (e.g., three of five without the skill versus all five with it), token usage, and completion time. To make this more granular, he borrows the idea of elements from a fact index: decompose the skill's instructions into discrete elements and write a question/answer pair for each, yielding roughly 25–30 items per skill. Each question is asked with and without the skill, and responses are graded by a judge or panel of judges, ideally from a different model family, with care taken that questions contain no answer clues and with optional tool access (e.g., web) to test practical understanding.

This produces a simple matrix of counts with four outcomes. If the model answers correctly both with and without the skill, the skill had no effect—the knowledge was already there. If it answered correctly without the skill but degraded with it, the skill is actively harmful; Petrov says such cases are rare in popular skills (about one in nearly 400 items in Anthropic skills) but more common in less popular ones, and they are the easiest to fix. The ideal case is failure without the skill and success with it, indicating new learning. A fourth case—failure both ways—suggests the skill is described imperfectly or unclearly. He contrasts this element-level analysis with brute-force line-by-line editing and notes that element-level work enables per-line coloring and more targeted refinement as models evolve.

- Distinguish knowledge-adding skills from process/management skills that only enforce repeatable flows.
- Evaluate skills deterministically by running tasks with and without the skill loaded, comparing solved tasks, token usage, and time.
- Decompose skills into elements with question/answer pairs (roughly 25–30 per skill) and grade with judges, ideally from another model family.
- A skill that doesn't change answers is redundant; one that degrades correct answers is harmful and should be fixed first.
- The ideal signal is failure without the skill and success with it, showing the skill teaches something new.