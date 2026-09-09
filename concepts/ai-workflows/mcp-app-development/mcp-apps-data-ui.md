---
domain: ai-workflows
subdomain: mcp-app-development
concept: mcp-apps-data-ui
title: MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed
sources:
  - title: "MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed"
    url: "https://www.youtube.com/watch?v=lbaXnx0KLA8"
    author: "Dustin Mihalik"
    date: "2026-09-09"
---

# MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed

In this talk, Dustin Mihalik from Indeed shares practical lessons from building MCP (Model Context Protocol) apps for Claude, ChatGPT, and Indeed's internal agent Career Scout. He emphasizes that when exposing a service through an MCP app, you must provide the model not only with UI elements but also with the underlying structured data. Simply injecting HTML or calling existing APIs as a black box leaves the model unable to answer user questions about the displayed results, leading to poor experiences. Mihalik's core rule is: 'everything you show to the user should also be provided to the model as data' (Mihalik, 2026).

He explains that MCP apps should return both structured content and a resource URI pointing to the HTML, keeping them in sync. Additionally, tool descriptions need to be updated to signal that results are automatically displayed as interface components, which prevents the model from redundantly describing or misrepresenting the output. The talk also covers challenges like getting Claude or ChatGPT to include links and controlling branding, solved through the MCP app specification and careful prompt/description design. Interactive elements such as Apply or View Details buttons also require the model to know what the user is viewing, reinforcing the need for transparent data sharing between the app and the model.

- Always give the model the same data that is shown in the UI to avoid a 'black box' where the model cannot answer follow-up questions.
- MCP apps must return structured content plus a resource URI for the HTML, and keep both in sync.
- Update tool descriptions (e.g., 'results were automatically displayed to the user as interface components') to guide model behavior and reduce discrepancies.
- Interactive UI elements like Apply/View Details require the model to understand what data is displayed so it can respond to user queries.
- Branding and link control in MCP apps are difficult but achievable through the MCP app specification and SDKs.