---
domain: android-kotlin
subdomain: gradle
concept: properties-and-providers
title: Understanding Gradle #34 – Properties and Providers
sources:
  - title: "Understanding Gradle #34 – Properties and Providers"
    url: "https://www.youtube.com/watch?v=n8Tgr4aLB18"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-08-31T04:56:30+00:00"
---

# Understanding Gradle #34 – Properties and Providers

The video explains the concepts of Property and Provider in Gradle, which were introduced to enable lazy configuration and better compatibility with Gradle's configuration model. Properties are typed container objects that hold configurable values, such as DirectoryProperty, and are used in extensions and tasks to avoid direct field access, allowing Gradle to track dependencies and configuration state. Providers are streams of values that can be queried and transformed, offering methods like map() and flatMap() for derived values and enabling 'provider-friendly' APIs that work seamlessly with Gradle's lazy evaluation.

The video demonstrates how to use DirectoryProperty as a task input, how to access properties from extensions, and how to combine providers using map() and flatMap() to compute values reactively. It also covers optional providers (without values), accessing providers during configuration time, handling FileCollections, and lists the supported property types. The key takeaway is that using properties and providers improves build performance and reliability by deferring calculations until needed and avoiding eager evaluation at configuration time.

- Properties (e.g., DirectoryProperty) are used as typed configuration containers in tasks and extensions, replacing direct field access to support lazy configuration.
- Providers allow you to model values that can be computed on demand, with map() and flatMap() for transforming and chaining dependent values.
- Gradle's APIs are provider-friendly, enabling you to wire inputs and outputs without explicit evaluation at configuration time.
- Providers can represent values with or without a value (optional), and it's important to know when to access them during configuration.
- The video covers supported property types and shows how to use them in both Kotlin and Groovy DSLs.