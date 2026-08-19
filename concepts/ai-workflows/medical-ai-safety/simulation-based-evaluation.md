---
domain: ai-workflows
subdomain: medical-ai-safety
concept: simulation-based-evaluation
title: Shipping AI to a Million Patients Without an A/B Test
sources:
  - title: "Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia"
    url: "https://www.youtube.com/watch?v=McknwOzbmyg"
    author: "AI Engineer"
    date: "2026-08-19T15:00:31+00:00"
---

# Shipping AI to a Million Patients Without an A/B Test

Jared Joselowitz builds the safety and evaluation stack behind Dora, a Ufonia voice agent that makes postoperative and preoperative calls to patients. Dora has made roughly 200,000 real clinical calls across 20 UK hospitals and is contracted to reach a million patients within two years. Because it asks about symptoms and gives advice, it is a regulated medical device, demanding rigorous pre-deployment evidence (Jared Joselowitz, Ufonia, 2026).

Traditional reactive approaches like shipping to 5% and watching a dashboard fail in this context: 5% is thousands of patients, and a red dashboard means someone was already harmed. Additionally, A/B testing is unethical and often illegal because randomizing patients into a worse variant cannot be justified. The solution borrows the simulation playbook from self-driving cars: a model plays the patient with hazards written alongside clinicians, and a second model judges every dialogue. Both models were validated rather than assumed—real patients in a patient and public involvement study found the simulated patient more realistic than a genuine consultation in three of four sets, and the automated judge matched or exceeded 10 clinicians across 240 cases at near-perfect sensitivity, the metric that matters most when missed red flags are catastrophic (Jared Joselowitz, Ufonia, 2026).

Prompts are optimized against a cost matrix instead of hand-tuned, acknowledging that brittle prompts can silently fail. The core philosophy is: "You do not ship the model, you ship the evidence." Simulation is necessary but not sufficient—new modalities introduce new hazards, but the same evaluation framework applies.

- A/B testing and reactive rollouts are not viable for clinical AI because harm occurs before a dashboard can react.
- Simulation-based evaluation uses a validated patient model and a validated judge model to assess safety pre-deployment.
- The patient model was validated via a public involvement study where real patients found simulated consultations more realistic than real ones in 3 of 4 sets.
- The judge model matched or beat 10 clinicians on 240 cases, achieving near-perfect sensitivity for critical red flags.
- Prompts are optimized against a cost matrix, and the final principle is to ship evidence, not just the model.