---
domain: ai-workflows
subdomain: ai-code-quality
concept: verification-debt
title: Guide, Verify, Solve — Anirban Chatterjee, Sonar
sources:
  - title: "Guide, Verify, Solve — Anirban Chatterjee, Sonar"
    url: "https://www.youtube.com/watch?v=03l29gJXpCE"
    author: "Anirban Chatterjee"
    date: "2026-08-09T17:45:13+00:00"
---

# Guide, Verify, Solve — Anirban Chatterjee, Sonar

Anirban Chatterjee, product marketing at Sonar, argues that AI development is transitioning from experimentation to engineering, but scaling AI-generated code requires adding safety and trust. He cites a Carnegie Mellon study using SonarQube metadata that found AI-assisted projects experienced a temporary productivity spike lasting about three months, followed by a decline, alongside a persistent rise in static analysis warnings and code complexity. This indicates that AI tools introduce hidden quality issues that accumulate over time, creating what Chatterjee calls 'verification debt.'

Chatterjee explains that the acceptable quality gap between AI output and production requirements depends on application criticality. For low-criticality experiments or internal tools, AI-generated code may suffice with minimal review. However, for high-criticality systems serving many users or facing adversarial threats, the quality bar is much higher. Since AI models are inherently error-prone and lack broader business and codebase context, human engineers must step in to close this gap through verification. This verification debt—the extra human effort needed to ensure AI-generated code meets production standards—must be addressed before shipping to avoid catastrophic effects and enable repeatable, scalable AI-assisted development.

- A Carnegie Mellon study found AI coding tools give a temporary productivity boost (~3 months) but lead to persistent increases in code complexity and static analysis warnings.
- The quality gap between AI-generated code and production requirements grows with application criticality, making verification essential for high-stakes systems.
- AI models remain error-prone and lack context about the broader codebase and business, reinforcing the need for human oversight.
- Verification debt—the human effort required to validate and fix AI-generated code—is a key challenge to scaling AI in software engineering.