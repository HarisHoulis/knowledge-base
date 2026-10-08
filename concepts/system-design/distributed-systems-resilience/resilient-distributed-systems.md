---
domain: system-design
subdomain: distributed-systems-resilience
concept: resilient-distributed-systems
title: Building Resilient Systems with Sam Newman
sources:
  - title: "Building resilient systems with Sam Newman"
    url: "https://newsletter.pragmaticengineer.com/p/building-resilient-systems-with-sam"
    author: "Gergely Orosz"
    date: "2026-10-07"
---

# Building Resilient Systems with Sam Newman

Sam Newman, author of Building Microservices, describes microservices as an architecture of "last resort" and reflects on being in the room when the term was coined: James Lewis pitched "micro apps" at a Lake District architecture symposium, and someone suggested "microservices" instead. He offers two definitions: the clear one is an independently deployable service (a change can be deployed without deploying other services), and the softer one is services split by business domain rather than technical layer.

For distributed systems, Newman condenses the eight fallacies into three rules: information takes time to travel, the thing you want to talk to may not be there, and resources are not infinite. In his experience most outages come from the third — resource pools running out. On idempotency, he contrasts idempotency keys (clean but hard to retrofit, requiring client and server changes) with server-side fingerprints (easy to retrofit but can reject legitimate requests as duplicates). He also cites David Woods' four resilience concepts — robustness, rebound, extensibility, and adaptability — and stresses that fail-open versus fail-closed decisions must account for business context.

On AI, Newman warns against "cognitive surrender": AI was pitched to free us from drudgery for more critical thinking, but current usage often causes more context switching and less thinking time. He argues the tech world misunderstands LLMs — they have no concept of causality and are not world models, so guardrails are not a long-term solution. He recommends hedging vendors (multi-vendor, multi-model) and swapping LLM functionality for deterministic code where possible, and advises designing module boundaries first, then letting AI roam freely only inside that structure.

- Microservices are defined by independent deployability, or more softly by business-domain boundaries; Newman calls them an architecture of last resort.
- Most distributed systems outages stem from resource exhaustion, one of his three rules alongside latency and unavailable resources.
- Idempotency keys are clean but hard to retrofit; server-side fingerprints are easy to retrofit but risk rejecting legitimate duplicate-looking requests.
- Woods' four resilience concepts are robustness, rebound, extensibility, and adaptability; fail-open vs fail-closed should follow business context.
- Newman warns of cognitive surrender to AI, notes LLMs lack causal world models, and advises multi-vendor hedging plus designing module boundaries before letting AI work inside them.