---
domain: ai-workflows
subdomain: ai-coding-agents
concept: ai-agents-large-codebases
title: AI Coding Agents Are Breaking Big Codebases
sources:
  - title: "AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph"
    url: "https://www.youtube.com/watch?v=Bdrs3uAX0_M"
    author: "AI Engineer"
    date: "2026-10-04"
---

# AI Coding Agents Are Breaking Big Codebases

Dan Adler argues that the software running the world is maintained in large, complex, long-lived codebases, not clean greenfield projects. He states that 72% of software industry workers work at companies with more than 500 people, managing thousands of repositories and decades of codebase history. These systems power everyday functions such as real-time bank transaction rejection, insurance reimbursement, package tracking, ride-hailing estimates, aircraft radar adjustments, and payroll (Dan Adler, "AI Coding Agents Are Breaking Big Codebases").

AI coding agents are generating more code faster than ever, creating a "tsunami" of generated code that engineers must review and maintain. Adler says this influx causes large codebases to start collapsing: millions of lines and tens of thousands of repositories cannot fit into a context window or be cloned and processed in real time. Agents bring inconsistent programming standards, propagate duplicate code because they do not know existing libraries, make inter-service dependencies fragile, introduce hidden problems through minor deviations, and discover new vulnerabilities that require constant oversight.

Adler frames the core problem as the amount of code itself: the same tools that accelerate development also create the conditions under which critical codebases break down. He notes that technical leaders feel this acutely, quoting a CEO of a top-10 automaker: "I don't know what this code does. AI wrote it for me." Existing agent-based development tools excel at small tasks but do not provide the infrastructure needed to see and understand 50,000-repository codebases, and this large-scale maintenance problem goes unnoticed. He calls for honoring the people who keep these codebases alive and treating this as a distinct infrastructure challenge.

- Most software workers operate in large organizations with thousands of repositories and decades of code history, and these codebases underpin critical real-world systems.
- AI agents accelerate code generation, producing a flood of code that must be reviewed, maintained, and reconciled with existing standards and libraries.
- Large codebases cannot fit into context windows or be cloned/processed in real time, leading to inconsistent agent behavior, duplicate code, fragile dependencies, and new vulnerabilities.
- Current agent tools are optimized for small tasks and do not solve the infrastructure problem of understanding tens of thousands of repositories, leaving the maintenance burden harder than ever.
- Adler calls for honoring codebase maintainers and addressing large-scale codebase health as a first-class infrastructure problem.