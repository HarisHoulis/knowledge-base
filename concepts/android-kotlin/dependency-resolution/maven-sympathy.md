---
domain: android-kotlin
subdomain: dependency-resolution
concept: maven-sympathy
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

Jake Wharton argues that while Gradle's dependency resolution picks the newest version by default, Maven's strategy of 'nearest definition' and first-declaration-wins can select older transitive versions. This creates a compatibility trap for Maven consumers of libraries built with Gradle. For example, if a library declares an older version of a dependency than what its own transitive dependencies request, Maven may choose the older version, leading to runtime errors like NoSuchMethodException.

Gradle users can inadvertently create this problem because their tests run with the newest resolved version, not the declared one. The article explores solutions: using Gradle's versionMapping to publish resolved versions, enabling failOnVersionConflict() to detect mismatches, or writing a custom task that fails when direct dependencies are upgraded transitively. The author provides a Groovy snippet for such a task and encourages making it a plugin.

The core message is that library maintainers using Gradle need to sympathize with Maven consumers and take steps to ensure published dependency versions are consistent, since Maven's resolution behavior is not intuitive.

- Maven's dependency resolution selects the nearest version in the tree, not the newest, and first declaration wins at equal depth, leading to surprising older-version choices.
- Gradle-built libraries can contain transitive conflicts invisible to Gradle's newest-wins resolution, but which cause Maven consumers to fail at runtime.
- Techniques like versionMapping, failOnVersionConflict(), and custom checks can help align declared and resolved versions before publishing.
- The author proposes a custom task that checks if first-order dependencies were upgraded transitively as a simple Maven-sympathy solution.