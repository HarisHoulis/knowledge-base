---
domain: ai-workflows
subdomain: decision-models
concept: multimodal-decision-apis
title: Gemini Decisions API
sources:
  - title: "Gemini Decisions API"
    url: "https://simonwillison.net/2026/Nov/11/gemini-decisions-api/"
    author: "Simon Willison"
    date: "2026-11-11"
---

# Gemini Decisions API

Simon Willison compares Google's new Gemini Decision 1 API against competing decision models from OpenAI (GPT-6 Luna) and Jev. Pricing is identical to GPT-6 Luna at 10 cents per million input tokens with free output, while Jev remains cheapest at 4.2 cents per million. The key differentiator is modality coverage: Jev is text and JSON only, OpenAI handles text and images, and Gemini Decision 1 is fully multimodal across text, images, audio, video, and PDFs.

Willison tested the API by submitting a video file (his "Yonkers stomping robot" clip) alongside four yes/no questions about whether it contained a dragon, a robot, and whether it was set in France or the USA. Jev and OpenAI return hard 1.0 or 0.0 answers, but Gemini returns calibrated probabilities instead—0.92 for robot and USA, and low values (0.05, 0.08) for dragon and France.

The practical takeaway is that Gemini's decision model trades binary certainty for confidence scores, which may be more useful for downstream logic, while its multimodal input support distinguishes it from the cheaper text-only Jev.

- Gemini Decision 1 is priced like GPT-6 Luna (10 cents per million input tokens, free output); Jev is cheapest at 4.2 cents per million
- Gemini is fully multimodal (text, images, audio, video, PDFs), versus OpenAI's text+images and Jev's text/JSON only
- Unlike Jev and OpenAI which return 1.0/0.0, Gemini returns probability scores for yes/no questions
- In a video test, Gemini correctly scored robot and USA high (~0.92) and dragon and France low (~0.05-0.08)