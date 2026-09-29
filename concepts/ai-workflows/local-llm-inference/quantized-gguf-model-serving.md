---
domain: ai-workflows
subdomain: local-llm-inference
concept: quantized-gguf-model-serving
title: Running Bonsai 2 27B (Ternary Quantized) Locally with Prism's llama.cpp Fork
sources:
  - title: "Bonsai 2 27B: Near-Lossless Compression in a 9x Smaller Footprint (HN comment)"
    url: "https://news.ycombinator.com/item?id=49746618#49747390"
    author: "Simon Willison"
    date: "2026-09-17"
  - title: "prism-ml/Ternary-Bonsai-2-27B-gguf"
    url: "https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf"
    author: "Prism ML"
  - title: "PrismML-Eng/llama.cpp release prism-b10685-7dffb15"
    url: "https://github.com/PrismML-Eng/llama.cpp/releases/tag/prism-b10685-7dffb15"
    author: "PrismML-Eng"
---

# Running Bonsai 2 27B (Ternary Quantized) Locally with Prism's llama.cpp Fork

Simon Willison documents a working setup for running the ~5.95 GB GGUF release of Bonsai 2 27B, a ternarized 27B model described as "Near-Lossless Compression in a 9x Smaller Footprint." The key caveat is that the GGUFs from the Prism ML Hugging Face repository require Prism's own fork of llama.cpp; standard builds will not work, so the runtime must be pulled from the PrismML-Eng/llama.cpp release tagged prism-b10685-7dffb15 (https://news.ycombinator.com/item?id=49746618#49747390).

The recipe is straightforward: download the macOS arm64 runtime tarball, fetch the Ternary-Bonsai-2-27B-PTQ1_0.gguf file, and launch llama-server against it with `-ngl 99 -fa on -c 32768` on a chosen port such as 8331. The bundled llama-server web UI is described as "very good," and the model can also be reached through an OpenAI-compatible endpoint, e.g. via `uvx llm openai endpoint http://127.0.0.1:8331/v1 --model bonsai-2-27b --responses hi`.

Throughput on an M5 Pro was reported at roughly 20 tokens/second, with 44 tokens/second after a server restart — an unexplained variance. Willison suspects something isn't fully working: startup logged `ggml_metal_device_init: - the tensor API is not supported in this environment - disabling`, suggesting the Metal tensor API path was unavailable and inference was not running optimally.

- Bonsai 2 27B's GGUFs only work with Prism's llama.cpp fork (release prism-b10685-7dffb15), not upstream llama.cpp.
- The model file is ~5.95 GB (Ternary-Bonsai-2-27B-PTQ1_0.gguf), loaded via llama-server with GPU offload and flash attention enabled on a 32k context.
- It is served through an OpenAI-compatible API, so existing tools like `llm` can point at the local endpoint.
- Observed ~20 tok/s on an M5 Pro (44 tok/s after a restart), with a startup warning that the Metal tensor API was disabled — likely indicating suboptimal performance.