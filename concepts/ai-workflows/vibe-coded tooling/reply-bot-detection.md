---
domain: ai-workflows
subdomain: vibe-coded tooling
concept: reply-bot-detection
title: Bluesky reply bot checker
sources:
  - title: "Bluesky reply bot checker"
    url: "https://simonwillison.net/2026/Sep/27/bluesky-bot-check/"
    date: "2026-09-27"
---

# Bluesky reply bot checker

Automated reply bots, described as a "scourge" on Twitter, have started manifesting on Bluesky as well. The author, who attracts a swarm of them due to a decent follower count, notes that unlike Twitter, Bluesky still has a freely available and useful API. The lack of such an API doesn't slow the bots down, but it does make investigating them much more frustrating.

To address this, the author had Opus 5.5 vibe code a tool, the Bluesky reply bot checker, which examines any Bluesky profile for evidence of a likely reply bot. The tool looks for signals such as replies posted within seconds of other posts from the same account, or accounts that never post their own content (or images or links) but instead consistently reply to messages from other, higher-follower users.

It also looks for question marks, because the author is extra infuriated by reply bots that waste his time answering a question no human ever posed.

- Reply bots are a familiar problem on Twitter and are now appearing on Bluesky.
- Bluesky's freely available API makes bot investigation easier than on Twitter, though its absence on Twitter doesn't slow the bots themselves.
- The checker tool was vibe coded with Opus 5.5 (via a pull request to the author's tools repo).
- Detection signals include: replies posted seconds after other posts from the same account, accounts that only reply rather than posting their own content/images/links, and targeting of higher-follower users.
- Question marks are also used as a signal, flagging bots that pose questions no human asked.