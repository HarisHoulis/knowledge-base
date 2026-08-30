---
domain: ai-workflows
subdomain: ai-voice-questions
concept: ai-voice-questions
title: Helping you ask ME questions with AI
sources:
  - title: "Helping you ask ME questions with AI"
    url: "https://kentcdodds.com/blog/helping-you-ask-me-questions-with-ai"
    date: "2026-02-24"
---

# Helping you ask ME questions with AI

The article describes new AI-powered features on kentcdodds.com for the Call Kent podcast, which traditionally required users to record a voice question. The new feature lets users type their question, choose an AI-generated voice, and optionally submit anonymously, lowering barriers for people who are uncomfortable recording themselves, such as non-native English speakers or those concerned about being judged. The text-to-speech flow validates the input, adds an AI disclosure prefix, and calls Workers AI through Cloudflare AI Gateway using a model like `@cf/openai/deepgram/aura-2-en`.

On the admin side, after Kent records his response, a background draft-processing pipeline runs through steps: generating audio, transcribing, generating metadata, and marking the episode READY. The pipeline uses ffmpeg to stitch intro, call, interstitial, response, and outro audio segments with filter_complex for silence removal, loudness normalization, and crossfading. Transcription is handled by Workers AI models, with special handling for `@cf/openai/whisper-large-v3-turbo` where base64 JSON payloads are used, while non-turbo `@cf/openai/whisper` accepts raw binary audio. The turbo model supports extra context fields like `initial_prompt` to improve transcript accuracy.

The article highlights how AI tools enable building features that were previously too time-consuming, and the resulting draft episodes (audio, transcript, title, description, keywords) can be edited and published quickly.

- Users can now submit text-based questions with AI-generated voices and choose to remain anonymous.
- The system uses Cloudflare AI Gateway, Workers AI text-to-speech, and transcription models.
- A draft episode pipeline automatically generates audio, transcript, and metadata with ffmpeg audio stitching.
- Base64 encoding for transcription is model-specific, with `whisper-large-v3-turbo` requiring base64 JSON and `whisper` accepting raw binary.