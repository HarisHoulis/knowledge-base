---
domain: ai-workflows
subdomain: web-automation
concept: cdp-web-automation
title: The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans
sources:
  - title: "The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans"
    url: "https://www.youtube.com/watch?v=26RtyAm9y_Q"
    author: "AI Engineer"
    date: "2026-08-14T15:30:00+00:00"
---

# The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans

The talk addresses teaching AI agents to use websites like humans, noting that web pages often resist non-human interaction. The core premise is that a browser driven via the Chrome DevTools Protocol (CDP) appears indistinguishable from a human with a mouse, because clicks and keystrokes travel the same path inside Chrome [1]. This insight underlies a practical approach to web automation.

The speaker argues for giving agents a command-line interface (CLI) rather than an MCP server. While both achieve similar task success (~83%), CLI offers significant advantages in reuse, speed, and cost: a CLI sequence can be precomposed and run without a model, while MCP requires model round-trips. In one study, MCP took 71 round trips and 8 minutes versus 7 turns and under 1 minute for CLI; Anthropic reports CLI can be 75x cheaper in token cost [1].

To effectively operate a browser, agents use a subset of CDP's 57 domains, organized into 'digital senses': see (DOM, accessibility tree, screenshot), hear (network traffic, console/logs), and operate (clicks, keystrokes, navigation). The third key is a 'loop on a ladder': a sense-act-verify cycle where actions are confirmed through a different channel than the action itself—e.g., after clicking, verify by checking the resulting page state rather than the click event [1].

- CDP-driven automation makes agent actions follow the same internal path as human input, appearing human-like to anti-bot systems.
- Prefer CLI tools over MCP servers for web automation: comparable capability (~83%), but superior in reuse, speed, and token cost (up to 75x cheaper).
- CDP provides multiple sensory channels—DOM, accessibility tree, screenshots, network traffic, and logs—to perceive and interact with pages.
- Use a sense-act-verify loop, confirming each action via a different channel (e.g., check page state after a click) to ensure success.