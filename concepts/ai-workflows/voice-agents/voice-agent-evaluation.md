---
domain: ai-workflows
subdomain: voice-agents
concept: voice-agent-evaluation
title: Voice AI Where One Wrong Question Breaks the Rules
sources:
  - title: "Voice AI Where One Wrong Question Breaks the Rules - Shiv Indap, Upstart & Brooke Hopkins, Coval"
    url: "https://www.youtube.com/watch?v=3osCbSufv8g"
    author: "AI Engineer"
    date: "2026-10-31"
---

# Voice AI Where One Wrong Question Breaks the Rules

Brooke Hopkins (founder of Coval, previously led evaluation infrastructure at Waymo) and Shiv Indap (voice AI lead at Upstart) discuss evaluating voice agents in regulated, high-stakes settings. Brooke draws a parallel between autonomous vehicles and autonomous voice agents: both must reliably get from point A to point B across many possible paths, using an architecture of many models working together to respond to the world. Coval builds assessments for voice agents, working with enterprises from fast-growing AI companies like Perplexity to Fortune 500 firms in customer support and logistics.

Shiv describes Upstart's lending use case: the fintech makes thousands of calls daily, and about 10% of applicants who don't get an instant decision must call to confirm information. The agent asks three questions (income stability for three months, intended use of funds, and outstanding obligations like child support or wage garnishments), but first must verify the caller is the right person. Because lending is highly regulated, a mistake is not just a CX issue but a potential regulatory issue: the agent cannot ask the amount when funds are for medical purposes, must probe ambiguous answers (e.g., "prom" requires clarifying whose graduation), and must politely avoid promising timelines like three business days.

Initially every call was human-audited, starting with a Google spreadsheet that degraded as columns grew from five to ten and about 15 people added data randomly. This drove the need for a structured human verification process, which Coval helped build. Metrics are framed as an LLM-as-judge running after the call—for example, a yes/no compliance check with an explanation—with humans reviewing the judge's outputs to validate it. Early metrics like call duration, accuracy, and clarity were narrowed over time to the most important ones.

- Regulated domains like lending turn voice-agent errors into potential regulatory violations, not just poor customer experience.
- Compliance rules are context-dependent: the agent must not ask certain follow-ups (e.g., medical fund amounts) and must clarify ambiguous answers.
- Ad-hoc human auditing via spreadsheets breaks down quickly, motivating structured verification tooling.
- LLM-as-judge metrics (e.g., yes/no compliance with explanation) need human review to validate the judge itself.
- Metric sets should be pruned over time to the most important measures rather than accumulating everything.