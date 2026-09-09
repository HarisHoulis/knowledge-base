---
domain: android-kotlin
subdomain: android-testing
concept: android-testing-tools
title: The Resurrection of Testing for Android
sources:
  - title: "The Resurrection of Testing for Android"
    url: "https://developer.squareup.com/blog/the-resurrection-of-testing-for-android"
    author: "Jake Wharton"
---

# The Resurrection of Testing for Android

This article by Jake Wharton on Square's blog addresses the historical difficulty of testing Android applications, caused in part by the Android API jar containing only stubs that throw RuntimeException("Stub!") for every method. Robolectric solves this by replacing those empty jars with real Android framework code, allowing unit tests to exercise actual code paths. The article demonstrates that simply annotating a test class with @RunWith(RobolectricTestRunner.class) is enough to enable layout inflation, view/activity creation, and UI interaction in local JVM tests. (Source: The Resurrection of Testing for Android, Square Engineering blog)

The post also covers Spoon, a tool that automates running instrumentation tests across multiple connected devices and aggregates results and screenshots. This gives a visual, cross-device view of app behavior. For assertions, the article introduces FEST Android, a fluent assertion API that yields more readable test code and far more descriptive failure messages than raw JUnit assertEquals or assertTrue calls. Together, these three libraries enable more efficient testing across both unit and instrumentation levels, increasing confidence in the code and enabling faster iteration. (Source: The Resurrection of Testing for Android, Square Engineering blog)

- Android's API jars are empty stubs, so Robolectric is needed to run real framework code in unit tests.
- Adding @RunWith(RobolectricTestRunner.class) enables local unit tests for Android views and activities.
- Spoon automates instrumentation tests on multiple devices and aggregates screenshots for visual insight.
- FEST Android provides fluent assertions with context-rich failure messages, improving test readability and debuggability.
- These tools together make Android testing more practical, boosting confidence and development speed.