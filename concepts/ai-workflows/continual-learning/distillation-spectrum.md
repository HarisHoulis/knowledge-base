---
domain: ai-workflows
subdomain: continual-learning
concept: distillation-spectrum
title: Bringing Continual Learning into Enterprises
sources:
  - title: "Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute"
    url: "https://www.youtube.com/watch?v=ZTA0GwpAUak"
    author: "AI Engineer"
    date: "2026-08-12T17:30:06+00:00"
---

# Bringing Continual Learning into Enterprises

Samuel Denton of Applied Compute discusses how enterprises can adopt continual learning through a spectrum of distillation approaches, ranging from offline batch learning from production traces to fully online unified inference-training engines. Most enterprises currently operate on the offline end, needing to improve agents from a static collection of traces, while the holy grail is a real-time flywheel where models learn continuously during serving. Applied Compute aims to meet enterprises wherever they are on this spectrum.

A second axis is hinting, which defines where the privileged information for a teacher model comes from. In offline hinting, hints derive from static data such as known rubrics, general behavioral priors (e.g., a support agent giving too many refunds), or production loss reports. The interplay of the online-offline spectrum and the hinting axis provides a framework for designing distillation strategies in real-world settings.

- The distillation spectrum spans offline (single batch of traces), periodic (daily batches), and fully online (unified inference+training) learning.
- Most enterprises today are on the offline end, looking to improve agents from a one-time set of production traces.
- A second axis is hinting: where teacher knowledge comes from (static rubrics, priors, or reports), independent of the online/offline timing.
- Applied Compute's goal is to deliver value across both ends of the spectrum, meeting enterprises where they are.