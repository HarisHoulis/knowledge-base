# CMP Navigation: Nav Compose 2.x vs Navigation 3 for a new learning app

## Question

A brand-new Compose Multiplatform app (shared Kotlin module + `androidApp`/`iosApp` shells), Kotlin 2.4.x, CMP 1.11.x. Which navigation library should we scaffold on in 2026: `org.jetbrains.androidx.navigation:navigation-compose` (Nav Compose 2.x, 2.9.2) or `org.jetbrains.androidx.navigation3:navigation3-ui` (Nav3, 1.1.x)? Research only — no code written.

## Context (fixed constraints)

- Small single-user **browse / search / read / listen** app (no deep-link/universal-link requirement, no complex multi-module layout).
- Targets Android + iOS with shared Compose UI.
- Learning app: the learner will follow official tutorials and the KMP wizard/template.

## Sources (primary)

- [JetBrains: Navigation in Compose (CMP docs, nav-compose 2.9.2)](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-navigation.html)
- [JetBrains: Navigation 3 in Compose Multiplatform](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-navigation-3.html)
- [JetBrains: Navigation and routing](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-navigation-routing.html)
- [JetBrains: Deep links](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-navigation-deep-links.html)
- [JetBrains: Multiplatform ViewModel (Nav3 scoping section)](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-viewmodel.html)
- [JetBrains: What's new in CMP 1.11.1 (dependency table)](https://kotlinlang.org/docs/multiplatform/whats-new-compose-111.html)
- [Android Developers: Navigation 3 overview](https://developer.android.com/guide/navigation/navigation-3)
- [Android Developers: Migrate from Navigation 2 to Navigation 3](https://developer.android.com/guide/navigation/navigation-3/migration-guide)
- [Android Developers: AndroidX Navigation (Nav2) release notes](https://developer.android.com/jetpack/androidx/releases/navigation)
- [Android Developers: AndroidX navigation3 release notes](https://developer.android.com/jetpack/androidx/releases/navigation3)
- [Android Developers Blog: Announcing Jetpack Navigation 3 (Google I/O 2025)](https://android-developers.googleblog.com/2025/05/announcing-jetpack-navigation-3-for-compose.html)
- [AndroidX reference: NavBackStackEntry](https://developer.android.com/reference/androidx/navigation/NavBackStackEntry)
- [Kotlin/KMP-App-Template (shared/build.gradle.kts, libs.versions.toml)](https://github.com/Kotlin/KMP-App-Template)
- [kmp.jetbrains.com wizard templates gallery](https://kmp.jetbrains.com/templates/)
- [Maven Central: org.jetbrains.androidx.navigation3/navigation3-ui versions](https://repo1.maven.org/maven2/org/jetbrains/androidx/navigation3/navigation3-ui/)
- [Maven Central: org.jetbrains.androidx.navigation/navigation-compose versions](https://repo1.maven.org/maven2/org/jetbrains/androidx/navigation/navigation-compose/)
- [Google Maven: androidx.navigation3/navigation3-ui metadata](https://dl.google.com/android/maven2/androidx/navigation3/navigation3-ui/maven-metadata.xml)
- [arkivanov/Decompose README](https://github.com/arkivanov/Decompose)
- [Maven Central: com.arkivanov.decompose/decompose versions](https://repo1.maven.org/maven2/com/arkivanov/decompose/decompose/)

## Findings

### 1. Architecture: library-owned graph vs user-owned back stack

**Nav Compose 2.x** is the port of AndroidX Navigation 2. The library owns the back stack inside a `NavController`/`NavHost`; the app defines a `NavGraph` DSL (`composable<T> { }`, `navigation` nesting) and navigates via `navController.navigate(route)` / `popBackStack`. Google's own I/O 2025 post lists the downsides this created: "the back stack state could only be observed indirectly… two sources of truth," and `NavHost` renders only the single top-most destination, blocking adaptive/list-detail layouts ([blog](https://android-developers.googleblog.com/2025/05/announcing-jetpack-navigation-3-for-compose.html)).

**Nav3** inverts this: *you* own the back stack. JetBrains: "Instead of operating a single library back stack, you create and manage a `SnapshotStateList` of states, which the UI observes directly" ([CMP Nav3 docs](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-navigation-3.html)). Google: "you, the developer, not the library, own and control the back stack. It's a simple list which is backed by Compose state… You can navigate by adding or removing items (Ts)" ([blog](https://android-developers.googleblog.com/2025/05/announcing-jetpack-navigation-3-for-compose.html)). `NavDisplay(backStack, entryProvider) { }` maps each `NavKey` in the list to composable content; `navigate` is `backStack.add(route)`, back is `removeLastOrNull()`. Because the stack is plain Compose state, `NavDisplay` can render more than one entry at once (adaptive "scenes"), and any custom animation/layout logic is reachable ([Navigation 3 overview](https://developer.android.com/guide/navigation/navigation-3)).

**`SavedStateConfiguration` and why it matters on iOS.** In Nav3 the back stack is a *polymorphic* `List<NavKey>` (routes implement `NavKey`, often through a sealed interface or open hierarchy). Persisting that list (for `rememberSaveable`/state restoration) requires serializing it. On Android, AndroidX uses reflection-based serialization; reflection is unavailable on Kotlin/Native (iOS) and Wasm. JetBrains: "To support non-JVM platforms like web and iOS, you need to implement polymorphic serialization for destination keys" ([CMP Nav3 docs](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-navigation-3.html)). The fix is the second `rememberNavBackStack(config, ...)` overload, which takes a `SavedStateConfiguration { serializersModule = SerializersModule { polymorphic(NavKey::class) { ... } } }` that registers subclass serializers (JetBrains recommends a `@Serializable sealed interface Route : NavKey` for small apps — closed polymorphism means the hierarchy's serializer is fully known at compile time and needs no manual registry; open hierarchies across modules need the explicit `SerializersModule`). Concretely on iOS: without it, back-stack state cannot be (de)serialized for save/restore, so state restoration silently breaks. For a small app the sealed-interface approach is ~5 lines; the ceremony only grows with multi-module route hierarchies.

### 2. State restoration / ViewModel scoping

**Nav Compose 2.x:** each back-stack entry scopes everything automatically. `androidx.navigation.NavBackStackEntry` implements `LifecycleOwner`, `ViewModelStoreOwner`, and `HasDefaultViewModelProviderFactory` ([AndroidX reference](https://developer.android.com/reference/androidx/navigation/NavBackStackEntry)); `viewModel { }` inside a destination is scoped to that entry, created on first show and cleared when the entry is popped. The CMP migration guide notes the Nav2 pattern (`navController.currentBackStackEntry` as lifecycle owner) versus Nav3 ([migration guide](https://developer.android.com/guide/navigation/navigation-3/migration-guide)).

**Nav3:** there is no built-in per-entry `ViewModelStoreOwner`. JetBrains: "When using ViewModels with Navigation 3 in common code, ViewModels are not automatically scoped to navigation entries by default. Without explicit scoping, each ViewModel will be tied to the Activity rather than the screen, even after the user has navigated away" ([CMP ViewModel docs](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-viewmodel.html)). You must opt in with entry decorators:

```kotlin
NavDisplay(
    entryDecorators = listOf(
        rememberSaveableStateHolderNavEntryDecorator(),
        rememberViewModelStoreNavEntryDecorator(), // from lifecycle-viewmodel-navigation3
    ),
    ...
)
```

On iOS there is no `Activity` — the fallback owner is the app/`ComposeUIViewController` scope. So without `rememberViewModelStoreNavEntryDecorator`, every screen shares one ViewModel store: ViewModels survive navigation (stale state, cross-screen collisions) and are never cleared per screen; without the `rememberSaveableStateHolderNavEntryDecorator` the same happens to `rememberSaveable` state. This is the single most likely "it just works on Android, mysteriously wrong on iOS" trap, and it is a *third* dependency (`org.jetbrains.androidx.lifecycle:lifecycle-viewmodel-navigation3`, 2.11.0 stable on Maven Central) plus two lines of boilerplate.

### 3. Deep links and type-safe routes

**Nav Compose 2.x** has the mature story. Type-safe routes via `@Serializable` objects/data classes (`composable<Profile>`, `navController.navigate(Profile("Alice"))`, `backStackEntry.toRoute()`) are the documented default ([CMP docs](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-navigation.html)); deep links are fully documented for CMP — `navDeepLink`/`navDeepLink<T>(basePath = ...)` with auto-generated URI patterns and a documented cross-platform (iOS/desktop/web) receive-handler pattern ([Deep links](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-navigation-deep-links.html)). Nav2 keeps accruing type-safety polish (value-class routes in 2.9.0-alpha03, `List<Enum>` args, lint checks).

**Nav3** has type-safe routes (routes implement `NavKey`) but the *deep-link* surface is still moving. AndroidX Nav3 1.2.0 alphas are actively reworking it: `1.2.0-alpha05` removed `fromIntent`/`fromMimeType`/`fromUri`/`fromUriString` factory functions in favor of constructors + an `extras` map, added `DeepLinkSerializer` and `BackStackMatcher`; `1.2.0-alpha06/07` changed `DeepLinkRequest` constructors and `DeepLinkMatcher` generics ([navigation3 release notes](https://developer.android.com/jetpack/androidx/releases/navigation3)). The official Nav2→Nav3 migration guide explicitly lists **"Deep links" as unsupported/not-yet-covered**, alongside more-than-one-level nested navigation, shared destinations, and custom destination types ([migration guide](https://developer.android.com/guide/navigation/navigation-3/migration-guide)). JetBrains' Nav3 CMP docs do not document deep links at all yet. For this app (no deep links), this is a non-issue; for a deep-link-heavy app it is the strongest reason to stay on Nav2 today.

### 4. Migration trajectory and support status

- **Nav2 (AndroidX) is officially in maintenance mode.** The AndroidX Navigation release notes carry a caution banner: "This library is in maintenance mode and will only receive critical fixes; new features are not planned" ([release notes](https://developer.android.com/jetpack/androidx/releases/navigation)). Latest stable there is 2.9.8 (Aug 2026), with 2.10.0-rc01. JetBrains' CMP port mirrors it: 2.9.2 stable bundled with CMP 1.11.1, and 2.10.0-alpha01/02 already published on Maven Central — so it *keeps getting versions*, but as maintenance/bug-fix releases, not feature work. It is **not formally deprecated** in JetBrains docs — it is still the default subject of the CMP navigation pages — but Google's I/O 2025 announcement positioned Nav3 as the replacement and Nav2's limitations as the reason.
- **Nav3 is the stated direction.** JetBrains: "Android's Navigation library has been upgraded to Navigation 3… a redesigned approach"; CMP supports it "for all supported platforms: Android, iOS, desktop, and web" since CMP 1.10 ([CMP Nav3 docs](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-navigation-3.html)). CMP 1.11.1 pins `org.jetbrains.androidx.navigation3:navigation3-*:1.1.2` ([what's new in 1.11.1](https://kotlinlang.org/docs/multiplatform/whats-new-compose-111.html)).
- **The upgrade path is a rewrite, not a migration.** Google: "It's easier to see Navigation 3 as a new library than a new version of the existing library… more of a rewrite," and the official guide prescribes replacing `NavController`/`NavHost` wholesale, adding the `NavKey` interface, moving destinations into an `entryProvider`, and "Remove Navigation 2 dependencies" ([migration guide](https://developer.android.com/guide/navigation/navigation-3/migration-guide)). Readiness: the guide covers single-atomic-change migrations of common apps and defers nested nav, shared destinations, custom destination types, and deep links.

### 5. API stability today

- **Nav Compose 2.x:** fully stable; 2.9.2 is the CMP-documented stable. 10+ years of API surface, no meaningful churn. Risk: maintenance mode means it won't gain new features and eventually won't track new Compose idioms; the version treadmill continues but only for critical fixes.
- **Nav3:** both tracks have stables — AndroidX `androidx.navigation3:*` at **1.1.6** and JetBrains `navigation3-ui` at **1.1.1** (Maven Central shows 1.1.1 as the newest stable dir; note the CMP 1.11.1 release notes list "Navigation3 1.1.2", a minor discrepancy between the docs table and the artifact index — flagging as uncertain). Core navigation (back stack, `NavDisplay`, entry decorators) is stable. But the API is **not settled**: AndroidX is at `1.2.0-alpha07` with breaking API changes in deep links/results (`ResultEventBus` added in `1.2.0-alpha05`, `DeepLinkRequest`/`DeepLinkMatcher` reworked through `alpha07`), and JetBrains has `1.2.0-alpha02` staged. Version skew risk: the JetBrains `navigation3-ui` wrapper pins `androidx.navigation3` base versions from Google Maven (its 1.1.1 POM depends on androidx navigation3 1.1.1), so the two tracks can lag each other.

Risks of scaffolding today: Nav2 = future rewrite (documented) but everything works; Nav3 = thinner CMP docs, the serialization config and ViewModel decorators are mandatory "gotchas," deep links undocumented, and pinning to 1.1.x stable is advised over 1.2.0 alphas.

### 6. Sample/template/tutorial adoption

- **kmp.jetbrains.com wizard:** the "Shared UI Multiplatform App" template downloads **KMP-App-Template** (confirmed from the template's `/template/download/KMP-App-Template` link on [kmp.jetbrains.com/templates/](https://kmp.jetbrains.com/templates/)), which depends on `org.jetbrains.androidx.navigation:navigation-compose:2.9.2` ([libs.versions.toml](https://github.com/Kotlin/KMP-App-Template/blob/main/gradle/libs.versions.toml), [shared/build.gradle.kts](https://github.com/Kotlin/KMP-App-Template/blob/main/shared/build.gradle.kts)). So the wizard ships **Nav Compose 2.x**. The bare wizard scaffold from the "Create your first app" tutorial includes *no* navigation library at all.
- **Official tutorials/docs:** all of the current JetBrains CMP navigation pages (Navigation in Compose, Navigation and routing, Deep links, the `nav_cupcake` example, the flagship KotlinConf app) document and use **Nav Compose 2.x**. Nav3 has a single dedicated docs page and the Android-side recipes (`terrakok/nav3-recipes`), but it is not yet what a learner meets in the standard curriculum.
- Net: a CMP learner in 2026 follows a Nav2-based curriculum and scaffold; Nav3 is present in docs but not yet in the default tooling path.

### 7. Decompose 3.5.0 as the third-party alternative

Decompose 3.5.0 (stable; `3.6.0-alpha01` in progress) is navigation-as-data: components with explicit lifecycles, back stack as a model you fully own, state preservation, instance retention (VM-like), back-button handling, and pluggable UI (Compose *or* SwiftUI, React, etc.) ([README](https://github.com/arkivanov/Decompose)). It would beat both JetBrains options when you want: (a) business logic decoupled from UI and unit-testable without any UI framework, (b) per-platform native UI (SwiftUI on iOS, Compose on Android) over a shared navigation model, (c) components that keep running in the background behind the top screen, or (d) escape from AndroidX's roadmap. For this specific app — a single-user browse/search/read/listen app with shared Compose UI and no need for native UI shells — Decompose is heavier than the problem: more boilerplate, deep links and typed routing are DIY, and it's a single-maintainer (though very established) library. It's the right tool if we later split iOS into SwiftUI; it's wrong if the goal is the shortest path to a working shared-UI app.

## Verdict

**For a brand-new small CMP learning app scaffolded in 2026, pick Navigation 3 (`navigation3-ui`, 1.1.x stable) — with one documented caveat.**

Reasoning:
1. Nav2 is officially in **maintenance mode** (AndroidX) while Nav3 is the documented direction, supported by JetBrains since CMP 1.10 and bundled in CMP 1.11. Scaffolding a *new* app on a maintenance-only library front-loads a rewrite that Google itself calls "more of a rewrite, not a migration."
2. For a small browse/search/read/listen app, Nav3's user-owned back stack (`SnapshotStateList` + `NavDisplay`) is *simpler and more Compose-idiomatic* than Nav2's graph DSL, `popUpTo`, and `NavBackStackEntry` bookkeeping — it teaches the state model the ecosystem is moving to.
3. The things that make Nav3 awkward right now (polymorphic-serialization config on iOS, ViewModel scoping decorators, undocumented deep links) are small for this app and are exactly the "learning surface" worth understanding: sealed-interface routes make the serializer a few lines, and the two entry decorators are boilerplate, not complexity.

Caveats / conditions:
- **If** the priority is "follow official tutorials byte-for-byte with zero friction," Nav Compose 2.x remains the lower-friction default (it's what the wizard, the template, and every current tutorial use), and is entirely fine for a learning-only app — but treat it as a stepping stone, not a destination.
- Pin Nav3 to **1.1.x stable** (JetBrains `1.1.1` / androidx base `1.1.6`), not the 1.2.0 alphas; add `lifecycle-viewmodel-navigation3` + the two entry decorators on day one; use a `sealed interface Route : NavKey` for routes; avoid deep links until JetBrains documents them for Nav3 CMP.
- Skip Decompose for this app; revisit only if we ever move iOS to SwiftUI or need pure-logic navigation testing.

## Uncertainties

- CMP 1.11.1 release notes list "Navigation3 1.1.2" while Maven Central's newest JetBrains `navigation3-ui` stable is 1.1.1 — versioning between the JetBrains wrapper and its androidx base is not perfectly in lockstep. Pin an explicit version rather than relying on the plugin's default.
- "Maintenance mode" is AndroidX's official wording for Nav2; JetBrains has not published an equivalent CMP-specific deprecation statement, and CMP continues shipping 2.9.x/2.10.x-alphas. The CMP track of Nav2 is therefore "still supported, not feature-developed."
- Nav3 deep-link support exists in androidx (`UriDeepLinkMatcher` etc.) but is undocumented in the JetBrains CMP docs and mid-rework in 1.2.0 alphas — treat as unsupported on CMP for now.
