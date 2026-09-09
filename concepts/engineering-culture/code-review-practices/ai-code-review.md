---
domain: engineering-culture
subdomain: code-review-practices
concept: ai-code-review
title: What is happening with code reviews?
sources:
  - title: "What is happening with code reviews?"
    url: "https://newsletter.pragmaticengineer.com/p/what-is-happening-with-code-reviews"
    author: "Gergely Orosz"
    date: "Tue, 08 Sep 2026 16:32:01 GMT"
---

# What is happening with code reviews?

The article discusses how AI agents generating large volumes of code have overwhelmed traditional code review processes, leading CTOs and engineering leaders to experiment with new review strategies. It notes that the number of pull requests on GitHub increased fivefold over three years, with growth accelerating sharply after late 2025, when AI agents became widely used for code generation. Teams are responding with approaches such as having humans review AI-generated review comments, triaging changes by risk (low-risk changes skip human review while high-risk changes require it), reviewing plans/tests/database schemas instead of implementation details, and producing smaller PRs to ease review.

- AI code generation has led to a massive influx of PRs, forcing teams to rethink code review.
- Common approaches include AI-generated reviews with human oversight, risk-based triage, and reviewing plans/tests/schemas instead of implementation.
- Some companies like Duckbill Group have dropped most human code review, relying on risk-based labeling, stronger guardrails, and increased test coverage.
- Noise from AI code review tools is a key challenge; custom tooling like Uber's uReview filters low-confidence comments.
- There is little evidence of companies entirely removing human review; even optimistic adopters keep humans in the loop for merges or high-risk changes.