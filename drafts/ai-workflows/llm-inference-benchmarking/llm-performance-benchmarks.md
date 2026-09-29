---
domain: ai-workflows
subdomain: llm-inference-benchmarking
concept: llm-performance-benchmarks
title: Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google
sources:
  - title: "Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google"
    url: "https://www.youtube.com/watch?v=l1-D89bAuOA"
    author: "AI Engineer"
    date: "2026-09-19"
---

# Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google

Ashok Chandrasekar and Jason Kramberger, Google engineers working on inference performance, discuss why simple LLM benchmarks often fail to represent production-scale inference. They map the benchmark ecosystem into model-server frameworks (e.g., vLLM, SGLang), competitive-analysis tools (e.g., MLPerf, SemiAnalysis, Artificial Analysis), web benchmarks (e.g., Locust, Grafana, k6), and production-scale LLM benchmarks such as LLMD and inference-perf (AI Engineer, 2026).

Production-scale inference stacks involve online serving and batch workloads, inference pools with many servers, prefill-decode disaggregation, and workload autoscaling. A benchmark that just specifies model, prompt count, input/output sequence length, and request rate, then reports token throughput, TTFT, and TPOT, may not capture these conditions (AI Engineer, 2026).

Reliable production-scale benchmarks need high load, realistic workloads, accurate metrics, load sweeps, and SLOs. The talk emphasizes finding the saturation/optimal point and measuring conformance to SLOs such as TTFT P90, rather than a single QPS number (AI Engineer, 2026).

The speakers identify common pitfalls: inaccurate metrics, lack of observability into the benchmark harness, reproducibility challenges from dataset randomness, and poor dataset quality. They note difficulty reproducing results shared by others as motivation for the talk (AI Engineer, 2026).

- Benchmark ecosystem spans model server frameworks, competitive analysis tools, web benchmarks, and production-scale LLM benchmarks.
- Simple benchmarks miss production complexities: online/batch serving, inference pools, prefill-decode disaggregation, autoscaling.
- Production benchmarks need high load, realistic workloads, metric fidelity, load sweeps, and SLO conformance.
- Common pitfalls are inaccurate metrics, no harness observability, reproducibility issues, and dataset quality.
- The speakers' open-source tools include inference-perf and LLMD, focused on reliable production inference benchmarking.