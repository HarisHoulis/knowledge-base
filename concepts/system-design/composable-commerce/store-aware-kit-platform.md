---
domain: system-design
subdomain: composable-commerce
concept: store-aware-kit-platform
title: Composable Commerce: Inside Shipt's Kit Platform
sources:
  - title: "Composable Commerce: Inside Shipt's Kit Platform"
    url: "https://www.infoq.com/articles/shipt-composable-commerce-design-ddd/"
    author: "Khurshid Hameed"
    date: "2026-10-14"
---

# Composable Commerce: Inside Shipt's Kit Platform

Shipt introduced a Kits feature that lets merchandisers quickly assemble themed grocery bundles for events, replacing a previously labor-intensive workflow. The platform is designed so merchandisers can easily create store-aware kits, meaning the bundles reflect what is actually available at a given store rather than a generic catalog [source: InfoQ article].

The architecture rests on a flexible model of items, shopping lists, and kits. This separation allows kits to be composed from reusable primitives while still displaying accurately based on local inventory and customer needs [source: InfoQ article].

By making kits store-aware, the platform addresses the mismatch between centrally defined bundles and per-store availability. The result is a composable commerce approach that streamlines merchandising operations and improves the accuracy of what customers see [source: InfoQ article].

- Shipt's Kits feature enables quick assembly of themed grocery bundles for events.
- The platform lets merchandisers create store-aware kits, replacing a labor-intensive workflow.
- A flexible model of items, shopping lists, and kits ensures accurate display based on local inventory and customer needs.