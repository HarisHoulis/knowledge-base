---
domain: android-kotlin
subdomain: android-development-tools
concept: simulator-over-emulator
title: Android Needs A Simulator, Not An Emulator
sources:
  - title: "Android Needs A Simulator, Not An Emulator"
    url: "https://jakewharton.com/android-needs-a-simulator/"
---

# Android Needs A Simulator, Not An Emulator

In this article, Jake Wharton argues that Android development lacks a true simulator and that existing emulator approaches are fundamentally inadequate for day-to-day work. He acknowledges the improvements made by Google's x86 emulator with HAXM and third-party Genymotion, but says these are still only incremental improvements. The official emulator configuration defaults to slow ARM emulation and disables GPU acceleration, and running instances remain resource-heavy, prone to hanging, and hard to manage.

Wharton proposes a simulator that sits between the Android runtime and the host operating system, similar to Apple's iOS simulator. Because Android apps are compiled to JVM bytecode before being dexed and packaged into an APK, a simulator could let developers run an exploded app directly on the JVM after only a resource scan and javac. This would dramatically shorten the development loop. He points to Robolectric and layoutlib as evidence that key Android pieces can run on the JVM, but neither is designed to host a full app during development.

The article also enumerates challenges a full simulator would need to overcome, such as faking Android framework internals, mapping app components and system services to the JVM, and handling graphics, sensors, and multi-process behavior. These are solvable but require significant sustained effort, and Wharton notes the Android tools team needs to invest in building and maintaining such a simulator.

- Existing emulator solutions are slow by default and difficult to manage; Genymotion improves on them but has licensing and reliability issues.
- A simulator could execute Android apps directly on the host JVM, reducing the development cycle to resource scanning, javac, and classpath loading.
- Robolectric and layoutlib prove that Android code can run as JVM code, but neither is sufficient for running development apps end-to-end.
- Building a true Android simulator requires solving hard problems around framework simulation, app components, and OS services, and needs dedicated tooling investment.