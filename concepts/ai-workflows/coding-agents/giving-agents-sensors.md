---
domain: ai-workflows
subdomain: coding-agents
concept: giving-agents-sensors
title: Locating a Mysterious Beep with Claude Code and Browser Microphones
sources:
  - title: "Locating the source of a mysterious beep with Claude"
    url: "https://simonwillison.net/2026/Nov/9/mysterious-beeps/"
    author: "Simon Willison"
    date: "2026-11-09"
---

# Locating a Mysterious Beep with Claude Code and Browser Microphones

Simon Willison used Claude Code to build "Beep Locator," a system for triangulating the source of an intermittent beep in a cluttered room. The architecture is a Python web server coordinating multiple listener devices (iPads, phones, laptops) over WebSockets; listeners capture a rolling 60-second audio buffer, run FFT-based beep detection in the browser, and report events to the server. When a beep is detected, the server has the lowest-latency device play a chirp so all listener clips can be time-aligned before triangulation (Willison, 2026).

The project began with a prompt asking Claude to write a problem.md, which led it to find the 2007 BeepBeep paper on acoustic ranging using commodity hardware. Claude then built most of the system, including a hot-swap installModule() mechanism that lets the admin server push new JavaScript to listeners over the WebSocket connection—avoiding repeated microphone permission prompts on each device. Willison iterated with feature prompts for rough-mode drag positioning, clap testing, timestamped map symbols, replayable recordings, a "This is the mystery beep" confirmation, and device repositioning (Willison, 2026).

The system located the beep to within about 40cm, and Willison found an old carbon monoxide detector needing new batteries. His key insight is that this demonstrates "giving Claude Code ears": while the model has no native audio input, it can write and run code that analyzes microphone data, letting it perceive and act on the physical world. He compares this to Martin Woodward debugging conference badge computers via webcam so his coding agent could see the results (Willison, 2026).

- A Python server plus WebSocket-connected browser listeners can triangulate sound using chirp-based clip alignment and FFT beep detection.
- A hot-swap module mechanism let the agent push new code to listeners without manual device interaction or permission prompts.
- Iterative natural-language feature prompts (clap mode, replay, repositioning) drove the system from prototype to working tool.
- Coding agents can be given indirect perception of the physical world by having them write code that processes sensor data.