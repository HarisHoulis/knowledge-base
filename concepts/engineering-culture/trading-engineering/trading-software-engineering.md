---
domain: engineering-culture
subdomain: trading-engineering
concept: trading-software-engineering
title: Software engineering at a proprietary trading company: Optiver
sources:
  - title: "Software engineering at a proprietary trading company: Optiver"
    url: "https://newsletter.pragmaticengineer.com/p/optiver"
    author: "Gergely Orosz"
    date: "Tue, 11 Aug 2026 16:17:39 GMT"
---

# Software engineering at a proprietary trading company: Optiver

Optiver is a proprietary trading firm and market maker that trades only its own capital. For software engineers, the company offers a rare environment: there are no external customers, and engineering decisions are driven by minimizing latency, which is described as 'enemy number one.' The firm operates at sub-nanosecond speeds, custom-manufactures its own hardware and FPGAs, and runs a high-frequency trading loop that watches markets, decides trades, and sends orders faster than competitors. This combination makes latency and high-performance computing central to every layer of the stack [1].

- Optiver is a proprietary trading firm with no external customers; the business itself is the customer, leading to unique incentives and a focus on internal motivation and engineering excellence.
- Latency is the primary engineering driver, influencing everything from software design to custom hardware and network infrastructure, with trading systems operating in sub-nanosecond timeframes.
- The company is transitioning from a pure low-latency focus to a quantitative trading approach where machine learning models and AI are key differentiators, while speed is now the floor.
- Engineering culture emphasizes 'build and own,' a strong testing and monitoring culture, and a cautious attitude to risk to avoid catastrophic bugs that can wipe out the company.
- Optiver's platform engineering is globalizing: moving from fragmented regional systems to unified, scalable platform infrastructure and CI/CD pipelines.