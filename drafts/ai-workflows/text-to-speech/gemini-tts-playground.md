---
domain: ai-workflows
subdomain: text-to-speech
concept: gemini-tts-playground
title: Gemini 3.8 TTS Playground
sources:
  - title: "Gemini 3.8 TTS Playground"
    url: "https://simonwillison.net/2026/Sep/23/gemini-tts-playground/"
    author: "Simon Willison"
    date: "2026-09-23"
---

# Gemini 3.8 TTS Playground

Google released two new Gemini text-to-speech models, `gemini-3.8-flash-tts` and `gemini-3.8-flash-lite-tts`, with a library of over 2,000 voices and the ability to create a custom voice from a 30-second audio sample of a voice the user has rights to use (Simon Willison, 2026).

Simon Willison built a bring-your-own-key Gemini 3.8 TTS Playground, vibe coded with GPT-6 Astra, taking advantage of the underlying Gemini API's open CORS policy (Simon Willison, 2026). The API notably makes it easy to define a full conversation between multiple characters, each with different voices and voice style instructions (Simon Willison, 2026).

In a demo, two pelicans debate whether they should move to the Pacifica Pier. Claude 4.5 Opus wrote the script, and the tool generated a URL to render it (Simon Willison, 2026). Generating 1m 18s of audio with Gemini 3.8 Flash TTS, not the cheaper Flash-Lite, took about 20 seconds and cost 2.74 cents (Simon Willison, 2026).

- Google released Gemini 3.8 Flash TTS and Flash-Lite TTS with over 2,000 voices and custom voice creation from a 30-second sample.
- Simon Willison vibe-coded a BYOK TTS playground with GPT-6 Astra, using the Gemini API's open CORS policy.
- The Gemini TTS API supports multi-character conversations with per-character voices and voice style instructions.
- A 1m 18s multi-voice demo generated in about 20 seconds for 2.74 cents using Gemini 3.8 Flash TTS.