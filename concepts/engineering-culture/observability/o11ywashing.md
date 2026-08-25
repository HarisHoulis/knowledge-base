---
domain: engineering-culture
subdomain: observability
concept: o11ywashing
title: From Cloudwashing to O11ywashing
sources:
  - title: "From Cloudwashing to O11ywashing"
    url: "https://charity.wtf/p/from-cloudwashing-to-o11ywashing"
    author: "Charity Majors"
    date: "Mon, 24 Nov 2025 18:53:14 GMT"
---

# From Cloudwashing to O11ywashing

In this article, Charity Majors criticizes how the term 'observability' has been watered down by vendors and misused by executives. She recounts a panel where an executive described traditional observability tools as capable of detecting faults but insufficient for understanding the quality of service from each customer's perspective, which he claimed required custom tooling. Majors argues that this is exactly the original definition of observability, and that such execs are unknowingly describing the problem observability should solve, not a new one (Majors, 2025).

Majors introduces the term 'o11ywashing' as the observability equivalent of 'cloudwashing', where vendors relabel legacy monitoring tools as observability. She draws parallels to IBM reclassifying mainframes as cloud in 2008, and argues that the o11ywashing problem will persist because traditional vendors cannot solve the underlying technical challenge of combining app, business, and system telemetry in a unified, cardinality-rich way. She emphasizes that observability is a systems problem, not just operational monitoring, and that the industry needs to communicate this to engineering executives in terms of outcomes, not technical details (Majors, 2025).

- Traditional 'observability' tools are often just monitoring, and they cannot answer product-quality questions from each customer's perspective.
- The term 'o11ywashing' describes vendors falsely labeling monitoring as observability, similar to cloudwashing.
- Observability is fundamentally a systems problem; it requires unified telemetry and the ability to slice by any dimension, such as customer ID or device.
- To combat o11ywashing, the industry must focus on telling executives about outcomes, not just technical features.
- If your tooling does not help you understand the quality of your product from each customer's perspective, it is not observability.