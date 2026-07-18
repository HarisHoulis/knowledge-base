# Knowledge Base

Personal knowledge base organized by domain/subdomain. Ingested and cross-referenced via an automated pipeline.

## Structure

See [CONTEXT.md](CONTEXT.md) for the domain tree and pipeline architecture.

## Pipeline

`fetch.py` polls RSS feeds from trusted sources, extracts + classifies content via LLM, and writes to the appropriate domain path.
