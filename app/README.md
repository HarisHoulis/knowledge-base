# KB App — progress-tracking prototype (PROTOTYPE)

> PROTOTYPE — throwaway code for issue #130, to react to. Builds on the #129 scaffold. Validated decisions fold into the real app; this prototype lands on a throwaway branch as a primary source. Not production.

Answers the question: *how is per-concept read/listen status + resume position surfaced in the UI — browse list badges, concept detail, resume entry point — how do status transitions happen, and how is resume position stored/restored across sessions?*

**Three structurally-different variants**, switchable via the floating bottom bar:

- **A — Badge-first**: explicit status badges on browse rows + Reader, a linear progress bar in the Reader, and manual status transitions ("Mark as done" / "Re-read" buttons). Resume lists IN_PROGRESS/REVISITING with a fraction bar.
- **B — Resume-first**: Resume is the hub — large ring cards with "Continue at X%". Reader auto-transitions: opening a concept starts the pass, scrolling to the end auto-finishes it. No badges in Browse — just status dots.
- **C — Minimal**: no badges at all. Browse filters by status via chips, rows carry a color accent; Reader shows a thin color accent + percent and a quiet status line. Transitions still happen on open/end but nothing is labelled.

**All three share one interaction core** (the thing being prototyped): the status model `NEW → IN_PROGRESS → CONSUMED → REVISITING`, a single char-offset resume position per concept, scroll position mapped to char offset (restored on reopen), and `CONSUMED` normalised to `position = bodyLength` (mirroring api-surface.md).

State lives in-memory in `FakeConceptRepository` (a `StateFlow<Map<String, Progress>>`) — persistence is the thing being checked, not something the prototype depends on.

## Verdict (resolution of #130)

**A's surfacing with B's Reader.** Browse rows + Resume cards carry the explicit status badges from A; the Reader follows B — ring progress in the header, no manual buttons, transitions are automatic (open starts the pass `NEW → IN_PROGRESS`, scrolling to the end auto-finishes `→ CONSUMED`, re-opening a finished concept `→ REVISITING`). Resume position stays a single char-offset, restored on reopen, `CONSUMED` → `position = bodyLength`.

## Run

One command (Android; iOS requires Xcode on macOS):

```
./gradlew :androidApp:assembleDebug
```

iOS framework compile check:

```
./gradlew :shared:compileKotlinIosSimulatorArm64
```

