---
domain: web-dev
subdomain: node-cli-tooling
concept: node-cli-tips
title: Tips for making a CLI-based tool with node
sources:
  - title: "Tips for making a CLI-based tool with node"
    url: "https://kentcdodds.com/blog/tips-for-making-a-cli-based-tool-with-node"
    date: "2016-11-18"
---

# Tips for making a CLI-based tool with node

To make a Node CLI, configure a `bin` field in `package.json` where the key is the terminal command name and the value is the path to the transpiled binary file, such as a file in `dist`. When npm or yarn installs the package, it creates a symlink to that file in `node_modules/.bin` for local installs, or places it on the global `$PATH` for global installs. Locally installed binaries can then be used in npm scripts.

The bin file itself should start with the shebang `#!/usr/bin/env node` so the system runs it with Node. Most of the rest of the file is typically argument parsing, for which the author has used `commander`, `meow`, and others, but prefers `yargs`. The author keeps little logic in the bin file because unit testing it is a pain, placing the main package logic elsewhere in `src`.

Testing the bin file can be done with integration tests, often using Jest snapshots, which the author says provides strong confidence about the impact of changes and recommends for testing CLIs. For this particular package, the author did not unit test the main logic or report coverage because low usage was expected.

- Declare a `bin` entry in `package.json` so npm/yarn symlinks the CLI file into `node_modules/.bin` or the global `$PATH`.
- Start the CLI file with `#!/usr/bin/env node` so the OS invokes Node.
- Use an argument parser such as `yargs` (or `commander`/`meow`) to process `process.argv`.
- Keep logic out of the bin file and put it in `src` because the bin file is painful to unit test.
- Test the CLI with integration tests and Jest snapshots, which the author highly recommends.