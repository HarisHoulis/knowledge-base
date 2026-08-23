# Markdown Rendering in the CMP Reader (Android + iOS)

## Question

How should the Reader render concept bodies and takeaways (markdown strings served over REST) in a Compose Multiplatform app targeting Android and iOS? The app scaffold (#129) and progress UX (#130) settled navigation and progress, but not content rendering. The recommendation must cover: multiplatform library landscape + maturity, plain-text fallback vs full markdown, link handling, how body/takeaways map to the settled Reader layout — and, decisively, how a renderer interacts with the settled progress model: **one shared char-offset per concept** (read/listen share it; TTS consumes the same offset, per #125/#126/#130 and the on-device TTS research).

Decision ticket: wayfinder research ticket #187 ("Choose how the Reader renders markdown in CMP"). Research only — no production code.

## Context

- Stack: Kotlin 2.4.10, Compose Multiplatform 1.11.1 stable, targets Android + iOS only.
- Content shape: 786 concept `.md` files (YAML frontmatter + body + takeaway bullets). The DB is canonical; the backend serves bodies/takeaways as markdown strings over REST behind `ConceptRepository`.
- The settled Reader layout (#130, variant B) renders plain `Text(body)` + labeled takeaways, restores position by scrolling to `restoreFraction × scrollState.maxValue`, and reports position back as `fraction × bodyLength` (`ReaderScreen.kt` in `prototype/progress-tracking`).
- Progress constraint: exactly **one** char offset per concept, shared between reading and listening. The TTS research (`docs/research/cmp-on-device-tts.md`) already fixed the unit as a *character offset into the concept's plain-text content (markdown stripped)*. Any markdown renderer must not fork this coordinate system.

## Sources

- [mikepenz/Multiplatform-Markdown-Renderer](https://github.com/mikepenz/Multiplatform-Markdown-Renderer) — README, release [v0.44.0](https://github.com/mikepenz/Multiplatform-Markdown-Renderer/releases/tag/v0.44.0) (2026-08-18), `ReferenceLinkHandler.kt`, `AnnotatedStringKtx.kt` (link handling), module layout
- [halilozercan/compose-richtext](https://github.com/halilozercan/compose-richtext) — README ("very experimental", "lacks iOS support"), [docs](https://halilibo.com/compose-richtext/), release 1.0.0-alpha05 (2026-06-08)
- [noties/Markwon](https://github.com/noties/Markwon) — repo metadata, release v4.6.2 (2021-02-08)
- [JetBrains/markdown](https://github.com/JetBrains/markdown) — `ASTNode.kt` (`startOffset`/`endOffset`), repo pushed 2026-08-20; Maven Central `org.jetbrains:markdown`
- Corpus analysis: regex scans over all `concepts/**/*.md` (786 files), run for this ticket
- Prototype reader: `git show prototype/progress-tracking:app/shared/src/commonMain/kotlin/io/kb/app/ui/reader/ReaderScreen.kt` and `ReaderViewModel.kt`
- Sibling research: `docs/research/cmp-on-device-tts.md` (settles the shared char-offset position model)

## Findings

### 1. Corpus reality: the markdown used is nearly plain prose

Regex scans across all 786 concept files (`concepts/**/*.md`):

| Feature | Files containing it | % of corpus |
|---|---|---|
| H1 heading (`# Title`) | 786 | 100% |
| Bullet lists (takeaways) | 786 | 100% |
| Inline code `` `…` `` | 86 | 10.9% |
| Absolute `http(s)` links `[text](url)` | 20 | 2.5% |
| Italics (genuine, e.g. *Morus bassanus*) | 2 | 0.3% |
| Fenced code blocks (``` ``` ```) | 0 | 0% |
| Tables (`\|…`) | 0 | 0% |
| Images (`![…]`) | 0 | 0% |
| H2–H6 headings | 0 | 0% |
| Blockquotes / numbered lists / hrules* / strikethrough | 0 | 0% |
| Raw HTML tags | 0 | 0% |
| Internal (non-http) markdown links | 0 | 0% |

\* The `^---$` hits in every file are the YAML frontmatter delimiters, not horizontal rules — frontmatter is stripped before the body reaches the app. Apparent raw-HTML matches were all false positives inside inline-code spans (e.g. `` `List<Item>` ``).

Implications: full GFM coverage is unnecessary today; inline styling (code spans, emphasis), lists, paragraphs, and clickable external links cover essentially 100% of real usage. Every body begins with an H1 that duplicates the frontmatter title shown in the Reader header, so the leading H1 should be dropped from the rendered body region.

### 2. Candidate landscape (verified against primary sources, Aug 2026)

| Candidate | KMP Android+iOS | Maturity / maintenance | Markdown coverage | Link handling | Offset-mapping feasibility | Deps added |
|---|---|---|---|---|---|---|
| **mikepenz `multiplatform-markdown-renderer`** v0.44.0 | Yes — Android, iOS, Desktop, Web, macOS | Strong: Apache-2.0, 1k★, releases Jun + Aug 2026, Renovate-driven, CI + build provenance | Full CommonMark + GFM (tables, task lists, alerts) out of the box | `LinkAnnotation.Url` + `linkInteractionListener` (modern CMP API) | Good — components expose the `ASTNode`, which carries `startOffset`/`endOffset` into the source string | Core `-m3`/`-m2` module + transitive `org.jetbrains:markdown` (actively maintained) |
| **compose-richtext** (`richtext-commonmark`) 1.0.0-alpha05 | **No iOS** — README: "All modules are Compose Multiplatform compatible but lacks iOS support" | Self-described "very experimental"; alpha cadence (~1/yr); author warns roadmap unclear | CommonMark-based | `LinkClickHandler` in richtext-ui | n/a — disqualified on platform support | — |
| **Markwon** v4.6.2 | No — Android Views only | Effectively dormant: last release Feb 2021, last push Apr 2024 | Excellent (Android) | Android-native | n/a — disqualified: not Compose, not KMP; using it only in `androidApp` forks the Reader into two implementations | — |
| **`org.jetbrains:markdown` parser + hand-rolled Compose renderer** | Yes (pure Kotlin) | Parser actively maintained (pushed Aug 2026, v0.7.x) — but the renderer would be ours forever | Whatever we implement | Ours (`LinkAnnotation.Url` directly) | Best — we own the AST→rendered-position mapping end to end | One small pure-Kotlin parser dep |
| **Plain-text fallback** (current prototype `Text(body)`) | Yes | n/a — zero deps | None — raw syntax shows for the 86 files with inline code and 20 files with links | None (links dead) | Exact — already implemented | None |
| Newer 2025–2026 entrants | — | Nothing else found that is real, maintained, and KMP-with-iOS; M2D/"Compose-Markdown" names from the ticket did not resolve to maintained projects on verification | | | | |

### 3. The decisive factor: interaction with the shared char-offset model

The settled model stores **one char offset per concept**, shared by read and listen. The TTS research already pinned the unit: an offset into the concept's **plain-text projection** (markdown syntax stripped, computed deterministically). A markdown renderer does not change what is stored; it changes what must be *mapped*. Analysis per candidate:

**mikepenz renderer — feasible at block granularity, without forking.** It parses with `org.jetbrains:markdown`, whose `ASTNode` exposes `startOffset`/`endOffset` into the source string, and every `MarkdownComponents` override receives that node. Therefore:

- At parse time, walk the AST leaves and build a **plain-text projection index**: concatenate visible leaf text, recording `(plainStart, plainEnd) ↔ (srcStart, srcEnd)` per leaf. This is ~50–80 lines of commonMain code operating on the same AST the library already produces.
- **Restore:** given the saved plain-text offset, binary-search the index to find the owning block (paragraph/list item) and scroll so that block is at the top. Block granularity is strictly finer than the prototype's current scroll-fraction restore, which is what users accepted in #130.
- **Writes:** when scroll settles, report the first plain-text offset of the topmost visible block (same debounced `snapshotFlow` hook the prototype already has).
- Intra-block precision (line-level via `TextLayoutResult.onTextLayout`) is possible later but not required — the corpus's blocks are short paragraphs/bullets.

The stored coordinate never changes shape: still `Int` chars into the plain projection, still normalized server-side (`position = bodyLength` on mark-done, where `bodyLength` becomes `projection.length`). Read/listen stay interoperable.

**Hand-rolled renderer — feasible with best fidelity.** Same AST, same technique, but we own the mapping and can make it line-exact from day one.

**Plain-text fallback — exact, already done.** Zero mapping work; the current implementation *is* the fallback.

**compose-richtext / Markwon — moot.** Disqualified on platform grounds regardless of offset handling (richtext's `AstNode` from commonmark-java has optional source spans, but there is no iOS artifact; Markwon is Views-based Android).

### 4. Link handling

- Corpus contains only absolute `http(s)` links (20 files) and **zero internal concept cross-links**, so no in-app link routing is needed today.
- mikepenz renders links via Compose Multiplatform's `LinkAnnotation.Url(destination, style, linkInteractionListener)` (verified in `AnnotatedStringKtx.kt`), which resolves through the platform handler (`LocalUriHandler` → system browser) identically on Android and iOS. The `linkInteractionListener` is our future interception point if internal links ever appear in the corpus — no rework required.
- Hand-rolled would use the identical API. Plain-text fallback leaves links inert — a real (if small) UX gap: 20 concepts cite sources as dead text.

### 5. Mapping body/takeaways onto the settled Reader layout (variant B)

- **Header** (title, ring/badge, status) — unchanged; title comes from metadata, not the body.
- **Body region** — replace the single `Text(uiState.body)` with the renderer, dropping the leading H1 (duplicates the header title in 100% of files). Parse in the ViewModel (the library README explicitly recommends VM-side parsing to retain state across navigation — relevant to keeping scroll/resume stable), then pass the parsed state to the composable. Keep the `Column + verticalScroll(scrollState)` skeleton: the progress-restore/write logic hangs off `scrollState`; the library's `LazyColumn` variant can be revisited later if long documents ever become a problem (they aren't — bodies are paragraph-scale).
- **Takeaways** — they are uniformly short bullet items (100% of files). Keep the settled labeled "Takeaways" section; feed the item strings through the same renderer (or keep styled `Text` rows — visually equivalent for bare bullets). Either way the layout contract from #130 is preserved.

### 6. Effort estimate if hand-rolling instead

Honest estimate for `org.jetbrains:markdown` + hand-rolled commonMain rendering of the features the corpus actually uses (paragraphs, H1-only headings, bullet lists, bold/italic, inline code, links): roughly 400–800 LOC plus styling/theming parity with Material 3 and unit tests — about 2–4 focused days up front, plus permanent ownership of edge cases (nesting, escaping, reference links) that the corpus doesn't exercise yet but future ingested content might. The mikepenz library is exactly this work, already done and maintained.

## Recommendation

**Adopt `com.mikepenz:multiplatform-markdown-renderer-m3` (v0.44.x) for the Reader body, and keep the settled progress coordinate unchanged: a char offset into the concept's plain-text projection.**

Rationale, tied to #187's deliverable:

1. **It is the only candidate that passes the hard filters.** compose-richtext ships no iOS artifacts; Markwon is dormant Android-Views-only; nothing newer survived verification. mikepenz is Apache-2.0, actively released (v0.44.0, Aug 2026), targets both platforms from `commonMain`, and needs only its core + `-m3` module (plus the JetBrains markdown parser, itself actively maintained — no new unmaintained transitive risk).
2. **It satisfies the decisive char-offset constraint without forking.** Its components expose the underlying AST whose nodes carry source `startOffset`/`endOffset`; a small parse-time plain-text projection index gives offset↔rendered-block mapping for restore and write-back. Stored offsets remain plain-text based, so read/listen sharing and server normalization are untouched. Rendering forces a *bridge*, not a *new position model*.
3. **Full markdown costs almost nothing here and buys forward compatibility.** The corpus is markdown-light (no fences/tables/images/H2+ today), so rendering risk is minimal — but ingestion keeps adding content, and inline-code styling (10.9% of files) plus working citation links (2.5%) are immediate user-visible wins over the plain-text fallback. The fallback remains trivially available behind the Reader seam (swap the composable) if the dependency ever becomes a liability.

For the screen-map ticket: the Reader screen keeps its #130 variant-B structure; the only change inside the body region is `Text(body)` → `Markdown(markdownState)` with VM-held parse state, leading-H1 stripping, and the offset bridge in the ViewModel layer.
