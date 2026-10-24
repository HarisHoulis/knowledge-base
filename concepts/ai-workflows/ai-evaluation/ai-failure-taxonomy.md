---
domain: ai-workflows
subdomain: ai-evaluation
concept: ai-failure-taxonomy
title: 1,368 AI Failures and What They Teach About Evals
sources:
  - title: "1,368 AI Failures and What They Teach About Evals — Vishal Srivastava, New York Life & Tanmay Sah"
    url: "https://www.youtube.com/watch?v=mMw3arwQsL0"
    author: "AI Engineer"
    date: "2026-10-22"
---

# 1,368 AI Failures and What They Teach About Evals

Vishal Srivastava and Tanmay Shah analyzed the public AI Incident Database to ask what AI failures teach us about evaluating AI systems, and whether that knowledge can be applied at the system level rather than just the model level. They observe that AI failures are increasing exponentially, with an almost vertical jump over the last four years in the era of foundation models, and argue that enterprise AI use cases far outnumber our ability to inspect each one individually—so a structured investigation method is needed.

They propose examining failures across three main dimensions. The development phase covers where the model or system is built—data quality, tool architecture, and system design—and errors there can propagate to the deployment phase, where sufficient controls can contain design flaws before they reach the final stage: the business context in which the system is used, which carries reputational, legal, and financial risk. Their core claim is that the model's technical power is only one part of the system, which must be evaluated holistically.

These dimensions break down into 13 sub-dimensions. Technical strength includes six: data quality, task-appropriate design, predictive validity, fairness checks, failure-mode mapping (where, when, how, and for whom the system can fail), and explainability for regulators. Deployment covers four: the powers given to the AI (inform vs. act on our behalf), human mediation effectiveness, influence control (internal employees who can catch errors vs. external customers where problems spread quickly), and production monitoring and containment. Business impact covers three: financial impact, legal consequences, and number of users affected.

Applying this 13-dimension framework back to the incident database, they find that almost 98% of AI failures can be captured by these dimensions—sometimes several at once—showing that AI failures have structure and should be reflected on and acted upon accordingly.

- AI failures are growing exponentially, especially since foundation models, outpacing the ability to review each use case individually.
- Failures should be analyzed across three phases: development, deployment, and business context—not just model capability.
- A 13-sub-dimension framework (technical strength, deployment controls, business impact) captures almost 98% of incidents in the AI Incident Database.
- Failures often involve multiple dimensions simultaneously, so evaluation must be system-level and holistic.