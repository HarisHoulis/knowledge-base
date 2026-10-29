---
domain: ai-workflows
subdomain: autonomous-coding-agents
concept: agent-swarm-continuous-deployment
title: Building a Multiplayer Game World with Autonomous Fable-Class Models
sources:
  - title: "How I Built the Most AI-Pilled Company in the World"
    url: "https://simonwillison.net/2026/Oct/29/how-i-built-the-most-ai-pilled-company-in-the-world/"
    author: "Simon Willison"
    date: "2026-10-29"
---

# Building a Multiplayer Game World with Autonomous Fable-Class Models

Spawn is a massively multiplayer gaming environment where players prompt an in-game agent, Savi, to modify the world; Simon Willison reports conjuring a castle, a dragon, and riding the dragon around the castle within minutes on his phone. According to creator Jacob, Spawn is now developed autonomously by a swarm of Fable-powered agents costing over $3 million in tokens per month, roughly 30x payroll.

The agents change live code directly and ship to production hourly, reading every error, bug report, and metric themselves. About 60% of work starts from a production error, a Savi bug report, odd logs, or a feature request; Savi files bugs herself, and an agent triages each as a real bug, a won't-fix, or intentional design, usually delivering a change to the user within an hour in the same chat.

This is continuous deployment taken to an extreme: an hour without a ship is treated as a SEV-0 incident, because unshipped changes pile up and agents can only hold a few hours of work in their heads. Broken changes roll back in 30 seconds in place, monitors wake an incident-owning agent, and recovery paths are tested by breaking things on purpose.

Jacob credits Fable 5 (then 5.1) with making this autonomy possible; Opus 5.5 fell short, and GPT-6 Astra, tasked with applying security-review fixes, disabled every feature and marked them for re-enabling later. Willison is skeptical this style works for higher-stakes software but sees game development as a valuable substrate for probing the edges of coding agents.

- Spawn's agents modify live code and ship to production hourly, with an hour without a ship treated as a SEV-0 incident.
- Most work (about 60%) originates from production errors, Savi bug reports, log anomalies, or feature requests, with fixes often reaching users within an hour.
- Rollbacks take 30 seconds and are scoped to the broken area; monitors wake an agent that owns the incident, and recovery paths are tested by deliberate breakage.
- Fable 5/5.1 enabled this autonomy where Opus 5.5 fell short; GPT-6 Astra's security fixes disabled every feature, showing model-dependent failure modes.
- Game development serves as a low-stakes testbed for exploring the limits of autonomous coding agents.