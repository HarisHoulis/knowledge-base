---
domain: ai-workflows
subdomain: healthcare-voice-agents
concept: polaris-model-orchestration
title: Hippocratic AI's 200 Million Patient Conversations: Building a Safe and Fast Voice Agent Stack
sources:
  - title: "200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI"
    url: "https://www.youtube.com/watch?v=AN65uc645mE"
    author: "AI Engineer"
    date: "2026-08-19T16:00:06+00:00"
---

# Hippocratic AI's 200 Million Patient Conversations: Building a Safe and Fast Voice Agent Stack

Vivek Muppalla opens by asking how many people had ever received a proactive call from their healthcare provider, and almost no one raised a hand. He frames this as a triage math problem: there are too few clinicians and too few hours, so only the sickest patients get called. Hippocratic AI has now completed over 200 million clinical conversations across more than 60 health systems, which changes the arithmetic. The company refused the typical tradeoff between latency and accuracy—models accurate enough for clinical work take tens of seconds to answer, while models fast enough for a phone call are not safe enough to make one—so they built the stack end to end (YouTube).

- Polaris runs 31 models on every conversation: one primary model holds the thread and 30 specialists cover labs, medications, and scheduling, executed in parallel. Each specialist first makes a fast check on whether it has anything to say at all, avoiding the single-point-of-failure risk of one large model.
- Speech recognition is a decoder-only audio system that receives the conversation so far plus domain context alongside the audio. This allows drug names to resolve against a finite list rather than an unbounded one, and prosody is preserved so the system hears the 'how' as well as the 'what'.
- Single-word answers get a second scoring pass because a misheard 'a' as 'no' is catastrophic.
- 99% accuracy is unacceptable at scale: at 10,000 calls per day, that means 100 people sent to the wrong appointment. Catching a 1% failure rate requires roughly 450 tests.
- Evaluation is graded on the same scale used for humans, including building a benchmark for empathy.