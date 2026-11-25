---
domain: engineering-culture
subdomain: code-review-and-verification
concept: formal-verification-over-code-review
title: The End of Code Review: Formal Verification as a Replacement for PR Checks
sources:
  - title: "The End of Code Review"
    url: "https://www.youtube.com/watch?v=UA3qEfR11zM"
    author: "Kent C. Dodds"
    date: "2026-11-24"
---

# The End of Code Review: Formal Verification as a Replacement for PR Checks

Kent C. Dodds argues that traditional PR-based code review is becoming untenable because AI agents write code faster than humans can read diffs. He notes that adding more review bots doesn't solve the problem: each additional bot tends to find something new, so flawed code still slips through, especially in large PRs. He points to teams like the AMP team that already commit directly to main and deploy, relying on tests rather than PR review.

The proposed alternative is formal verification, a roughly 60-year-old technique now made more accessible by recent advances. Rather than testing selected inputs, formal verification means writing down exactly what the code is supposed to do and letting a machine prove it does so for every possible input. Unlike 100% test coverage, which can still ship bugs, a proof mathematically confirms the implementation matches the specification.

The catch is that a proof only confirms what was specified: a wrong specification yields a green light for the wrong behavior. So specification review becomes the critical human step, replacing line-by-line code review. Dodds frames formal verification as the bridge from a reviewed specification to an implementation that provably matches it, and cites tools like Bend and interest from GitHub's Copilot and Grokbot teams as signs this is becoming practical.

- Agents write code faster than humans can read diffs, making PR review a bottleneck.
- Adding more review bots doesn't guarantee correctness—each bot tends to find something new.
- Formal verification proves code matches a specification for all possible inputs, unlike tests that cover only chosen cases.
- A proof only validates the specification, so reviewing the spec becomes the critical human checkpoint.
- Tools like Bend and interest from GitHub Copilot and Grokbot teams are making formal verification more accessible.