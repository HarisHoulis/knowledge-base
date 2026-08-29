---
domain: ai-workflows
subdomain: podcast-ai-pipeline
concept: ai-text-to-speech-questions
title: Helping YOU ask ME questions with AI
sources:
  - title: "Helping YOU ask ME questions with AI"
    url: "https://kentcdodds.com/blog/helping-you-ask-me-questions-with-ai"
    date: "2026-02-24"
---

# Helping YOU ask ME questions with AI

The article describes new AI-powered features added to kentcdodds.com for the Call Kent podcast, allowing users to submit questions via text instead of recording audio. Users can type a question, choose an AI voice to speak it, and optionally remain anonymous. This lowers barriers for non-native English speakers, those concerned about audio quality or judgment, and those who prefer more time to compose their thoughts (Kent C. Dodds, 2026). The feature is built on Cloudflare's AI platform, using Workers AI for text-to-speech, transcription, and metadata generation, with AI Gateway managing the API calls. The text-to-speech endpoint validates input, prepends an AI disclosure prefix, and triggers the TTS model. On the author's side, a background pipeline processes the episode draft: it stitches audio with ffmpeg, transcribes the call and response using Whisper, formats the transcript, and generates metadata such as title and description. The system also handles model-specific quirks—for example, the Whisper turbo model expects base64 audio in JSON, while the non-turbo model accepts raw binary. By automating these steps, Kent can quickly edit a complete draft instead of creating everything manually, making the podcast more accessible and efficient (Kent C. Dodds, 2026).

- Users can submit written questions that are converted to speech with a chosen AI voice, and can choose to remain anonymous.
- The implementation uses Cloudflare AI Gateway and Workers AI for TTS, transcription, and metadata generation.
- A background pipeline automatically creates a full episode draft (audio, transcript, title, description, keywords) after the host records a response.
- ffmpeg is used to stitch audio segments together, and model-specific handling is required for Whisper (base64 for turbo, binary for non-turbo).
- This feature reduces friction for non-native speakers and users who prefer anonymity or more time to formulate their questions.