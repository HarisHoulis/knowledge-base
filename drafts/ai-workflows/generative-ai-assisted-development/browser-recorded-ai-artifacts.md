---
domain: ai-workflows
subdomain: generative-ai-assisted-development
concept: browser-recorded-ai-artifacts
title: Kākāpō Party: Generating and Recording AI Pixel Art for a Keynote
sources:
  - title: "Kākāpō Party"
    url: "https://simonwillison.net/2026/Sep/26/kakapo-party/"
    author: "Simon Willison"
    date: "2026-09-26"
  - title: "Kākāpō Party (tool)"
    url: "https://tools.simonwillison.net/kakapo-party"
    author: "Simon Willison"
    date: "2026-09-26"
  - title: "Claude transcript for kākāpō animation"
    url: "https://claude.ai/share/43bec0be-a0a3-4737-bfac-34894af34ddc"
  - title: "Claude Code + Playwright transcript"
    url: "https://gisthost.github.io/?368b481fba654c4fb84d90188da77581/page-001.html"
---

# Kākāpō Party: Generating and Recording AI Pixel Art for a Keynote

Simon Willison describes using Claude Opus 5.5 to generate an animated pixel-art kākāpō party for the closing slide of his WeAreDevelopers World Congress North America keynote. He fed three Google image search photos of kākāpō parrots into Claude with a prompt asking for an HTML5 canvas animation of at least 20 pixel-art kākāpō jumping up and down with confetti. The result was published as a hosted tool page (tools.simonwillison.net/kakapo-party), which he calls "pretty great".

To embed the animation in a Keynote file, he downloaded the HTML and asked a local Claude Code session to produce a 15-second video of the file in a browser, with instructions to click a few times to trigger the confetti, not start clicking until 3 seconds in, and spread clicks around the clickable area.

Claude Code used Playwright to produce the video, and Willison notes the script was "pleasingly short". The script launches Chromium with a recorded video context at 1280x720, navigates to the local HTML file, and issues ten timestamped mouse clicks spread across centre, corners, edges and mid-positions between 3.0s and 13.2s, then holds until 16 seconds before closing the context. The captured video was exactly what he needed for the final slide.

- Claude Opus 5.5 was used to generate an HTML5 canvas pixel-art animation from a few reference photos and a natural-language prompt.
- Claude Code plus Playwright was used to programmatically render and record the animation as a 15-second video for embedding in Keynote.
- The Playwright script used a recorded-video context, scheduled timestamped clicks to trigger the confetti effect, and kept the timing spread across the clickable area.
- The workflow chains text prompting, code generation, and browser automation to produce presentation assets.