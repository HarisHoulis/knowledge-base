---
domain: system-design
subdomain: modular-monolith
concept: modular-monolith-framework
title: Agoda Reduces API Code Review Time by 64% with Modular Architecture
sources:
  - title: "Agoda Reduces API Code Review Time by 64% with Modular Architecture"
    url: "https://www.infoq.com/news/2026/11/agoda-modular-monolith-framework/"
    author: "Leela Kumili"
    date: "2026-11-23"
---

# Agoda Reduces API Code Review Time by 64% with Modular Architecture

Agoda introduced a modular monolith framework in its post-booking API to reduce coupling without undertaking a full rewrite. The approach relies on domain components, Data Mapper patterns, typed builders, and ArchUnit tests to enforce architectural boundaries between modules.

Measured against legacy changes, framework-backed changes showed a 64% shorter median code review time and 34% faster initial feedback. The results suggest that enforcing modular boundaries within a monolith can meaningfully improve developer workflow without the cost of migrating to a distributed architecture.

- Modular monolith reduced coupling in Agoda's post-booking API without a full rewrite.
- Domain components, Data Mapper, typed builders, and ArchUnit tests enforce module boundaries.
- Framework-backed changes had 64% shorter median code reviews and 34% faster initial feedback than legacy changes.