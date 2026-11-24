---
domain: system-design
subdomain: mobile-analytics
concept: view-agnostic-analytics
title: How LinkedIn Built a View-Agnostic Analytics System for Modern iOS UI Architectures
sources:
  - title: "How LinkedIn Built a View-Agnostic Analytics System for Modern iOS UI Architectures"
    url: "https://www.infoq.com/news/2026/11/linkedin-view-agnostic-analytics/"
    author: "Sergio De Simone"
    date: "2026-11-23"
---

# How LinkedIn Built a View-Agnostic Analytics System for Modern iOS UI Architectures

LinkedIn engineers addressed a problem introduced by modern iOS UI systems: the logical UI structure no longer necessarily mirrors the native UIKit hierarchy, which breaks analytics tooling that assumes a direct mapping between views and tracked elements. Their solution is a view-agnostic analytics system built around a shared MeasurableNode contract (InfoQ, Sergio De Simone).

The MeasurableNode abstraction decouples analytics from any specific rendering framework, so instrumentation can describe logical UI elements independently of how they are realized in UIKit. This lets the same analytics model work across differing UI architectures without depending on the native view tree.

By standardizing on a common contract, LinkedIn gains consistent measurement of user interactions even as UI frameworks evolve, avoiding analytics logic tightly coupled to a particular view implementation.

- Modern iOS UI architectures can decouple logical UI structure from the native UIKit hierarchy, breaking view-based analytics.
- LinkedIn introduced a shared MeasurableNode contract to make analytics view-agnostic.
- The abstraction decouples instrumentation from any specific rendering framework or view tree.
- This enables consistent interaction measurement as UI architectures evolve.