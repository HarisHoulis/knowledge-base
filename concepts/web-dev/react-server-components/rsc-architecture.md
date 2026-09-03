---
domain: web-dev
subdomain: react-server-components
concept: rsc-architecture
title: RSC with Dan Abramov and Joe Savona Live Stream
sources:
  - title: "RSC with Dan Abramov and Joe Savona Live Stream"
    url: "https://kentcdodds.com/blog/rsc-with-dan-abramov-and-joe-savona-live-stream"
    author: "Kent C. Dodds"
    date: "2023-03-14"
---

# RSC with Dan Abramov and Joe Savona Live Stream

The live stream, summarized on Kent C. Dodds's blog, explores React Server Components (RSC) with Dan Abramov and Joe Savona. The conversation covers how RSC enables all components to run on the server, sending results to the client, which allows any number of components per page and provides automatic bundle splitting—unused components are excluded from the client bundle. However, the speakers clarify that this is not the primary benefit; instead, RSC expands the React model to allow each component to fetch its own data, thereby co-locating data dependencies and reducing client-side component count (Kent C. Dodds, 2023, https://kentcdodds.com/blog/rsc-with-dan-abramov-and-joe-savona-live-stream).

The speakers compare RSC to frameworks like Remix, noting that RSC provides greater flexibility in composing server code while retaining client state during navigation. They acknowledge trade-offs, such as waterfall issues and the N+1 problem when rendering lists, and suggest solutions like data loaders, batching, caching, and observability. They also discuss streaming as a default behavior, explaining that every component acts like an implicitly deferred loader, which requires coordination of fetches to manage multiple response headers and loading states.

Further discussion touches on runtime characteristics, caching, and request/response access. RSC deduplicates fetch requests per request via async context, and frameworks like Next.js add caching options such as cash keys. The speakers note that accessing cookies and headers is framework-specific, with Next.js and Remix offering similar utilities. They also address the separation of server and client files, viewing it as a beneficial trade-off to prevent exposing server secrets, and mention ongoing work on mutations to make interactions more ergonomic.

- RSC allows server-side component rendering with automatic bundle splitting, but its main value is co-locating data dependencies with components and enabling a request-response model.
- RSC introduces challenges like waterfalls and N+1 queries, which can be mitigated with parallel data loading, caching, and observability.
- Streaming is a default behavior in RSC, making every component an implicit deferred loader and requiring coordinated fetch strategies.
- React does not patch fetch; instead, frameworks implement deduplication and caching per request, and access to request/response objects remains framework-specific.
- Separating server and client files is a deliberate design choice that improves safety and developer experience.