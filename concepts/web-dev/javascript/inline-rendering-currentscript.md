---
domain: web-dev
subdomain: javascript
concept: inline-rendering-currentscript
title: Inline rendering with document.currentScript
sources:
  - title: "Inline rendering with document.currentScript"
    url: "https://simonwillison.net/2026/Oct/17/document-currentscript/"
    author: "Simon Willison"
    date: "2026-10-17"
---

# Inline rendering with document.currentScript

A short note pointing to a technique for rendering content inline in HTML using `document.currentScript`. A `<script>` element can replace itself with generated content when the page loads, so `The year is <script>document.currentScript.replaceWith(new Date().getFullYear())</script>` renders the current year directly in place.

Defining a shortcut function such as `$=(...n)=>document.currentScript.replaceWith(...n)` turns this into a tiny template language, letting you write `The year is <script>$(new Date().getFullYear())</script>`. The approach relies on `document.currentScript` referring to the script element currently executing, which is then swapped out for the rendered value.

- `document.currentScript` lets an inline script reference and replace its own `<script>` element.
- Replacing the script element with a value renders content inline without a separate templating library.
- A one-line helper like `$=(...n)=>document.currentScript.replaceWith(...n)` creates a minimal template language.