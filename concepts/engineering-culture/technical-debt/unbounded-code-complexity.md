---
domain: engineering-culture
subdomain: technical-debt
concept: unbounded-code-complexity
title: There's No Limit to How Bad Code Can Get
sources:
  - title: "There's No Limit to How Bad Code Can Get"
    url: "https://zachkehs.com/blog/theres_no_limit_to_how_bad_code_can_get/#9-ref"
    author: "Zach Kehs"
  - title: "Quoting Zach Kehs"
    url: "https://simonwillison.net/2026/Sep/6/zach-kehs/"
    author: "Simon Willison"
    date: "2026-09-06"
---

# There's No Limit to How Bad Code Can Get

Zach Kehs draws an analogy between physical buildings and software: while a building will collapse if you keep adding floors and rooms indefinitely, software faces no such physical constraint. Consequently, code can always get worse—there can always be another layer of indirection or a reduction in performance ([Kehs, via Simon Willison](https://simonwillison.net/2026/Sep/6/zach-kehs/)).

This observation highlights that software complexity is not self-limiting; without deliberate effort, technical debt can accumulate without bound. It underscores the importance of proactive refactoring, code review, and architectural discipline to counteract the natural tendency toward degradation ([original post](https://zachkehs.com/blog/theres_no_limit_to_how_bad_code_can_get/#9-ref)).

- Software lacks the physical constraints of buildings, so code quality can degrade indefinitely.
- Every added layer of indirection or performance reduction makes the code worse.
- Technical debt must be actively managed because there is no natural limit to complexity.