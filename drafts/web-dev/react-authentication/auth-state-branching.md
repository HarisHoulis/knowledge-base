---
domain: web-dev
subdomain: react-authentication
concept: auth-state-branching
title: Authentication in React Applications
sources:
  - title: "Authentication in React Applications"
    url: "https://kentcdodds.com/blog/authentication-in-react-applications"
    author: "Kent C. Dodds"
    date: "2019-05-20"
---

# Authentication in React Applications

The article presents a simple pattern: at the top of the React tree, call `useUser()` and render either `<AuthenticatedApp />` or `<UnauthenticatedApp />` depending on whether a user exists. This avoids redirect logic and makes it impossible to render the wrong side of the app when no user is logged in (kentcdodds.com).

To set this up, wrap the app in `AppProviders`, which composes `AuthProvider` and `UserProvider`. `AuthProvider` bootstraps auth data—if a token is in `localStorage`, it retrieves the user's data—and postpones rendering its children until that check completes, showing a `FullPageSpinner` in the meantime (kentcdodds.com). `UserProvider` then keeps user data in sync in memory and on the server.

The `AuthenticatedApp` and `UnauthenticatedApp` components can render their own routers or share components, but the top-level branch means the rest of the app never has to wonder if the user is logged in (kentcdodds.com). The article notes that for apps with many shared screens, developers can litter `useUser()` hooks or add a `useIsAuthenticated()` boolean hook throughout the codebase.

- Branch at the top level with `user ? <AuthenticatedApp /> : <UnauthenticatedApp />` instead of using redirects.
- Use `React.lazy` to code-split authenticated and unauthenticated apps so each loads only when needed.
- `AuthProvider` holds user data and blocks rendering with a spinner until it determines whether a token exists and retrieves the user's information.
- Separate `AuthProvider` (auth bootstrapping) from `UserProvider` (keeping user data up to date).
- Apps with many shared screens can use `useUser()` or a `useIsAuthenticated()` hook throughout the codebase.