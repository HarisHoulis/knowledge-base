# KB App — CMP scaffold (PROTOTYPE)

> PROTOTYPE — throwaway code for issue #129, to react to. Validated decisions fold into the real app; this scaffold lands on a throwaway branch as a primary source. Not production.

Answers the question: *does this CMP app structure, toolchain wiring, and stack feel right?*

- Module layout: wizard default — `shared` (all Kotlin/Compose) + `androidApp` shell + `iosApp` Xcode project.
- Navigation: Nav3 sealed `Route : NavKey` + `SavedStateConfiguration`.
- UDF: multiplatform ViewModel + immutable `UiState` (working Browse example).
- API seam: Ktor client behind `ConceptRepository` + `FakeConceptRepository`.
- TTS seam: `expect`/`actual` `TtsEngine` skeleton.

## Run

One command (Android; iOS requires Xcode on macOS):

```
./gradlew :androidApp:assembleDebug
```

iOS framework compile check (no Xcode needed for metadata):

```
./gradlew :shared:compileKotlinMetadata
```
