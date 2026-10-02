---
domain: ai-workflows
subdomain: code-verification
concept: visual-regression-verification
title: Why AI Didn't Actually Make You Ship Faster: Verification as the New Bottleneck
sources:
  - title: "Why AI Didn't Actually Make You Ship Faster — Gabriel Spencer-Harper, Meticulous"
    url: "https://www.youtube.com/watch?v=HLTa7Vcs4X0"
    author: "AI Engineer"
    date: "2026-10-02"
---

# Why AI Didn't Actually Make You Ship Faster: Verification as the New Bottleneck

Gabe Spencer-Harper, co-founder and CEO of Meticulous, argues that the limiting factor on AI-assisted development is no longer code generation but verification: "AI writes code faster than humans can test it," so verification and validation have become the new bottleneck (Gabe Spencer-Harper). When an AI opens a pull request, most organizations would not dare press merge without doing the hard work of checking functional flags, roles, permissions, settings, configurations, and edge cases to understand the full impact of the change.

Assertion-based tests alone cannot close that gap, he claims, because no matter how thoroughly a person or an agent tries to predetermine correct behavior through assertions, the space of possible states is too large to cover completely (Gabe Spencer-Harper). This produces three consequences: errors or regressions with business consequences; engineering teams spending a double-digit percentage of their time supporting end-to-end test suites (manually checking, reviewing, debugging flaky tests, and maintaining the suite); and the lost opportunity — with exhaustive verification you could program in new ways, updating all dependencies, doing large-scale refactors, and merging any AI-generated change with complete confidence.

Meticulous is presented as that verification layer. It is installed as a single line of JavaScript in non-production environments (localhost, QA, development, staging) that instruments the browser and records thousands of user workflows, such as clicking the login button, the settings panel, or the analytics panel (Gabe Spencer-Harper). On a pull request, the CI runner replays a subset of those recorded workflows against the running app, sending events one by one and taking a screenshot at each point in time, producing a screenshot sequence for the pre-change and post-change code.

Those two sequences are compared and surfaced as before/after comparisons in a comment on the merge request, typically within a few minutes, showing what will change in the application if the code is merged — including across light and dark mode, and including multiple manifestations of the same logical error (Gabe Spencer-Harper). Rather than encoding expected behavior in assertions, the tool shows only what changed and leaves the judgment call to the developer or an agent during review. The service is used by engineering teams at Discord, Dropbox, Notion, ElevenLabs, and LaunchDarkly.

- AI writes code faster than humans can test it, making verification and validation the new bottleneck rather than code generation.
- Assertion-based tests are insufficient because the space of possible application states is too large to fully predetermine through assertions.
- Three consequences of the status quo: business-impacting regressions, double-digit percentages of engineering time spent maintaining and debugging end-to-end test suites, and the inability to safely do large refactors or bulk dependency updates.
- Meticulous records real user workflows via a single line of non-production JavaScript, replays them in CI on each pull request, and posts before/after screenshot comparisons so reviewers decide whether a change is expected.
- Exhaustive verification is framed as an enabler of new ways of programming: merging AI-generated changes, dependency updates, and large-scale refactors with complete confidence.