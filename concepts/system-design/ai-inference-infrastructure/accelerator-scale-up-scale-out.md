---
domain: system-design
subdomain: ai-inference-infrastructure
concept: accelerator-scale-up-scale-out
title: Microsoft Commits Maia to Multi-Gigawatt Inference, and Its Efficiency Metric Draws Questions
sources:
  - title: "Microsoft Commits Maia to Multi-Gigawatt Inference, and Its Efficiency Metric Draws Questions"
    url: "https://www.infoq.com/news/2026/10/azure-maia-300/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Steef-Jan Wiggers"
    date: "2026-10-16"
---

# Microsoft Commits Maia to Multi-Gigawatt Inference, and Its Efficiency Metric Draws Questions

Microsoft plans to scale its Maia accelerator family to multi-gigawatt deployments starting in 2027, positioning Maia as the primary inference system for its own products. The Maia 300 design collapses scale-up and scale-out onto a single Ethernet fabric, and moves KV state between prefill and decode workers without that state leaving the fabric.

Practitioners have raised questions about the tokens-per-watt claim that leads the announcement, suggesting the headline efficiency metric is not fully substantiated by the disclosed details.

- Microsoft will scale Maia to multi-gigawatt deployments from 2027 as its primary inference system for internal products.
- Maia 300 unifies scale-up and scale-out on one Ethernet fabric.
- KV state is moved between prefill and decode workers without leaving the fabric.
- The tokens-per-watt efficiency claim leading the announcement has drawn practitioner scrutiny.