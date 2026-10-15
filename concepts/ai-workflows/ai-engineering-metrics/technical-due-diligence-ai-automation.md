---
domain: ai-workflows
subdomain: ai-engineering-metrics
concept: technical-due-diligence-ai-automation
title: What Technical Due Diligence Finds When the Deck Says '70% Automated'
sources:
  - title: "What Technical Due Diligence Finds When the Deck Says '70% Automated'"
    url: "https://www.youtube.com/watch?v=gDRCpTMCqEU"
    author: "Soukaïna Abelhad"
    date: "2026-10-13"
---

# What Technical Due Diligence Finds When the Deck Says '70% Automated'

Soukaïna Abelhad, a technical lead on AI, presents three methods for verifying automation claims during technical due diligence. She notes that a dangerous number is not always fabricated — it is often a true measurement that leads to a conclusion it cannot confirm. The first check is pure arithmetic: teams with high AI implementation merged 98% more code merge requests, review time increased 91%, and the average query became 154% larger (Faros data, over 10,000 developers across 1,255 teams). This observational telemetry warns that more work has entered the system and verification workload has increased accordingly. Auditors should ask for the company's own 18-month theory, place workload volume next to total human labor costs, and count everyone whose work exists thanks to AI — operators, reviewers, trainers, escalation and bug fix specialists. If human labor is appropriate to the workload, the presentation describes assistance, not labor elimination.

Even if the arithmetic holds, the definition may still be wrong. Uber says 70% of their code merge requests are AI-related, but this doesn't give a full level of autonomy, and the period and total number were not disclosed. Every automation statement fits into a ladder: AI prepared the draft, it was edited by humans, it was approved by humans, or there was no human intervention at all. Finance calls the latter end-to-end processing — a complete process from start to finish without human intervention within set boundaries. The boundary question matters: does it end when code is compiled, when the merge request is approved, or when changes go into production? AI authorship and autonomy are two different statements.

Assuming the definition is accurate, can we trust the measurements? Meta found a 24 percentage point gap between the automated evaluator and the merger decision after adjusting for human levels. Four maintainers from three repositories reviewed 296 AI-generated merge requests for various unique issues without knowing if the patch was created by AI or a human. The automated evaluator was significantly more optimistic than the humans responsible for accepting the job. Abelhad saw the same from the other side: in one project, 10 out of 10 results passed automated verification, but once experts were brought in, few or none survived. Maturity of assessment is the first signal of credibility — ask who marked up the reference data, whether the expert agrees with it, and whether someone is measuring this agreement.

Finally, even if the claim passes these tests, it must withstand economic ones. Builder.ai's insolvency was due to revenue funding issues beyond AI claims, but the warning existed: the Wall Street Journal questioned AI capability claims in 2019, the Financial Times reported in May 2025 that the 2024 revenue forecast was revised down from $220 million to around $55 million, and the company filed for Chapter 7 bankruptcy on June 2. The process did not turn the warning into a filter. Start with the cost of acceptable workflows, apply actual implementation, direct process success, and acceptable quality, then subtract the costs of AI, human verification, escalation, and rework. The metric needed is the cost of an accepted autonomous task; if a task is not completed, escalates, or needs rework, it is considered a cost.

- A dangerous automation number is often a true measurement leading to a conclusion it cannot confirm — verify arithmetic, definition, and measurement before trusting it.
- Ask for the company's own 18-month theory and compare workload volume against total human labor costs, counting all AI-enabled roles (operators, reviewers, trainers, escalation and bug fix specialists).
- Distinguish AI authorship from autonomy: automation claims fit a ladder from AI-drafted to fully end-to-end, and the boundary of 'no human intervention' must be explicitly defined.
- Automated evaluators can be significantly more optimistic than human reviewers (Meta found a 24 percentage point gap); ask who labeled reference data and whether expert agreement is measured.
- Even claims passing technical checks must withstand economics: compute the cost of an accepted autonomous task, subtracting AI, human verification, escalation, and rework costs.