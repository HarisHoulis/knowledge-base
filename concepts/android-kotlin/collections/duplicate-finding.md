---
domain: android-kotlin
subdomain: collections
concept: duplicate-finding
title: Perils of duplicate finding
sources:
  - title: "Perils of duplicate finding"
    url: "https://jakewharton.com/perils-of-duplicate-finding/"
---

# Perils of duplicate finding

The article explores different approaches to finding duplicate elements in a Kotlin collection, highlighting subtle pitfalls in the standard library. The author's initial attempts using `toList() - toSet()` and `MutableList.removeAll` both incorrectly remove all occurrences of each element, not just the first, due to behavior inherited from Java. The correct approach involves using a `HashSet`'s `add` method as a predicate with `filterNot`, keeping elements that are already in the set. The `filterNotTo` variant is shown to be both the most readable and the most performant, avoiding unnecessary intermediate collections and allocations.

- Kotlin's `minus` operator with a collection removes all occurrences of each element, not just one.
- `MutableList.removeAll` also removes all occurrences, matching Java's `Collection.removeAll` behavior.
- `set.add` returns `false` if the element is already present, making it a clean predicate for detecting duplicates.
- `filterNotTo(HashSet(), HashSet<Int>()::add)` is the fastest and allocates the fewest bytes.