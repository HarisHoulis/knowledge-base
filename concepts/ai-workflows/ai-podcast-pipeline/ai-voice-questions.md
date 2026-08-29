---
domain: ai-workflows
subdomain: ai-podcast-pipeline
concept: ai-voice-questions
title: Helping YOU ask ME questions with AI
sources:
  - title: "Helping YOU ask ME questions with AI"
    url: "https://kentcdodds.com/blog/helping-you-ask-me-questions-with-ai"
    date: "2026-02-24"
---

# Helping YOU ask ME questions with AI

A notable detail is handling model-specific transcription requirements: the whisper-large-v3-turbo model expects base64 in the JSON payload, while the non-turbo whisper model accepts raw binary audio. The turbo path allows including instruction fields like initial_prompt, which improves transcript quality for proper nouns and the podcast format. The result is that the host typically has a full draft (audio, transcript, title, description, keywords) ready to edit before publishing.

- Users can now submit text questions for Call Kent podcast, choosing an AI voice and anonymity, lowering barriers to participation.
- Text-to-speech is implemented via Cloudflare Workers AI through AI Gateway, including validation and an AI disclosure prefix.
- Episode draft processing is automated with a step-based pipeline: generating audio, transcribing, formatting transcript, and generating metadata.
- Audio stitching uses ffmpeg with filters for silence removal, loudness normalization, and crossfade.
- Transcription requires model-specific handling: whisper-large-v3-turbo expects base64 in JSON, while non-turbo accepts raw MP3 binary.