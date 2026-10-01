---
domain: engineering-culture
subdomain: mobile engineering strategy
concept: shopify-native-mobile
title: Why has Shopify dropped React Native?
sources:
  - title: "Why has Shopify dropped React Native?"
    url: "https://newsletter.pragmaticengineer.com/p/shopify-native-mobile"
    author: "Gergely Orosz"
    date: "Tue, 29 Sep 2026 15:53:19 GMT"
---

# Why has Shopify dropped React Native?

Shopify announced that “Native is now the future of mobile development” after six years of betting on React Native. In 2020, the company moved to React Native primarily to speed Android launches and share code across iOS and Android; by 2025 it reported that all six mobile apps had been migrated, with fast screen loads, hot reloading, and TypeScript enabling cross-platform developer mobility (The Pragmatic Engineer).

The reversal is driven by AI coding agents. Shopify’s Head of Mobile, Mustafa Ali, said coding models have improved enough that “building the same feature in Swift and Kotlin no longer carries the cost it used to,” and agents now handle enough implementation, translation, testing, and review that sharing implementation is no longer the deciding factor. Native keeps Shopify closer to platform capabilities and first-party tooling with fewer framework and dependency layers (The Pragmatic Engineer).

Shopify had also migrated major apps to React Native’s New Architecture, but reported only modest gains: about 10% faster Android startup, 3% on iOS, and some complex screens became slower until tuned. The article situates the move in a broader mobile debate: Airbnb previously abandoned React Native for native performance, Notion has pursued a long native migration, and Kotlin Multiplatform offers shared business logic while keeping each platform native (The Pragmatic Engineer).

- Shopify moved to React Native in 2020 to unify iOS and Android development and launch Android versions faster; by 2025 it said six apps were migrated and the transition was successful.
- In 2026, Shopify announced a return to native, citing AI coding agents that reduce the cost of building and maintaining separate Swift and Kotlin implementations.
- Mustafa Ali said agents now do enough implementation, translation, testing, and review work that React Native’s shared-implementation advantage no longer outweighs native’s platform proximity.
- React Native’s New Architecture brought only modest performance gains, with app startup improving about 10% on Android and 3% on iOS, and some complex screens slowing until tuned.
- The article compares the shift to prior reversals like Airbnb’s move back to native, Notion’s long native migration, and Kotlin Multiplatform’s shared-logic approach.