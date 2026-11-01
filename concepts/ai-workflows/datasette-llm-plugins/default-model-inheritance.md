---
domain: ai-workflows
subdomain: datasette-llm-plugins
concept: default-model-inheritance
title: datasette-llm 0.1a9 Inherits LLM's Default Model
sources:
  - title: "datasette-llm 0.1a9"
    url: "https://simonwillison.net/2026/Oct/31/datasette-llm/"
    author: "Simon Willison"
    date: "2026-10-31"
---

# datasette-llm 0.1a9 Inherits LLM's Default Model

datasette-llm 0.1a9 is a small UX release for the plugin that underpins Datasette Agent. The main change is that the plugin now picks up the default model configured in LLM, so users no longer have to explicitly set a default model when starting Datasette Agent (source).

Previously, running Datasette Agent required an extra setting such as `-s plugins.datasette-agent.default_model gpt-6-astra`. With this release, a command like `uvx --with datasette-agent datasette content.db --internal internal.db` works without that configuration step (source).

The author notes that larger upgrades to Datasette Agent are in the pipeline, framing this release as an interim quality-of-life improvement to the underlying `datasette-llm` plugin (source).

- datasette-llm now inherits the default model from LLM, removing the need to configure one explicitly.
- Datasette Agent can be started without the `plugins.datasette-agent.default_model` setting.
- Described as a small UX improvement ahead of bigger Datasette Agent upgrades.