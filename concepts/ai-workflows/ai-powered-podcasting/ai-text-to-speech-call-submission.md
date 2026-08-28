---
domain: ai-workflows
subdomain: ai-powered-podcasting
concept: ai-text-to-speech-call-submission
title: Helping You Ask Me Questions with AI
sources:
  - title: "Helping YOU ask ME questions with AI"
    url: "https://kentcdodds.com/blog/helping-you-ask-me-questions-with-ai"
    date: "2026-02-24"
---

# Helping You Ask Me Questions with AI

Kent C. Dodds added AI-powered features to kentcdodds.com to make it easier for community members to ask questions on the Call Kent podcast. Users can now submit questions via text instead of recording themselves, choose an AI voice to read the question aloud, and optionally remain anonymous with a generic avatar. This addresses barriers like language concerns, audio quality worries, and desire for anonymity. [Source](https://kentcdodds.com/blog/helping-you-ask-me-questions-with-ai)

- Users can submit text questions and select an AI voice instead of recording themselves, with an optional anonymous mode.
- The text-to-speech endpoint adds an AI disclosure prefix before generating audio via Cloudflare AI Gateway and Workers AI.
- After the host records a response, a background draft pipeline auto-generates audio, transcript, title, description, and keywords.
- ffmpeg stitches together intro, call, interstitial, response, and outro audio with silenceremove, loudnorm, and acrossfade filters.
- The Whisper turbo transcription model requires base64 audio and supports an initial_prompt to improve transcript quality.