---
domain: java-tools
subdomain: parameterized-testing
concept: testparameterinjector-migration
title: Migrating from Burst to TestParameterInjector
sources:
  - title: "Migrating from Burst to TestParameterInjector"
    url: "https://code.cash.app/migrating-from-burst-to-testparameterinjector"
    author: "Jake Wharton"
---

# Migrating from Burst to TestParameterInjector

Square's Burst library, introduced in 2014, allowed JUnit 4 tests to be parameterized by enum values, reducing boilerplate and enabling test variation across themes, sizes, and settings in Cash App. Although Burst remained stable, Google's TestParameterInjector library was released in 2021 as a successor that subsumes Burst's approach and adds support for more types and dynamically generated data, leading Square to deprecate Burst and migrate codebases.

- TestParameterInjector replaces Burst for JUnit 4-based projects, requiring only small changes: swap the runner and annotate parameters with @TestParameter.
- Burst's @Burst field annotation is replaced by @TestParameter for Java tests, and constructor/method parameters need @TestParameter added.
- TestParameterInjector supports more parameter types and dynamic data generation beyond Burst's enum-based approach.
- For Android instrumentation tests, TestParameterInjector currently only works on API 26 and newer.