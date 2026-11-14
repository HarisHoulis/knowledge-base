---
domain: system-design
subdomain: api-versioning
concept: date-based-api-versioning
title: Google Cloud Moves the Compute Engine API to Immutable Date-Based Versions
sources:
  - title: "Google Cloud Moves the Compute Engine API to Immutable Date-Based Versions"
    url: "https://www.infoq.com/news/2026/11/compute-engine-api-versioning/"
    author: "Steef-Jan Wiggers"
    date: "2026-11-14"
---

# Google Cloud Moves the Compute Engine API to Immutable Date-Based Versions

Google Cloud has made date-based versioning of the Compute Engine API generally available, replacing the single mutable /v1 surface with immutable quarterly snapshots such as 2026-09-01. Callers select a version per request via a header or query parameter, so new versions can change defaults, error formats, and IAM checks without affecting existing /v1 callers.

The model mirrors approaches used by Azure Resource Manager and Stripe, which have relied on immutable, date-stamped API versions for years. The core idea is that a version identifier pins behavior: once a snapshot is published, its semantics stay fixed, and evolution happens by introducing new snapshots rather than mutating the existing surface.

This decouples provider-side changes from client-side breakage, letting Google evolve defaults and security checks on its own schedule while consumers upgrade deliberately.

- Compute Engine API now offers immutable quarterly date-based versions (e.g. 2026-09-01) alongside /v1.
- Version is selected per request via a header or query parameter.
- New versions can alter defaults, error formats, and IAM checks without impacting /v1 callers.
- The pattern follows Azure Resource Manager and Stripe's long-standing date-based versioning.