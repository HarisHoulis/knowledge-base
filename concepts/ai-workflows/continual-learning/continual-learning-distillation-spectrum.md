---
domain: ai-workflows
subdomain: continual-learning
concept: continual-learning-distillation-spectrum
title: Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute
sources:
  - title: "Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute"
    url: "https://www.youtube.com/watch?v=ZTA0GwpAUak"
    author: "AI Engineer"
    date: "2026-08-12T17:30:06+00:00"
---

# Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute

Samuel Denton of Applied Compute discusses how enterprises can adopt continual learning by understanding the distillation spectrum. The spectrum ranges from offline distillation, where a single batch of production traces is used to improve an agent, to fully online continual learning, where inference and training are unified in a single engine that updates the model after every production request [1]. Most enterprises currently operate at the offline end, collecting traces and trying to improve their agents from that one-time data; Applied Compute aims to meet enterprises across the whole spectrum [1]. Another key axis is hinting—the source of privileged information that makes a teacher model smarter than the student. Offline hinting derives from static data, known rubrics, general behavioral priors (e.g., a support agent too willing to give refunds), or production loss reports, independent of the model's current policy [1].

- Distillation exists on a spectrum from offline batch learning to fully online continual learning with unified inference and training.
- Most enterprises currently start with offline distillation—learning from a single batch of production traces.
- Applied Compute positions itself to provide value across the entire distillation spectrum, not just at one end.
- A second axis is 'hinting': where the teacher's privileged information comes from, with offline hints drawn from static data, rubrics, priors, or loss reports.