# ADR 0003: Audit Subagent as LLM-Based Retry Loop

The pipeline writes LLM-generated concept files to a `drafts/` directory and runs two concurrent LLM-based audits (Classification + Content) before moving them to the canonical KB tree. A failing audit returns structured JSON feedback for a surgical LLM retry (max 2 iterations). Only the failing audit re-runs. Exhaustion creates a GitHub issue with the entry path and audit feedback.

Single-pass generation was simpler but insufficient for trust. A blocking inline LLM review with retries provides precision while keeping the pipeline self-correcting for the common case and explicit about failures for the edge case.
