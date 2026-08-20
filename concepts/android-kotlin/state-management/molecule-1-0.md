---
domain: android-kotlin
subdomain: state-management
concept: molecule-1-0
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule 1.0 is a stable release of Cash App's Compose-based library for managing application state. The article highlights two major features added since the initial announcement: Kotlin multiplatform support (JVM, JS, native) and an immediate recomposition mode that removes the need for a frame clock. These features enable state-producing composables to be used outside of Compose UI, such as in Views, notifications, or widgets, by exposing state as a StateFlow or Flow.

The article demonstrates how a simple counter composable can be migrated to a StateFlow using launchMolecule with ContextClock mode, or to a Flow using moleculeFlow with Immediate mode. This allows state logic to be unit tested with Turbine on the JVM, and run on platforms like iOS or web. Molecule is positioned as a tool for managing state using Compose across multiplatform projects.

- Molecule 1.0 supports Kotlin multiplatform targets including JVM, JS, and native.
- Immediate recomposition mode allows state production without relying on a frame clock.
- State-producing composables can be exposed as StateFlow for use in non-Compose contexts.
- Flow-based state can be unit tested with Turbine on the JVM.
- Molecule enables state reuse across platforms like iOS and web.