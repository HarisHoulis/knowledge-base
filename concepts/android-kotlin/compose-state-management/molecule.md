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

Molecule is a Compose-based library for managing application state, now releasing its first stable version 1.0. The library has gained two major features since its announcement: support for Kotlin multiplatform targets (JVM, JS, and native) and an immediate recomposition mode that removes the need for a frame clock. These features enable state-producing composables to run outside the context of Compose UI, exposing plain data as StateFlow or Flow for use in Views, notifications, widgets, or other platforms.

- Molecule 1.0 is stable and supports Kotlin multiplatform targets including JVM, JS, and native.
- Immediate recomposition mode triggers recomposition on state changes without requiring a frame clock.
- State logic can be exposed as StateFlow to Android Views or as Flow for reactive consumption.
- Molecule enables unit testing of state composables using Turbine on the JVM.
- It runs on any platform supported by the JetBrains Compose runtime, such as iOS SwiftUI or web DOM.