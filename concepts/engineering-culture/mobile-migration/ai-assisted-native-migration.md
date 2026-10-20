---
domain: engineering-culture
subdomain: mobile-migration
concept: ai-assisted-native-migration
title: Why Shopify Migrated From React Native
sources:
  - title: "Why Shopify Migrated From React Native"
    url: "https://blog.bytebytego.com/p/why-shopify-migrated-from-react-native"
    author: "ByteByteGo"
    date: "2026-10-20"
---

# Why Shopify Migrated From React Native

Shopify adopted React Native in 2020 to avoid implementing every feature twice in Kotlin and Swift, to let developers move between platforms, and to maintain feature parity across iOS and Android (ByteByteGo). The framework carried ongoing costs, though: the team spent effort optimizing React Native performance, contributing to framework upgrades, and managing external dependency changes, while native code offered tighter platform synergy and fewer dependency layers.

By 2025, coding agents had shifted the economics. Shopify rebuilt core parts of its app in Swift and Kotlin as prototypes and found agents could take an implementation on one platform as a reference and write the equivalent for the other, with developers verifying conventions and architecture. Duplication concerns no longer outweighed the benefits of native development, so Shopify chose a greenfield migration, shipping the shopper-facing Shop app first and the 300+ screen merchant app later.

To run the migration, Shopify built Helix, which breaks a large feature into small, reviewable checkpoints in a sensible order, each gated by behavioural tests, visual review against the React Native reference, adversarial code reviews, and a final developer review. Because Shopify keeps business logic independent of the UI and exposes app state and actions through a headless CLI, agents can navigate and assert on state without parsing screenshots, making behavioural checks fast.

The Shop app shipped natively in 12 weeks: iOS startup dropped from 3200 ms to about 2400 ms, Android from about 4400 ms to 2200 ms, crash-free sessions rose, and Android app size fell from 293 MB to 184 MB. The takeaway is that a fast feedback loop for validating agent-generated code is what makes a large migration safe.

- React Native's 2020 rationale (no duplicate implementations, shared developers, feature parity) weakened once coding agents made cross-platform native implementation cheap
- Shopify chose greenfield over brownfield because the existing React Native app served as a strong reference and fresh native builds proved faster
- Helix decomposes migration into small reviewable checkpoints gated by behavioural tests, visual review, adversarial code review, and developer review
- Separating business logic from UI and exposing state/actions via a headless CLI lets agents run fast behavioural checks instead of screenshot parsing
- Results: Shop app native in 12 weeks, Android startup roughly halved, higher crash-free sessions, Android app size down from 293 MB to 184 MB