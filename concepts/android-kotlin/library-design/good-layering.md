---
domain: android-kotlin
subdomain: library-design
concept: good-layering
title: Integration verbosity and good layering
sources:
  - title: "Integration verbosity and good layering"
    url: "https://jakewharton.com/integration-verbosity-and-good-layering/"
---

# Integration verbosity and good layering

The article argues that apparent verbosity in certain library integrations, such as using Android's view binding with activities or fragments, is not a design flaw but a consequence of the library operating at a well-defined layer of abstraction. View binding is a type-safe representation of an XML layout and has no inherent knowledge of higher-level components like activities; thus, the manual binding and inflation steps are appropriate. Similarly, Dagger, SQLDelight, and RecyclerView intentionally leave configuration and lifecycle decisions to the caller, which enables powerful integrations like Hilt, multi-platform database support, and ViewPager 2 to be built on top of them.

- View binding's lack of built-in activity/fragment integration is a deliberate design choice reflecting its abstraction layer.
- Verbosity in core library APIs often leaves room for flexible and future integrations, avoiding assumptions about the caller's environment.
- Past mistakes like Picasso's global singleton and Retrofit 1's default Gson show that baking in opinions makes alternative use-cases harder.
- Library authors should keep core libraries unopinionated and push integration conveniences into separate, evolvable integration libraries.