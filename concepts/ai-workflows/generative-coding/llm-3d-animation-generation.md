---
domain: ai-workflows
subdomain: generative-coding
concept: llm-3d-animation-generation
title: Yonkers Rises: Prompting an LLM to Build a Three.js Mech Animation
sources:
  - title: "Yonkers Rises"
    url: "https://simonwillison.net/2026/Nov/10/yonkers-rises/"
    author: "Simon Willison"
    date: "2026-11-10"
---

# Yonkers Rises: Prompting an LLM to Build a Three.js Mech Animation

Simon Willison built a small tool called Yonkers Rises after realizing he didn't know where Yonkers is located. He looked it up on Google Maps, then prompted Claude Fable 5.2 Medium to create a Three.js animation in which Yonkers rises up as a giant mech and stomps around Manhattan, Queens, and Brooklyn, using OpenStreetMap mapping data (https://simonwillison.net/2026/Nov/10/yonkers-rises/).

The prompt contained a mobile keyboard typo, "átomos," which the model correctly interpreted as "stomps." The experiment served two purposes: embedding the location and shape of Yonkers in the author's memory, and testing the 3D modeling and animation capabilities of Claude Fable 5.2.

- LLMs can generate working Three.js 3D animations from a single natural-language prompt.
- The model inferred intent from a typo ("átomos" → "stomps"), showing robustness to noisy input.
- OpenStreetMap data can be combined with generated code to render real-world geography.
- Prompting for a playful visualization is a technique for learning geography.