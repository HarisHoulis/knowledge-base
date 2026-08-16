---
domain: android-kotlin
subdomain: language-evolution
concept: java-19-report-card
title: Report card: Java 19 and the end of Kotlin
sources:
  - title: "Report card: Java 19 and the end of Kotlin"
    url: "https://jakewharton.com/report-card-java-19-and-the-end-of-kotlin/"
    author: "Jake Wharton"
    date: "2022-09-20"
---

# Report card: Java 19 and the end of Kotlin

In his 2019 talk, Jake Wharton predicted what Java 19 would look like. This article grades those predictions against the actual Java 19 release. Local methods (predicted to be a feature) were never realized, receiving an F. Multiline strings, records, and sealed interfaces were delivered as expected, earning A grades. Pattern matching for instanceof was delivered in Java 16 and is in preview for switch, but lacks some anticipated syntax, earning a C. Virtual threads just made it into preview with a B grade (Wharton, 2022).

Despite the title's implication, Kotlin did not end. Kotlin continued to evolve with features like context receivers and sealed interfaces. Wharton concludes that Java and Kotlin both thrive, and he encourages developers to update to Java 19 immediately, noting that the latest JDK is always the best long-term version (Wharton, 2022). The article serves as a retrospective on language evolution and the unpredictability of feature timelines.

- Local methods never made it into Java, failing the prediction.
- Multiline strings, records, and sealed interfaces were delivered as expected.
- Pattern matching and record destructuring are still in preview, with some gaps.
- Virtual threads arrived in preview, marking a significant step for concurrency.
- Kotlin survived and continued evolving, so the 'end of Kotlin' prophecy was wrong.