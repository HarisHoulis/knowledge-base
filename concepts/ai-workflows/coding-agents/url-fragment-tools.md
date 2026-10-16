---
domain: ai-workflows
subdomain: coding-agents
concept: url-fragment-tools
title: LaTeX Renderer: A URL-Fragment Tool Built with Claude Code
sources:
  - title: "LaTeX renderer"
    url: "https://simonwillison.net/2026/Oct/15/latex/"
    author: "Simon Willison"
    date: "2026-10-15"
---

# LaTeX Renderer: A URL-Fragment Tool Built with Claude Code

Simon Willison built a LaTeX renderer inspired by Paul Ford and Aboard Foundary's Tiny Little Office, a suite of web app content editors whose signature trick is storing all document data in the URL `#fragment` section, making every document a bookmarkable, shareable link. Tiny Little Office also ships an llms.txt file telling agents how to construct URLs that render as documents, which Claude used to generate a working deck link.

Willison had Claude Code (Opus 5.5 Extra) build a similar tool for LaTeX, prompting it to render LaTeX passed via a fragment hash, support a compressed prefix using a LaTeX-optimized compression dictionary, use the best available LaTeX render library from a CDN (including WebAssembly options), and show an editor when loaded without a fragment. The rendered view is bookmarkable and can toggle back to source editing.

He reused patterns from his existing tools repo: an `<iframe sandbox="...">` mechanism borrowed from his SVG in Markdown tool for XSS protection, and a Gist/URL loading feature copied from the same tool. The finished tool uses Pako 2.1.0, MathJax 4.1.3, faster-latex 0.3.1, and DOMPurify 3.4.16.

- Tiny Little Office stores document data in the URL fragment, making documents bookmarkable and shareable, and provides an llms.txt file so agents can construct renderable URLs.
- Willison prompted Claude Code to build a LaTeX renderer supporting fragment-hash input, a compression-dictionary prefix, CDN-based rendering, and an editor/rendered toggle.
- XSS protection was handled by reusing an iframe sandbox pattern from the SVG in Markdown tool, plus a Gist/URL loading feature.
- The tool relies on Pako 2.1.0, MathJax 4.1.3, faster-latex 0.3.1, and DOMPurify 3.4.16.