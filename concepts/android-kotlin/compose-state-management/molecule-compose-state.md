---
domain: android-kotlin
subdomain: compose-state-management
concept: molecule-compose-state
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule is a Compose-based library for managing application state, originally announced two years ago. With the release of version 1.0, it gains support for Kotlin multiplatform targets (JVM, JS, and native) in addition to Android, as well as an immediate recomposition mode that eliminates the need for a frame clock. These features enable state-producing composables to be separated from UI-rendering composables, increasing reuse across different platforms and destinations.

- Molecule 1.0 adds Kotlin multiplatform support (JVM, JS, native) and an immediate recomposition mode.
- State logic can be written as composables and exposed to existing View-based Android apps as StateFlow, easing migration to Compose UI.
- The immediate mode allows Molecule to be used as a presenter, producing values whenever state changes, independent of UI frame clocks.
- Unit testing is simplified through integration with Turbine, and tests can run on any supported platform.
- Molecule is now stable and targeted at managing state in Compose-based applications across platforms.