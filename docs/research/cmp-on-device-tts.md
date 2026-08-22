# On-Device TTS in Compose Multiplatform (Android + iOS)

## Question

How should "listen to content" work on-device in a Compose Multiplatform app targeting Android and iOS? The human decision is already made: on-device TTS (no server-side synthesis). The app reads markdown-derived concept content and must support play/pause/stop with position tracking (per-concept listened status + resume position). What is the recommended integration shape, and is a maintained multiplatform TTS library worth using over a hand-rolled `expect`/`actual` wrapper?

## Context

Decision ticket: wayfinder research ticket #124 ("Choose how on-device TTS works in CMP"). Research only — no production code. Target is a Compose Multiplatform app (Android + iOS). The TTS layer must expose play, pause, resume, stop, and a playback position that can be synced back into app state so each concept can record listened-status and a resume position.

## Sources

- [TextToSpeech (Android Developers)](https://developer.android.com/reference/android/speech/tts/TextToSpeech)
- [AOSP `TextToSpeech.java` (platform_frameworks_base)](https://github.com/aosp-mirror/platform_frameworks_base/blob/master/core/java/android/speech/tts/TextToSpeech.java)
- [AOSP `UtteranceProgressListener.java`](https://github.com/aosp-mirror/platform_frameworks_base/blob/master/core/java/android/speech/tts/UtteranceProgressListener.java)
- [AVSpeechSynthesizer (Apple Developer Documentation)](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer)
- [AVSpeechUtterance (Apple Developer Documentation)](https://developer.apple.com/documentation/avfaudio/avspeechutterance)
- [AVSpeechSynthesizerDelegate (Apple Developer Documentation)](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizerdelegate)
- [AVSpeechBoundary (Apple Developer Documentation)](https://developer.apple.com/documentation/avfaudio/avspeechboundary)
- [Use platform-specific APIs — Kotlin Multiplatform docs (JetBrains)](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-connect-to-apis.html)
- [TextToSpeechKt (GitHub)](https://github.com/Marc-JB/TextToSpeechKt) — Maven Central `nl.marc-apps:tts`, README, and source files `TextToSpeech.kt`, `TextToSpeechInstance.kt`, `TextToSpeechAndroid.kt`, `TextToSpeechIOS.kt`, `TtsProgressConverter.kt` (androidMain + appleMain)
- [CopiloTTS (GitHub)](https://github.com/sigmadeltasoftware/CopiloTTS) — README, Maven Central `app.drivista:copilotts`

## Findings

### 1. Android: `TextToSpeech` has no pause — pause is `stop()` + re-speak

From the AOSP source, the public control surface of `android.speech.tts.TextToSpeech` is `speak(...)`, `stop()`, `playSilentUtterance(...)`, `setSpeechRate(float)`, `setPitch`, `setLanguage(Locale)`, `setVoice(Voice)`, `getVoices()`, `setAudioAttributes(...)`, `synthesizeToFile(...)`, and `shutdown()`. **There is no `pause()` or `resume()` method.** The only interruption primitive is `stop()`; speaking again with `QUEUE_FLUSH` discards and replaces the queue.

Consequences for pause/resume on Android:
- Pausing must be simulated: record the current position, call `stop()`, and on resume re-`speak()` the remaining text with `QUEUE_FLUSH`.
- `speak()` is asynchronous and queues (`QUEUE_FLUSH` = drop current + replace, `QUEUE_ADD` = append). Completion/error/interruption surface through `UtteranceProgressListener`, which is set via `setOnUtteranceProgressListener(...)`.
- Input length is capped: `getMaxSpeechInputLength()` returns **4000 characters** (`TextToSpeech.java:2553`), so long concept content must be split into multiple utterance chunks anyway. Chunking is also what makes position/resume tractable (see Finding 4).

### 2. Android: per-utterance callbacks, and position is engine-dependent

`UtteranceProgressListener` (AOSP source) delivers:
- `onStart(utteranceId)`, `onDone(utteranceId)` — per utterance, keyed by the `utteranceId` passed to `speak(...)`.
- `onError(utteranceId, errorCode)` — distinct from done; never both for the same utterance.
- `onStop(utteranceId, interrupted)` — fired when a `stop()` or `QUEUE_FLUSH` interrupts an utterance. This is the callback that fires when we "pause" via `stop()`.
- `onRangeStart(utteranceId, start, end, frame)` — char start/end indices plus an audio frame position, documented as: "Only called if the engine supplies timing information by calling `SynthesisCallback.rangeStart(int, int, int)`." Timing-supply is engine-specific, so relying on `onRangeStart` for position is not portable across Android TTS engines.

Voice/rate are configurable: `Voice` objects via `setVoice`/`getVoices()` (API 21+), `setLanguage(Locale)`, and `setSpeechRate(float)` (0.5–2.0, `TextToSpeech.Engine.DEFAULT_RATE = 100` internally). Native engines synthesize on-device by default; network voices are opt-in and flagged via `Voice.isNetworkConnectionRequired()`.

### 3. iOS: `AVSpeechSynthesizer` has native pause/resume and word-level position

Apple's docs define the control surface:
- `speak(AVSpeechUtterance)` queues utterances; `pauseSpeaking(at:)`, `continueSpeaking()` (resumes "from its paused point"), and `stopSpeaking(at:)` control playback. `AVSpeechBoundary` gives `.immediate` or `.word` boundaries for pause/stop.
- The synthesizer is **not retained by the system** ("The system doesn't automatically retain the speech synthesizer, so you need to manually retain it until speech concludes").
- `AVSpeechUtterance` exposes `rate` (Float, `AVSpeechUtteranceDefaultSpeechRate` ≈ 0.5, with `MinimumSpeechRate`/`MaximumSpeechRate`), `voice` (`AVSpeechSynthesisVoice`), `pitchMultiplier`, `volume`, and `preUtteranceDelay`/`postUtteranceDelay`.

Position tracking: the delegate protocol `AVSpeechSynthesizerDelegate` includes `speechSynthesizer(_:willSpeakRangeOfSpeechString:utterance:)`, which "tells the delegate when the synthesizer is about to speak a portion of an utterance's text" — it delivers the `NSRange` (character offsets) of the next word within the utterance. This is true word-level character-position tracking, natively supported, on iOS only.

### 4. The asymmetry that matters: position granularity

| Capability | Android (`TextToSpeech`) | iOS (`AVSpeechSynthesizer`) |
|---|---|---|
| Native mid-utterance pause | **No** — `stop()` discards; resume = re-speak remaining text | **Yes** — `pauseSpeaking(at:)` / `continueSpeaking()` resumes from the pause point |
| Word/character position | `onRangeStart` exists but is engine-dependent ("Only called if the engine supplies timing information") | `willSpeakRangeOfSpeechString` gives reliable word character ranges |
| Reliable position primitive | Segment index (which enqueued chunk is active), via per-utterance `onStart`/`onDone`/`onStop` | Char offset within the utterance string (word granularity) |

Therefore the shared position model should be a **character offset into the full concept text**, computed per platform:
- iOS: offset of the active utterance + `NSRange.location` from `willSpeakRangeOfSpeechString`.
- Android: sum of characters in all completed segments + optional `onRangeStart` delta when the engine supplies timing; otherwise fall back to the last segment's start offset (segment-level granularity).

### 5. Compose Multiplatform: `expect`/`actual` is the stable, documented path

JetBrains' KMP docs describe `expect`/`actual` (functions, classes, interfaces, properties) as the standard mechanism for platform-specific APIs, with hierarchical source sets (`commonMain`, `androidMain`, `appleMain`/`iosMain`). For non-trivial logic the documented pattern is a common interface + per-platform implementations, constructed via an `expect fun` factory or a DI framework (Koin is called out in the docs). Both `TextToSpeech` (JVM) and `AVSpeechSynthesizer`/`AVSpeechSynthesizerDelegate` (Kotlin/Native `platform.AVFAudio.*`) are directly usable from Kotlin — TextToSpeechKt's `appleMain` `TtsProgressConverter` is a live example of an `AVSpeechSynthesizerDelegateProtocol` implementation in Kotlin/Native.

### 6. Maintained multiplatform TTS libraries (verified) — and their gaps

Two real, maintained KMP TTS libraries exist; both verified against GitHub/Maven Central:

- **TextToSpeechKt** — `nl.marc-apps:tts` (MIT, 58★, last push 2026-01-24, v3.0.0 on Maven Central). Pure Kotlin Multiplatform targeting Android, iOS, macOS, JS, Wasm, plus a `tts-compose` module (`rememberTextToSpeechOrNull()`). Supports rate/pitch/volume, voice/language selection, coroutine-based `say(...)`. **Gap:** the public `TextToSpeechInstance` interface has no `pause()`/`resume()` and no position/progress callbacks — only start/done/error/stop. Neither its Android nor its iOS `TtsProgressConverter` implements `onRangeStart` / `willSpeakRangeOfSpeechString`. Position tracking and pause/resume would have to be layered on top by the app (chunk + track segment index + `stop()` to pause).

- **CopiloTTS** — `app.drivista:copilotts` (MIT, 29★, created 2025-12, last push 2026-06-03). Newer. Exposes `pause()`, `resume()`, `stop()`, and a `progress` `StateFlow` (0.0–1.0). **Gaps:** `pause()` is documented as **iOS only** ("Pause speech (iOS only)") — matching the platform asymmetry above; Android must fall back to stop+re-speak. On iOS it is not pure Kotlin: the native path requires hand-written Swift glue implementing a `TTSNativeHandler` protocol that must be registered before Koin starts, and the library expects Koin DI. It also ships an optional ONNX/HuggingFace model stack the app doesn't need.

No moko or other TTS library was found; those names are not real/verified and should not be assumed.

## Recommendation

**Adopt the asymmetry-aware approach: hand-roll a thin `expect`/`actual` TTS engine in the shared module, and skip both libraries.** Neither verified library delivers the hard requirement (pause/resume **and** position tracking) in pure KMP: TextToSpeechKt has neither, and CopiloTTS's pause is iOS-only plus requires Swift glue and Koin. The wrapper is small, both platform APIs are directly accessible from Kotlin, and the position model must be platform-idiomatic anyway.

### Integration shape (commonMain interface + per-platform actuals)

```kotlin
// commonMain
data class TtsPlaybackState(
    val isPlaying: Boolean,
    val isPaused: Boolean,
    val positionChars: Long,   // char offset into the full concept text
    val error: TtsError? = null,
)

interface TtsEngine {
    val state: StateFlow<TtsPlaybackState>
    fun play(text: String, fromPositionChars: Long = 0)
    fun pause()
    fun resume()
    fun stop()
    fun setSpeechRate(rate: Float)
    fun release()
}
```

- **Position unit:** character offset into the concept's plain-text content (markdown already stripped). Android derives it from completed segments (+ engine `onRangeStart` delta when available); iOS derives it from utterance offset + `willSpeakRangeOfSpeechString`'s `NSRange.location`.
- **Android actual:** wraps `TextToSpeech` + `UtteranceProgressListener`. Splits text into chunks (respecting `getMaxSpeechInputLength()` = 4000), enqueues with unique `utteranceId`s, tracks the active segment index. `pause()` = record position + `stop()`; `resume()` = re-`speak()` remaining chunks with `QUEUE_FLUSH`. `onStop(id, interrupted=true)` maps to the paused state.
- **iOS actual:** wraps `AVSpeechSynthesizer` + `AVSpeechSynthesizerDelegate`; the app must keep a strong reference to the synthesizer. `pause()` = `pauseSpeaking(at: .immediate)`; `resume()` = `continueSpeaking()`; position updates come from `willSpeakRangeOfSpeechString`. Use `AVSpeechSynthesisVoice` for voice selection and `AVSpeechUtterance.rate` for speed.
- **State sync:** the `state` `StateFlow` is collected by a ViewModel that persists `(conceptId, positionChars, listenedStatus)` on pause/stop/completion (matching the per-concept listened-status + resume-position requirement). Progress is pushed from the engine out to app state; the app never polls the platform engines.

### Rationale checks against the sources

- Chunked per-utterance speak is required on Android anyway (4000-char cap) and is what makes segment-level resume reliable (`onRangeStart` cannot be trusted cross-engine).
- iOS natively supports true pause and word-level position, so the wrapper must not force the segment model onto iOS — the shared char-offset position lets each platform use its best primitive.
- `expect`/`actual` + hierarchical source sets is the documented, stable KMP mechanism (Finding 5); both libraries' existence was verified but both fail the requirement, so the default recommendation is a small owned wrapper.
