---
domain: android-kotlin
subdomain: compose-state-management
concept: molecule-1-0-stable
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule is a Compose-based library for managing application state, and it has reached its first stable release with version 1.0. This release adds two major features: support for Kotlin multiplatform targets (JVM, JS, and native) in addition to Android, and an immediate recomposition mode that triggers whenever new changes are produced, removing the need for a frame clock. These features make Molecule more flexible for separating state-producing composables from UI-rendering composables, as demonstrated by the counter example in the article (source: https://code.cash.app/molecule-1-0).

The article shows how pure Compose UI apps can separate state logic into composables like counter(), which can then be exposed as a StateFlow via launchMolecule(mode = ContextClock) for use with traditional Views, notifications, widgets, or other non-Compose destinations. Alternatively, using moleculeFlow(mode = Immediate) exposes the state as a Flow that emits values immediately on state changes, enabling simple unit testing with Turbine on the JVM. Since Molecule runs on every Kotlin multiplatform target supported by the JetBrains Compose runtime, the same state logic can be reused on iOS targeting SwiftUI, on the web targeting the DOM, and in other environments, making Compose-based state management broadly applicable across platforms (source: https://code.cash.app/molecule-1-0).

- Molecule 1.0 is the first stable release and now supports Kotlin multiplatform targets (JVM, JS, native) alongside Android.
- Immediate recomposition mode allows Molecule to produce state changes without relying on a frame clock, emitting values as soon as state changes occur.
- State-producing composables can be exposed as StateFlow or Flow, enabling integration with View-based apps, notifications, widgets, and other output destinations.
- Unit testing is simplified by combining Molecule flows with Turbine, and these tests can run on the JVM.
- Molecule works on all JetBrains Compose runtime targets, making state management reusable across iOS, web, and other platforms.