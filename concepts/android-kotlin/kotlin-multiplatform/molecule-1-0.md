---
domain: android-kotlin
subdomain: kotlin-multiplatform
concept: molecule-1-0
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule, a Compose-based library for managing application state, has reached its first stable version 1.0. Originally announced two years ago for Android, the library now supports Kotlin multiplatform targets including JVM, JS, and native, alongside Android. It also introduces an immediate recomposition mode that removes the need for a frame clock, allowing state-producing composables to run outside UI rendering contexts.

- Molecule 1.0 is the first stable release of the Compose-based state management library.
- Adds support for Kotlin multiplatform targets (JVM, JS, native) in addition to Android.
- Immediate recomposition mode triggers recomposition immediately on state changes without a frame clock.
- State logic can be exposed as StateFlow or Flow, enabling unit testing with Turbine on the JVM.
- Allows reuse of Compose state logic across Android Views, notifications, widgets, iOS, and web DOM.