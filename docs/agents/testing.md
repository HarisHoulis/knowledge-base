# Testing conventions

## Seam pattern

Inject a callable (`*, audit_fn=None`) rather than mocking third-party libraries or making real calls. The callable receives a prompt string and returns a raw response string; the unit under test handles parsing and error recovery.

This keeps tests deterministic, fast, and free of environment dependencies.

## Test directories

| Suite | Location | Marker | Requires | Run with |
|---|---|---|---|---|
| Unit | `tests/` | — | nothing | `pytest` (default) |
| Integration | `tests/integration/` | `@pytest.mark.integration` | `DEEPSEEK_API_KEY` | `pytest -m integration` |

Integration tests are excluded from the default `pytest` run via `addopts = "-m 'not integration'"` in `pyproject.toml`.

## Example

The audit module (`kb_pipeline/audit.py`) exposes `audit_fn` on both `content_audit` and `classification_audit`. See `tests/test_audit.py` for stub injection, prompt verification, and error-path coverage.
