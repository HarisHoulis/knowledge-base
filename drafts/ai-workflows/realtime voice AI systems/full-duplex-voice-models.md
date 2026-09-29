---
domain: ai-workflows
subdomain: realtime voice AI systems
concept: full-duplex-voice-models
title: How OpenAI Built GPT-Live: Full-Duplex Voice Architecture
sources:
  - title: "How OpenAI Built GPT-Live"
    url: "https://blog.bytebytego.com/p/how-openai-built-gpt-live"
    author: "ByteByteGo"
    date: "Tue, 22 Sep 2026 15:32:06 GMT"
---

# How OpenAI Built GPT-Live: Full-Duplex Voice Architecture

Voice systems have gone through three architectural generations, according to ByteByteGo's interview with OpenAI GPT Voice team engineers Zahan Malkani and Justin Uberti. Cascaded designs chain separate ASR, LLM, and TTS models, which loses vocal information like tone and accumulates latency across three serial stages. Turn-based end-to-end speech-to-speech models process audio directly but still depend on a turn detector that decides when the user has finished — a component that either cuts users off, introduces awkward delays, or mishandles interruptions — and they require a full retraining run whenever a new frontier LLM appears.

The third generation, full-duplex, lets the model listen and talk simultaneously by continuously emitting audio tokens on a fixed clock (roughly one frame per 80ms in the open Moshi model, cited as a reference), where silence is simply another token. This removes the turn detector entirely, solving interruption and unnaturalness problems, but creates two new challenges: continuous inference is expensive because the model never idles, and the model must respond within milliseconds so it cannot be too large.

OpenAI's GPT-Live-1, launched July 2026, addresses this by separating talking from thinking: a small, fast voice model handles the conversation while a capable frontier model (GPT-5.5 in the article's example) performs reasoning and tool calling via delegation, keeping the conversation going while a lookup runs. Serving is split into a live path carrying only audio on a fixed clock, and an async path handling delegations and tool calls. The live path is optimized with WARP (WebRTC Abridged Roundtrip Protocol), which parallelizes standard WebRTC's six setup steps down to one round trip; keeping each conversation resident in GPU memory on one model instance so only new frames are processed; and a managed handoff mechanism that pre-loads a replacement instance before switching, also used for context compaction. The async path cuts latency by prefilling the frontier model's session at conversation start, so the model already has the context when the first delegation arrives.

Evaluation of full-duplex systems differs from turn-based models, which can be scored one turn at a time by sending a request and scoring the response (the source text is truncated at this point).

- Three voice generations: cascaded ASR+LLM+TTS pipelines (information loss, additive latency, operational complexity), turn-based speech-to-speech with a turn detector, and full-duplex models that listen and speak at once.
- Full-duplex removes the turn detector by continuously emitting audio tokens on a fixed clock, where silence is just another token — but this makes serving expensive since the model never idles and must stay small enough for millisecond responses.
- GPT-Live separates talking from thinking: a small voice model keeps the conversation going while a frontier model is delegated expensive reasoning and tool calls, reducing the speed-versus-quality trade-off and improving modularity.
- The serving system splits into a live path (audio only, fixed clock) and async path (delegations, tool calls), so slow tool calls don't delay audio.
- Latency optimizations include WARP for one-round-trip session setup, keeping conversations resident in GPU memory per model instance, managed handoff between instances for restarts/updates/compaction, and prefilling the frontier model's session at conversation start.