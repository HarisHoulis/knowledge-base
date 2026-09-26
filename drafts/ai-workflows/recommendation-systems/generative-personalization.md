---
domain: ai-workflows
subdomain: recommendation-systems
concept: generative-personalization
title: Teaching LLMs to Speak Spotify: An LLM-Centric Recommender at Spotify
sources:
  - title: "Teaching LLMs to Speak Spotify — Yves Raimond & Jacqueline Wood, Spotify"
    url: "https://www.youtube.com/watch?v=2LRIAfng7eA"
    author: "AI Engineer"
    date: "2026-09-25"
---

# Teaching LLMs to Speak Spotify: An LLM-Centric Recommender at Spotify

Yves Raimond and Jacqueline Wood describe Spotify's move from classic ranking-based recommendation to what they call "generative personalization." They frame the problem's scale: roughly 760 million monthly active users across 184 markets, and a catalog of over 100 million tracks plus videos, podcasts, and audiobooks, which makes selection unusually complex (Raimond & Wood, Spotify talk).

The history runs in three phases: manual curation (about 10 billion playlists, many created hourly), learning from those curatorial signals to produce scalable recommendations (e.g. Discover Weekly, launched 2014), and the current phase where models are given the ability to speak and understand English so they can generate and explain experiences rather than only rank items (Raimond & Wood).

The speakers characterize the transition as three shifts: from personalization as guesswork (a ranking algorithm outputting a list) to personalization as reasoning that analyzes whether results are relevant in a given context; away from opaque multi-stage "black box" ranking toward transparent, user-controlled personalization; and from pure recommendations toward experiences that are created and explained (Raimond & Wood).

Concrete products illustrate the shift: Spotify DJ lets users steer a personalized session by pointing it in a direction; on-demand playlists accept both broad and detailed natural-language queries (e.g. bands playing in San Francisco tonight, or a playlist for a run that adapts across stages of the run); and "flavor profile," launched in New Zealand, exposes in natural language what the algorithm has understood about a user so it can be edited — for example marking all Disney music as the kids' and requesting it not be recommended (Raimond & Wood).

- Spotify is moving from ranking-based recommendation to "generative personalization," where LLMs both generate and explain personalized experiences.
- Scale drives difficulty: ~760M monthly active users in 184 markets and a catalog of 100M+ tracks plus videos, podcasts, and audiobooks.
- Three stated shifts: guesswork → reasoning, black-box ranking → transparent and user-controlled personalization, recommendations → created experiences.
- Features cited: Spotify DJ (steerable sessions), natural-language on-demand playlists, and "flavor profile," which surfaces and lets users edit the algorithm's understanding of their taste.