---
domain: ai-workflows
subdomain: coding-agents
concept: ai-generated-blender-models
title: .blend URL Viewer: Viewing AI-Generated Blender Models in the Browser
sources:
  - title: ".blend URL Viewer"
    url: "https://simonwillison.net/2026/Sep/9/blender-viewer/"
    author: "Simon Willison"
    date: "2026-09-09"
  - title: ".blend URL Viewer tool"
    url: "https://tools.simonwillison.net/blender-viewer"
    author: "Simon Willison"
    date: "2026-09-09"
  - title: "Blender coding agents on macOS (TIL)"
    url: "https://til.simonwillison.net/llms/blender-coding-agents-macos"
    author: "Simon Willison"
  - title: "vibe-coded-blender-projects (Pluribus Fabergé egg deliverables)"
    url: "https://github.com/simonw/vibe-coded-blender-projects/tree/main/pluribus-faberge-egg/deliverables"
    author: "Simon Willison"
---

# .blend URL Viewer: Viewing AI-Generated Blender Models in the Browser

Simon Willison describes a workflow for generating Blender 3D models with AI coding agents and viewing the results in the browser (https://simonwillison.net/2026/Sep/9/blender-viewer/). He first used ChatGPT Images 2.5 with the prompt "Generate a photo of a faberge egg that's themed after the TV show Pluribus - research first", which produced an image he judged "honestly not bad for a first attempt!".

He then pasted that image into Codex running GPT-6 Astra (high) with the prompt "Use your blender local skill to create a blender model of this faverge egg". The agent ran for 17m51s and produced several `.blend` files, published in the vibe-coded-blender-projects repository. The "blender local skill" is a skill file he created previously, as documented in his TIL on Blender coding agents on macOS.

To make the output shareable, Willison added an existing vibe-coded Blender viewing experiment to his tools collection, creating the .blend URL Viewer. The tool accepts a URL parameter pointing at a `.blend` file so the model can be viewed directly in a browser, e.g. the Pluribus Jeweled Egg v1 model hosted on GitHub.

The post ties together image generation, agentic coding with a local tool skill, and a small JavaScript viewer tool as an end-to-end pipeline from prompt to browsable 3D artifact.

- ChatGPT Images 2.5 generated a Fabergé-egg image themed after the TV show Pluribus from a single research-first prompt.
- The image was passed to Codex running GPT-6 Astra (high), which used a "blender local skill" to build a Blender model, taking 17m51s and producing several `.blend` files.
- A pre-existing Blender viewing experiment was added to the tools collection as the .blend URL Viewer.
- The viewer takes a URL to a `.blend` file (e.g. hosted on GitHub) and renders the model in the browser.