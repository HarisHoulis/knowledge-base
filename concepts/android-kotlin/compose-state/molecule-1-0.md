---
domain: android-kotlin
subdomain: compose-state
concept: molecule-1-0
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule 1.0 is a stable release of Cash App's Compose-based library for managing application state. The stable version adds support for Kotlin multiplatform targets (JVM, JS, native) in addition to Android, and introduces an immediate recomposition mode that removes the need for a frame clock. These features allow state-producing composables to be reused outside Compose UI, such as exposing them as StateFlow to Views or other destinations (Molecule 1.0, para. 2).

By separating state logic into composables, developers can migrate logic to Compose early while keeping View-based UIs. The immediate mode is useful when using Molecule as a presenter, as it recomposes whenever there are pending changes. Unit testing becomes simpler when the output is a Flow, testable with Turbine on the JVM. Multiplatform support means the same state logic can run on web (DOM) or iOS (SwiftUI) (Molecule 1.0, para. 5).

- Molecule 1.0 is stable and supports Kotlin multiplatform (JVM, JS, native) in addition to Android.
- Immediate recomposition mode triggers on pending changes, removing reliance on a frame clock.
- State-producing composables can be exposed as StateFlow for use with Views, notifications, widgets, and more.
- Output as Flow enables straightforward unit testing with Turbine on JVM.
- Multiplatform support allows running the same state logic on web and iOS.