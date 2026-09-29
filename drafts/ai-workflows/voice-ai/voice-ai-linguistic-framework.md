---
domain: ai-workflows
subdomain: voice-ai
concept: voice-ai-linguistic-framework
title: A Linguistic Map for Voice Agents: Diagnosing Failures in Human-AI Conversation
sources:
  - title: ""My name is... my name is...": A Linguistic Map for Voice Agents — Midam Kim, ServiceNow"
    url: "https://www.youtube.com/watch?v=IDNfAZVKvPE"
    author: "AI Engineer"
    date: "2026-09-15T16:30:08+00:00"
---

# A Linguistic Map for Voice Agents: Diagnosing Failures in Human-AI Conversation

Midam Kim, an ML engineer at ServiceNow and a researcher of speech communication, argues that voice AI failures should be analyzed through linguistics. Human communication is a joint activity: participants exchange sounds and words, take turns, and continuously update their mental models. Voice agents must participate in this same joint activity because users expect the communication patterns humans have evolved over thousands of years (AI Engineer, 2026).

Kim illustrates the framework with a personal call failure. The bot misheard “m” as “n” in the spelling of “Midam,” an STT failure at the listening/sound level. TTS then applied English-centric reading rules and said “Madam,” a speaking/sound failure. When Kim struggled to find and read an account number, the bot cut him off, failed to track his mental model, and asked him to repeat information instead of using interactive clarification. The result was irritation and a request to speak to a human (AI Engineer, 2026).

The proposed framework separates listening and speaking channels across four components: sounds, words, interaction, and mental model. On the listening side, this means recognizing speech, understanding words, waiting for the right turn-taking timing, and inferring user intention. On the speaking side, it includes pronunciation and related production concerns. By locating failures at specific linguistic layers, teams can design voice agents that ground conversation, manage timing, clarify interactively, and maintain a shared mental model (AI Engineer, 2026).

- Human communication is a joint activity; voice agents must maintain shared mental models and interactive grounding.
- Voice AI failures can be diagnosed across listening/speaking channels and sound, word, interaction, and mental-model components.
- STT misrecognition, English-centric TTS pronunciation, interruptions, and lack of clarification all degrade user trust.
- Bots should respect turn-taking timing and use interactive clarification rather than cutting users off or repeating requests.