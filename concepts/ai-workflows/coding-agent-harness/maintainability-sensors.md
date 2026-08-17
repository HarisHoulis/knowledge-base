---
domain: ai-workflows
subdomain: coding-agent-harness
concept: maintainability-sensors
title: Maintainability sensors for coding agents
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html"
    author: "Martin Fowler"
---

# Maintainability sensors for coding agents

In this article, Martin Fowler discusses the use of sensors in coding agent harnesses, building on Birgitta Böckeler's mental model that describes a system of guides and sensors. The purpose of this system is to increase the probability of good agent outputs and enable self-correction before issues reach human eyes. Fowler highlights that Birgitta has started publishing an article about her experiences using sensors to keep a codebase maintainable.

The specific focus of this installment is static analysis, particularly basic code linting, as a sensor for maintainability. By incorporating linting into the coding agent harness, teams can automatically detect potential style issues, bugs, and other problems in agent-generated code. This approach is part of a broader effort to maintain code quality as AI agents become more involved in software development.

Overall, the article emphasizes the importance of feedback loops in AI-assisted coding, where sensors like linters provide immediate signals that allow the agent to correct course proactively, reducing the burden on human reviewers and helping preserve long-term codebase maintainability.

- Coding agent harnesses use a combination of guides and sensors to improve agent output quality.
- Sensors enable self-correction before issues reach human eyes.
- Static analysis, especially basic code linting, serves as a key sensor for maintainability.
- Integrating linting into the harness helps keep codebases maintainable as AI agents contribute code.