---
domain: engineering-culture
subdomain: code-review
concept: code-review-alignment
title: How to Kill the Code Review
sources:
  - title: "How to Kill the Code Review"
    url: "https://www.youtube.com/watch?v=YgEv7IQzGdM"
    author: "AI Engineer"
    date: "2026-08-17"
---

# How to Kill the Code Review

The speaker, Ankit Jain, argues that traditional code review is failing under the increasing volume of code. He cites 861% code churn, a rising incident-to-PR ratio, increasing median review time, and over 30% of changes merged without any review, indicating the current process is both a bottleneck and ineffective. With AI writing and reviewing code, the human role becomes questionable; when AI reviews and nobody reads, the system is misconfigured. Code review was only formalized around 2006 with Google's Mondrian, but its true purpose goes beyond catching bugs and security issues to include alignment: knowledge sharing, mentorship, architectural feedback, and onboarding. The speaker concludes that while semantic accuracy can be improved with better tooling, alignment must survive as a human collaboration element. He also critiques spec-driven development as resembling the waterfall model with no feedback loop, and suggests that interactive agent sessions are still needed because specs are inherently incomplete and issues are discovered during implementation.

- Traditional code review is failing: 861% code churn, rising incidents-to-PR ratio, longer review times, and over 30% of changes merged without review.
- When AI writes and reviews code, and humans merely skim, the process is misconfigured.
- Code review provides not just quality checks but also alignment through knowledge sharing, mentorship, architectural feedback, and onboarding.
- Semantic accuracy can be automated, but alignment requires human collaboration.
- Spec-driven development is a linear waterfall model lacking a feedback loop; interactive agent sessions reveal the need for iterative refinement.