---
domain: web-dev
subdomain: react-performance
concept: react-profiler-monitoring
title: React Production Performance Monitoring
sources:
  - title: "React Production Performance Monitoring"
    url: "https://kentcdodds.com/blog/react-production-performance-monitoring"
    date: "2020-03-16"
---

# React Production Performance Monitoring

React provides a production-focused profiling API to help detect slow user experiences that slip through PR review, because user complaints are not reliable quality control ([source](https://kentcdodds.com/blog/react-production-performance-monitoring)). The `<Profiler />` component wraps part of the tree and calls an `onRender` callback with render timing data, but it only works in production if the app is built with `react-dom/profiling` and `scheduler/tracing-profiling`; enabling the profiler build has a small performance cost ([source](https://kentcdodds.com/blog/react-production-performance-monitoring)).

The callback receives `id`, `phase`, `actualDuration`, `baseDuration`, `startTime`, `commitTime`, and `interactions`. To avoid hurting performance while measuring, React limits the information available, so profilers should be placed strategically with sensible `id` props so performance issues can be traced to specific parts of the app ([source](https://kentcdodds.com/blog/react-production-performance-monitoring)). Profilers can be nested; a re-render of a nested component triggers the callbacks for that profiler and its ancestor profilers, but not unrelated sibling profilers ([source](https://kentcdodds.com/blog/react-production-performance-monitoring)).

The article recommends sending the callback data to a monitoring tool such as Grafana, and because re-renders can happen often, batching the data and sending it every ~5 seconds. This data can reveal trends and performance regressions or spikes ([source](https://kentcdodds.com/blog/react-production-performance-monitoring)).

- React's `<Profiler>` API enables measuring component render performance in production when using the profiler build.
- `onRenderCallback` provides `id`, `phase`, `actualDuration`, `baseDuration`, `startTime`, `commitTime`, and `interactions`.
- Production profiling has limitations and overhead; place profilers strategically with meaningful IDs.
- Batch profiler data and send it to monitoring tooling every ~5 seconds instead of sending every render.
- Nested profilers report ancestor renders, not unrelated sibling profilers.