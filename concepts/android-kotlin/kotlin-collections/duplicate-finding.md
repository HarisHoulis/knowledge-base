---
domain: android-kotlin
subdomain: kotlin-collections
concept: duplicate-finding
title: Perils of duplicate finding
sources:
  - title: "Perils of duplicate finding"
    url: "https://jakewharton.com/perils-of-duplicate-finding/"
---

# Perils of duplicate finding

The article explores how to find duplicate integers in a Kotlin array, driven by the need to prevent a user from specifying a reserved value twice. It starts with a straightforward map-based approach using `groupBy` and `filterValues`, which works but seems wasteful. The author then attempts more concise alternatives using collection operations like `minus` and `removeAll`, only to discover surprising behaviors: both `minus` and `removeAll` remove *all* occurrences of each element in the supplied collection, not just one occurrence per element, leading to incorrect results. This behavior is inherited from Java's `Collection.removeAll`.

- `List.minus(collection)` and `MutableList.removeAll(collection)` remove all occurrences of each element in the collection, not just the first, making them unsuitable for finding duplicates.
- `MutableSet.add` returns `false` for elements already seen, enabling a clean duplicate-detection idiom with `filterNot`.
- Using `filterNotTo(HashSet(), HashSet<Int>()::add)` is the most efficient and minimal-allocation approach among the tested methods.
- Kotlin's `minus` and `removeAll` behavior is inherited from Java's `Collection.removeAll`.