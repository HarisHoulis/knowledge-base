---
domain: system-design
subdomain: infrastructure-as-code
concept: plan-time-unknown-values
title: OpenTofu 1.13 Lets Module Authors Reduce Unknown Values at Plan Time
sources:
  - title: "OpenTofu 1.13 Lets Module Authors Reduce Unknown Values at Plan Time"
    url: "https://www.infoq.com/news/2026/10/opentofu-1-13-unknown-values/"
    author: "Mark Silvester"
    date: "2026-10-26"
---

# OpenTofu 1.13 Lets Module Authors Reduce Unknown Values at Plan Time

OpenTofu 1.13 introduces new functions that let module authors provide type and value hints for values that are unknown during planning, allowing more expressions to resolve at `tofu plan` time rather than being deferred to apply (InfoQ, Mark Silvester).

The mechanism centers on `convert` and `assume` functions, which supply the planner with type and value information for otherwise-unknown values. This reduces the amount of deferred evaluation, producing more complete plans.

Because the hints are assumptions rather than guarantees, OpenTofu validates them: if a value that was unknown during planning later violates a stated guarantee, an error is reported during apply.

- OpenTofu 1.13 adds `convert` and `assume` functions for supplying type and value hints to the planner.
- More expressions can resolve during `tofu plan` instead of being deferred to apply.
- Guarantees made about unknown values are checked, with violations surfacing as apply-time errors.