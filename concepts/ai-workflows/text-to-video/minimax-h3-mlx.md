---
domain: ai-workflows
subdomain: text-to-video
concept: minimax-h3-mlx
title: Running MiniMax-H3 on Apple Silicon with MLX
sources:
  - title: "PipeNetwork/minimax-h3-mlx"
    url: "https://simonwillison.net/2026/Aug/4/minimax-h3-mlx/#atom-everything"
    date: "2026-08-04T19:10:09+00:00"
---

# Running MiniMax-H3 on Apple Silicon with MLX

MiniMax-H3 is a text-to-video model that generates both visual and audio content. A Python package ports it to MLX, enabling local inference on Apple Silicon. The author successfully ran it on an M5 Max MacBook Pro by cloning the repo and downloading model files via Hugging Face Hub using uv commands (Simon Willison, 2026).

Running the model required approximately 115 GB of model files, and generating a single video took just under 45 minutes. While the video output was impressive, the audio was described as 'weird speech-like garbage' because no guidance was provided for the audio track. The official prompting guide on Hugging Face contains detailed recommendations for achieving better audio-visual results, which the author had not consulted beforehand (Simon Willison, 2026).

- MiniMax-H3 is a text-to-video model with audio generation, ported to MLX for Apple Silicon.
- Local execution requires downloading ~115 GB of model files.
- Video generation took ~45 minutes on a M5 Max MacBook Pro.
- Audio quality depends heavily on prompt guidance; a prompting guide is available.
- The MLX port enables on-device inference without cloud dependencies.