---
domain: ai-workflows
subdomain: recommender-systems
concept: llm-recommender-scaling
title: Why LLM Recommenders Will Be AI's Biggest Consumer App
sources:
  - title: "Why LLM Recommenders Will Be AI's Biggest Consumer App — Devansh Tandon, Meta"
    url: "https://www.youtube.com/watch?v=lIgdnF0s0kQ"
    author: "Devansh Tandon (AI Engineer)"
    date: "2026-09-25"
---

# Why LLM Recommenders Will Be AI's Biggest Consumer App

Devansh Tandon (Meta) argues that recommender systems scale like LLMs and that the industry is at a very early stage of the scaling curve, and that the LLM recommender will become one of the biggest consumer applications of AI (Tandon, AI Engineer). He points to the 2020 power-law scaling result — as model size, data, and compute increase, loss falls on a log-linear scale, enabling predictable improvements and driving capital investment in AI. Recommenders, which were the largest production ML models at major tech companies before the LLM wave and still serve over a billion active users daily, follow a similar power-law curve: data/compute/model size on the X axis against loss reduction or recommendation-quality gains (entropy or AUC) on the Y axis, translating into engagement and revenue impact at scale.

He cites Meta's HSTU work (2024 and a continuation this year) as real-world evidence that scaling model size, compute, and data yields clear offline recommendation-quality improvements. Meta earnings reports show the product impact: Instagram Reels viewing time up 30% year-over-year, with improvements from simplifying ranking architecture for efficient model scaling, doubling the length of user interaction sequences, and increasing the richness of each user interaction — direct parallels to LLM power-law curves.

Tandon introduces the "token flywheel" between training and engagement: you train a model and run inference (tokens), better recommendations stimulate consumer engagement and time spent by daily active users, which converts to monetization or subscription revenue that pays for the next training run. Each step on the scaling curve is one revolution of this flywheel, which sits at the core of many consumer businesses.

He frames four paradigms ("four S-curves") driving the industry forward. The first is the more traditional recommender S-curve focused on feature development and user and content onboarding (transcript ends mid-discussion of this paradigm). He also references his prior AI Engineer talk on training Gemini to speak on YouTube, covering semantic identifiers and generative search — ideas that have since moved from research to large-scale production systems across YouTube, Meta, Spotify, and DoorDash.

- Recommender systems follow LLM-like power-law scaling curves and the industry is at an early stage of that curve.
- LLM recommenders are positioned to become one of the biggest consumer AI applications.
- Meta's HSTU work and doubled user interaction sequence lengths in Instagram/Reels illustrate recommendations scaling driving engagement (Reels viewing time up 30% YoY) and revenue.
- The "token flywheel": training → inference/tokens → better recommendations → engagement → monetization → funding the next training run.
- Four S-curves of the recommendation paradigm are proposed, with the first being the traditional feature-development and user/content-onboarding curve.