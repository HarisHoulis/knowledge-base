---
domain: web-dev
subdomain: browser-performance
concept: web-workers
title: Speed up your App with Web Workers
sources:
  - title: "Speed up your App with Web Workers"
    url: "https://kentcdodds.com/blog/speed-up-your-app-with-web-workers"
    author: "Kent C. Dodds"
    date: "2019-10-04"
---

# Speed up your App with Web Workers

JavaScript is single-threaded, so long-running synchronous code on the main thread can block all other JavaScript and make a page unresponsive; the article demonstrates this with an infinite `while (true) {}` loop in the console [source]. Web Workers are a browser standard that allow JavaScript files to run in separate threads, so CPU-heavy work like cryptocurrency mining can happen off the main thread [source]. A basic worker is created with `new Worker('worker.js')`, and main/worker communicate via `postMessage` and `onmessage`; workers can also be terminated with `worker.terminate()` [source].

For practical modular use, the author recommends Jason Miller's `workerize` and `workerize-loader` webpack loader, which let you move a module and its imports into a worker [source]. In a client-side search example using `match-sorter` and `Downshift`, putting `getItems` in a worker improved performance; because worker communication is asynchronous, the calling code had to change from synchronous to async [source]. The article concludes by suggesting developers profile their apps for JavaScript hot spots that could benefit from a separate thread [source].

- JavaScript is single-threaded; long-running main-thread code can freeze the UI.
- Web Workers let the browser run JavaScript in separate threads with message-based communication.
- Minimal Worker API: `new Worker('worker.js')`, `postMessage`, `onmessage`, and `terminate`.
- `workerize` and `workerize-loader` help use workers with modules and webpack.
- Worker communication is asynchronous, so calling code may need an async refactor.