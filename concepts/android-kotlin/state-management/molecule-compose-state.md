---
domain: android-kotlin
subdomain: state-management
concept: molecule-compose-state
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule is a Compose-based library for managing application state, originally announced two years ago. The 1.0 release adds Kotlin multiplatform support (JVM, JS, native) and an immediate recomposition mode, making it more flexible for non-UI contexts. The library allows state-producing composables to run outside Compose UI, exposing results as StateFlow or Flow for use in views, notifications, widgets, and other targets.

- Molecule 1.0 supports Kotlin multiplatform targets, including JVM, JS, and native.
- Immediate recomposition mode triggers recomposition on state changes without a frame clock.
- State logic can be migrated to Compose early and exposed to Views via StateFlow.
- Flow-based state simplifies unit testing with Turbine on the JVM.
- Works across platforms like iOS (SwiftUI) and web (DOM) using the Compose runtime.