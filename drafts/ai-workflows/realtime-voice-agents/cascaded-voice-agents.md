---
domain: ai-workflows
subdomain: realtime-voice-agents
concept: cascaded-voice-agents
title: Realtime Voice Agents with Frontier Intelligence
sources:
  - title: "Realtime Voice Agents with Frontier Intelligence — Bohan Li, EliseAI"
    url: "https://www.youtube.com/watch?v=MBHOH1NmDqc"
    author: "AI Engineer"
    date: "2026-09-15"
---

# Realtime Voice Agents with Frontier Intelligence

The talk describes a cascaded voice-agent architecture built to combine real-time responsiveness with frontier-model intelligence. The speaker maps the stack to self-driving car layers: perception (speech transcription), planning (LLM reasoning), and controls (text-to-speech/audio output) [AI Engineer, 2026]. The goal is to speed up each layer without sacrificing intelligence.

To reduce transcription latency and improve accuracy, the system uses a streaming speculative transcriber: a fast streaming model (Flux) works alongside or below an accurate batch transcriber (Scribe V2) that uses more context. When the accurate layer fires, it can correct or cancel earlier streaming detections; in the example, the correct layer understands a question about name/date of birth and fixes earlier errors before text is released to the agent [AI Engineer, 2026].

At the language-model layer, the approach reduces expensive round trips and tool-calling inferences. Background agents perform tool calls for the main agent and push tool results into the main agent's context, so the main agent behaves as if it made the call itself [AI Engineer, 2026]. Each transcription detection can also trigger an eager agent generation, but output is not emitted until the user has finished speaking. If a background tool call later finds the needed information (e.g., name and date of birth), the eager generation is canceled and retriggered with the correct context [AI Engineer, 2026].

- Cascaded voice agents separate perception/transcription, planning/LLM, and controls/TTS to improve speed while retaining frontier intelligence.
- Streaming speculative transcription layers a fast streaming model with a slower context-aware accurate model, allowing corrections before finalizing user text.
- Background tool calling offloads tool calls from the main agent and injects results into its context to avoid extra LLM round trips.
- Eager generation starts LLM output early per transcription detection but suppresses emission until end-of-speech; it can cancel and retrigger when corrected context or tool results arrive.