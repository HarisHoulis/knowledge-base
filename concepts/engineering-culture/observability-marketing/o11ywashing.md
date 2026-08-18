---
domain: engineering-culture
subdomain: observability-marketing
concept: o11ywashing
title: From Cloudwashing to O11ywashing
sources:
  - title: "From Cloudwashing to O11ywashing"
    url: "https://charity.wtf/p/from-cloudwashing-to-o11ywashing"
    author: "Charity Majors"
    date: "2025-11-24"
---

# From Cloudwashing to O11ywashing

In this post, Charity Majors recounts a panel of engineering executives who believe traditional observability tools are only useful for detecting whether systems are up or down. One executive explained that they had built a custom solution to measure key workflows through startup payment and success, because they wanted to observe service quality from each customer's perspective. Majors argues that this reveals a profound misunderstanding: the executive is describing the original definition of observability without realizing it, while dismissing what are actually just monitoring tools as 'traditional observability.' She compares this to cloudwashing, where IBM reclassified mainframes as 'cloud' in 2008, and notes that vendors are now similarly rebranding monitoring as observability (o11ywashing) to capture large budgets. The problem persists because traditional vendors cannot solve the core need: combining app, business, and system telemetry in a unified, traceable way to understand customer experience per customer. Majors urges the observability community to communicate in terms of business outcomes to engineering executives, not just technical details. She concludes with a litmus test: if your tooling doesn't help you understand the quality of your product from each customer's perspective, it isn't observability, just monitoring dressed up in marketing dollars.

- Traditional 'observability' tools are often just monitoring: they answer whether systems are up/down but not how individual customers experience the product.
- The original definition of observability includes understanding each customer's perspective, which requires unified traceable data across app, business, and system telemetry.
- O11ywashing is the rebranding of monitoring as observability, analogous to cloudwashing, and is fueled by large budgets and unsolved problems.
- To win, advocates must tell stories to engineering executives using results and outcomes, not just technical details like cardinality and dimensionality.
- A simple test: if your observability tooling cannot help you see product quality from each customer's perspective, it is not observability.