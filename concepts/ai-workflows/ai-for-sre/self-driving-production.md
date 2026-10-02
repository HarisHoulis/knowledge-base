---
domain: ai-workflows
subdomain: ai-for-sre
concept: self-driving-production
title: The 5 Levels of Self-Driving Production
sources:
  - title: "The 5 Levels of Self-Driving Production — Eric Schwartz, Traversal"
    url: "https://www.youtube.com/watch?v=y-OVWZD4j6U"
    author: "AI Engineer"
    date: "2026-10-02"
---

# The 5 Levels of Self-Driving Production

Eric Schwartz, a product manager at Traversal, describes how code-writing agents are reshaping the software development lifecycle. He divides software development into three phases — system design, development, and troubleshooting — and argues that while AI coding agents have dramatically shortened development, the time enterprises spend on troubleshooting has grown. More code is written, teams understand it less, and production environments become more complex, so engineers get bogged down in bug fixes instead of creative architecture. He cites estimates that businesses spend over $400 billion a year on this problem, that 40% of managers say it affects their teams, and that engineers spend over seven hours each week fixing bugs.

- AI coding agents shorten development but shift enterprise effort toward troubleshooting, producing more code and less shared understanding of what runs in production.
- Existing monitoring tools (Datadog, Elastic, Splunk, ServiceNow) report what is broken and what may be related, but not the root cause or the remediation.
- Root cause analysis is hard because a single failure can require tracing five to ten steps through dozens of services and petabytes of data, and no single engineer holds the full context — leading to large 'war room' debugging efforts.
- Traversal's founding premise is that root cause analysis is a problem of cause and effect rather than observation, drawing on causal machine learning expertise from academia and quantitative finance.