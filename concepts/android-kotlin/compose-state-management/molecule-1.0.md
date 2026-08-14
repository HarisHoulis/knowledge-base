---
domain: android-kotlin
subdomain: compose-state-management
concept: molecule-1.0
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule 1.0 is a stable release of a Compose-based library for managing application state. Originally announced two years ago, it now supports Kotlin multiplatform targets (JVM, JS, and native) in addition to Android, and introduces an immediate recomposition mode. These features allow state-producing composables to be separated from UI-rendering composables, increasing reuse in View-based Android apps by exposing state logic as StateFlow or Flow. The immediate mode triggers recomposition whenever there are new changes, which is useful for presenter-like logic and simplifies unit testing with Turbine on the JVM. Multiplatform support enables running the same state logic across iOS, web, and other targets, as demonstrated by the article's example of updating a DOM element from a coroutine in Kotlin/JS.

- Molecule 1.0 adds Kotlin multiplatform support and an immediate recomposition mode.
- State-producing composables can be exposed as StateFlow or Flow, facilitating integration with existing View-based UIs and non-UI destinations.
- Immediate mode allows state logic to be tested independently with Turbine, running on JVM.
- Multiplatform support enables state logic to run on JVM, JS, and native targets, increasing code reuse and testability.