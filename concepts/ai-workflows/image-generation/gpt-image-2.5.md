---
domain: ai-workflows
subdomain: image-generation
concept: gpt-image-2.5
title: Introducing ChatGPT Images 2.5
sources:
  - title: "Introducing ChatGPT Images 2.5"
    url: "https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/"
    date: "2026-09-08T22:46:33+00:00"
  - title: "Introducing ChatGPT Images 2.5"
    url: "https://openai.com/index/introducing-chatgpt-images-2-5/"
    author: "OpenAI"
---

# Introducing ChatGPT Images 2.5

OpenAI released ChatGPT Images 2.5, introducing two new API model IDs: `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`. According to the documentation, Sunburst is optimized for editing precision, while Flare is designed for fast, high-quality everyday image generation (source: OpenAI announcement). The article also notes the author upgraded their `openai_image.py` CLI tool to support passing one or more reference images, enabling image editing via the command line. A demonstration shows adding 'a raccoon scientist studying the chart thoughtfully' to an existing image using the Sunburst model (source: Simon Willison).

- Two new model IDs: `gpt-image-2.5-sunburst` (editing precision) and `gpt-image-2.5-flare` (fast everyday generation).
- The CLI tool `openai_image.py` now supports reference images for editing workflows.
- Example usage: `uv run ... openai_image.py 'prompt' -i image.png -m gpt-image-2.5-sunburst`.