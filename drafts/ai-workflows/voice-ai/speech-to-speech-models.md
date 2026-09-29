---
domain: ai-workflows
subdomain: voice-ai
concept: speech-to-speech-models
title: Speech-to-Speech Model Research at Google DeepMind
sources:
  - title: "Speech-to-Speech Model Research at Google DeepMind — Valeria Wu Fon & Tom Ouyang, Google DeepMind"
    url: "https://www.youtube.com/watch?v=18Um2VjMM_g"
    author: "AI Engineer"
    date: "2026-09-15"
---

# Speech-to-Speech Model Research at Google DeepMind

Valeria Wu Fon, product lead for the speech-to-speech model in Gemini, and Tom Ouyang, an engineer on speech-to-speech in Gemini, present Google DeepMind’s work on voiceifying the agentic future. They frame voice as the most natural way for humans to interact with both the physical and virtual world, and point to Google products such as Search Live and Gemini Live, as well as Cloud/API deployments for enterprise voice agents, as evidence that voice applications will grow. They argue that speech-to-speech models are the right approach for building robust universal voice agents (Wu Fon & Ouyang, 2026).

Ouyang gives historical context for speech modeling. Up until around 2018, ASR systems typically involved many components: feature extraction, acoustic modeling, pronunciation modeling, language modeling, and second-pass rescoring to turn audio into text. Around 2018, systems moved toward end-to-end neural models that learn the mapping between acoustic inputs and text with less domain knowledge. But these models were narrow: they did speech-to-transcription, not responding or translating, and if you wanted tone, emotion, speed, word biasing, or images, you had to build those as separate system parts, which limited scalability (Ouyang, 2026).

In the LLM era, Gemini models have been natively multimodal. During pre-training, they use interleaved multimodal examples: for example, a text prompt plus video and audio inputs asking the model to summarize a bedtime story and annotate timestamps; or video captioning biased by both video and audio; or generating audio from video or text. ASR, TTS, and agentic tasks are learned under one unified token embedding space. This gives the team a foundation where the model already understands audio, video, text, and how these relate and transition, enabling further audio applications (Ouyang, 2026).

- Voice is described as the most natural human interface, with growing applications in Google products such as Search Live and Gemini Live and in enterprise voice agents via Cloud/API.
- Speech-to-speech models are presented as the way to build robust universal voice agents, rather than only chaining ASR and TTS.
- Traditional ASR evolved from multi-component pipelines to end-to-end neural systems, but remained narrow and did not handle responses, translation, tone, emotion, speed, or multimodal biasing without extra engineering.
- Gemini’s natively multimodal pre-training uses interleaved audio, video, text, and agentic tasks in a unified token embedding space, providing a foundation for audio research and applications.