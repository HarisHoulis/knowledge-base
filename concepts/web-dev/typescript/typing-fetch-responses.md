---
domain: web-dev
subdomain: typescript
concept: typing-fetch-responses
title: Using fetch with TypeScript
sources:
  - title: "Using fetch with TypeScript"
    url: "https://kentcdodds.com/blog/using-fetch-with-type-script"
    date: "2021-01-26"
---

# Using fetch with TypeScript

The article walks through adding TypeScript types to a fetch-based HTTP request function, using the GraphQL Pokemon API as an example. Initially, after converting the file to .ts, only implicit any errors appear, but the return type is Promise<any>, so the real work begins when the function is used and expected typed data is needed. The author defines a PokemonData type and explicitly types the function's return as Promise<PokemonData>.

- Type the return value of fetch wrapper functions with explicit types like Promise<PokemonData> to avoid Promise<any> issues.
- Since response.json() returns Promise<any>, annotate the parsed response with a JSONResponse type that models the expected shape.
- Use Omit to exclude client-added fields (e.g., fetchedAt) from API data types, preventing lies to TypeScript.
- Object.assign(pokemon, { fetchedAt: ... }) allows monkey-patching without type errors, unlike direct property assignment.
- TypeScript's Promise type only captures the resolved value, not the rejection reason, so catch errors remain typed as unknown.