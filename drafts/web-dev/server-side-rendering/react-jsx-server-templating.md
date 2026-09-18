---
domain: web-dev
subdomain: server-side-rendering
concept: react-jsx-server-templating
title: React/JSX as a Server-Side Templating Language
sources:
  - title: "React/JSX as a server-side templating language"
    url: "https://kentcdodds.com/blog/react-jsx-as-a-server-side-templating-language"
    date: "2018-10-01"
---

# React/JSX as a Server-Side Templating Language

At PayPal, a PR migrated an Express codebase from a custom template system to React function components and JSX to unify frontend and backend templating and reduce maintenance overhead. Previously the app used express-es6-template-engine for profile/settings pages, React/JSX for the client app, and a custom tagged-template solution for marketing pages, so engineers had to maintain three systems. The change consolidated on React and JSX for both server and client ([source](https://kentcdodds.com/blog/react-jsx-as-a-server-side-templating-language)).

JSX compilation was easy: installing react and react-dom in the server let the existing paypal-scripts Babel config add React plugins automatically. The main challenge was integrating HTML strings from other PayPal modules, such as a polyfill service that injects a script with a nonce into the head. React escapes interpolated values as XSS protection, so directly rendering the HTML string would be escaped. Using dangerouslySetInnerHTML on a div would work but produce invalid/undesirable markup in head. The author created a RawText component that renders <raw-text dangerouslySetInnerHTML={{__html: children}} />, then removed the raw-text tags from the final static markup via removeRawText ([source](https://kentcdodds.com/blog/react-jsx-as-a-server-side-templating-language)).

Localization also needed adjustment: the client app used a singleton message store, which does not work well on the backend. The author built a simple React Context provider/consumer and a Message component to retrieve messages by key. Other notes included extensive use of React.Fragments, changing class to className and style to object syntax, and replacing template literal ${} with JSX {}. The conclusion is that using one templating solution reduces long-term maintenance burden, and refactoring experiments back to the winning abstraction is important ([source](https://kentcdodds.com/blog/react-jsx-as-a-server-side-templating-language)).

- Migrated paypal.me Express pages from custom template systems to React function components and JSX.
- React's escaping protects against XSS but required a RawText/dangerouslySetInnerHTML workaround for inserting trusted raw HTML into <head>.
- Used React Context instead of a singleton for server-side localization messages.
- Noted JSX syntax changes: className, style objects, fragments, and {} instead of ${}.
- Goal: one templating solution for frontend and backend to reduce maintenance burden.