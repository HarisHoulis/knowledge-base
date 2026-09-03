---
domain: android-kotlin
subdomain: dependency-injection
concept: assisted-inject-migration
title: AssistedInject is dead, long live AssistedInject!
sources:
  - title: "AssistedInject is dead, long live AssistedInject!"
    url: "https://code.cash.app/assisted-inject-is-dead-long-live-assisted-inject"
    author: "Jake Wharton"
---

# AssistedInject is dead, long live AssistedInject!

Jake Wharton announces that Square AssistedInject is deleted after about five years. The same functionality is now available directly in Dagger, and InflationInject has moved to its own repository. The article, published on code.cash.app, walks through a migration from Square AssistedInject to Dagger's built-in assisted injection in four discrete steps, starting with version 0.6.0. The first step is upgrading to 0.7.0, which requires qualifier annotations (like @Named) on assisted parameters of the same type, because relying on parameter names is unsafe. The second step is upgrading to 0.8.1, replacing @Assisted with @Inflated in inflation injection constructors, which lets Dagger validate that its own @Assisted is used only with its own @AssistedInject.

- Square AssistedInject is deprecated and removed; Dagger now includes built-in assisted injection, and InflationInject is separated into its own project.
- Migration involves four steps: upgrade to 0.7, upgrade to 0.8, switch to Dagger's annotations, and remove Square dependencies.
- Dagger uses @AssistedFactory instead of @AssistedInject.Factory and disambiguates same-type assisted parameters via @Assisted("name") rather than qualifier annotations.
- When a factory returns a supertype of the created class, a separate DaggerFactory interface plus @Binds is required to satisfy Dagger's return type matching.
- InflationInject 1.0.0 uses new Maven coordinates and imports under app.cash.inject, but is unlikely to see much further development because of Jetpack Compose UI.