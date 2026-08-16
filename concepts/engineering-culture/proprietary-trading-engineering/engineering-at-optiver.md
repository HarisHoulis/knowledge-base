---
domain: engineering-culture
subdomain: proprietary-trading-engineering
concept: engineering-at-optiver
title: Software engineering at a proprietary trading company: Optiver
sources:
  - title: "Software engineering at a proprietary trading company: Optiver"
    url: "https://newsletter.pragmaticengineer.com/p/optiver"
    author: "Gergely Orosz"
    date: "Tue, 11 Aug 2026 16:17:39 GMT"
---

# Software engineering at a proprietary trading company: Optiver

This article from The Pragmatic Engineer examines software engineering at Optiver, a leading proprietary trading firm. Unlike typical tech companies, Optiver has no external customers; the business itself is the customer, which removes external deadline pressures but emphasizes personal motivation and risk awareness. The dominant technical concern is minimizing latency, described as 'enemy number one,' driving decisions from kernel-level software to custom-manufactured hardware. However, the article notes that ultra-low latency is no longer a sufficient competitive moat; today, investment in AI models and quantitative strategies is increasing (Alex Itkin, CTO Optiver US). A cautionary tale of Knight Capital's $440M bug-induced near-bankruptcy underscores the high stakes (Optiver interview).

Optiver's engineering organization has transitioned from regional 'unblock yourself' systems (1986–2020) to global platforms (2020–present), leading to a stronger platform engineering group and a rebuilt CI system designed for scale and multi-region use (Pat Cooney, Head of Global Platform Engineering). The company has ~950 engineers out of ~2,200 employees, executing over 10 million trades daily across 100 exchanges. Engineering roles span a three-layer tech stack, with heavy use of C++ and FPGAs, while hardware engineering includes custom chips and partnerships with AMD. Network infrastructure relies on dedicated fiber, microwave links, and co-location facilities.

Engineering practices at Optiver balance speed with caution, given the potential for catastrophic financial losses from bugs. A strong testing and monitoring culture is paired with a risk-aware mindset. AI is a growing focus: the article reports that Optiver invests more in improving models than in lowering latency, and that AI infrastructure providers like NVIDIA, Groq, and Cerebras actively court trading firms. Additionally, AI labs such as Anthropic and OpenAI are now recruiting from prop shops, valuing their infrastructure expertise and experience building custom high-performance hardware.

- Proprietary trading firms like Optiver have no external customers; minimizing latency is the central engineering driver.
- Optiver shifted from regional 'unblock yourself' systems to global platforms starting in 2020, expanding platform engineering.
- The company builds custom hardware (FPGAs, chips) and leases dedicated fiber and microwave links to reduce latency.
- AI and machine learning models are becoming more important than ultra-low latency as a competitive differentiator.
- Engineering culture emphasizes caution to avoid catastrophic bugs, exemplified by Knight Capital's near-collapse.