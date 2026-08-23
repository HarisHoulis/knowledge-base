# KB App — listen-mode player prototype (PROTOTYPE)

> PROTOTYPE — throwaway code for issue #188, to react to. Builds on the #130 progress-tracking prototype (which builds on the #129 scaffold). Validated decisions fold into the real app; this prototype lands on a throwaway branch as a primary source. Not production.

Answers the question: *how should the listen-mode player look and behave — play/pause/seek controls, resume-from-audio-position (the char-offset restored into speech), rate/voice access, iOS background audio (AVAudioSession) — integrated with #130's Reader?*

**Three structurally-different player variants**, switchable via the floating bottom bar (`L` prefix). The app defaults to **L-B (Immersive)**, the winning variant. Enter listen mode from the Reader's top-right **Listen** toggle; it resumes from the concept's saved char-offset. The `#130` read variants (`A/B/C`) still work when not listening.

- **L-A — Dock**: a compact player pinned to the bottom of the Reader — play/pause, a seek slider, live position, tap-to-cycle rate and voice. The reading text stays visible above, and the header ring advances as the position moves.
- **L-B — Immersive**: full-screen player — a large ring wrapping the play/pause button, seek slider, explicit rate chips (0.75/1/1.25/1.5×), tap-to-cycle voice, and an inline note that audio keeps playing in the background on iOS. A "Back to reading" button exits.
- **L-C — Inline**: minimal controls sitting in the reading flow — small play/pause, a thin progress bar, cycle rate/voice, and a quiet "Listening · x%" caption. Least chrome.

**All three share one interaction core** (the thing being prototyped): playback is a single **char offset into the concept body** — the same model #130 uses for scroll position — so listen and read share one resume position. The fake player (`FakeTtsPlayer`) simulates on-device TTS by advancing the offset over time and writing it to the in-memory repository, so the Reader's ring/bar stay live; `CONSUMED` fires when the end is reached. No real audio in this prototype — the engines are the #124-shaped stubs.

**Read ↔ listen sync:** the two modes stay in sync because they share one index — the char offset. Tapping **Listen** starts playback from the concept's saved position (where reading left off); exiting back to **Reading** re-scrolls the body to exactly where audio stopped (the Reader re-restores its scroll whenever the mode flips). The headless/immersive mode composes fresh from the shared position on every switch, so the handoff is exact in both directions.

**Deliberately not decided here (flagged for the screen-map ticket):** real TTS plumbing (segment-splitting on Android, AVSpeechSynthesizer delegate on iOS per `docs/research/cmp-on-device-tts.md`), and the concrete `AVAudioSession` category/`UIBackgroundModes` wiring for iOS background audio. The Immersive variant shows how that capability is surfaced in the UI.

State lives in-memory in `FakeConceptRepository` (as in #130).

## Verdict (resolution of #188)

**L-B (Immersive) wins**, with one requirement carried in: **reading and listening must stay index-synced** — listen resumes from the read position and reading returns to the audio position (see "Read ↔ listen sync" above). The winning shape: full-screen player with a large ring around the play/pause button, seek slider, explicit rate chips (0.75/1/1.25/1.5×), tap-to-cycle voice, and a surfaced note that audio keeps playing in the background on iOS. L-A (Dock) and L-C (Inline) are rejected — the immersive surface reads better than docked or inline controls for a listening pass.

## Run

One command (Android; iOS requires Xcode on macOS):

```
./gradlew :androidApp:assembleDebug
```

iOS framework compile check:

```
./gradlew :shared:compileKotlinIosSimulatorArm64
```

## Prior prototype (what this builds on)

The #130 progress-tracking prototype's verdict: **A's surfacing with B's Reader** — Browse rows + Resume cards carry explicit status badges; the Reader uses ring progress in the header with automatic transitions (`NEW → IN_PROGRESS` on open, `→ CONSUMED` at the end, `→ REVISITING` on re-open); one shared char-offset resume position, `CONSUMED` → `position = bodyLength`. The listen player shares that same char-offset, so read and listen stay in one place.

