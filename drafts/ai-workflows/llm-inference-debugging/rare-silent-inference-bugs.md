---
domain: ai-workflows
subdomain: llm-inference-debugging
concept: rare-silent-inference-bugs
title: Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story
sources:
  - title: "Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer"
    url: "https://www.youtube.com/watch?v=btxG75rNJC4"
    author: "AI Engineer (AI21: Asaf Gardin & Yuval Belfer)"
    date: "2026-09-19T18:30:06+00:00"
---

# Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story

Speakers from AI21 (Yuval Belfer and Asaf Gardin) describe a class of production bug they consider the hardest to deal with: silent failures in LLM serving where there is no crash, no warning, no error, yet the output is wrong and the system reports high confidence. Because these are engineering problems rather than model quality problems, they cannot be fixed by optimizing the model itself — there is high confidence but the output is bad ("Two Bugs That Hid in Plain Sight").

The first case, called the "imposter request," appeared while training AI21's Jamba model — a hybrid architecture combining transformer attention layers with Mamba (SSM) state layers — during GRPO-style RL training. The symptom was "one in a thousand" gibberish: it did not appear in the first 500 or 900 requests, and only manifested under real workload. It was rare enough to be hard to reproduce but common enough that shipping it was unacceptable, and it occurred only in vLLM, not in any other inference framework, making it engine-specific ("Two Bugs That Hid in Plain Sight").

The debugging strategy was to force a fast, deterministic reproduction loop. The team turned to a common vLLM CLI flag, `gpu-memory-utilization`, which controls how much GPU memory is allocated for weights, activations, and KV cache, and reduced it from 90% to 20%. Running many simultaneous requests under that constraint made request number ~8854 return gibberish; sampling all batches at temperature zero then allowed them to reproduce the same failing request deterministically. To isolate whether the fault was in the model or the inference stack, they used Hugging Face Transformers as a baseline, since its Mamba kernels are a plain, vanilla implementation while vLLM's kernels and engine have been heavily modified to support many features ("Two Bugs That Hid in Plain Sight").

- The hardest production bugs in LLM serving are silent: no crash, no warning, no error, and high confidence — so they look like quality issues but are actually engineering bugs.
- The "one in a thousand" gibberish bug was rare enough to be hard to reproduce but common enough to block shipping, occurred only under load, and appeared only in vLLM (not other frameworks).
- Reproduction was forced by lowering vLLM's `gpu-memory-utilization` from 90% to 20% and running many concurrent requests, which surfaced gibberish around request 8854.
- Sampling at temperature zero made the failing request deterministic, enabling a fast debug feedback loop.
- Hugging Face Transformers served as a baseline — a vanilla Mamba-kernel implementation — to determine whether the fault lay in the model or in the heavily modified vLLM engine and kernels.