# Rules Compliance (Fitness Functions)

Every rule in `architectural-rules.md`, `design-rules.md`, `python-rules.md`, `agentic-execution.md`, and `plan-execution.md` carries a designated enforcement mechanism (architectural-rules #8, Ch. 6): unenforced decisions decay silently, so nothing in the five files is left to chance.

Two tiers:

- **CI tier** — mechanical, gated by `scripts/check-rules.sh`, `scripts/check-fitness.py`, or the existing Python toolchain. Fails the build on violation.
- **Review tier** — enforced per-diff by the auto-code-review Standards sub-agent. Trade-off statements (architectural #4) and variance (architectural #9) additionally surface in PR review notes.

## Enforcement matrix

| Rule | Tier | Vehicle |
| --- | --- | --- |
| architectural #1 Modularisation | CI + Review | `check-fitness.py` dependency matrix; auto-code-review Standards axis |
| architectural #2 Extensibility over implementation | Review | auto-code-review Standards axis |
| architectural #3 Expose only what's needed | CI + Review | `check-fitness.py` dependency direction; auto-code-review Standards axis |
| architectural #4 Trade-off awareness | Review | Standards axis; trade-off surfaced in PR review notes |
| architectural #5 Why over how | Review | auto-code-review Standards axis |
| architectural #6 Guidance, not prescription | Review | auto-code-review Standards axis |
| architectural #7 Right-size decisions | Review | auto-code-review Standards axis |
| architectural #8 Compliance / fitness functions | CI | this map + `check-rules.sh` |
| architectural #9 Variance process | Review | Standards axis; variance surfaced in PR review notes |
| design #1 Composite use-cases | Review | auto-code-review Standards axis |
| design #2 Small complexity, small mental overhead | Review | auto-code-review Standards axis |
| design #3 High cohesion, low coupling | Review | auto-code-review Standards axis |
| design #4 Reusable + autonomous components | Review | auto-code-review Standards axis |
| design #5 Prefer weaker connascence | Review | auto-code-review Standards axis |
| design #6 Structural decay alert | CI + Review | `check-fitness.py` `pipeline.py` size baseline; auto-code-review Standards axis |
| python #1 Interpreter | CI | `check-rules.sh` bare-`python` scan |
| python #2 Typing | CI | `python3 -m mypy .` |
| python #3 Lint defaults | CI | `python3 -m ruff check .` + `ruff format --check` |
| python #4 Injectable-callable seam | Review | auto-code-review Standards axis |
| python #5 Integration gating | CI | pytest `addopts` in `pyproject.toml` |
| python #6 Standard-library-first | Review | auto-code-review Standards axis |
| agentic-execution #1–4 | Review | auto-code-review Standards axis |
| plan-execution #1–4 | Review | auto-code-review Standards axis |

## Notes

- **Fitness-function baselines** — `check-fitness.py` guards the `kb_pipeline/` intra-package dependency matrix (full allow-list, any unlisted edge fails) and a `pipeline.py` line-count baseline in `scripts/baselines.json` with a +10% tolerance; the baseline is bumped explicitly via `--update-baseline`. The matrix checks dependency direction only — cohesion, minimum public surface, and other structural decays stay on the Review axis.
- **AGENTS.md `@reference` resolution** — extra CI check in `check-rules.sh`: every `@path` under the External File Loading block must resolve to an existing file.
- **python-rules #3's cited config values** are deliberately **not** CI-checked as values; the ruff gate itself enforces them.
- **Bare-`python` scan scope** — scans executable/config text (`scripts/`, `tests/`, `.github/workflows/`, `AGENTS.md`, `pyproject.toml`), not `docs/` prose: the rules themselves and fenced code snippets describe bare `python` without invoking it.
