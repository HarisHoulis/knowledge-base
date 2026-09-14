---
domain: ai-workflows
subdomain: adversarial agents
concept: adversarial-morality-stress-test
title: Loophole: Adversarial Agents To Stress Test Your Morality
sources:
  - title: "Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley"
    url: "https://www.youtube.com/watch?v=hOWU0KPUp1k"
    author: "AI Engineer"
    date: "2026-09-14T15:00:19+00:00"
---

# Loophole: Adversarial Agents To Stress Test Your Morality

Brendan Rappazzo presents Loophole, an open-source terminal game built on an adversarial agent framework. The user specifies morals in natural language; one agent codifies them into a rich legal system; then two adversarial agents search for contradictions: one seeks loopholes (immoral but legal), the other seeks overreach (moral but illegal) (AI Engineer, 2026).

A judging agent reviews the original morals, generated legal code, and synthetic case law. It first tries to auto-patch cases that are imperfect translations rather than true contradictions. If the issue is an underspecification or contradiction in the user's morals, it escalates to the user to judge (AI Engineer, 2026).

The project originated from Rappazzo's experience opting out of DNA data uses after sending a sample to 23andMe. He wanted case-by-case consent for uses like solving cold cases, but found enumerating all cases cognitively prohibitive. He draws an analogy to legal systems as codifications of moral beliefs and to case law/common law as a way to handle nuance and difficult translation from morals to rules (AI Engineer, 2026).

Rappazzo says the project is independent from Morgan Stanley, where he is a machine-learning researcher, and that he has been building extensions on top of the open-source game (AI Engineer, 2026).

- Loophole turns a user's stated morals into a synthetic legal system and stress-tests it with adversarial agents.
- Adversarial agents target two failure modes: immoral-but-legal loopholes and moral-but-illegal overreach.
- A judge agent auto-patches translation errors but escalates genuine moral underspecification or contradictions to the user.
- Inspiration came from DNA-data consent and the difficulty of case-by-case moral enumeration; legal systems/case law serve as the analogy.
- It is an open-source side project, not affiliated with Morgan Stanley.