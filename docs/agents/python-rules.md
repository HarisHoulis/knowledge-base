# Python Rules

Language-specific conventions for Python code in this repo, mirroring the conventions in `pyproject.toml`, `docs/agents/testing.md`, and the global guardrails. Each carries its rationale.

1. **Interpreter** — Always use `python3`, never bare `python` (e.g. `python3 -m pytest`).
   - *Rationale:* This system has no `python` binary; bare `python` fails or silently invokes the wrong interpreter.

2. **Typing** — New and edited code is mypy-typed; run mypy on changed files.
   - *Rationale:* Static types turn a class of runtime failures into compile-time ones and keep the type surface explicit for readers and the type checker.

3. **Lint defaults** — Follow ruff defaults as configured in `pyproject.toml` (line-length 88, target py39, selected rule sets); keep files clean under ruff.
   - *Rationale:* Consistent formatting and lint keep diffs reviewable and match the repo's existing CI gate.

4. **Injectable-callable seam** — For testable units, inject a callable (e.g. `*, audit_fn=None`) rather than mocking third-party libraries or making real calls, per `docs/agents/testing.md`.
   - *Rationale:* Injectable callables make unit tests deterministic, fast, and free of environment dependencies; mocks couple tests to library internals.

5. **Integration gating** — Mark tests that hit the real LLM API `@pytest.mark.integration`; don't run integration tests automatically — notify the user of the command (`pytest -m integration`).
   - *Rationale:* Integration tests need `LLM_API_KEY` and real API access; gating keeps default runs fast and hermetic while preserving the deeper suite for CI.

6. **Standard-library-first** — Prefer native framework / standard-library utilities over new third-party dependencies.
   - *Rationale:* Each added dependency is a maintenance and supply-chain cost; the standard library covers most needs without it.
