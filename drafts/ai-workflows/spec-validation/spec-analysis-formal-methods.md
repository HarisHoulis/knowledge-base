---
domain: ai-workflows
subdomain: spec-validation
concept: spec-analysis-formal-methods
title: Catching Specification Bugs Before Coding Agents Write Code
sources:
  - title: "Your Spec Has Bugs. Catch Them Before Your Agent Codes. - Rajath Mahendrappa Kotyal, AWS"
    url: "https://www.youtube.com/watch?v=0EnLxIbAvYk"
    author: "AI Engineer"
    date: "2026-11-11"
---

# Catching Specification Bugs Before Coding Agents Write Code

Rajath Mahendrappa Kotyal (AWS Automated Reasoning group) presents the Kiro specification analyzer, a tool that validates specifications before they are handed to a coding agent. The motivating example: one rule says out-of-stock orders are marked backordered, another says no order can be placed as delayed — each sensible alone, but contradictory when read together, creating ambiguity for the LLM. He cites research showing a 20-40% drop in LLM generation accuracy for fuzzy queries, 60-90% of valid code still turning out wrong, and twice as many regressions on deployment, arguing bugs should be caught in design documents and flowcharts before any code is written.

The analyzer uses a three-step process. First, the LLM refines the specification wording itself. If that fails, the English rules are formalized into SMT-LIB formulas passed to a SAT/satisfiability solver that returns whether the expression is valid. If the solver flags ambiguity — a double interpretation within or between sentences — the LLM is asked to re-check and the loop iterates. To distinguish inherent LLM behavior from incidental interpretation, the LLM translates the same rules seven to ten times, and the resulting interpretations are grouped by logical equivalence to see which assumptions each falls under.

The tool detects conflicts (one rule contradicting another) and gaps (no rule covering an expected case, e.g. a missing entry). When ambiguity remains, the user is presented with concrete options — e.g. for the vague instruction "delete the entry": leave as is, delete the entry, or keep but hide it from users. Kotyal stresses that the user remains the ultimate source of correctness: only they hold the implicit domain knowledge the LLM lacks, so every part of the rulebook should be checked before submission. He notes there is currently little evidence on how formalization can be used in agents and that the technology is still being developed.

Conclusion: always check the specification before handing it to the agent — the LLM translates, the solver checks, and the person makes the decision; absent an answer, LLM evaluators are used or implementation is refrained from.

- Specifications can contain contradictions and gaps that are invisible line-by-line but break LLM interpretation when read together.
- Pipeline: LLM refines wording, then formalizes rules into SMT formulas checked by a solver, iterating on detected ambiguity.
- Multiple LLM translations are grouped by logical equivalence to identify which interpretations stem from inherent model behavior.
- Conflicts and gaps are surfaced to the user as explicit choices; the human remains the authority due to implicit domain knowledge.
- Formal methods for agent specifications are still early-stage, with little evidence on their effectiveness.