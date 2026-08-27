---
domain: engineering-culture
subdomain: trading-systems
concept: proprietary-trading-engineering
title: Software engineering at a proprietary trading company: Optiver
sources:
  - title: "Software engineering at a proprietary trading company: Optiver"
    url: "https://newsletter.pragmaticengineer.com/p/optiver"
    author: "Gergely Orosz"
    date: "Tue, 11 Aug 2026 16:17:39 GMT"
---

# Software engineering at a proprietary trading company: Optiver

Proprietary trading firms like Optiver operate in a unique engineering environment where the business itself is the only customer, and the primary technical driver is minimizing latency. Unlike Big Tech or startups, there are no external deadlines or customer feature requests; instead, engineers focus on achieving a competitive edge through superior software and hardware. The article highlights that while ultra-low latency was once the main moat, the industry has shifted toward data-driven quantitative trading, with AI models becoming a key differentiator. Optiver's evolution from regional systems to global platforms reflects a broader need to reduce fragmentation and duplication across engineering teams, as seen in the creation of a unified platform engineering group and a rebuilt CI system (Pragmatic Engineer).

The engineering organization at Optiver emphasizes a 'build and own' culture, with roles spanning engineering, research, and trading. The tech stack is layered, with a significant investment in custom hardware, FPGAs, and partnerships with vendors like AMD and NVIDIA. The article underscores the caution exercised in an industry where a single bug can be catastrophic, referencing the Knight Capital incident that nearly bankrupted the firm. AI is increasingly central, both as a tool in trading models and for internal software development, including agentic coding. Finally, hiring practices have shifted from mostly junior talent to experienced engineers, with a focus on onboarding and feedback loops (Pragmatic Engineer).

- Optiver has no external customers; the business itself is the customer, leading to a focus on internal performance and competitive edge over standard product development.
- Latency is 'enemy number one,' driving custom hardware design, FPGA use, and even custom chips, though AI models are now becoming a bigger differentiator than raw speed.
- The company is transitioning from fragmented regional systems to global platforms, investing heavily in platform engineering and standardized CI/CD to reduce duplication.
- A single bug can be catastrophic, as exemplified by the Knight Capital $440M loss, so engineering practices emphasize caution, monitoring, and risk management despite the need for speed.
- AI is playing an expanding role, both in trading strategies and in software development practices, with the company adopting AI tooling and exploring agentic coding.