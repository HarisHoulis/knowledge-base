# LLM Response Parse Failure in Daily Ingest

## Investigation

Issue #249 — research why daily-ingest runs log `[!] LLM response parse failed: Expecting value: line 1 column 1 (char 0)` and propose solutions with reasoning and trade-offs. Example run: [daily-ingest #34](https://github.com/HarisHoulis/knowledge-base/actions/runs/33773029847/job/100707782141).

---

## 1. What the warning means

The warning is raised exactly once in the codebase, in `classify_summarize` (`kb_pipeline/llm.py:85`), from a bare `json.loads(content)` at `llm.py:76`, where `content = body["choices"][0]["message"]["content"]`. The two observed messages decode as follows:

| Message | `json.loads` input | Meaning |
|---|---|---|
| `Expecting value: line 1 column 1 (char 0)` | `""` (empty string) | Provider returned a `200` with an **empty** `content` field. |
| `Expecting value: line 1 column 1 (char 0)` | string starting with a non-JSON char | `content` starts with prose or a markdown fence (`` ` ``), so the first token is not a JSON value. |
| `Unterminated string starting at: line N column M (char NNNN)` | valid prefix, cut mid-string | `content` was **truncated before the JSON closed** — generation stopped mid-answer. |

Both happen only after the HTTP call succeeded: a network/provider error would surface as `LLM request failed` (`llm.py:83`) and a valid-but-nonconforming object as `LLM output validation failed` (`llm.py:79`). In the reference run there were **0** of those — every failure was a `200` whose payload could not be parsed.

---

## 2. Where it happens and what the code does today

### `classify_summarize` (`kb_pipeline/llm.py:36-86`)

- Sends `POST {LLM_API_URL}/chat/completions` with `response_format: {"type": "json_object"}`, `temperature: 0.3`, `max_tokens: 2000`, timeout 60, non-streaming.
- The environment in the reference run (visible in the archived job's step env) is: `LLM_API_URL=https://api.deepseek.com/v1`, `LLM_MODEL=deepseek-v4-flash`.
- The request does **not** send a `thinking` parameter — DeepSeek's documented default is **thinking mode enabled, effort `high`** ([thinking mode guide](https://api-docs.deepseek.com/guides/thinking_mode)), and in that mode `temperature`/`top_p` are accepted but **silently ignored**.
- On `JSONDecodeError` (or `KeyError`/`IndexError`/`TypeError`) it logs the warning and returns `None` (`llm.py:84-86`).
- It never inspects `finish_reason`, `usage.completion_tokens_details.reasoning_tokens`, or the raw `content`; the log line therefore cannot distinguish empty-vs-truncated-vs-fenced, nor say why generation stopped.

### Downstream handling (`kb_pipeline/pipeline.py`)

- `run_pipeline` calls `classify_fn(text, entry)` at `pipeline.py:428`; a `None` result increments `skipped` and `continue`s (`pipeline.py:429-431`).
- The URL hash is **not** marked processed on that path (`processed.add(h)` only runs later, `pipeline.py:467-468`), so a parse-failed entry is retried on the next run if it is still in the feed. Net effect: transient drop for that run plus wasted API time, **not permanent data loss**.
- The warning itself carries no entry title/URL, so correlating failures to sources from logs is manual.

### Adjacent risk — audits fail open (`kb_pipeline/audit.py`)

The audits hit the same endpoint/params (`response_format: json_object`, thinking default-on) and parse with `json.loads` at `audit.py:116`, but any parse/request failure logs `audit failed` and returns `{"pass": True}` (`audit.py:119-127`). A malformed audit response therefore **promotes content without verification**. Not the warning under investigation (different message), but the same root cause — worth its own ticket.

---

## 3. Evidence from the reference run

- Mode: `workflow_dispatch` dry-run, `--limit=10 --audit`; 19 sources, 313 seen, 38 written, 275 skipped.
- **13 parse failures total: 10× `Expecting value … (char 0)`, 3× `Unterminated string …`.** 0 request errors, 0 validation failures. Interleaved with successful parses in the same run → intermittent, endpoint-level.
- Timing: each failing call occupies ~16 s — a full completion attempt, not a fast error.
- DeepSeek's official JSON Output guide documents both failure modes:
  - > "When using the JSON Output feature, the API may occasionally return empty content. We are actively working on optimizing this issue." ([JSON Output guide](https://api-docs.deepseek.com/guides/json_mode))
  - > "the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens`" ([chat-completions reference](https://api-docs.deepseek.com/api/create-chat-completion))

---

## 4. Root-cause analysis

**Primary cause — the DeepSeek endpoint intermittently returns empty or truncated `content` on `200`, and the code treats any unparseable body as a hard failure.**

Two documented DeepSeek behaviors explain the specific shapes:

1. **Empty `content` (`Expecting value … char 0`)** — DeepSeek explicitly acknowledges that JSON Output mode "may occasionally return empty content". This is the dominant signature (10/13) and requires no further local condition.
2. **Truncated `content` (`Unterminated string`)** — generation hit the `max_tokens` ceiling (`finish_reason: "length"`) before the JSON object closed. `max_tokens: 2000` is the binding cap, and with thinking mode **on by default at high effort** the budget is shared between the chain-of-thought (`reasoning_content`, surfaced as `usage.completion_tokens_details.reasoning_tokens`) and the visible answer. Long, ambiguous 15k-char inputs provoke heavy reasoning, which starves the answer budget — consistent with a visible cut at ~2.8k chars (~700 visible tokens, the rest consumed by reasoning) and, at the extreme, an all-reasoning response with empty `content`.

**Contributing factors**

- `temperature: 0.3` is intended to keep classification deterministic, but is ignored while thinking is enabled — the determinism goal is not being met.
- The JSON-mode recipe is only half followed: the prompt names the fields but gives **no example object** and no "output only the JSON object" clamp. DeepSeek's guide calls for the word "json" plus an explicit example; `json_object` is guidance, not constrained decoding.
- No client resilience: no retry on transient empty/truncated bodies, no `finish_reason`/usage inspection, no defensive extraction (e.g. fence stripping).
- No observability: the log drops `finish_reason`, usage, and raw content, so the empty-vs-truncated split above cannot be confirmed per call from archived logs — it is inferred.

---

## 5. Impact

- **No permanent data loss.** A parse-failed URL is not added to `processed_hashes`, so it is retried on a later run while still in the feed window.
- Per occurrence: ~16 s of run time and a wasted completion (~2k output tokens). At ~25% of classify attempts in the reference run, this meaningfully inflates run duration and cost and buries real warnings.
- Persistent entries (one that reliably triggers high-effort reasoning) can log the warning every run indefinitely, which is how the operator noticed it.

---

## 6. Proposed solutions

Options are ranked by leverage-per-effort. Items **A–C** are independent; **D/E** are follow-ups.

### A. Fix the DeepSeek request configuration (lowest effort, likely largest effect)

Change the request in `classify_summarize` and `audit._call_llm`:

1. **Disable thinking for structured JSON output** — `thinking: {"type": "disabled"}` via `extra_body` (OpenAI SDK) / body field. This returns the full `max_tokens` budget to the answer, makes `temperature` effective again, and matches DeepSeek's documented toggle.
   - Trade-offs: loses chain-of-thought quality for the classification/summary step. For deterministic structured extraction that is an acceptable (arguably desirable) loss; if summary quality regresses, keep thinking on but combine with (2).
2. **Raise `max_tokens`** from 2000 (classify) / 500 (audit) to give real headroom — cost is per token actually generated, so a higher cap is nearly free in the common case and only protects against truncation.
   - Trade-offs: none meaningful at this volume; a runaway answer costs slightly more, mitigated by the validation + retry loop below.
3. **Complete the JSON-mode prompt recipe** — add a one-shot example object and a "respond with only the JSON object, no markdown, no prose" line to `SYSTEM_PROMPT`.
   - Trade-offs: prompt is shared state; validate that field coverage/output quality doesn't drift (the dry-run is the cheap check).

### B. Add observability (prerequisite to proving A worked)

In the failure handler of `classify_summarize`, log: `finish_reason`, `usage` (completion vs reasoning tokens), `len(content)` plus a short (≤200 char) excerpt, and the entry `title`/`link` from `meta`.

- Trade-offs: none — pure diagnosis. This is what converts "occasional parse failed" into "empty content, `finish_reason: length`, 1999 reasoning + 1 completion tokens on entry X", which pins the fix.

### C. Add one retry on empty/truncated bodies

Before returning `None`, retry once when `content` is empty/whitespace-only or `finish_reason == "length"` (optionally feeding the fragment back), consistent with DeepSeek's "occasionally" framing.

- Trade-offs: retry costs a second completion on the failure path only; guards against transient empties without masking a systematic misconfiguration (a persistent failure still returns `None` and shows up in stats). Do **not** retry indefinitely — one retry, mirroring the existing audit-retry ethos.

### D. Defensive parse (low priority)

Strip ``` fences and attempt extraction of the first `{…}` span before `json.loads` as a last resort.

- Trade-offs: rescues fence-wrapped or prose-prefixed responses, but can mask genuine model non-compliance; keep it clearly subordinate to A/C. DeepSeek only returns valid JSON when generation completes, so with A+C this is nearly dead code.

### E. Surface the failure rate

Count parse failures distinctly (e.g. a `llm_failed` stat and/or a `logger.warning` per entry with title/URL), optionally aggregating into a GitHub issue when the rate crosses a threshold — mirroring the existing Content Extraction Error surfacing pattern.

- Trade-offs: visibility vs issue noise; a threshold avoids paging the operator on a single blip.

### F. Adjacent (own ticket): audits must not fail open

Change `audit._run_audit` to treat an unparseable audit response as a failed audit (retry/escalate) instead of `{"pass": True}`.

- Trade-offs: correct-by-construction (malformed audits must not auto-pass content) but it is a behavioral change outside this ticket's scope.

---

## 7. What NOT to do

- **Do not switch providers or model.** The failure is intermittent, documented upstream, and addressable client-side.
- **Do not switch to `response_format: {"type": "json_schema"}`** — DeepSeek's API accepts only `text` and `json_object`; `json_schema` is rejected with a `400` ([chat-completions reference](https://api-docs.deepseek.com/api/create-chat-completion)).
- **Do not "fix" data loss** — there is none to fix; the retry-on-next-run behavior is already correct and should be preserved.

---

## 8. Recommendation summary

**Ship A(1) + A(2) + B together, validate with a dry-run, then add C.** The observed signatures are two documented DeepSeek JSON-mode failure modes, both aggravated by thinking-mode-on-by-default consuming the 2000-token budget and by the request not disabling it. Disabling thinking and raising the cap attack the mechanism directly; the logging improvement makes the fix verifiable from the next run's logs. E and F are worthwhile but separate tickets; D is optional insurance.

Verification: the same dry-run (`--limit=10 --audit`) after the change should show zero `LLM response parse failed` warnings and zero regression in "would write" counts; `B` makes the reason auditable if any remain.
