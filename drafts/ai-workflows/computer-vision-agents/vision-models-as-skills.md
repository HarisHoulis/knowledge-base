---
domain: ai-workflows
subdomain: computer-vision-agents
concept: vision-models-as-skills
title: Skill Issue: Stop Deploying Vision Language Models, Use Them with Skills
sources:
  - title: "Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face"
    url: "https://www.youtube.com/watch?v=dKcTBQzR7jI"
    author: "AI Engineer"
    date: "2026-09-23T13:30:16+00:00"
---

# Skill Issue: Stop Deploying Vision Language Models, Use Them with Skills

Merve Noyan argues that developers should stop calling vision language models (VLMs) directly for computer vision tasks and instead build vision programs "in the language of vision from start to finish" (Merve Noyan, "Skill issue: stop deploying vision language models, use them with Skills", AI Engineer, 2026-09-23). VLMs, she says, are never real-time — you might get 30–40 FPS on a toaster for classification or instance segmentation, and they are unreliable: a model like RF-DETR, covered by Joseph in the preceding talk, "will always outperform your visual comprehension language model." She also warns that many developers deploy models without reading licenses, citing YOLO's AGPL 3.0 license and urging a switch to Apache 2.0 models.

Her model-selection criteria are threefold: license first (Apache 2.0, MIT, or at least non-commercial), performance on par regardless of model size or architecture (she checks benchmarks after each computer vision conference), and "vibes."

She presents a toolkit, "Vibe Vision" — inspired by a post by Maziar — that exposes models as tools (e.g., SAM 3.1 as a tool for calling Gemma 4) so a coding agent can act as a computer vision engineer. The most interesting part is a training conveyor: where you only have unlabeled images, use a VLM as a labeler and a VLM as an evaluator, then train the model you actually need. In the example pipeline, an image dataset is annotated, passed to two judges — Gemma 4 E4B (~8B) and LFM 2.5 VL (~2B) — because research suggests an ensemble is better, after which smaller but more powerful vision models let you label cheaply.

The supporting infrastructure runs on Hugging Face-style hosting: Jobs for one-time batch processing or training, serverless inference routing across multiple providers, and containers for dumping intermediate data on dataset and model repositories. Long-term agentic tasks require controlling the labeling process and the training process.

- VLMs are not real-time and are outperformed by purpose-built CV models: RF-DETR will always beat a visual comprehension language model for detection/segmentation.
- Check the license first — prefer Apache 2.0 or MIT; YOLO's AGPL 3.0 catches developers who later have to pay.
- Package models as tools/skills for coding agents (e.g., SAM 3.1 as a tool for Gemma 4) rather than prompting VLMs directly.
- Bootstrap unlabeled data with a conveyor: VLM as labeler, VLM as judge (ensembling e.g. Gemma 4 E4B + LFM 2.5 VL), then train a small specialized model.