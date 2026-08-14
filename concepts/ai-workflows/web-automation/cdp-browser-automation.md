---
domain: ai-workflows
subdomain: web-automation
concept: cdp-browser-automation
title: The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans
sources:
  - title: "The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore"
    url: "https://www.youtube.com/watch?v=26RtyAm9y_Q"
    author: "Corey Gallon"
    date: "2026-08-14T15:30:00+00:00"
---

# The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans

This talk argues that AI agents can be made to use websites indistinguishably from humans by driving a browser through the Chrome DevTools Protocol (CDP). The core premise is that a CDP-driven browser behaves exactly like a human with a mouse from the perspective of anti-bot systems like Google and CloudFlare: agent clicks and keystrokes travel the same internal path as human input. To pull this off, the speaker recommends three things: a CLI-based toolchain instead of an MCP server, the Chrome Agent tool to speak CDP, and a sense-act-verify loop executed repeatedly (Corey Gallon, 2026, https://www.youtube.com/watch?v=26RtyAm9y_Q).

- A CDP browser is indistinguishable from a human user with a mouse, making it the key to human-like web automation.
- CLI tools beat MCP servers on reuse, speed, and cost despite similar task success rates (83% vs 83%), with one task taking 7 turns/under 1 minute for CLI vs 71 round trips/8 minutes for MCP.
- CDP exposes 57 domains (hundreds of methods/events) that map to digital senses: see (DOM, accessibility tree, screenshots), hear (network traffic, console logs), and operate (clicks, keystrokes, navigation).
- The interaction loop is sense, act, verify; verification must use a different channel than the action, e.g., after clicking, check the resulting page state rather than trusting the click event.