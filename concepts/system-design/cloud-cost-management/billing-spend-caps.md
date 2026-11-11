---
domain: system-design
subdomain: cloud-cost-management
concept: billing-spend-caps
title: Google Cloud Spend Caps Reach General Availability with API and Monthly Resets
sources:
  - title: "Google Cloud Spend Caps Reach General Availability with API and Monthly Resets"
    url: "https://www.infoq.com/news/2026/11/google-cloud-spend-caps/"
    author: "Steef-Jan Wiggers"
    date: "2026-11-10"
---

# Google Cloud Spend Caps Reach General Availability with API and Monthly Resets

Google Cloud has made spend caps on Cloud Billing Budgets generally available, allowing teams to pause new usage of a service in a project once a monthly budget is reached without deleting existing resources. The GA release adds an API, estimated live costs, and automatic monthly resets of the cap.

Coverage is limited: caps apply only to the Gemini API, the Agent Platform, Cloud Run, and Cloud Run functions. Overage incurred during enforcement delays is still billed, so the cap is a guardrail rather than a hard financial ceiling.

- Spend caps pause new service usage at the monthly budget threshold without deleting resources
- GA adds an API, estimated live costs, and automatic monthly resets
- Only Gemini API, Agent Platform, Cloud Run, and Cloud Run functions are covered
- Usage during enforcement delays is still billed