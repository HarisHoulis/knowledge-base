---
domain: ai-workflows
subdomain: continual-learning
concept: distillation-spectrum
title: Bringing Continual Learning into Enterprises
sources:
  - title: "Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute"
    url: "https://www.youtube.com/watch?v=ZTA0GwpAUak"
    author: "Samuel Denton"
    date: "2026-08-12T17:30:06+00:00"
---

# Bringing Continual Learning into Enterprises

In this talk, Samuel Denton of Applied Compute outlines a spectrum for distillation in continual learning, ranging from offline distillation—where a single batch of production traces is used to improve an agent—to fully online continual learning, where inference and training are unified in a continuous flywheel (Denton, 2026). He notes that most enterprises currently sit at the offline end, working with static trace batches, while the online end represents the 'holy grail' of continual learning. Applied Compute aims to meet enterprises wherever they are on this spectrum and provide value across both ends.

Denton also introduces a second orthogonal axis: hinting. The key question is where the privileged information for a teacher model comes from. Offline hinting derives hints from static or offline data, such as known rubrics or general behavioral priors (e.g., a customer support agent that is too willing to give refunds). Online hinting, in contrast, would come from the model's own on-policy rollouts. This framing helps enterprises decide how to approach self-distillation and continual learning based on their data availability and production maturity.

- Distillation exists on a spectrum from offline one-time trace batches to fully online unified training/inference flywheels.
- Most enterprises are currently at the offline end, using static production traces to improve agents.
- Hinting is an orthogonal axis: privileged information for a teacher can come from static rubrics/priors or from on-policy rollouts.
- Applied Compute's goal is to provide value across the entire distillation spectrum, not just at one end.