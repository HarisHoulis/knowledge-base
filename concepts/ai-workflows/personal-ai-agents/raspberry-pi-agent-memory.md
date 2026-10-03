---
domain: ai-workflows
subdomain: personal-ai-agents
concept: raspberry-pi-agent-memory
title: Building a Personal AI Agent with Graph Memory on a Raspberry Pi
sources:
  - title: "I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j"
    url: "https://www.youtube.com/watch?v=oUZEt4EiPbk"
    author: "AI Engineer"
    date: "2026-10-03T16:30:34+00:00"
---

# Building a Personal AI Agent with Graph Memory on a Raspberry Pi

Jeremy Adams, who works at Neo4j on graphs and graph databases, presents a personal agent-memory project running on a Raspberry Pi 4B rather than on his laptop ("I didn't want one on my laptop"). He describes himself as coming from an old-school system administration and DevOps background and wanting to wait until personal agents are "really reliable" before trusting them on his main machine. Instead he prioritized a setup that is cheap, open, and hackable, and above all understandable: "it was more important to me to understand what was happening than to have a bunch of features."

The hardware stack he demonstrates live includes a Raspberry Pi 4B (not the latest model) running a 64-bit ARM operating system, a Bluetooth keyboard, an HDMI USB video capture device to project the Pi's desktop, a USB receiver for a microphone, and battery power. On the software side he runs Nano Claw alongside Docker, with a small Docker-based Neo4j database providing graph storage for agent memory. He notes the 64-bit ARM build lets him run more, though not everything, on the device.

He frames the talk around the ongoing hype cycle for personal agents, polling the audience on experience with OpenClaw, Agent Hermes, and similar tools, on offline/peripheral hardware work, and on graph experience generally — reporting the largest such group to date. He also mentions seeing a Craigslist listing in Portland, Oregon for a Mac mini with OpenClaw pre-installed, as an example of the current hype.

The demonstration is intentionally improvised, with the Pi powered on and connected in front of the audience ("I'm literally putting it all together right before your eyes"), including a QuickTime-based capture workaround and re-plugging USB-C connectors.

- Adams runs the agent on a Raspberry Pi 4B with a 64-bit ARM OS, Docker, Nano Claw, and a small Docker-based Neo4j graph database rather than on his laptop.
- His design priorities were a cheap, open, hackable system he fully understands, over one with many features.
- He comes from a systems-administration/DevOps background and wants to wait for reliability before running personal agents on his primary machine.
- The live setup uses an HDMI USB capture device, Bluetooth keyboard, USB microphone receiver, and battery power to make the Pi demo visible and audible.