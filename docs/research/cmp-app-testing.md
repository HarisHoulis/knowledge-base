# CMP app testing strategy: UI tests, screenshot testing, previews, mocked backend (2026)

## Question

What testing options exist for the Compose Multiplatform (Android + iOS) app under `app/`, and which settle the strategy for ticket #182? Cover: multiplatform UI tests (`runComposeUiTest`), screenshot/snapshot testing, `@Preview` in `commonMain`, and a mocked-backend path (Ktor `MockEngine` vs a fake repository seam). Research only — informs the decision on #182.

## Context (fixed constraints)

- CMP 1.11.1, Kotlin 2.4.10, AGP 9.1.0 (`com.android.kotlin.multiplatform.library` in `shared`), targets Android + iOS only (no desktop).
- `shared` module: `commonMain`/`androidMain`/`iosMain`; screens under `ui/*` with UDF ViewModels (`uiState` StateFlow + one-shot event flow).
- `App()` takes `repository: ConceptRepository = FakeConceptRepository()` — the existing seam from the #129 scaffold.
- Repo testing convention `docs/agents/testing.md`: inject a callable rather than mocking third-party libraries; integration tests gated by marker.
- Agent machine (#165): `macos-latest`; iOS simulator builds need no signing.

## Sources (primary)

- [Kotlin: Testing Compose Multiplatform UI (`runComposeUiTest`)](https://kotlinlang.org/docs/multiplatform/compose-test.html)
- [Android Developers: Compose Preview Screenshot Testing](https://developer.android.com/studio/preview/compose-screenshot-testing)
- [Android Developers: Compose Preview Screenshot Testing release notes](https://developer.android.com/studio/preview/compose-screenshot-testing-release-notes)
- [Android Developers: screenshot testing best practices](https://developer.android.com/training/testing/ui-tests/screenshot)
- [Kotlin: Compose Multiplatform previews](https://kotlinlang.org/docs/multiplatform/compose-previews.html)
- [Ktor: Testing the client (`MockEngine`)](https://ktor.io/docs/client-testing.html)
- [JetBrains/compose-multiplatform](https://github.com/JetBrains/compose-multiplatform) and [JetBrains/compose-multiplatform-core](https://github.com/JetBrains/compose-multiplatform-core) (plugin source; `ui-test` API surface)

## Findings

### 1. Multiplatform UI tests: `runComposeUiTest` in `commonTest`

- One common test body runs on **iOS via `:shared:iosSimulatorArm64Test`** and on **Android via instrumented tests only** (`:shared:connectedAndroidTest`). The Android **local** JVM test configuration (`androidUnitTest`) is explicitly unsupported — no Robolectric path — so the Android side needs an emulator/device.
- Setup: commonTest dependency `org.jetbrains.compose.ui:ui-test:1.11.1`. Android device-test wiring: `withDeviceTestBuilder { sourceSetTreeName = "test" }` in the `androidLibrary {}` block, an `androidDeviceTest` source set with an `AndroidManifest.xml` exposing `androidx.activity.ComponentActivity`, `testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"`, plus `androidx.compose.ui:ui-test-junit4-android` and `debugImplementation("androidx.compose.ui:ui-test-manifest")`.
- API: `import androidx.compose.ui.test.v2.runComposeUiTest` with `@OptIn(ExperimentalTestApi::class)`. **Experimental** — may change.
- The `runComposeUiTest` environment has **no ViewModelStoreOwner**, so composables that call `viewModel()` can't be tested/previewed directly — state must be injected (stateless screens).

### 2. Screenshot testing: the CMP premise does not exist

- **Compose Multiplatform has no screenshot-testing feature.** There is no `compose.screenshotTest {}` DSL in the CMP Gradle plugin, no `@ScreenshotTest` annotation, and no matching docs page or release note. The `ui-test` API exposes `captureToImage` on **Android only**; there is no multiplatform/iOS capture API.
- The tooling that resembles it is **Jetpack/AGP's Compose Preview Screenshot Testing** (Android-only): plugin `com.android.compose.screenshot` (alpha), enabled via `android.experimental.enableScreenshotTest=true`, `screenshotTest` source set, tasks `update{Variant}ScreenshotTest` / `validate{Variant}ScreenshotTest`, annotation **`@PreviewTest`** (`@ScreenshotTest` is not in the current tool).
- It renders **host-side via layoutlib** (no emulator), reference images under `{module}/src/screenshotTest{Variant}/reference`, HTML report at `build/reports/screenshotTest/preview/{variant}/index.html`. Works with AGP 8.5+; AGP 9 compatible (alpha12+).
- **KMP is explicitly unsupported**: the plugin "is engineered exclusively for Android projects. They don't support non-Android targets in KMP projects." So it cannot live in `shared`/`commonMain`, and all app screens live there — it could only reach an Android application/library module (e.g. the `androidApp` shell).

### 3. `@Preview` in commonMain: supported

- The original `androidx.compose.ui.tooling.preview.Preview` is now fully multiplatform (CMP 1.10 deprecated the custom `org.jetbrains.compose.ui.tooling.preview.Preview`).
- Setup: `commonMain` dep `org.jetbrains.compose.ui:ui-tooling-preview:1.10.0+`; tooling on the classpath via `debugImplementation("org.jetbrains.compose.ui:ui-tooling:1.10.0")` or `androidRuntimeClasspath(...)` under the AGP 9 `androidLibrary {}` KMP plugin.
- Previews are rendered by the **Android tooling pipeline** (an Android target is required); there is no separate iOS preview renderer. No relationship to screenshot testing inside CMP.

### 4. Ktor `MockEngine`: multiplatform, complements rather than replaces the fake seam

- `io.ktor:ktor-client-mock` works in `commonTest`; `MockEngine { request -> respond(...) }` stubs HTTP with no network, identically on iOS native tests and Android. It exercises the real client config (ContentNegotiation/JSON, serialization, request building) minus the wire.
- Complementary to a fake-repository seam: `MockEngine` validates the HTTP+serialization layer; a fake repo isolates pure state/logic. The repo convention prefers injected seams over mocking libraries.

## Verdict

The research constrains the #182 decision (settled in the ticket resolution):

1. **UI tests** — commonTest `runComposeUiTest`; run on the iOS simulator (`iosSimulatorArm64Test`) and Android instrumented (`connectedAndroidTest`). Requires **stateless screens** (state + callbacks injected), since the test environment has no `ViewModelStoreOwner`.
2. **Snapshot testing** — dropped for v1: CMP has no screenshot feature, and Jetpack's layoutlib tool is Android-module-only and KMP-unsupported, so it can't cover the screens in `shared`. Revisit only if CMP ships its own.
3. **Previews** — supported in `commonMain`; a `@Preview` per screen with a hand-built sample `UiState`, once screens are stateless.
4. **E2E with a mocked backend** — rejected: no mocking of code we own. E2E core-flow tests run on emulator/simulator against the real backend; `FakeConceptRepository` remains only as the scaffold's dev placeholder, not a test seam. `MockEngine` reserved for a thin client/serialization test if the client layer ever needs it.

## Uncertainties

- `runComposeUiTest` is **Experimental** — API may shift as CMP 1.12 matures.
- Jetpack screenshot testing is alpha and under active churn; the AGP 9 compatibility notes are from alpha12+.
- The `androidDeviceTest` instrumented path (manifest, runner, emulator) is untested in this repo — wiring is part of the implementation that graduates from #182.
