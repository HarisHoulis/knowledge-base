---
domain: java-tools
subdomain: kotlin-jvm-compilation
concept: case-insensitive-class-collision
title: Case-insensitive filesystems considered harmful (to me)
sources:
  - title: "Case-insensitive filesystems considered harmful (to me)"
    url: "https://jakewharton.com/case-insensitive-filesystems-considered-harmful-to-me/"
    author: "Jake Wharton"
---

# Case-insensitive filesystems considered harmful (to me)

Jake Wharton describes a recurring problem with case-insensitive filesystems when building Kotlin/JVM projects. While developing against Jetpack Compose sources, he encountered CI test failures on macOS and Windows workers caused by a NoClassDefFoundError involving two class names differing only by capitalization: CompositionTests$testInsertOnMultipleLevels$1$Item$1 and CompositionTests$testInsertOnMultipleLevels$1$item$1. On case-insensitive filesystems, these two distinct class files collide and one overwrites the other, producing a corrupt classpath.

Wharton identifies the root cause in Compose's test code: two nested functions, one named `Item` and another named `MockViewValidator.item`, each contain a lambda. The Kotlin compiler mangles these lambdas' generated class names with the enclosing function's name, producing files that are identical except for case. A case-sensitive filesystem stores both separately, but the default macOS/Windows filesystems treat them as the same file, so the later output overwrites the earlier one. The upstream fix renamed the second extension function to `validateItem` to eliminate the near-identical class name.

He argues this is a compiler-level bug: the Kotlin compiler should mangle otherwise unnamed lambda class names more aggressively to avoid case-insensitive collisions. He provides a minimal reproducer with top-level classes `Hey` and `hey` that clobber each other, and he filed JetBrains issue KT-47123. The post calls for tools to be more robust across both case-sensitive and case-insensitive filesystems.

- On case-insensitive filesystems, Kotlin-generated class files that differ only by case can overwrite each other, causing runtime NoClassDefFoundError.
- A real-world example occurred in Jetpack Compose sources, where nested functions `Item` and `MockViewValidator.item` generated colliding class names with lambda suffixes.
- The upstream fix renamed one function (`item` to `validateItem`), but Wharton argues the Kotlin compiler should prevent such collisions by further mangling names.
- A minimal reproducer: defining top-level `class Hey` and `class hey` yields only one `.class` file on a case-insensitive filesystem.
- Wharton filed JetBrains issue KT-47123 about this issue.