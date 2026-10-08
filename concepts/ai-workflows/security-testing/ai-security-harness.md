---
domain: ai-workflows
subdomain: security-testing
concept: ai-security-harness
title: Cloudflare Uses an AI Harness to Probe and Harden Its WAF
sources:
  - title: "Cloudflare Uses an AI Harness to Probe and Harden Its WAF"
    url: "https://www.infoq.com/news/2026/10/cloudflare-sec-harness/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Matt Foster"
    date: "2026-10-07"
---

# Cloudflare Uses an AI Harness to Probe and Harden Its WAF

Cloudflare placed frontier AI models inside a controlled testing harness to probe its Web Application Firewall (WAF). Rather than relying solely on human-crafted test cases, the company used blocked attacks as starting points for the models to generate and refine new variations, turning existing detections into seeds for further adversarial exploration.

The harness constrains the models' behavior, keeping the AI-driven probing within a controlled environment while it iterates on attack payloads. This approach aims to harden the WAF by continuously surfacing evasive variants that might otherwise slip past existing rules.

- Cloudflare embedded frontier AI models in a controlled harness to test its WAF.
- Blocked attacks served as seeds for models to generate and refine new attack variations.
- The goal is to harden the WAF by discovering evasive variants of known attacks.