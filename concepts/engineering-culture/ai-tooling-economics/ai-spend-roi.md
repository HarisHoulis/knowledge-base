---
domain: engineering-culture
subdomain: ai-tooling-economics
concept: ai-spend-roi
title: What's the ROI of Software Engineers' Spending on AI?
sources:
  - title: "What's the ROI of software engineers' spending on AI?"
    url: "https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers"
    author: "Gergely Orosz"
    date: "2026-10-20"
---

# What's the ROI of Software Engineers' Spending on AI?

Gergely Orosz surveyed engineering leaders and senior engineers at 27 workplaces, plus aggregate data from CodeRabbit and Gitar, to understand how much companies spend on AI coding tools per engineer and whether that spend translates into more output. CodeRabbit saw weekly PRs rise about 113% and monthly PRs 127% among the same cohort of 20,000 developers, while Gitar reports "AI-native" teams shipping 60+ PRs/dev/week, suggesting PR frequency tiers track company culture more than tooling alone.

Spending varies wildly and is unrelated to company size: a two-person .NET shop spends $3,000/dev/month while a publicly traded company with 1,500 engineers caps devs at $150/month. Spend peaked in June/July and has roughly halved for API-plan companies, driven by model changes like Opus 5.5 and moves to open models. Spending caps are common at medium-and-above spenders but usually easy to bypass; subsidized subscriptions often hide true costs, and some subsidies are ending, threatening 5-10x bill increases. Claude and Opus 5.5 dominate spend, with Cursor, Codex and GitHub Copilot also mentioned.

High spenders include a quant shop whose AI spend hit $8M/month in September (16x January's $500K), averaging $1,600/dev/month with a $25,000 per-employee limit—traders, not devs, are the biggest users. ROI there is measured as trading-desk profit, so rising spend raises no questions. The .NET shop reports 60 PRs/dev/week and 5-10x PR frequency, feeling like a 5-7 person team.

ROI remains largely unmeasured elsewhere. Several companies report flat PR frequency or unchanged merge velocity despite heavy spend; one team lead saw PR size triple while velocity stayed flat, and another noted "accelerated slop" when quality standards are maintained. Where AI clearly helps: triaging customer issues (a day to minutes), code research across Slack/design docs/PR history, and POC prototyping (weeks to hours). One team using Scrum+Kanban reports closing 3x more user stories per month.

- AI spend per engineer ranges from under $150 to $3,000+/month and is unrelated to company size; caps are common but often easy to bypass.
- PR throughput roughly doubled year-over-year per CodeRabbit data, but many companies report flat merge velocity or PR frequency despite heavy AI spend.
- Clear wins concentrate in triage, code research, and POC prototyping rather than raw PR volume; quality-focused teams see little speedup.
- Claude/Opus 5.5 dominate spend; costs peaked in summer and roughly halved for API-plan companies as models improved and open models entered.
- Few companies can articulate AI ROI; trading firms tie it to desk P&L, while most others lack a comparable measure.