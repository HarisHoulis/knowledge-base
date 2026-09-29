# ADR-0009: Disable thinking on the audit LLM call

The audit request now sends `{"thinking": {"type": "disabled"}}` and `max_tokens: 1000` (raised from 500), written inline in `audit._call_llm`. The audit model emitted hidden reasoning before its JSON verdict; with thinking enabled that reasoning consumed the output budget, so the visible `content` came back empty, `json.loads` raised, and `_run_audit` fail-closed to `{"pass": False}` — surfacing as the wave of "Audit exhaustion" issues. Raising the cap alone is a race against unbounded reasoning; disabling thinking removes the consumer of the budget so the verdict reliably fits.

Audit-only, not audit+classify: the classification call shares the request shape but is a separate call site with its own fix (`max_tokens` there is already 2000). Disabling thinking rather than only raising `max_tokens` is the actual-cause fix; the return contract, retry semantics, and escalation shape are unchanged.
