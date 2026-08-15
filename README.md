# Knowledge Base

Personal knowledge base organized by domain/subdomain. Ingested and cross-referenced via an automated pipeline.

## Structure

See [CONTEXT.md](CONTEXT.md) for the domain tree and pipeline architecture.

## Pipeline

`python -m kb_pipeline` polls RSS feeds from trusted sources, extracts + classifies content via LLM, and writes to the appropriate domain path.

## Fitness checks

CI enforces the `kb_pipeline/` architecture via `scripts/check-fitness.py` against `scripts/baselines.json`: a dependency matrix, module-set coverage guard, and per-module size baselines. See [docs/fitness-functions.md](docs/fitness-functions.md) for the diagrams and how to update baselines.

## Development

Linting and formatting run automatically on `git push` via pre-commit. Install the hook once:

```
pre-commit install --hook-type pre-push
```

To run the checks manually: `ruff check`, `ruff format --check`, and `mypy .`.
