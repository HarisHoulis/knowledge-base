---
domain: web-dev
subdomain: test-governance
concept: playwright-test-governance
title: Leapwork Play Reaches GA with Governance for Playwright Tests
sources:
  - title: "Leapwork Play Reaches GA with Governance for Playwright Tests"
    url: "https://www.infoq.com/news/2026/11/leapwork-play-playwright/"
    author: "Mark Silvester"
    date: "2026-11-05"
---

# Leapwork Play Reaches GA with Governance for Playwright Tests

Leapwork made its Play service generally available on September 30, 2026, targeting teams that manage Playwright test suites. Play wraps standard Playwright code with requirement traceability and approval workflows, and suites can run either in existing CI pipelines or through Leapwork's hosted execution service. Existing Playwright suites are imported without changes, and engineers can connect Jira, Git repositories and product documentation to build a knowledge base that supplies context for generated tests; browser journeys can also be recorded and turned into tests.

Play monitors connected repositories for pushes that change application behaviour or the interface and recommends corresponding test updates. Its product page also describes self-healing that repairs broken test steps rather than failing a run, though the sources do not clarify whether locator repairs require approval or how they appear in audit history. Each test is linked to its originating requirement, ticket or document, and the service retains authoring history and approvals alongside full execution logs that can be exported as evidence. It also reports flaky tests and coverage across applications or teams.

Role-based permissions and approval workflows govern who can create and run tests, with full governance, security and audit capabilities included in enterprise packages (the free tier's specific controls are unspecified). Donovan Brady, VP of developer relations at Leapwork, framed the problem as proving where a test came from and managing thousands of tests across dozens of teams. Teams can also drive Play through an AI coding assistant via a Model Context Protocol server, with Claude Code, Codex and Cursor named as clients, and hosted execution is Chromium-based with parallel runs plus environment and test data management. Open-source Playwright already offers failure diagnostics via its Trace Viewer; Play's added scope is central management of test provenance and approvals across teams.

- Play imports existing Playwright suites unchanged and runs them in existing CI pipelines or Leapwork's hosted service.
- Tests are linked to originating requirements, tickets or documents, with authoring history, approvals and execution logs exportable as evidence.
- Repository monitoring recommends test updates when application behaviour or UI changes, and self-healing repairs broken steps, though approval and audit details for repairs are unspecified.
- Role-based permissions and approval workflows are included in enterprise packages; free-tier controls are not detailed.
- Play can be operated through AI coding assistants via an MCP server, with Claude Code, Codex and Cursor as clients.