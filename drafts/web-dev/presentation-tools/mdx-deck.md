---
domain: web-dev
subdomain: presentation-tools
concept: mdx-deck
title: mdx-deck: Slide Decks Powered by Markdown and React
sources:
  - title: "mdx-deck: slide decks powered by markdown and react"
    url: "https://kentcdodds.com/blog/mdx-deck-slide-decks-powered-by-markdown-and-react"
    author: "Kent C. Dodds"
    date: "2018-08-20"
---

# mdx-deck: Slide Decks Powered by Markdown and React

The author describes moving through presentation tools like PowerPoint, Prezi, Google Slides, and slides.com, but remained frustrated by limitations, especially the difficulty of including interactive elements and WYSIWYG annoyances. He admired HTML/CSS/JS slides because interactive demos could be embedded directly, unlike recorded videos that sometimes failed to replay.

MDX, created by John Otander and later announced by Tim Neutkens, made it possible to write markdown that can import and render React components. The author calls MDX “the REAL DEAL” because it solves a need he previously hacked around, such as when building the glamorous docs site.

Brent Jackson then created mdx-deck, which combines markdown ease with React component interactivity. The author highlights features including writing presentations in markdown, importing React components, customizable themes and components, a zero-config CLI, presenter mode, speaker notes, production export, and PDF export. Pairing it with Netlify’s GitHub integration allows an automatically deployed slide deck from a GitHub project.

The author is porting his “Simply React” slides to mdx-deck, deployed on Netlify with a PDF version, and is excited by the ability to create browser presentations that are easy to run locally, deploy, export as PDF, and remain interactive.

- mdx-deck lets you write presentations in markdown while importing and using React components directly in slides.
- It includes a zero-config CLI, customizable themes/components, presenter mode, speaker notes, production export, and PDF export.
- Combining mdx-deck with Netlify’s GitHub integration enables automatically deployed slide decks from a GitHub project.
- The author is porting his “Simply React” slides to mdx-deck as an example of the workflow.