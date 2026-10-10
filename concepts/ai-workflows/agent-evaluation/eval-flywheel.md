---
domain: ai-workflows
subdomain: agent-evaluation
concept: eval-flywheel
title: Why 80% Reliability Isn't Good Enough: Closing the Customer Feedback Loop in Agent Evaluation
sources:
  - title: "Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab"
    url: "https://www.youtube.com/watch?v=Emo5FGGY-wM"
    author: "AI Engineer"
    date: "2026-10-09"
---

# Why 80% Reliability Isn't Good Enough: Closing the Customer Feedback Loop in Agent Evaluation

Felipe Blanes, a technical specialist at the Amazon AGI Lab, describes the "benchmark illusion": teams optimize against public benchmarks and self-generated synthetic data, then release to production where customers immediately do unexpected things and break the product. Because static scores leave you with nothing to do after release but hope the numbers reflect reality, the gap between benchmark performance and real-world reliability goes undetected. Blanes traces this to a standard development process — gather requirements, build, run evals, release — that treats evaluation as a one-time gate rather than an ongoing loop.

To close that gap, the lab proposes an evaluation flywheel, a repeating cycle rather than a static score. The first step is defining success, and crucially the definition must come from the customer, not from the team's own assumptions. The second step is collecting signals: engineers instinctively reach for metrics and toolkits, but Blanes stresses that you must also talk to customers, make appointments, attend them, and understand what problem they are actually trying to solve, because raw data can be misleading.

The third step is gap diagnosis, where signals from toolkits, observations, and customer meetings are classified into categories to identify where the product falls short. The talk's framing is that the answer is not better benchmarks but a closed feedback loop with the customer, which is what allows reliability to improve beyond the 80% that benchmarks alone can certify.

- Optimizing for public or synthetic benchmarks creates a "benchmark illusion": customers do unexpected things in production and break the product.
- Static evaluation scores leave teams with only hope after release; the fix is a repeating evaluation flywheel that closes the customer feedback loop.
- Success must be defined by what the customer considers success, not by the team's own criteria.
- Collecting signals requires both metrics/toolkits and direct customer conversations, since data alone can be misleading.
- Gap diagnosis classifies collected signals to pinpoint where the product actually falls short.