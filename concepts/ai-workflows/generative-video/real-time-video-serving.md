---
domain: ai-workflows
subdomain: generative-video
concept: real-time-video-serving
title: Generative Video at the Speed of Light — Keegan McCallum
sources:
  - title: "Generative Video at the Speed of Light — Keegan McCallum, uRun"
    url: "https://www.youtube.com/watch?v=Xln-On3syJk"
    author: "AI Engineer"
    date: "2026-08-18T16:30:29+00:00"
---

# Generative Video at the Speed of Light — Keegan McCallum

Keegan McCallum opens by noting that $10 now buys roughly three hours of continuously generated video, and $50 buys fifteen, contrasting this with the audience's own habits of burning similar amounts on coding tokens in a single hour. He argues that the interesting axis in generative video has shifted from quality to efficiency and long-horizon capability: while a slower clip may have better motion, it costs on the order of a hundred times more to produce than a real-time generation.

- The cost of real-time generative video has dropped to about $10 for three hours, making it comparable to coding token spend.
- Quality is no longer the primary differentiator; efficiency and long-horizon generation now define the field.
- Helios, a distilled 14B-parameter model, is one of over forty real-time or long-horizon video models released this year.
- Real-time generation enables new interaction shapes: webcam haircut previews, visual media for non-text thinkers, and live steering of generations rather than a slot-machine workflow.
- The main engineering challenge is serving: global GPU placement, WebRTC with ICE/TURN, and a continuous streaming pipeline synchronized frame-by-frame with user controls.