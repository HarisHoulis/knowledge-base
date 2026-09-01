---
domain: android-kotlin
subdomain: compose-state-management
concept: molecule
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule is a Compose-based library for managing application state, originally announced two years ago. Today, version 1.0 is released as its first stable version. The library has gained two major features since its initial announcement: support for Kotlin multiplatform targets (JVM, JS, and native) in addition to Android, and an immediate recomposition mode that removes the need for a frame clock. These features make Molecule more flexible for separating state management from UI rendering.

- Molecule 1.0 is stable and supports Kotlin multiplatform targets (JVM, JS, native) plus Android.
- It allows state-producing composables to run outside Compose UI, exposing results as StateFlow for use in View-based apps, notifications, and widgets.
- The immediate recomposition mode triggers recomposition when there are new changes, which is useful for presenter-like usage.
- Unit testing is simplified by exposing composable logic as Flow and testing with Turbine on the JVM.
- Molecule can be used across platforms, e.g., running the same counter logic on web (DOM) or iOS with SwiftUI.