---
domain: ai-workflows
subdomain: synthetic-data-generation
concept: reverse-inference-synthetic-data
title: Don't be data poor — Anuj Iravane, Anterior
sources:
  - title: "Don’t be data poor — Anuj Iravane, Anterior"
    url: "https://www.youtube.com/watch?v=XAsb7MIAzm8"
    author: "AI Engineer"
    date: "2026-08-19"
---

# Don't be data poor — Anuj Iravane, Anterior

Because generation begins with the label, labels are correct by construction, eliminating manual ground-truth labeling. Clinicians control the generation process via reusable 'skills' rather than code, enabling rapid iteration and domain expertise integration. Roughly 90% of Anterior's datasets are now synthetic, and in blind reviews clinicians can distinguish synthetic from real data only about 60% of the time—barely above chance, validating the approach (Anterior AI Engineer, 2026).

- Anterior generates synthetic training/eval data by reversing their inference pipeline: sample a label and reasoning trace, then generate the input record.
- Policy-as-decision-tree enables sampling a diverse, uniform distribution of cases, avoiding the narrow collapse common when asking LLMs to invent variety.
- A coarse-to-fine generation pipeline builds patient journeys with consistency checks, producing realistic document bundles while avoiding data retention legal issues.
- Synthetic data makes ground truth correct by construction and gives clinicians control via 'skills', resulting in ~90% synthetic datasets that are nearly indistinguishable from real data.