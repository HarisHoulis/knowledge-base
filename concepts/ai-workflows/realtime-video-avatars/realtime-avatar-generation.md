---
domain: ai-workflows
subdomain: realtime-video-avatars
concept: realtime-avatar-generation
title: Voice agents with Realtime Video — Sidney Primas, LemonSlice
sources:
  - title: "Voice agents with Realtime Video — Sidney Primas, LemonSlice"
    url: "https://www.youtube.com/watch?v=z1dqv74SpUs"
    author: "AI Engineer"
    date: "2026-08-18T16:00:06+00:00"
---

# Voice agents with Realtime Video — Sidney Primas, LemonSlice

Sidney Primas discusses the engineering challenges behind realtime, long-duration video avatars, using an example of Teddy Roosevelt in a replica Oval Office running for eight hours. Because realtime generation has no access to future frames, each generated block inherits and compounds errors from prior blocks. LemonSlice addresses this by enforcing a causal attention mask during training and collapsing roughly 30 denoising steps into a single step to achieve realtime performance.

Audio is the hidden bottleneck: emotion and facial expression depend heavily on the audio embedding, yet standard audio encoders trained on audiobooks are monotone, so an expressive model requires a custom audio encoder. The broader approach is to point a world model at humans, accepting higher training and deployment costs in exchange for free full-body movement, object interaction, and physics. Surprisingly, serving this model costs about the same as serving a voice model, and the orchestration of threads and queues across GPU and CPU—the 'model harness'—is now seen as key to durable value.

- Realtime video generation is causally constrained: each frame depends only on past frames, so errors accumulate over hours unless the model is trained to respect this.
- LemonSlice compresses roughly 30 denoising steps to a single step to hit realtime, while using an attention mask to enforce causal generation during training.
- Audio embeddings drive emotion and facial expression; generic audiobook-trained encoders are too monotone, so expressive models need custom audio encoders.
- Deployment cost for the realtime video avatar is roughly on par with voice-only models, despite the extra visual complexity.
- The 'model harness'—multi-threaded orchestration across GPU/CPU to prevent stutter during interrupts—is where much of the durable value will reside.