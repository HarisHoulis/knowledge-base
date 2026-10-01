---
domain: system-design
subdomain: cloud-infrastructure
concept: container-apps-express
title: Azure Container Apps Express and Sandboxes Reach GA
sources:
  - title: "Container Apps Express Reaches GA on a Newly Generally Available Sandbox Layer"
    url: "https://www.infoq.com/news/2026/10/container-apps-express-sandboxes/"
    author: "Steef-Jan Wiggers"
    date: "2026-10-01"
---

# Azure Container Apps Express and Sandboxes Reach GA

Microsoft has made Azure Container Apps Express generally available alongside Container Apps Sandboxes, the microVM compute layer it runs on [1]. Express is positioned as a simplified way to run containers without the overhead of environment provisioning, and it scales to zero when idle [1].

Startup is subsecond, achieved through prewarmed pools [1]. The trade-off is a reduced feature set: custom domains, zone redundancy, Key Vault references, OpenTelemetry, and Dapr are not supported in Express [1].

- Azure Container Apps Express is now generally available, together with the underlying Container Apps Sandboxes microVM compute layer [1].
- Express skips environment provisioning and can scale to zero [1].
- Subsecond startup is enabled by prewarmed pools [1].
- Express does not support custom domains, zone redundancy, Key Vault references, OpenTelemetry, or Dapr [1].