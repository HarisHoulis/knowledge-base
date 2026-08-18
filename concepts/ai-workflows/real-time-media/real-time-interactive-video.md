---
domain: ai-workflows
subdomain: real-time-media
concept: real-time-interactive-video
title: The Next Medium: Why Real-Time Interactive Video Changes Everything
sources:
  - title: "The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor"
    url: "https://www.youtube.com/watch?v=5dCAmSDOAjI"
    author: "AI Engineer"
    date: "2026-08-18T17:30:18+00:00"
---

# The Next Medium: Why Real-Time Interactive Video Changes Everything

In this talk, Ahmed Ahres argues that real-time interaction is not merely a speedup but a change of medium, using the analogy of Uber and GPS: just as Uber could not exist without continuous positioning rather than consulting a static map, real-time video transforms what is creatable. He traces this through film history, noting that the viewfinder allowed directors to adjust while shooting, which ultimately enabled platforms like Instagram and TikTok. Current generated video, by contrast, is batch-oriented: prompt, wait, receive a file, and no further interaction.

Ahres defines world models not as Gaussian splatting or longer clips, but as video that is interactive, effectively infinite, and generated fast enough to steer. He demonstrates this by injecting a cat into a still-generating scene. The implications fall into three categories: control through instant feedback, character-driven worlds for robotics training and education, and live avatars—which he candidly admits are not yet working properly. On the engineering side, the batch playbook does not carry over: streaming pixels replaces file returns, every session is stateful, and sub-100-millisecond latency requires placing GPUs close to users rather than in a single region.

- Real-time video is a medium shift, not a speedup—analogous to GPS replacing maps and the viewfinder enabling modern film.
- World models should be infinite, interactive, and steerable in real time, not just longer or more detailed generated clips.
- The potential splits into instant-feedback control, character-driven worlds for robotics/education, and live avatars (still unsolved).
- Real-time streams require stateful, low-latency infrastructure, making the existing batch generation playbook inadequate.