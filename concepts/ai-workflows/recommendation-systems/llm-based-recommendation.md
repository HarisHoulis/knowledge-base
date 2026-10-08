---
domain: ai-workflows
subdomain: recommendation-systems
concept: llm-based-recommendation
title: How Netflix Taught an LLM to Recommend Movies
sources:
  - title: "How Netflix Taught an LLM to Recommend Movies So That You Keep Watching"
    url: "https://blog.bytebytego.com/p/how-uber-built-a-genie-to-answer"
    author: "ByteByteGo"
    date: "2026-10-07"
---

# How Netflix Taught an LLM to Recommend Movies

Netflix built GenRec, an LLM-based recommendation system that ranks the full content catalog. The original engine relied on thousands of hand-crafted features across users, items, and interactions, making it costly to onboard new use cases. GenRec instead uses an LLM to interpret a user's viewing history and assign scores to movies and shows, leveraging the model's world knowledge and language understanding to capture relationships between content and behavior. Netflix calls the process of expressing information in text 'verbalization'.

A general-purpose LLM is not a good recommender on its own: it may favor globally popular titles, suggest items outside the catalog, and lacks personalization. GenRec is trained in two phases. Phase 1 adapts an open-source foundation LLM with proprietary Netflix data to build a Netflix-aware foundation, updated infrequently. Phase 2 post-trains the model to rank items based on reward signals while meeting cost targets, and runs more frequently to keep up with new releases and shifting viewer choices.

Training examples are built from user interactions such as clicks, viewing time, thumbs feedback, watchlist additions, and abandoned sessions, formatted as conversations. The 'user message' contains history, context, metadata, and the recommendation task; the 'assistant message' describes what the user did next. At serving time, GenRec receives context to score items rather than chatting with users. Netflix applies 'context engineering' to decide what to include in prompts, weighing strong evidence versus weak signals, compressing repetitive behavior, adding richer metadata for cold-start items, and testing how ranking quality changes with more history. Cleaning, compression, and rewording reportedly cut tokens to roughly one-third of the original amount.

GenRec combines multiple training objectives: a primary ranking objective that assigns higher scores to items with strong engagement signals (with thresholds and filtering to reduce label noise), a language-modeling objective to preserve language understanding and enable future text applications like explaining recommendations, and weighting to prevent excessive influence from specific events.

- GenRec uses an LLM to rank Netflix's full catalog, replacing reliance on thousands of hand-crafted features.
- Training happens in two phases: a Netflix-aware foundation model, then post-training to rank based on reward signals.
- User interactions are converted into conversation-format training examples pairing context with the user's next action.
- Context engineering selects and compresses history to control token cost, cutting tokens to about one-third.
- Multiple objectives preserve language understanding while optimizing ranking and controlling event influence.