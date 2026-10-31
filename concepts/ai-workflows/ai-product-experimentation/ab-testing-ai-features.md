---
domain: ai-workflows
subdomain: ai-product-experimentation
concept: ab-testing-ai-features
title: Why A/B Testing AI Features Is Weird: Lessons from Bumble's AI Photo Feedback
sources:
  - title: "78% Wanted This AI Feature. Almost Nobody Used It - Supriya Subudhi, Bumble"
    url: "https://www.youtube.com/watch?v=CvmZtAPmAW4"
    author: "AI Engineer"
    date: "2026-10-31"
---

# Why A/B Testing AI Features Is Weird: Lessons from Bumble's AI Photo Feedback

Supriya Subudhi, a product manager at Bumble (a dating app with over 20 million monthly active users), argues that a positive A/B test result is only the beginning when evaluating AI features, not the end. She illustrates this with Bumble's AI-powered photo feedback feature, which gives users AI-generated advice on improving their dating profile photos.

The first pitfall: users ask for a feature and then ignore it. In discovery research, almost 78% of users said they wanted feedback and advice on improving their profiles, but when Bumble ran an A/B test where 50% received the feature, only 10-15% actually used it. Openness to AI does not predict usage. The fix was to integrate the AI journey into existing user flows—prompting for feedback when users add photos or when they struggle to find matches—rather than creating a separate feature users had to discover.

The second pitfall: average wins mask problems. Overall results looked great—more people added photos and made more profile changes than the control group—but detailed inspection revealed the AI advised people to smile more even when they were already smiling. A positive average is no longer sufficient to measure success; teams must dig into the details. She also contrasts error tolerance across domains: bad AI-generated song picks in a Spotify-style AI DJ are acceptable, but errors in a banking app that advises on budgets are far more serious.

- 78% of surveyed users said they wanted AI profile feedback, but only 10-15% used it when shipped—stated interest doesn't predict adoption
- Embedding AI features into existing user flows (e.g., prompting when adding photos) drove adoption better than a standalone feature
- Positive average metrics can hide quality failures; detailed review caught the AI telling already-smiling users to smile more
- Acceptable AI error rates depend on domain stakes—low for music recommendations, high for financial advice