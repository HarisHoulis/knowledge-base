---
domain: web-dev
subdomain: react-performance
concept: react-profiling
title: Profile a React App for Performance
sources:
  - title: "Profile a React App for Performance"
    url: "https://kentcdodds.com/blog/profile-a-react-app-for-performance"
    author: "Kent C. Dodds"
    date: "2019-09-16"
---

# Profile a React App for Performance

The React DevTools includes a Profiler tab that can record app interactions and display profiling data as a Flamegraph or Ranked chart. After installing the browser extension, you open the ⚛ Profiler tab, start profiling, interact with the app, and stop profiling to inspect the results (Kent C. Dodds, 2019).

A key pitfall is profiling in development mode. React ships development-time warnings and checks that add significant overhead, so measurements are tainted. To measure production performance, build and serve the production app. However, React's normal production build removes profiling code, causing “Profiling not supported.” The fix is to alias `react-dom$` to `react-dom/profiling` and `scheduler/tracing` to `scheduler/tracing-profiling` in webpack, or use `react-scripts build --profile` with CRA >= 3.2.0 (Kent C. Dodds, 2019).

Another issue is minification: production builds mangle function and class names, so the profiler shows components like `Anonymous`, `ee`, or `Z`. Disabling Terser name mangling via `keep_classnames: true` and `keep_fnames: true` preserves component names in profiling output (Kent C. Dodds, 2019).

Finally, profiling on a fast development machine can understate real-user performance. Chrome DevTools CPU throttling, such as 6x slowdown, provides a better approximation; in the article’s example, a render went from 6.5ms to 31.8ms after throttling (Kent C. Dodds, 2019).

- Install the React DevTools browser extension, open the ⚛ Profiler tab, start profiling, interact with the app, then stop and inspect Flamegraph/Ranked views.
- Do not profile development mode: React’s dev-only warnings add overhead and skew measurements; profile a production or production-profiling build instead.
- Enable production profiling by aliasing `react-dom$` to `react-dom/profiling` and `scheduler/tracing` to `scheduler/tracing-profiling`; CRA >= 3.2.0 can use `npx react-scripts build --profile`.
- Disable Terser function/class name mangling with `keep_classnames` and `keep_fnames` to keep component names readable in profiler output.
- Use CPU throttling (e.g., Chrome’s 6x slowdown) to better approximate slower user devices and expose performance issues.