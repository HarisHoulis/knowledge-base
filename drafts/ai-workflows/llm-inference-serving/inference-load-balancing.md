---
domain: ai-workflows
subdomain: llm-inference-serving
concept: inference-load-balancing
title: Routing LLM Inference in Production: From Engine Signals to Policy
sources:
  - title: "Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI"
    url: "https://www.youtube.com/watch?v=sOB3HSiG8vo"
    author: "Qianru Lao & Lu Zhang (AI Engineer)"
    date: "2026-09-19"
---

# Routing LLM Inference in Production: From Engine Signals to Policy

Qianru Lao and Lu Zhang, who work on the inference team at OpenAI, describe how their system for routing LLM inference in production evolved from routing based on feedback loops driven by engine signals to a more explicit and predictable policy that is still informed by engine signals, but used differently [AI Engineer talk]. The inference load balancer (ILB/IRB) sits between front-end CPU clusters, which act as gateways that receive user requests and prepare them into inference requests, and engine clusters on the right, which are GPU clusters each hosting multiple inference engines. The ILB runs on the front-end clusters and has two main responsibilities: selecting an engine and proxying the request; the talk focuses on engine selection.

In some ways the ILB resembles a traditional load balancer: a request targets a model, and a model is backed by multiple engines that may live in different clusters, regions, or even across continents, which provides resiliency against localized degradation or cluster failures. But inference introduces nuances: the router must consider real-time signals such as time to first token (TTFT), time between output tokens (token throughput), utilization, and KV cache locality — sending follow-up turns of the same conversation back to the same engine avoids recomputation, improves efficiency, and reduces latency. The combination of performance, reliability, locality, and cache awareness is what makes this an interesting problem.

In the early days, routing began by filtering out engines that could not serve a request due to capability, compute, or data residency constraints. Among the remaining engines, the ILB used weighted consistent hashing to select the best destination engine for a request or a certain user. Weights came from a periodic feedback loop: inference engines report the signals of interest, and a controller periodically smooths those signals and computes a performance score. That score is compared against the fleet average, and each engine's weight is adjusted — up when performance is better than the fleet average, down when it is worse. The weight then affects routing, forming a control loop conceptually similar to a proportional (P) controller from control theory, borrowed for its proportional part. Its nice properties include combining the useful signals into a single routing decision and adapting to observed performance, including constraints that make some engines busier because they can serve more requests or more kinds of requests.

The remainder of the talk covers the newer control-plane/data-plane driven architecture and the responsibilities of each, a concrete case study of reducing global network overhead, and protection mechanisms that keep the system stable under production-level stress [AI Engineer talk].

- The inference load balancer sits between front-end CPU gateway clusters and GPU engine clusters, and is responsible for two things: selecting an engine and proxying the request.
- Unlike a traditional load balancer, inference routing must weigh real-time signals (TTFT, inter-token time/throughput, utilization) plus KV cache locality, since routing follow-up turns to the same engine avoids recomputation and cuts latency.
- Early routing filtered engines by capability, compute, and data residency constraints, then used weighted consistent hashing to pick a destination engine for a request or user.
- Weights were produced by a periodic feedback loop: a controller smoothed engine-reported signals into a performance score, compared it to the fleet average, and adjusted each engine's weight accordingly — a proportional (P) controller-style loop.
- The system later moved to an explicit, more predictable policy informed by engine signals, with a control-plane/data-plane architecture, a case study on reducing global network overhead, and stability protection mechanisms under production stress.