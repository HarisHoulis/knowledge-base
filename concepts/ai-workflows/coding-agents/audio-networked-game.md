---
domain: ai-workflows
subdomain: coding-agents
concept: audio-networked-game
title: Chirp Pong: Two-Player Phone Game Using Audio Networking
sources:
  - title: "Chirp Pong"
    url: "https://simonwillison.net/2026/Oct/15/chirp-pong/"
    author: "Simon Willison"
    date: "2026-10-15"
---

# Chirp Pong: Two-Player Phone Game Using Audio Networking

Simon Willison built Chirp Pong, an experiment testing whether two separate phones running static HTML could play a two-player game where networking happens via chirps sent through the microphone. He reports that it seems to work. The game is a competitive pong-like experience where players hold their phones close together and game state is transmitted via audio noises interpreted by the Web microphone API. Willison prompted for graphical and gameplay twists to make it more fun and intertwined than pong. The tool was built with Claude Opus 5.5 Extra in Claude Code.

- Two-player game runs on separate phones as static HTML with no conventional network connection
- Game state is transmitted via audio chirps captured by the Web microphone API
- Built with Claude Opus 5.5 Extra in Claude Code from a single prompt