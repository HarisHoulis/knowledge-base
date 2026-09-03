---
domain: engineering-culture
subdomain: code-review
concept: rethinking-code-review
title: Maybe We Shouldn't Be Reviewing All This Code
sources:
  - title: "Maybe We Shouldn't Be Reviewing All This Code"
    url: "https://martinfowler.com/rachels-ramblings/code-review.html"
    author: "Rachel Laycock"
---

# Maybe We Shouldn't Be Reviewing All This Code

Rachel Laycock responds to Brian Houck's defense of code review in an era of AI-generated code. She argues that code review has become overloaded with responsibilities—quality assurance, knowledge transfer, mentoring, architectural alignment, and collective ownership—and that waiting until a completed pull request to address these is too late. Laycock advocates shortening feedback loops by moving feedback closer to the decision it informs, using pairing, team design sessions, trunk-based development, and automated checks like static analysis and fitness functions.

- Rather than automating code review, teams should question why the ceremony exists and move important conversations earlier (pairing, design sessions).
- AI increases code volume dramatically—Meta saw 106% more lines per human-landed diff and median PR size grew 64%—making mandatory human review a bottleneck.
- Human review still matters for high-risk changes: security-sensitive boundaries, large blast radius, unfamiliar critical systems, or low team confidence.
- Teams should build collective understanding through shared practices, because 'we need engineers to understand systems, not diffs.'