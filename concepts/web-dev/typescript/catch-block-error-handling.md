---
domain: web-dev
subdomain: typescript
concept: catch-block-error-handling
title: Get a catch block error message with TypeScript
sources:
  - title: "Get a catch block error message with TypeScript"
    url: "https://kentcdodds.com/blog/get-a-catch-block-error-message-with-typescript"
    date: "2021-10-28"
---

# Get a catch block error message with TypeScript

The article explains that TypeScript defaults the catch clause variable to `unknown` and disallows explicit type annotations like `Error` (showing error ts1196). Because JavaScript allows throwing any value (strings, numbers, null, etc.), the catch variable must remain `any` or `unknown`. The author then demonstrates a simple utility function, `getErrorMessage`, that safely extracts a message by checking `instanceof Error` and falling back to `String(error)`. An updated, more robust version uses a type guard `isErrorWithMessage` and `JSON.stringify` to handle cases where the thrown value is an object with a `message` property or contains circular references. The key takeaway is that TypeScript's strictness helps developers handle truly unpredictable runtime scenarios.

- In TypeScript, catch clause variables are typed as `unknown` by default, and you cannot annotate them as `Error`; you must use `any` or `unknown`.
- Use `error instanceof Error` to safely access the `message` property when the thrown value is an actual `Error` object.
- For non-Error thrown values, fall back to `String(error)` or `JSON.stringify` to produce a meaningful message.
- A reusable `getErrorMessage` utility centralizes this logic across catch blocks.
- Instead of fighting TypeScript's restrictions, leverage them to handle unexpected edge cases.