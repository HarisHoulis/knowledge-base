---
domain: android-kotlin
subdomain: state-management
concept: molecule-stable-release
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule 1.0, a Compose-based library for managing application state, has been released as a stable version. Originally announced two years ago, it now supports Kotlin multiplatform targets including JVM, JS, and native, in addition to Android. The library also introduces an immediate recomposition mode, which triggers recomposition whenever there are new changes to produce, eliminating the need for a frame clock in certain scenarios. These features allow state-producing composables to be reused across different platforms and contexts, such as exposing state as a StateFlow for Views or as a Flow for testing and multiplatform rendering. The article demonstrates a counter composable that increments every second, which can be launched via launchMolecule in ContextClock mode to produce a StateFlow, or via moleculeFlow in Immediate mode to produce a Flow. The examples show how this enables unit testing with Turbine on the JVM and web/DOM usage on JS, highlighting Molecule's versatility in separating state logic from UI rendering.

- Molecule 1.0 is a stable, multiplatform library for managing application state using Compose.
- It supports JetBrains Compose runtime targets: JVM, JS, native, and Android.
- Immediate recomposition mode produces new values as soon as state changes, useful for presenter-style logic.
- State-producing composables can be exposed as StateFlow or Flow, enabling integration with Views, unit testing, and web platforms.
- Unit tests can be written with Turbine and run on the JVM.