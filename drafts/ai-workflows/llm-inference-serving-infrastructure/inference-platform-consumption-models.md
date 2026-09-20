---
domain: ai-workflows
subdomain: llm-inference-serving-infrastructure
concept: inference-platform-consumption-models
title: Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads
sources:
  - title: "Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads — Sitanshu Gupta, CoreWeave"
    url: "https://www.youtube.com/watch?v=cQQbJqvZkpo"
    author: "Sitanshu Gupta (AI Engineer)"
    date: "2026-09-19"
---

# Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads

Sitanshu Gupta, who leads all of inference at CoreWeave (previously training and inference at AWS Annapurna Labs and SambaNova), describes the inference platform CoreWeave is building to serve everything from small models to trillion-parameter workloads [Vertical Mobility, AI Engineer]. He frames the talk around consumption models: derive what the platform should look like from how customers consume inference, so the platform does not have to be repeatedly re-architected, and explains why performance is central to those design choices.

CoreWeave offers two main consumption models. Serverless lets customers come in through an API or UI, pay per token, and avoid managing hardware or cluster orchestration — making the breadth of the served model catalog the key differentiator. Dedicated inference is for customers who want to know exactly which hardware they run on; they still use CoreWeave's orchestration layers, but model deployment and model performance are their responsibility, with the platform providing the capabilities and knobs to serve those features. On the serverless side, the classic problem is noisy neighbors: if many customers hit the same model, requests may time out depending on available capacity. CoreWeave addresses this with provisioned throughput, where customers who know their traffic profile can have capacity carved out for them behind the scenes — still billed per token and still not managing hardware, but without the noisy-neighbor problem, as long as throughput and SLAs are maintained.

Gupta then breaks down workload shapes, noting their relative mix is continuously changing and that agentic workloads are currently very prominent. Agentic and chat workloads are similar: both are real-time, both have very long input sequences and typically very short outputs, and both thus care more about throughput than latency. The biggest difference is multi-turn behavior — agentic multi-turn exchanges are super low latency, whereas in chat the user has to read the response before replying, so turnarounds are naturally slower. That difference ultimately maps to KV cache management. Real-time voice and video are also streaming workloads and are described as absolutely, totally latency sensitive. Batch is the opposite end: SLAs are very loose — seconds, minutes, sometimes even hours (customers offering 10–12 hours of workload capability to process whenever possible).

Because these four workload shapes must coexist, the platform has to play "the game of Tetris" in the time dimension to fit them together and maximize utilization of the underlying infrastructure, and batch's loose SLAs become an explicit input to design choices in the stack. Gupta closes the excerpted portion by beginning a high-level walkthrough of how the stack is shaped and the request flow for both serverless and dedicated consumption (the transcript cuts off mid-sentence).

- Two primary consumption models: serverless (API/UI, pay-per-token, no hardware or orchestration management, model-catalog breadth as the differentiator) and dedicated (customer picks hardware and owns model deployment and performance, using CoreWeave's orchestration layers and platform knobs).
- Serverless noisy-neighbor risk is mitigated by provisioned throughput: capacity is carved out behind the scenes for customers who know their traffic profile, still billed per token and still hardware-agnostic, preserving SLAs.
- Workload shapes differ mainly on latency vs throughput: agentic and chat are real-time with long inputs and short outputs; agentic's distinguishing feature is very-low-latency multi-turn interaction, which drives KV cache management choices, while chat turns are paced by the user.
- Real-time voice and video are streaming and extremely latency sensitive, whereas batch workloads have very loose SLAs (seconds to minutes, sometimes hours), with customers willing to hand over work to be processed whenever capacity allows.
- Fitting these workload shapes together in the time dimension is framed as a scheduling "Tetris" problem aimed at maximizing utilization of the underlying infrastructure, which shapes design choices in the stack.