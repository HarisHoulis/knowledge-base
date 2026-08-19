---
domain: ai-workflows
subdomain: health-ai-safety
concept: guardrails-first
title: Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health
sources:
  - title: "Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health"
    url: "https://www.youtube.com/watch?v=YXEqC05WEI0"
    author: "AI Engineer"
    date: "2026-08-19T14:30:18+00:00"
---

# Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health

Rashi Agrawal opens with two stark examples of consumer health AI failure: a healthy 60-year-old man was directed to sodium bromide by a popular assistant and ended up hospitalized for three weeks, and a Mount Sinai study found that consumer health AIs under-triaged life-threatening emergencies half the time. ECRI has named chatbot misuse the top health technology hazard of 2026, while roughly 40 million people already use AI for self-triage. Agrawal argues these are not frontier problems but the production baseline, and that most failures are architectural decisions made before a single token is generated (source: 2026 AI Engineer talk, YouTube).

- Strip PHI at the pipeline boundary on ingestion so it is never stored, making redaction unnecessary.
- Place deterministic rules—such as 911/988 routing, intent routing, and identity verification—in a code layer above the model, not in the prompt.
- Do not trust the prompt as a security boundary; frontier labs themselves show that every layer above the user can be overridden by prompt injection.
- Run safety as a continuous evaluation layer with judges scoring live traffic, and when a score drops, first ask whether the judge is right.
- Apply a structured decision framework: consider the five stakeholders, identify five risks, and plan for a five-day launch with five rules for deciding.