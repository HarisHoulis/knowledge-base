---
domain: ai-workflows
subdomain: generative-video
concept: next-frame-prediction-world-models
title: Next-Frame Prediction as World Modeling: Lessons from Building Runway
sources:
  - title: "You Can't Tell What's Real Anymore. Here's What Comes Next - Cristóbal Valenzuela, Runway"
    url: "https://www.youtube.com/watch?v=q4ITwvlFplQ"
    author: "AI Engineer"
    date: "2026-11-03"
---

# Next-Frame Prediction as World Modeling: Lessons from Building Runway

Cristóbal Valenzuela reflects on nearly a decade building Runway, framing generative video as a continuation of an idea cinema discovered over a century ago: video is an optical illusion created by connecting frames fast enough to produce the appearance of movement. Runway's work takes that same idea—predicting the next frame—and scales it with large networks and compute, drawing on the scaling laws that have driven language models. He shows the company's first AI film from 2019, a 128x128-pixel piece called "Orange," as a baseline against which today's generated footage looks unrecognizable.

Valenzuela argues that the most interesting consequence of next-frame prediction is not pretty imagery but what the model must learn to do it well: physics, object permanence, gravity, occlusion, motion, and how objects function in the real world. A model that can render a camel standing on a ball or water behaving correctly in a container must implicitly understand those dynamics. He describes Runway as sitting at the intersection of art and science, with roots in creative communities alongside researchers working on diffusion and large-scale video models.

He claims the visual Turing test has effectively been passed—Runway has tried to quantify whether people can distinguish real from generated video, and he says they cannot, including himself after ten years in the field. He also notes that evaluation benchmarks for video models go beyond creativity (essentially whether a viewer likes the output), and he expects today's best output to look as crude as "Orange" within a few years.

- Video is an optical illusion—frames connected fast enough create the appearance of movement—and generative video scales that century-old cinematic idea with modern compute.
- Scaling next-frame prediction yields emergent understanding of physics, object permanence, gravity, occlusion, and motion, not just realistic pixels.
- Valenzuela claims the visual Turing test has been passed: people, including him, struggle to distinguish real from generated video.
- Runway positions itself at the intersection of art and science, combining creative-community roots with diffusion and large-video-model research.
- Video-model benchmarks extend beyond subjective creativity to whether the model correctly renders object interactions and dynamics.