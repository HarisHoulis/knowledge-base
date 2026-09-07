---
domain: web-dev
subdomain: firebase
concept: firebase-cloud-functions-setup
title: Super simple start to Firebase functions
sources:
  - title: "Super simple start to Firebase functions"
    url: "https://kentcdodds.com/blog/super-simple-start-to-firebase-functions"
    author: "Kent C. Dodds"
    date: "2020-11-12"
---

# Super simple start to Firebase functions

This guide demonstrates the simplest possible path to creating and deploying Firebase Cloud Functions. It instructs readers to create a Firebase project, then configure a minimal `firebase.json` (an empty object) and a `.firebaserc` file that associates the repository with the project ID [1]. The actual function code lives in a `functions` directory, with a `package.json` containing `firebase-admin` and `firebase-functions`, and an `index.js` exposing an HTTP endpoint via `functions.https.onRequest` [1]. The article explicitly notes that both dependencies are required, and that the `engines.node` field is needed so Firebase knows which Node.js version to use.

Beyond local setup, the tutorial covers testing functions with the Firebase emulator (`firebase emulators:start`) and deploying them with `firebase deploy`. First-time deployment requires enabling billing by upgrading to the Blaze pay-as-you-go plan; otherwise Firebase returns an HTTP 400 error mentioning billing must be enabled. The guide reassures readers that there is a generous free tier and that charges typically only begin after heavy usage [1].

For automation, the author shows how to generate a CI token with `firebase login:ci`, store it as a GitHub secret, and create a GitHub Actions workflow that deploys on every push to the `main` branch. The workflow checks out the repo, sets up Node 12, installs dependencies in the `functions` directory, and runs `npx firebase-tools deploy --token "$FIREBASE_TOKEN"` [1]. This makes continuous deployment straightforward once the token and secrets are configured.

- A Firebase Cloud Functions setup can be minimal: an empty `firebase.json`, a `.firebaserc` with the project ID, and a `functions` directory containing `package.json` and `index.js`.
- The mandatory runtime dependencies are `firebase-admin` and `firebase-functions`, and the `engines.node` field must specify a Node.js version.
- Local testing via `firebase emulators:start` is possible before deploying, and deployment requires upgrading to the Blaze plan, which requires a billing account.
- Automated deployments can be configured using a GitHub Actions workflow that runs `npx firebase-tools deploy` with a token generated via `firebase login:ci`.