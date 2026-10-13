---
domain: engineering-culture
subdomain: version-control-infrastructure
concept: centralized-source-control-at-scale
title: Redesigning Source Control at Anthropic
sources:
  - title: "Redesigning source control at Anthropic"
    url: "https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic/"
    author: "Simon Willison"
    date: "2026-10-13"
---

# Redesigning Source Control at Anthropic

Anthropic's code change volume grew dramatically in 2026, from around 2,500 merged changes per day in May to over 30,000 per day by September. Simon Willison notes that the public release dates of Anthropic's models (not internal availability) appear on the chart he modified, and speculates that Fable/Mythos class models were a key factor in the increased coding velocity.

To handle this scale, Anthropic built a new source control system called Scion, which Willison describes as sounding like a reinvention of centralized source control along the lines of Subversion. The requirements were extreme: the main branch history alone is almost 100 GB, a compressed working copy exceeds 25 GB, and the company performs on the order of 25 million code checkouts per day for CI, which would amount to over 600 PB of git traffic per day if fetched naively. A team of seven people built the system, and the migration from Git was completed in five months.

Anthropic also uses a code review system called "Antique" and makes extensive use of adversarial review, where a model tries to find flaws in the work. Willison relates this to his own experience playing Claude and GPT off against each other for adversarial review. He notes the article's observation that adversarial review, while effective, can be myopic, requiring skilled engineers to steer Claude away from over-engineering parts of the system in response to hypothetical concerns.

- Anthropic's merged code changes grew from ~2,500/day in May 2026 to over 30,000/day by September 2026
- Scion, their new source control system, resembles a reinvention of centralized source control like Subversion, built by a team of seven in five months
- Scale requirements include ~100 GB main branch history, 25+ GB compressed working copies, and ~25 million daily CI checkouts (600+ PB/day of naive git traffic)
- Adversarial review is highly effective but can be myopic, requiring engineers to prevent over-engineering in response to hypothetical concerns