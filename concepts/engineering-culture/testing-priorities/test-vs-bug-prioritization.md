---
domain: engineering-culture
subdomain: testing-priorities
concept: test-vs-bug-prioritization
title: Should I write a test or fix a bug?
sources:
  - title: "Should I write a test or fix a bug?"
    url: "https://kentcdodds.com/blog/should-i-write-a-test-or-fix-a-bug"
    date: "2020-06-15"
---

# Should I write a test or fix a bug?

The article argues that writing automated tests is no different from any other engineering task: it competes for limited time and must be evaluated on the cost of doing nothing and the benefit of getting it done. The author stresses that deciding to do one thing first does not mean you will never do the other; it is about relative urgency (KentC.Dodds.com, 2020).

Several scenarios illustrate this thinking. A bug that only affects users without an avatar wanting to change their bio is low impact, so adding tests to a checkout flow—which could break and cost money—should take precedence. Conversely, a startup running out of money and not yet selling a useful product should skip testing and focus on shipping; only if broken code ruins demos should you invest in a few quick E2E tests for common demo paths (KentC.Dodds.com, 2020).

The key takeaway is to treat testing as a gift that keeps giving, but not as a universal absolute. Prioritize consciously based on risk, business stage, and the potential harm of doing nothing, rather than defaulting to either always testing or never testing (KentC.Dodds.com, 2020).

- Treat tests as one of many tasks, not an automatic requirement.
- Evaluate cost/benefit: what happens if you don’t test now, and what is the payoff of doing it now?
- Critical flows without coverage (e.g., checkout) often justify testing over fixing low-impact bugs.
- When time is limited, skip tests to ship the product, but add minimal E2E tests if stability is blocking demos.
- Tests are a long-term investment, but prioritization still depends on context.