---
domain: ai-workflows
subdomain: multimodal-video-moderation
concept: modality-misalignment-and-originality-attribution
title: Modality Misalignment and Originality Attribution in Short-Form Video
sources:
  - title: "Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta"
    url: "https://www.youtube.com/watch?v=jNE8No-wvok"
    author: "Aditya Gautam (Meta), AI Engineer"
    date: "2026-09-23"
---

# Modality Misalignment and Originality Attribution in Short-Form Video

Aditya Gautam (Meta) describes the data characteristics and two core problems his team works on for short-form video surfaces. The data is chaotic: over 100 million items and much more viral content, confrontational content, users actively trying to take over the system, multilingual text on screens and in images, and a very dynamic landscape where new AI tools appear month to month, causing drift. There is also no clear ground truth for the problems being solved (Gautam, Meta).

The first problem is modality misalignment, specifically intramodality mismatch — the video's content does not match what the user clicked on, with injected advertising, agendas, political content, or confrontational behavior appearing inside a clip. Gautam calls this a very solvable problem: use CLIP-style models to embed image, video, audio, text, and figure modalities and compare them via cosine similarity. The harder part is understanding what happens at the level of each clip and each frame, which requires deep vision/video understanding.

The second problem is understanding unoriginal content. With widely available AI tools it has become very easy to duplicate, copy, and transform videos, making it hard to detect unoriginal content and to find a video's source. This has caused problems with attribution, credit, and ecosystem imbalance, with many duplicate videos that should not be present.

For scale, the talk argues for multi-agent systems rather than a single agent or single LLM, but only because the problem is genuinely complex and needs specialized nodes for search, content understanding, and reasoning; if one agent/LLM can solve a problem, multi-agent is unnecessary. The architecture centers on a centralized "review agent" that acts as an orchestrator or API gateway, decomposing signals and routing: a perception agent as a sophisticated VLM with many image and video tools, and a retriever/receiver agent that takes the ID from the review agent, pulls the video from the database, and breaks it into smaller pieces using semantic embedding and temporal-change detection — working not at a fixed frame rate but at points of temporal change, compressing similar frames together. Assessment should be holistic and 360-degree — not exact reproduction — covering the whole inter-agency pipeline from the LLM level, tools, and MCP. Optimization specific to vision and metadata lets the team avoid building the intelligent workflow for all videos and instead select a small candidate group for these tasks.

- Short-form video data at Meta scale (100M+ items) is chaotic, adversarial, multilingual, and drifts month to month as new AI tools appear, with no clear ground truth.
- Two target problems: intramodality modality misalignment (video content not matching the clicked intent, detected via CLIP-style embeddings and cosine similarity) and unoriginal content detection and source attribution.
- AI tools make copying and transforming video cheap, causing attribution, credit, and ecosystem-imbalance problems from duplicate content.
- A multi-agent design is justified only for genuinely complex problems: a centralized review/orchestrator agent decomposes signals to a sophisticated VLM perception agent and a retriever agent that segments video by temporal change rather than fixed frame rate.
- Metadata- and vision-specific optimization lets the pipeline avoid running the intelligent workflow on every video, selecting only a small candidate subset; evaluation is holistic rather than exact reproduction.