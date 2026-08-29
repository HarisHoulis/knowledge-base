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

Molecule is a Compose-based library for managing application state, originally announced by Cash App. Version 1.0 is now stable and introduces two major features: support for Kotlin multiplatform targets (JVM, JS, and native) and an immediate recomposition mode that removes the need to supply a frame clock. These features enable state-producing composables to be separated from UI-rendering composables, increasing reuse across platforms and destinations.

- Molecule 1.0 is the first stable release, adding Kotlin multiplatform support and immediate recomposition mode.
- State logic written in Compose can be exposed as StateFlow for use in existing View-based Android apps.
- Immediate mode recomposes on state changes, making it suitable for presenter-like use cases without UI frame timing.
- The library supports all Kotlin targets supported by JetBrains Compose runtime, enabling unit tests on JVM and usage on iOS/web.
- Unit testing is simplified with Turbine, as shown with a counter example.