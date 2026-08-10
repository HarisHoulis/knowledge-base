---
domain: engineering-culture
subdomain: observability-marketing
concept: o11ywashing
title: From Cloudwashing to O11ywashing
sources:
  - title: "From Cloudwashing to O11ywashing"
    url: "https://charity.wtf/p/from-cloudwashing-to-o11ywashing"
    author: "Charity Majors"
    date: "Mon, 24 Nov 2025 18:53:14 GMT"
---

# From Cloudwashing to O11ywashing

Charity Majors argues that the term "observability" has been co-opted by vendors and executives in a manner analogous to "cloudwashing"—where marketing paints traditional monitoring tools as true observability. She recounts a panel where an executive described traditional observability as merely detecting uptime/downtime, missing that the real goal is understanding the quality of service from each customer's perspective. Majors contends that this is the original definition of observability, and that standard metrics, logs, and traces are not sufficient; true observability requires unifying app, business, and system telemetry, sliced by customer ID or device. [1]

The article draws a parallel to IBM's 2008 "cloudwashing" of its mainframe, and warns that observability is now facing the same fate because it is a large budget item. Majors emphasizes that the problem is not going away, and that Gartner-type analysts will only help after the industry wins the market. She calls for engineers to tell the story of observability to executives in terms of business outcomes, not technical details like cardinality. [1]

Ultimately, Majors states bluntly: if your tooling doesn't help you understand the product from each customer's perspective, "it isn't fucking observability." It is just monitoring dressed up in marketing dollars, or "o11ywashing." [1]

- Traditional observability tools (metrics, logs, traces) are monitoring, not true observability.
- Observability means understanding quality of service from each customer's perspective, requiring unified telemetry.
- O11ywashing is the new cloudwashing: vendors rebranding monitoring as observability.
- Engineers must communicate observability value to executives in terms of outcomes, not technical structures.
- A litmus test: if tooling can't slice by customer ID and show experience, it's not observability.