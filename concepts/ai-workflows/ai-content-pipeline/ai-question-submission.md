---
domain: ai-workflows
subdomain: ai-content-pipeline
concept: ai-question-submission
title: Helping YOU ask ME questions with AI
sources:
  - title: "Helping YOU ask ME questions with AI"
    url: "https://kentcdodds.com/blog/helping-you-ask-me-questions-with-ai"
    date: "2026-02-24"
---

# Helping YOU ask ME questions with AI

The author added AI-powered features to kentcdodds.com to make it easier for community members to ask questions on the Call Kent podcast. Previously, users had to record a 120-second voice question; now they can type their question, choose an AI-generated voice, and optionally remain anonymous. An AI disclosure prefix is automatically added to generated audio for transparency.

- Users can type questions instead of recording themselves, reducing barriers like language, audio quality, and fear of judgment.
- Anonymous submissions are supported via a checkbox, using a generic Kody avatar in episode artwork.
- Cloudflare Workers AI is used via AI Gateway for text-to-speech, with model @cf/openai/deepgram/aura-2-en.
- A background pipeline automates audio stitching, transcription, and metadata generation, producing a draft episode ready for editing.
- Whisper transcription uses whisper-large-v3-turbo with base64 JSON payload to include initial_prompt for better transcript quality.