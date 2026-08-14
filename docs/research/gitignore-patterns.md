# What other patterns should this repo's `.gitignore` contain?

Question: the repo's `.gitignore` (a Python project using pytest, mypy, ruff, pre-commit, GitHub Actions, shell scripts) contains only `state.json`, `.DS_Store`, `*.egg-info/`, `__pycache__/`, `.ai/plans/`. Which patterns are missing, and which are obsolete?

## Recommendations

Concrete, minimal list. Verified against the repo as of 2026-08-14 (`git status --short --ignored`, `git check-ignore -v`, `pyproject.toml`, `.pre-commit-config.yaml`, `.github/workflows/*.yml`, `scripts/daily-ingest.sh`, `kb_pipeline/config.py`).

### Python tooling & caches (ADD)

- `.pytest_cache/` — pytest's default cross-session cache dir.
- `.mypy_cache/` — mypy's incremental type-check cache dir (always written unless pointed at `/dev/null`).
- `.ruff_cache/` — ruff's default cache dir.
- `*.py[cod]` (optional) — loose bytecode files; `__pycache__/` already covers Python 3's bytecode dirs, so this is belt-and-braces for legacy layouts.

All three cache dirs currently *appear* ignored only because mypy, pytest, and ruff each write a `*`-ignoring `.gitignore` inside their own cache dir (`git check-ignore -v` reports `.mypy_cache/.gitignore:2:*`, `.pytest_cache/.gitignore:2:*`, `.ruff_cache/.gitignore:2:*`). The root `.gitignore` is the canonical, tool-documented place for them.

Not applicable now: coverage.py artifacts (`.coverage`, `htmlcov/`, `coverage.xml`) — the repo has no coverage config, plugin, or CI coverage step, so these would be speculative. Add if you adopt coverage.

### Build & packaging (ADD)

- `build/` — PEP 517 build output dir (not yet generated; CI uses `pip install -e .`).
- `dist/` — distribution archives output dir (same: not yet generated).
- Keep `*.egg-info/` — already present; the editable install in `ci.yml` (`pip install -e ".[dev]"`) generates the in-place `kb_pipeline.egg-info/` (currently ignored via `git check-ignore` → `.gitignore:3:*.egg-info/`).

`build/` and `dist/` are the standard packaging-output pair. Not yet produced by this repo, but cheap and conventional to ignore pre-emptively.

Not applicable: `/site` (mkdocs output) — no mkdocs config exists; `docs/` is plain markdown.

### Environment & secrets (ADD)

- `.venv/` / `venv/` — virtualenv directories; CI installs into the system interpreter, but a local venv is the standard dev workflow.
- `.env` / `.envrc` — local secrets (this repo already consumes `LLM_API_KEY`, `LLM_API_URL`, `LLM_MODEL`, cookie values via env vars; a local `.env` must never be committed).

### OS & editor noise

- macOS: keep `.DS_Store`. Add `__MACOSX/` and `._*` (resource forks) only if the repo distributes archives; other macOS template entries (`.AppleDouble`, `.Spotlight-V100`, `.fseventsd`, …) target volume/media trees, not a git working tree — not applicable here.
- Editor artifacts (Vim swap `*.sw[a-p]`/backup `*~`, `.idea/`, `.vscode/`): per Git's own docs these belong in the user-global `core.excludesFile`, not the repo file — not applicable here.

### REMOVE

- `state.json` — obsolete. Both `kb_pipeline/config.py:12` (`KB_STATE` defaults to `~/.kb-pipeline/state.json`) and `scripts/daily-ingest.sh:29` write it outside the repo, and `.github/workflows/daily-ingest.yml` caches `~/.kb-pipeline/state.json`. No `state.json` is tracked or ever generated in the repo tree. The root pattern does nothing.

Keep: `.ai/plans/` (deliberate convention — commit `6c8230a` dropped those files) and `__pycache__/`.

## Sources

### Ruff — `.ruff_cache/`

Ruff's settings docs: "By default, Ruff stores cache results in a `.ruff_cache` directory in the current project root" (`cache-dir` default `".ruff_cache"`).
https://docs.astral.sh/ruff/settings/#cache-dir

Ruff's default `exclude` list also names the dirs it expects to be tool dirs: `.mypy_cache`, `.ruff_cache`, `.venv`, `venv`, `dist`, `node_modules`, `__pypackages__`, `.pytype`, `.nox`, `.tox`, `.eggs` — corroborating that these are conventional ignored dirs.
https://docs.astral.sh/ruff/settings/#exclude

### mypy — `.mypy_cache/`

Mypy config docs: `cache_dir` default `.mypy_cache`; "the cache is only read when incremental mode is enabled but is always written to, unless the value is set to `/dev/null`". This repo runs `python3 -m mypy .` in CI and via pre-commit, so `.mypy_cache/` is produced locally.
https://mypy.readthedocs.io/en/stable/config_file.html#confval-cache-dir

### pytest — `.pytest_cache/`

Pytest cache docs show the default cachedir as `<project>/.pytest_cache` (e.g. `cachedir: /home/sweet/project/.pytest_cache`); the `cacheprovider` plugin is enabled by default.
https://docs.pytest.org/en/stable/cache.html

Note: this repo's `pyproject.toml` does **not** set `addopts = "-p no:cacheprovider"`, so the cache is active.

### pre-commit — no in-repo ignore needed

Pre-commit docs, "Managing CI Caches": "`pre-commit` by default places its repository store in `~/.cache/pre-commit`" (overridable via `PRE_COMMIT_HOME` or `XDG_CACHE_HOME`). Nothing is created in-repo, so pre-commit contributes no patterns to this `.gitignore`.
https://pre-commit.com/#managing-ci-caches

### github/gitignore — Python template (canonical collection)

The upstream Python template is the reference collection for almost every Python recommendation above: `__pycache__/`, `*.py[codz]`, `build/`, `dist/`, `*.egg-info/`, `htmlcov/`, `.tox/`, `.nox/`, `.coverage`, `.coverage.*`, `.pytest_cache/`, `.env`, `.venv`, `venv/`, `.mypy_cache/`, `.dmypy.json`, `.ruff_cache/`, `/site` (mkdocs).
https://github.com/github/gitignore/blob/main/Python.gitignore

### github/gitignore — macOS template

`Global/macOS.gitignore` lists `.DS_Store`, `.localized`, `__MACOSX/`, `.AppleDouble`, `.LSOverride`, `._*`, `.Spotlight-V100`, `.fseventsd`, `.Trashes`. Only `.DS_Store` (already present) is relevant to a working tree; the rest target volumes/media and are not applicable.
https://github.com/github/gitignore/blob/main/Global/macOS.gitignore

### github/gitignore — Vim template

`Global/Vim.gitignore` covers swap (`[._]*.sw[a-p]`), backup (`*~`), `.netrwhist`, `tags`. Per Git's own docs (below) these are better in the user-global excludes file; not recommended for this repo file.
https://github.com/github/gitignore/blob/main/Global/Vim.gitignore

### Git — `gitignore` pattern semantics

Git's `gitignore` manual documents the semantics that matter here:
- "If there is a separator at the end of the pattern then the pattern will only match directories" — so `__pycache__/`, `.mypy_cache/` etc. ignore the whole tree recursively.
- A pattern with no slash may "match at any level below the .gitignore level" — bare `__pycache__/` covers bytecode dirs at any depth.
- "Files already tracked by Git are not affected."
- Backup/temporary/editor files "generally go into a file specified by `core.excludesFile`" (the user-global ignore file) — the primary source for keeping editor noise out of the repo file.
- "It is not possible to re-include a file if a parent directory of that file is excluded" — relevant if you ever add negation patterns.
https://git-scm.com/docs/gitignore

### Python packaging — `build/`, `dist/`, `*.egg-info/`

The upstream Python template (above) is the authoritative pattern collection for these; the behaviors they cover are setuptools/PEP 517 build outputs. `kb_pipeline.egg-info/` is generated by the in-place editable install (`pip install -e .`) used in `ci.yml`; `build/` and `dist/` would come from `python -m build` / `pip wheel`, which this repo does not yet run.
https://github.com/github/gitignore/blob/main/Python.gitignore

### Repo source — `state.json` is obsolete

- `kb_pipeline/config.py:11-13`: `STATE_PATH` defaults to `$HOME/.kb-pipeline/state.json`.
- `scripts/daily-ingest.sh:29`: `KB_STATE="${KB_STATE:-$HOME/.kb-pipeline/state.json}"`.
- `.github/workflows/daily-ingest.yml`: caches `path: ~/.kb-pipeline/state.json`.
- `git ls-files` contains no `state.json`; `git status --ignored` shows none in the tree.
