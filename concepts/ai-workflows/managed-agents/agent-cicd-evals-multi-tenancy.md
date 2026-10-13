---
domain: ai-workflows
subdomain: managed-agents
concept: agent-cicd-evals-multi-tenancy
title: Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy
sources:
  - title: "Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4)"
    url: "https://www.youtube.com/watch?v=QSeaZ6qHyXs"
    author: "AI Engineer"
    date: "2026-10-12"
---

# Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy

This Q&A session from Anthropic's AI Engineer talk covers operational questions about running managed agents. For CI/CD, Anthropic provides a CLI called NCLI that wraps their API and works like Terraform: long-lived resources are declared in YAML within the codebase, and CI/CD pipelines update NCLI whenever those resources change. Anthropic reports using the same approach internally to create reliable, long-lasting resources.

On message timing, you can queue messages while the model is doing other work, but not while it is waiting for the result of a special tool. Execution is paused at that point, and the system expects you to send the tool result; for consistency, calls are blocked during this window, and sending a message anyway returns a 400 error.

For evals, Anthropic runs extensive evaluations whenever new models or capabilities emerge, using internal tools over different datasets to run sessions at scale (e.g. 10,000 sessions in parallel in the cloud), then analyzes results and adjusts prompts and assumptions to remove what is no longer needed. The advice for users is to use high-quality data for evaluation, since garbage in is garbage out; vague grading criteria (e.g. "get 100%") are not meaningful for performance. A practical approach is to review past sessions, evaluate the results, and build a dataset from historical session analysis.

On multi-tenancy, resources are tied to a workspace, and any API key within that workspace can access them. A Claude platform administrator configures workspaces for the organization and decides who has access to which space, so workspaces should be designed around access control—grouping people who should share access to given resources into one space.

- NCLI is a Terraform-like CLI wrapping the API: declare long-lived resources in YAML in your codebase and drive updates via CI/CD; Anthropic uses it internally.
- Messages can be queued while the model does other work, but not while it waits for a special tool result—execution pauses, calls are blocked, and sending anyway returns a 400 error.
- Anthropic evaluates extensively on new model releases, running up to 10,000 sessions in parallel in the cloud, then adjusts prompts and tool assumptions.
- For your own agents, use high-quality evaluation data and build datasets from historical sessions; vague grading criteria are not useful.
- Resources are tied to a workspace; a platform administrator configures workspaces and access, so design workspaces around access control.