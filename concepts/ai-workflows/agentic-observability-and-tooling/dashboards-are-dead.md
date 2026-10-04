---
domain: ai-workflows
subdomain: agentic-observability-and-tooling
concept: dashboards-are-dead
title: Dashboards Are Dead: Why Agents Need Tool Search, Not More Tools
sources:
  - title: "Dashboards Are Dead — Sarah Simionescu, Composio"
    url: "https://www.youtube.com/watch?v=YiFqcu9YA38"
    author: "Sarah Simionescu"
    date: "2026-10-04"
---

# Dashboards Are Dead: Why Agents Need Tool Search, Not More Tools

Sarah Simionescu (Composio) opens with a confession: she used Datadog every day for six months but had never actually looked at its control panel. When a colleague asked to see a notification, the dashboard froze on her and she "had no idea where anything was" — not Datadog's fault, but hers, for using a dashboard without ever opening it. Her argument: the control panel is dead, and that is good news for everyone except the people who build dashboards (Simionescu).

The autopsy goes back to 2022: one prod bug meant five windows and five tools — read Slack, query Datadog, check PostHog for a session, fix the bug in VS Code, open a PR in GitHub — each with its own interface and its own query language (Datadog syntax, JQL, Slack search modifiers), redesigned on every release. Dashboards and query languages were, she argues, mere translation layers "because the machines on the other end couldn't understand what you really wanted" (Simionescu). In 2023 the "shine button" arrived: one click let an LLM sometimes write the right query, as long as the question didn't require more than two database connections. It soon became native to many tools.

Anthropic's MCP protocol (November 2024) promised an open standard for connecting AI systems to data sources, letting an agent like Claude generate and execute a request on your behalf. But MCP is only a channel, and it is up to the service to decide how to communicate with the agent — which makes reality "a mess for three reasons": agents don't learn (every conversation starts from scratch; skills are a band-aid), context bloat (loading more tools and skills degrades the model — a toolkit with over 200 tools makes the model "just sink," selecting the wrong tool or failing to resolve dependencies), and isolation (each MCP server knows only itself, so any task spanning two applications leaves the user to join it up). As she puts it, "MCP gave agents a door to every annex, but left them standing in thousands of separate rooms with no map and no memory of ever having been there" (Simionescu).

Her mock-up of the 2026 workflow: Claude connected to the Composio MCP, paste the Slack message link, and ask it to use Sentry and Datadog to find the root cause and create a draft PR. The agent first calls Composio's search to specify the task — retrieve three Slack messages, look for Sentry issues, look for Datadog logs — and Composio returns for each not only the necessary tools but also a plan for their use (Simionescu).

- Dashboards and per-tool query languages were translation layers between humans and data; users wanted answers, not toolbars (Simionescu).
- The 2023 "shine button" let LLMs write queries, but broke down when a question required more than two database connections (Simionescu).
- MCP (announced by Anthropic, November 2024) standardizes the channel to data, but leaves each service to define how it talks to the agent, so cross-app tasks still fall back on the user (Simionescu).
- Three failure modes of the current MCP reality: agents have no memory across conversations, huge tool lists blow up the context window and degrade tool selection, and each server is isolated (Simionescu).
- Proposed fix: an agent-facing search step that resolves the task to a minimal set of tools plus a plan for using them (Composio MCP demo) (Simionescu).