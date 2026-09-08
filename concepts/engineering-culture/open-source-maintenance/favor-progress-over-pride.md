---
domain: engineering-culture
subdomain: open-source-maintenance
concept: favor-progress-over-pride
title: Favor Progress Over Pride in Open Source
sources:
  - title: "Favor Progress Over Pride in Open Source"
    url: "https://kentcdodds.com/blog/favor-progress-over-pride-in-open-source"
    author: "Kent C. Dodds"
    date: "2020-08-24"
---

# Favor Progress Over Pride in Open Source

Kent C. Dodds discusses the decision to deprecate his popular open-source library glamorous in favor of emotion, which he considered objectively better. He emphasizes that when a superior solution with a reasonable migration path emerges, maintainers should prioritize community health over personal pride. The post presents a framework for handling situations where another contributor solves the same problem better, suggesting collaboration or deprecation rather than competitive duplication. Dodds argues that maintaining multiple poorly differentiated solutions fragments community effort and forces users into unnecessary decisions, while deprecation frees maintainers and users to move on to new problems. He addresses nuances such as disagreement over superiority, difficult migrations, inability to collaborate, and commercial products, ultimately recommending that maintainers add documentation notes or deprecate when a better alternative exists.

- When a objectively better solution with a reasonable migration path exists, deprecate your own project and direct users to the alternative.
- Competitive duplicating efforts fragments the community and wastes effort on multiple solutions to the same problem.
- Deprecation is a gift: it frees maintainers to work on new problems and ensures users get the best solution.
- If migration is hard, continue maintaining but document the superior alternative so new users start with the better choice.
- Sunk cost of contributor effort should not justify continuing an inferior project when a better alternative is available.