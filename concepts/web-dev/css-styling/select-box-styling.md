---
domain: web-dev
subdomain: css-styling
concept: select-box-styling
title: Select Styling Specimens
sources:
  - title: "Select Styling Specimens"
    url: "https://simonwillison.net/2026/Nov/22/select-styling/"
    author: "Simon Willison"
    date: "2026-11-22"
---

# Select Styling Specimens

Simon Willison built a reference page cataloguing all the ways an HTML `<select>` element can be styled, motivated by frustration that select boxes render inconsistently across browsers and look ugly by default in Chrome. He prompted Claude to generate the page with the goal of taking screenshots in every desktop and mobile browser.

After experimentation he settled on a preferred CSS recipe: `appearance: none` to strip native styling, custom padding with extra right-side space for the arrow, a light border with rounded corners, and an inline SVG data-URI chevron positioned via `background` shorthand. The result is a consistent, minimal select box across browsers.

- Native `<select>` styling varies by browser and is considered ugly in Chrome
- `appearance: none` removes default browser styling as a starting point
- An inline SVG data-URI chevron avoids extra asset requests
- Extra right padding reserves space for the custom dropdown arrow