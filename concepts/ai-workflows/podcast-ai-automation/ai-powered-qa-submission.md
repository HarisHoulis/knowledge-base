---
domain: ai-workflows
subdomain: podcast-ai-automation
concept: ai-powered-qa-submission
title: Helping YOU ask ME questions with AI
sources:
  - title: "Helping YOU ask ME questions with AI"
    url: "https://kentcdodds.com/blog/helping-you-ask-me-questions-with-ai"
    author: "Kent C. Dodds"
    date: "2026-02-24"
---

# Helping YOU ask ME questions with AI

Kent C. Dodds added AI-powered features to kentcdodds.com for the Call Kent podcast, allowing users to submit questions as text instead of recording themselves. Users can select an AI-generated voice for their question and optionally remain anonymous, addressing concerns about language barriers, audio quality, and privacy (Kent C. Dodds, "Helping YOU ask ME questions with AI", https://kentcdodds.com/blog/helping-you-ask-me-questions-with-ai).

The implementation uses Cloudflare's Workers AI platform via AI Gateway for text-to-speech generation, adding an AI disclosure prefix to the generated audio. On the admin side, a background pipeline processes draft episodes: it generates audio, transcribes the conversation using Whisper models, and automatically creates metadata such as title, description, and keywords. ffmpeg stitches together intro, call, interstitial, response, and outro audio with filters like silenceremove, loudnorm, and acrossfade (Kent C. Dodds, "Helping YOU ask ME questions with AI", https://kentcdodds.com/blog/helping-you-ask-me-questions-with-ai).

A technical detail highlights that the whisper-large-v3-turbo model expects base64 audio in JSON, while the non-turbo Whisper model accepts raw binary. The turbo path also allows an initial_prompt to improve transcription quality. The author emphasizes that these AI tools significantly reduce manual editing work, making it easier for everyone to ask questions and open discussions (Kent C. Dodds, "Helping YOU ask ME questions with AI", https://kentcdodds.com/blog/helping-you-ask-me-questions-with-ai).

- Users can submit questions as text, choose an AI voice, and remain anonymous.
- Cloudflare Workers AI handles text-to-speech, transcription, and metadata generation.
- ffmpeg combines audio segments with filters like silenceremove, loudnorm, and acrossfade.
- The pipeline generates a full draft episode (audio, transcript, title, description, keywords) for quick editing.
- Whisper turbo model requires base64 audio in JSON and supports context prompts for better transcription.