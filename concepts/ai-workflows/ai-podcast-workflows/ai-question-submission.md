---
domain: ai-workflows
subdomain: ai-podcast-workflows
concept: ai-question-submission
title: Helping YOU ask ME questions with AI
sources:
  - title: "Helping YOU ask ME questions with AI"
    url: "https://kentcdodds.com/blog/helping-you-ask-me-questions-with-ai"
    date: "2026-02-24"
---

# Helping YOU ask ME questions with AI

Kent C. Dodds introduced new AI-powered features on kentcdodds.com to make it easier for community members to ask questions on the Call Kent podcast without recording themselves. Users can type a question, choose an AI voice, and optionally remain anonymous, which addresses concerns like non-native English, audio quality, fear of judgment, and desire for more time to formulate thoughts. A text-to-speech endpoint validates the question, adds an AI disclosure prefix, and uses Workers AI through Cloudflare AI Gateway to generate audio (source).

On the admin side, a background draft-processing pipeline automates episode creation. After a response is recorded, the system generates audio, transcribes the conversation using Workers AI, and produces metadata such as title and description; the resulting draft is editable before publishing. The implementation includes model-specific handling: `@cf/openai/whisper-large-v3-turbo` expects base64 in JSON, while the non-turbo Whisper model accepts raw binary. ffmpeg stitches the intro, question, interstitial, response, and outro tracks together. The author reports that this reduces manual work and enables more community participation (source).

- Users can submit podcast questions as text, choose an AI voice, and remain anonymous.
- An AI disclosure prefix is automatically added to generated voice audio.
- Admin workflow uses a draft-processing pipeline to generate audio, transcript, and metadata automatically.
- Cloudflare Workers AI powers text-to-speech, transcription, and metadata generation.
- The system uses ffmpeg to stitch audio segments for the final episode.