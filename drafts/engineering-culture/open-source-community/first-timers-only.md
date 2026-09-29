---
domain: engineering-culture
subdomain: open-source-community
concept: first-timers-only
title: First Timers Only
sources:
  - title: "First Timers Only"
    url: "https://kentcdodds.com/blog/first-timers-only"
    author: "Kent C. Dodds"
    date: "2015-08-04"
---

# First Timers Only

Kent C. Dodds, maintainer of angular-formly, describes making his open source project contributor-friendly through a CONTRIBUTING.md file, organized code, an up-for-grabs label, a githook running tests and eslint, npm scripts, and screencasts. Despite this, he realized something was still missing for newcomers (https://kentcdodds.com/blog/first-timers-only).

After Koen Weyn submitted his first ever GitHub pull request, Dodds tried an experiment: he wrote tests for a new feature, used `describe.skip` from Mocha so the build would not fail, and posted an issue with exact instructions. He shared it on Twitter, Gitter, and Slack, and Stephen Bluck completed it as his first open source contribution. Dodds repeated this approach several more times and created a first-timers-only label for such issues (https://kentcdodds.com/blog/first-timers-only).

Dodds argues that the hard part of getting into open source is not implementing a feature, but figuring out how to contribute. He acknowledges he could finish features faster himself, but finds it rewarding to help newcomers, and notes that PRs are often submitted and merged within a few hours. He urges maintainers to add the first-timers-only label, reference makeapullrequest.com, and help bring kindness back to open source (https://kentcdodds.com/blog/first-timers-only).

- Maintainers can lower barriers by providing CONTRIBUTING.md, labeled issues, pre-commit checks, npm scripts, and screencasts.
- The first-timers-only label explicitly marks issues suitable for newcomers and helps them find a way to contribute.
- The hardest part for first-time contributors is often learning how to contribute, not implementing the feature itself.
- Letting someone else implement a feature you could do yourself can create first-time contributors and still result in quick merges.
- Dodds asks maintainers to add the first-timers-only label and promote kindness in open source.