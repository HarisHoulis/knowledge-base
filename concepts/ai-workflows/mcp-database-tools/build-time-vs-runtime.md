---
domain: ai-workflows
subdomain: mcp-database-tools
concept: build-time-vs-runtime
title: Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google
sources:
  - title: "Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google"
    url: "https://www.youtube.com/watch?v=9R--1tg45Jg"
    author: "AI Engineer"
    date: "2026-09-09T13:00:04+00:00"
---

# Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google

The presentation introduces the speakers' work on the MCP Toolbox for Databases, an open-source project with about 15.7k GitHub stars, 132 active contributors, and support for over 40 databases. The toolbox provides connection pooling, integrated authentication, and observability out of the box. Google also offers a managed MCP solution that connects to agents and IDEs like Gemini CLI, Antigravity CLI, and Cloud Code, with security and identity management via Model Armor. The project reached 20 million tool calls last month (source: Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google).

- Build-time tools, such as NL2SQL and control-plane/admin tools, are useful for developers but require human involvement and are not safe for production environments without safeguards.
- Runtime tools should use structured, predefined SQL queries to provide built-in security, prevent SQL injection, and reduce agent hallucinations.
- Control-plane tools can perform dangerous actions like deleting tables; they need explicit human oversight.
- MCP Toolbox for Databases offers open-source and managed hosting options with extensible support for many databases and integrated observability.
- Identity-based safety barriers are proposed to prevent data leakage in production deployments of AI agent tools.