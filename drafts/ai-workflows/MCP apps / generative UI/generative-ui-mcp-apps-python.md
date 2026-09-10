---
domain: ai-workflows
subdomain: MCP apps / generative UI
concept: generative-ui-mcp-apps-python
title: Generative UI... in Python? — Jeremiah Lowin, Prefect
sources:
  - title: "Generative UI... in Python? — Jeremiah Lowin, Prefect"
    url: "https://www.youtube.com/watch?v=Krzs8GeiWTc"
    author: "AI Engineer"
    date: "2026-09-10T16:30:07+00:00"
---

# Generative UI... in Python? — Jeremiah Lowin, Prefect

MCP apps extend the MCP protocol by allowing a tool result to be returned to the user as a full UI—HTML, CSS, and JavaScript—rather than passing through the agent’s context window. The user can then interact directly with that UI, use tools, and send information back to a backend host, enabling experiences like booking a table, changing a seat, or interacting with a schedule [source]. A future MCP release is expected to let the agent interact with the app as well, opening use cases such as playing chess against the agent in a visual app [source].

Jeremiah Lowin, author of FastMCP, notes that FastMCP’s user base is mostly Python engineers, which creates a challenge: how to deliver best-practice, interactive, beautiful UIs without pretending that the full frontend ecosystem can be jammed into Python or shipping React with Python [source]. He argues against creating a “Frankenstein” system that forces all frontend tooling into Python [source].

Instead, the talk frames the problem around enterprise Python developers using the FastMCP ecosystem. These users primarily need MCP apps and UIs for sharing information throughout their organization and collecting information throughout their organization, not for consumer-grade, fully branded custom UIs [source]. The talk is positioned as a reasoned approach to a strange new capability enabled by agents and MCP, though the transcript excerpt ends before the full solution is presented [source].

- MCP apps bypass the agent’s context window by returning HTML/CSS/JavaScript UI directly to the user for direct interaction.
- The user can interact with the app and its backend host, enabling interactive workflows such as booking or scheduling.
- An upcoming MCP release will let the agent interact with the app too, enabling new use cases.
- FastMCP’s users are mostly Python engineers, so the challenge is delivering good UIs without forcing React or the frontend ecosystem into Python.
- Enterprise users mainly need UIs for sharing and collecting information across their organization, not consumer-grade branded UIs.