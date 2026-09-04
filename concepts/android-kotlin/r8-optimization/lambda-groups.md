---
domain: android-kotlin
subdomain: r8-optimization
concept: lambda-groups
title: R8 Optimization: Lambda Groups
sources:
  - title: "R8 Optimization: Lambda Groups"
    url: "https://jakewharton.com/r8-optimization-lambda-groups/"
    author: "Jake Wharton"
---

# R8 Optimization: Lambda Groups

R8, Android's code shrinker and optimizer, merges Kotlin lambdas that share the same 'shape' into a single synthetic class called a lambda group, reducing the number of classes in the APK. In the example, two Kotlin lambdas filtering an Employee sequence in EmployeeRepository are combined into one `-$$LambdaGroup$ks$...` class with an integer id to discriminate behavior and a single Object capture field, as described in Jake Wharton's post. This happens despite the lambdas capturing different types (LocalDate vs Employee), because each captures exactly one value and implements the same functional interface.

- R8 merges Kotlin lambdas of the same shape into a single synthetic 'lambda group' class, reducing class count.
- The merged class uses an integer id and an Object capture field to dispatch among the original lambda bodies.
- This optimization works even when lambdas capture different concrete types, as long as the number and kind of captures fit a common shape.
- Java lambdas are not yet merged into lambda groups; the feature is tracked in Issue 153773246.
- Merging is package-local by default but can be made global with `-allowaccessmodification`.