---
domain: engineering-culture
subdomain: observability
concept: o11ywashing
title: From Cloudwashing to O11ywashing
sources:
  - title: "From Cloudwashing to O11ywashing"
    url: "https://charity.wtf/p/from-cloudwashing-to-o11ywashing"
    author: "Charity Majors"
    date: "2025-11-24"
---

# From Cloudwashing to O11ywashing

In this post, Charity Majors recounts a panel where an executive claimed that traditional observability tools work for operational availability but fail to capture customer experience from each customer's perspective, leading them to build custom tooling. Majors argues that this executive is describing the original definition of observability without realizing it, and that what they call "traditional observability" is actually monitoring—the three pillars of metrics, logs, and traces. She introduces the term "o11ywashing" to describe how vendors rebrand monitoring as observability, analogous to cloudwashing in cloud computing (Charity Majors, 2025).

Majors emphasizes that observability is a systems problem, requiring a unified combination of application, business, and system telemetry, not siloed operational tools. She stresses the need to communicate this to engineering executives in terms of outcomes and business results, rather than technical details like cardinality and dimensionality. She concludes that if tooling does not help understand the quality of the product from each customer's perspective, it is not observability—just monitoring dressed up in marketing dollars (Charity Majors, 2025).

- The term "traditional observability" as used by execs often actually means monitoring (metrics, logs, traces), which is insufficient for understanding customer experience.
- Observability must combine app, business, and system telemetry in a unified way to slice by customer ID, site location, device ID, etc.
- O11ywashing is the new cloudwashing: vendors rebranding monitoring as observability to capture budget.
- To win, observability advocates must tell the story to engineering executives in terms of outcomes, not just technical details.
- If your tooling doesn't help you understand each customer's perspective, it isn't observability—it's monitoring.