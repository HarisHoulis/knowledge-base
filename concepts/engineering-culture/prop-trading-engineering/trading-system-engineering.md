---
domain: engineering-culture
subdomain: prop-trading-engineering
concept: trading-system-engineering
title: Software engineering at a proprietary trading company: Optiver
sources:
  - title: "Software engineering at a proprietary trading company: Optiver"
    url: "https://newsletter.pragmaticengineer.com/p/optiver"
    author: "Gergely Orosz"
    date: "2026-08-11"
---

# Software engineering at a proprietary trading company: Optiver

Optiver is a proprietary trading firm that trades only its own capital, giving it no external customers. This unique position shapes its engineering culture: there are no external deadlines, and personal motivation to improve is highly valued. The article explains that latency is the 'enemy number one,' driving nearly every major engineering decision, from custom hardware to kernel-level work. However, ultra-low latency is no longer a competitive moat; instead, AI models are becoming the key differentiator, with slow models triggering fast models at the network edge to make real-time trading decisions (Orosz, 2026).

The engineering organization at Optiver is split into engineering, research, and trading roles, with a strong emphasis on platform engineering that has shifted from regional 'unblock yourself' systems to global platforms since 2020. The tech stack spans software, custom FPGAs, and physical network infrastructure, including dedicated fiber and co-located data centers. Engineering practices balance speed with caution, highlighted by the Knight Capital bug that caused a $440M loss and nearly bankrupted the company, underscoring the financial stakes of software errors. AI is increasingly important, and AI labs like Anthropic and OpenAI are recruiting from prop shops for their infrastructure and hardware expertise (Orosz, 2026).

- No external customers: engineers work on internal systems motivated by personal improvement rather than client deadlines.
- Latency is the top technical priority, influencing custom hardware, FPGAs, and network infrastructure decisions.
- AI models are becoming a differentiator, with the fastest systems operating at sub-nanosecond speeds and slow models triggering fast ones.
- Platform engineering shifted from regional silos to global, company-wide platforms starting around 2020.
- A single software bug, like Knight Capital's $440M loss, can be existential; hence high caution despite a fast-moving business.