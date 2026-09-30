---
domain: ai-workflows
subdomain: ai-assisted software development
concept: ai-code-review-bottleneck
title: The Death of Code Review and the AI Verification Bottleneck
sources:
  - title: "The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI"
    url: "https://www.youtube.com/watch?v=_mi3alkqy4s"
    author: "Laurie Voss"
    date: "2026-09-30"
---

# The Death of Code Review and the AI Verification Bottleneck

AI agents have made code generation much faster while verification remains human-paced, creating a bottleneck. A study of over 100,000 GitHub developers found that those using autonomous agents wrote 741% more code but released only 30% more software; the authors attribute this gap to verification [1]. The path to production still runs through human steps, especially code review, and checking trustworthiness remains expensive for sensitive code [1].

Human review capacity is limited. A two-decade-old Cisco study processing 2,500 inspections and 3.2 million lines found reviewers stop finding bugs effectively after about 400 lines in one review or 450 lines per hour; a 10,000-line agent PR could therefore require three to four business days for full human review, and one developer can run many agents at once [1].

Responses range from adding test-only roles—which fails due to burnout and limited human capacity—to removing humans from the code-writing loop. Peter Steinberger argues developers should design agent loops rather than prompt code, and Andrej Karpathy argues a human in the cycle slows the system [1]. OpenAI reported building an internal product with no hand-written code: starting from an empty repository, agents produced about one million lines and roughly 1,500 merged pull requests with only three engineers over five months [1].

- Autonomous agents caused 741% more code to be written but only 30% more software to be released, pointing to verification as the bottleneck.
- Human review effectiveness drops after about 400 lines in one review or 450 lines per hour; a 10,000-line agent PR could take three to four business days to review.
- Some advocates propose removing humans from the code-writing loop, instead designing agent loops and excluding oneself from the development cycle.
- OpenAI reported an internal product built without handwritten code: agents produced roughly one million lines and about 1,500 merged PRs with three engineers in five months.