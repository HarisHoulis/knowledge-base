---
domain: ai-workflows
subdomain: mobile-development
concept: coding-agents-shift-native-vs-cross-platform
title: Shopify returns to native mobile because coding agents changed the cost calculus
sources:
  - title: "Native is now the future of mobile at Shopify"
    url: "https://shopify.engineering/back-to-native"
    author: "Shopify Engineering"
  - title: "Native is now the future of mobile at Shopify (link blog)"
    url: "https://simonwillison.net/2026/Sep/10/shopify-react-native/"
    author: "Simon Willison"
    date: "2026-09-10"
---

# Shopify returns to native mobile because coding agents changed the cost calculus

Shopify announced it is moving its mobile apps back from React Native to native development. The company originally switched from native to React Native in 2020 for three reasons: to stop building the same features twice, to let developers work across the stack, and to spend less time chasing feature parity and more time shipping value (Shopify Engineering, "Native is now the future of mobile at Shopify").

The reasons for reversing the decision are not that React Native's tradeoffs disappeared. As the post acknowledges, native still means building and maintaining software on two platforms, and that cost has not gone away. What changed is that AI coding agents can now handle enough of the implementation, translation, testing, and review work that cross-platform code sharing is no longer the deciding factor it was in 2020.

Simon Willison characterizes it as a well-written post that gives full credit to React Native as a great platform for the six years Shopify used it (Simon Willison, 2026-09-10). Shopify is the maintainer of three significant React Native libraries—react-native-skia, flash-list, and restyle. Skia and flash-list are finding new homes, while restyle, which has a smaller user base than the others, will be archived at the end of 2026.

- Shopify moved native → React Native in 2020 to avoid duplicate feature work, enable full-stack developers, and reduce feature-parity chasing.
- The move back to native is justified by coding agents doing implementation, translation, testing, and review work—not by native's two-platform cost disappearing.
- Native still requires building and maintaining software on two platforms; that cost is unchanged.
- Shopify's React Native libraries are being transitioned: react-native-skia and flash-list are finding new homes, and restyle will be archived at the end of 2026.