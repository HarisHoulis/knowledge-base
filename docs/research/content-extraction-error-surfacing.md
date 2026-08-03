# Content-Extraction Error Surfacing

## Investigation

Issue #33 — investigate and recommend a mechanism for capturing trafilatura content-extraction errors and surfacing them as GitHub Issues.

---

## 1. Error source

**Finding: Python logger, not C-library stderr.**

Trafilatura emits messages like `parsed tree length: 1`, `empty HTML tree`, and `discarding data` through Python's standard `logging` module via `logging.getLogger("trafilatura")`. These are typically at `INFO` or `DEBUG` level — not from a C extension on stderr.

The full logging path is:

```
trafilatura.core / trafilatura.utils
  → logging.getLogger("trafilatura").info/debug(...)
    → logging.basicConfig handler in cli.py
      → stdout
```

In `cli.py:27` the trafilatura logger is pinned to `WARNING`, which suppresses these messages during normal operation. Even if the level were lowered to `INFO`, the messages would only appear in stdout logs — they are not captured as structured data anywhere.

### Two failure modes

| Mode | Trigger | Current handling |
|------|---------|-----------------|
| **Silent empty** | `trafilatura.extract(html)` returns `None` or empty string when the page has no extractable content (JS-rendered, paywall, non-article) | `extract_text` converts `None` to `""` via `or ""`. The caller (`pipeline.py:164`) sees an empty string, checks `len(text) < 200`, logs "skipping (too short)", and continues. **No error is raised or recorded.** |
| **Exception** | `trafilatura.extract(html)` raises an exception (e.g., lxml parser error on malformed HTML) | No `try`/`except` around the call in `extract_text()` (`fetcher.py:125-130`). The exception propagates uncaught and crashes the pipeline. |

---

## 2. Existing patterns

`_escalate_failure` in `pipeline.py:38-56` creates a GitHub issue via `gh issue create`. It is:

- **Well-isolated** — injected as the `escalation_fn` dependency in `_audit_with_retry`.
- **Stubable** — tests already use `make_escalation_stub()` to capture calls.
- **Reusable** — its signature `(url: str, entry_path: Path, feedback: str)` is generic enough for extraction errors, though the title is hardcoded to "Audit exhaustion: {filename}".

The `gh issue create` subprocess call is shared infrastructure: `GITHUB_TOKEN` is available on GitHub Actions runners, and `FileNotFoundError`/`CalledProcessError` are handled gracefully.

---

## 3. Deduplication

**Recommendation: One cumulative issue per run, not one per error.**

| Approach | Pros | Cons |
|----------|------|------|
| One issue per error | Self-contained, easy to close individually | 10–50+ issues on a bad run; buries real audit escalations |
| One cumulative issue per run | Single triage surface; easy to scan all failures at once | Harder to track individual resolution; issue title must be date-keyed |

**Decision:** Cumulative. The operator opens the daily "content extraction issues" issue, scans the list, and either fixes the source or closes it as a known transient. If the same entries fail repeatedly across runs, the recurring daily issue provides the signal.

Title format: `Content extraction errors: YYYY-MM-DD (N entries)`

---

## 4. Noise reduction

**What ticket #1 (link fallback) will eliminate:**
Entries where the RSS feed only provides a summary/blurb (no full HTML content) and the link fallback would fetch the real article page. Today these entries get the summary text passed to trafilatura, which often produces "empty HTML tree" or very short output.

**Remaining error sources after ticket #1:**
- Malformed HTML from the source origin server
- Paywalled or auth-gated pages (e.g., Medium member-only stories)
- Pages rendered entirely client-side (JS-generated DOM)
- Temporary network or server errors at fetch time

**Actionability assessment:**
- Paywall/auth errors → actionable: the source needs cookie headers or should be filtered
- Client-side rendered → actionable: the source is incompatible with trafilatura and should be reconsidered
- Malformed HTML → actionable: may indicate a source regression worth investigating
- Transient fetch errors → not actionable individually, but a pattern across runs is

**Verdict:** The remaining errors are actionable enough to warrant surfacing. A transient blip causes one issue; actual source problems are caught.

---

## 5. Frequency control

**Recommendation: No threshold in the first implementation.**

- If even one extraction failure occurs, the operator should know — it may indicate a broken source.
- If noise becomes a problem (e.g., a source consistently produces 1 transient failure per run), the operator can add a `MIN_FAILURES` constant later.
- A threshold of `>=3` would be a sensible default if one is demanded, but start without it.

---

## Proposed design

### Changes

**`kb_pipeline/fetcher.py`** — Wrap `trafilatura.extract()` in a try/except and collect errors:

```python
def extract_text(html: str) -> str:
    if not html.strip():
        return ""
    if not html.strip().startswith("<"):
        return html.strip()
    try:
        result = trafilatura.extract(html, output_format="markdown", include_links=True)
        return result or ""
    except Exception:
        logger.warning("  [!] trafilatura extraction failed", exc_info=True)
        return ""
```

Additionally, set up a `logging.Handler` on the `trafilatura` logger at `INFO` level to capture silent-failure messages before they are suppressed. Or, simpler: lower `trafilatura`'s logger level to `INFO` during extraction and watch for messages matching known patterns. The simplest approach is a dedicated handler that buffers messages from `trafilatura` into a list that `run_pipeline` can inspect.

**`kb_pipeline/pipeline.py`** — Add extraction-error collection to `run_pipeline`:

1. Before the entry loop, initialise an empty list for extraction errors.
2. After `extract_text(content)` (line 164), check if `text` is empty AND there was a trafilatura log capture → record `(url, entry_title, error_message)`.
3. After all entries are processed, if the list is non-empty, call a new `_escalate_extraction_failures()` that creates a single GH issue with the cumulative list.

Reuse `_escalate_failure`'s internals (the `gh issue create` subprocess call) but with a different title and a body that lists all entries rather than one.

### Test plan

| Test | What it verifies |
|------|-----------------|
| `extract_text` wraps trafilatura exceptions → returns `""` | Exception safety |
| Pipeline collects extraction errors across entries | Cumulative collection |
| Pipeline creates one GH issue with the cumulative list when errors exist | Integration with escalation |
| Pipeline does not create an issue when no errors occur | Clean-run silence |

### Implementation cost

| File | Lines |
|------|-------|
| `fetcher.py` | ~10 (try/except around extract) |
| `pipeline.py` | ~40 (error collection, cumulative escalation function, wiring) |
| `test_fetcher.py` | ~15 (exception-safety test) |
| `test_pipeline.py` | ~25 (collection + escalation tests) |
| **Total** | **~90** |

### Recommendation summary

**Build it.** The feature is low-cost (~90 lines), uses existing infrastructure (`_escalate_failure` pattern, `gh issue create`, dependency injection), and addresses a real gap — every extraction error today is either silently swallowed or crashes the pipeline. The cumulative-per-run approach keeps noise manageable while ensuring the operator is aware of failing sources.
