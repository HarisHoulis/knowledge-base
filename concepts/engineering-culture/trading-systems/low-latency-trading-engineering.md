---
domain: engineering-culture
subdomain: trading-systems
concept: low-latency-trading-engineering
title: Software engineering at a proprietary trading company: Optiver
sources:
  - title: "Software engineering at a proprietary trading company: Optiver"
    url: "https://newsletter.pragmaticengineer.com/p/optiver"
    author: "Gergely Orosz"
    date: "Tue, 11 Aug 2026 16:17:39 GMT"
---

# Software engineering at a proprietary trading company: Optiver

The article provides an in-depth look at software engineering at Optiver, a proprietary trading firm that trades only its own capital and has no external customers. This unique setup means the business itself is the customer, shifting engineering incentives toward internal efficiency and extreme performance. The dominant technical driver is minimizing latency—the time between request and response—which influences decisions across the software stack, kernel-level work, and even custom hardware manufacturing. According to Orosz (2026), latency is now considered the "floor" rather than a competitive moat, and AI models are becoming the new differentiator, with slow models using fast triggers and fast models running at the network edge for real-time decisions.

The engineering organization at Optiver is structured into three main areas: engineering (building the full trading platform stack), research (quantitative scientists creating models), and trading (quantitative traders who adjust system parameters). A major shift from regional systems to global platforms began around 2023, aiming to reduce fragmentation and duplication. The company also emphasizes a "build and own" culture, with platform engineering playing an increasingly important role. The article notes that the firm has approximately 950 engineers and executes over 10 million trades daily across 100 exchanges (Orosz, 2026).

Technical depth includes a three-layer tech stack, custom FPGAs, hardware partnerships, and physical infrastructure like dedicated fiber and microwave links. Engineering practices highlight a careful balance between speed and risk, with a strong testing culture and robust monitoring to avoid catastrophic bugs—the article references the Knight Capital incident as a cautionary tale. AI adoption is significant, and the firm is a target for AI infrastructure providers like NVIDIA due to heavy GPU spending. The piece also covers hiring and career development, noting a shift from hiring mostly juniors to more experienced engineers (Orosz, 2026).

- Optiver has no external customers; the trading business is the sole customer, creating unique incentives focused on internal performance and speed.
- Latency minimization drives all major engineering decisions, from software and kernel work to custom hardware and physical network infrastructure.
- Ultra-low latency is now just the baseline; AI models and data-driven strategies are the new competitive differentiator.
- The engineering org is split into engineering, research, and trading roles, with a move from regional silos to global platform engineering.
- AI labs like Anthropic and OpenAI actively recruit from prop shops like Optiver for their infrastructure and high-performance computing expertise.