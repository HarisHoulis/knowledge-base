---
domain: android-kotlin
subdomain: kotlin-optimization
concept: intermediate-collection-avoidance
title: Intermediate collection avoidance
sources:
  - title: "Intermediate collection avoidance"
    url: "https://jakewharton.com/intermediate-collection-avoidance/"
    author: "Jake Wharton"
---

# Intermediate collection avoidance

The article cautions that this technique only benefits when the source list supports random access. For linked or persistent lists, performance would be abysmal, so it's best used on internal lists where the backing structure is known or controlled.

- Fuse map with terminal operations like joinToString to avoid intermediate collections.
- Use Array(size) or MutableList(size) initializer lambdas to transform data efficiently.
- The lambda initializer variants are faster and allocate less memory, as shown in benchmarks.
- Only use these techniques on random-access sources; otherwise performance degrades.