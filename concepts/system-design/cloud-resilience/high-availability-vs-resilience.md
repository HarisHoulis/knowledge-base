---
domain: system-design
subdomain: cloud-resilience
concept: high-availability-vs-resilience
title: High Availability Is Not Resilience: Why Cloud Systems Fail When It Matters Most
sources:
  - title: "High Availability Is Not Resilience: Why Cloud Systems Fail When It Matters Most"
    url: "https://www.infoq.com/articles/high-availability-not-resilience-cloud/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Alexey Golev"
    date: "Thu, 01 Oct 2026 09:00:00 GMT"
---

# High Availability Is Not Resilience: Why Cloud Systems Fail When It Matters Most

Alexey Golev argues that high availability (HA) and resilience are distinct problems in cloud systems. A routine TLS 1.3 upgrade silently broke Route 53 health checks, causing a CDN to stop routing traffic to a healthy region while internal dashboards showed nothing wrong (Golev, 2026).

The article links such failures to control-plane dependencies that create invisible failure modes. Because these dependencies are not reflected in normal monitoring, a system can appear healthy while its actual traffic-routing or recovery paths are broken (Golev, 2026).

Golev also notes that recovery capability erodes without explicit ownership, implying resilience requires ongoing organizational responsibility rather than reliance on HA alone (Golev, 2026).

- HA and resilience are different problems; a highly available system can still fail when it matters most.
- Control-plane dependencies, such as Route 53 health checks, can create invisible failure modes.
- Internal dashboards may show nothing wrong even when a CDN stops routing traffic to a healthy region.
- Recovery capability erodes without explicit ownership.