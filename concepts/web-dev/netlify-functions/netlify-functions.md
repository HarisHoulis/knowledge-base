---
domain: web-dev
subdomain: netlify-functions
concept: netlify-functions
title: Super simple start to Netlify functions
sources:
  - title: "Super simple start to Netlify functions"
    url: "https://kentcdodds.com/blog/super-simple-start-to-netlify-functions"
    author: "Kent C. Dodds"
    date: "2020-11-11"
---

# Super simple start to Netlify functions

The article explains how to get started with Netlify Functions for serverless backend logic without managing servers. It begins by describing the problem: a static Gatsby site needs server-side functionality for a contact form to send emails, and Netlify Functions offer a simple solution. The author outlines four basic steps: create a `netlify.toml` file pointing to a `./functions` directory, write a simple `hello.js` handler that returns a response, commit and push to GitHub, and connect the repository to Netlify via the dashboard. Netlify automatically deploys each JavaScript file in the configured directory as an AWS Lambda function and exposes it at a `/.netlify/functions/` endpoint.

- Netlify Functions let you deploy serverless endpoints by simply placing JavaScript files in a configured `./functions` directory and connecting a Git repository to Netlify.
- Each function file exports an `async` handler that returns a response object, and Netlify handles deployment to AWS Lambda behind the scenes.
- The default endpoint is `/.netlify/functions/<filename>`, and this path is not configurable directly.
- Because Netlify deploys only the function files, bundling with `netlify-lambda` is recommended to include dependencies and enable local testing.
- Changes committed to GitHub trigger automatic redeployment, making the workflow fast and empowering for static sites requiring lightweight server-side logic.