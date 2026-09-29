---
domain: web-dev
subdomain: javascript-tooling
concept: spelunking-node-modules
title: Spelunking in node_modules: Debugging Jest/JSDOM Console Mocking
sources:
  - title: "Spelunking in node_modules 👷"
    url: "https://kentcdodds.com/blog/spelunking-in-node-modules"
    author: "Kent C. Dodds"
    date: "2018-01-22"
---

# Spelunking in node_modules: Debugging Jest/JSDOM Console Mocking

Kent C. Dodds recounts upgrading dependencies for kcd-scripts and paypal-scripts, then updating downshift alongside React and kcd-scripts. Tests began emitting an Uncaught Error stack trace from JSDOM even though the tests still passed and the test file mocked console.error to suppress React's expected error logs ([source](https://kentcdodds.com/blog/spelunking-in-node-modules)).

Following the stack trace, he found that JSDOM's reportException uses a VirtualConsole that emits jsdomError and logs through the console passed to it. By modifying code inside node_modules and adding console.log probes, he discovered that the console in his test file was not the same as the console JSDOM was using: Jest creates a fake testConsole in an isolated environment, but that console was not being passed to JSDOM's VirtualConsole ([source](https://kentcdodds.com/blog/spelunking-in-node-modules)).

He fixed this in Jest's jest-environment-jsdom by creating the testConsole before JSDOM initialization and passing it so JSDOM could create a VirtualConsole with it. The change became Jest PR #5227 and was merged. The article's takeaways: learn how dependencies work, node_modules contains huge amounts of JavaScript you can modify, and solve your own problems by contributing fixes rather than only reporting and reverting ([source](https://kentcdodds.com/blog/spelunking-in-node-modules)).

- Upgrading dependencies can reveal issues in transitive tooling; tests may pass while JSDOM logs errors.
- Jest isolates tests with its own global/console; JSDOM's VirtualConsole was using a different console, so console.error mocking did not suppress JSDOM errors.
- Inspecting and modifying node_modules with logs and debugger is a practical way to trace dependency behavior and identify fixes.
- The fix moved Jest's testConsole creation before JSDOM init and passed it to jest-environment-jsdom; PR #5227 was merged.