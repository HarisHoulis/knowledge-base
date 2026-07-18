# ADR 0002: Python Package over n8n / Make.com

The pipeline is a Python package (`kb_pipeline`) rather than a visual workflow in n8n (self-hosted) or Make.com (SaaS).

An orchestrator would provide a visual DAG, retry logic, error notifications, and a UI for monitoring. However, the pipeline has exactly one linear path (fetch → extract → classify → write) with no branching or conditional retry logic — a minimal package matches the complexity. n8n adds Docker overhead and a learning curve; Make.com costs $9-16/mo. If the pipeline grows to need DAG branching, parallel processing, or multi-step error recovery, migrating to an orchestrator is straightforward because the individual functions are already isolated.
