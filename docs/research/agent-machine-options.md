# Agent machine for the digest app + backend (2026)

## Investigation Date

2026-08-22

## Question

How do app/backend tickets for the new Compose Multiplatform (Android + iOS) app + Ktor backend get **developed** and **verified** after the wayfinder map resolves? The current agent-triage workflow (`.github/workflows/agent-triage.yml`) runs on `ubuntu-latest`, claims a `ready-for-agent` issue, runs opencode (deepseek) to implement it, and opens a PR. Extending that machine to the app/backend hits hard constraints: Kotlin/Native cannot compile iOS targets from Linux (iOS needs a macOS host with Xcode), GitHub-hosted macOS runners are assumed "paid" (not free-tier-first), Android builds need the Android SDK + Gradle (heavy but feasible on ubuntu with caching), and the Ktor backend is a plain JVM fat-JAR (trivial on ubuntu).

The three candidate options to compare:

- **(a)** extend agent-triage to app/backend tickets on ubuntu runners + verify iOS locally on the human's Mac before merge
- **(b)** agent runs locally via opencode on the human's Mac for app tickets; GH Actions is only a CI gate (not a dev machine)
- **(c)** GitHub-hosted macOS runner for full CI

Settled context this research rests on (per the ticket): monorepo (#164) — app under `app/`, backend under `backend/`; Ktor backend is plain JVM; iOS (`iosArm64`/`iosSimulatorArm64`) compiles only on macOS with Xcode.

## Sources

- [S1] Kotlin/Native supported targets and hosts (JetBrains) — https://kotlinlang.org/docs/native-target-support.html
- [S2] Kotlin/Native overview (JetBrains) — https://kotlinlang.org/docs/native-overview.html
- [S3] Create your Compose Multiplatform app (JetBrains KMP docs) — https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-multiplatform-create-first-app.html
- [S4] iOS integration methods (JetBrains KMP docs) — https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-ios-integration-overview.html
- [S5] Direct integration — `embedAndSignAppleFrameworkForXcode` (JetBrains KMP docs) — https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-direct-integration.html
- [S6] Build final native binaries (XCFrameworks) (JetBrains KMP docs) — https://kotlinlang.org/docs/multiplatform/multiplatform-build-native-binaries.html
- [S7] GitHub Actions billing (GitHub Docs) — https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions
- [S8] Actions runner pricing (GitHub Docs) — https://docs.github.com/en/billing/reference/actions-runner-pricing
- [S9] GitHub-hosted runners reference — hardware specs + public-repo free (GitHub Docs) — https://docs.github.com/en/actions/reference/runners/github-hosted-runners
- [S10] GitHub-hosted runners overview (GitHub Docs) — https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners/about-github-hosted-runners
- [S11] Actions limits — concurrency and job time limits (GitHub Docs) — https://docs.github.com/en/actions/reference/limits
- [S12] Ubuntu 24.04 runner image software list (actions/runner-images) — https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2404-Readme.md
- [S13] macOS 14 runner image software list (actions/runner-images) — https://github.com/actions/runner-images/blob/main/images/macos/macos-14-arm64-Readme.md
- [S14] actions/setup-java (GitHub Actions) — https://github.com/actions/setup-java
- [S15] Gradle Compatibility Matrix (Gradle Docs) — https://docs.gradle.org/current/userguide/compatibility.html
- [S16] OpenCode docs — Intro (local CLI/TUI, install on macOS) — https://opencode.ai/docs/
- [S17] OpenCode docs — CLI (`opencode run`, `serve`, `github run`) — https://opencode.ai/docs/cli/
- [S18] OpenCode docs — GitHub integration (tokens, workflow examples) — https://opencode.ai/docs/github/
- [S19] OpenCode docs — Agent Skills (`.opencode/skills/` discovery) — https://opencode.ai/docs/skills/
- [S20] OpenCode docs — Commands (custom `/command`s) — https://opencode.ai/docs/commands/
- [S21] anomalyco/opencode `github` composite action (`action.yml`) — https://raw.githubusercontent.com/anomalyco/opencode/dev/github/action.yml
- [S22] anomalyco/opencode repository (OpenCode project) — https://github.com/anomalyco/opencode
- [S23] Apple Developer Documentation — "Running your app on simulated or physical devices" — https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices
- [S24] Repo visibility check: `HarisHoulis/knowledge-base` is **PUBLIC** (verified via `gh repo view` — `"visibility":"PUBLIC", "isPrivate":false`)

## Findings

### 1. Kotlin/Native iOS targets require a macOS host with Xcode — not compilable from Linux

The official Kotlin/Native host-support table ([S1]) is explicit:

- Tier 1 lists `iosSimulatorArm64` and `iosArm64` under the heading **"Apple macOS hosts only"**; Tier 3 `iosX64` is likewise "Apple macOS hosts only".
- Test running: "This is only available on a native host for the specific target. For example, you can run `macosArm64` and `iosArm64` tests only on the macOS ARM64 host."
- The **Hosts** table shows, for **Building final binaries**: Linux x86_64 → "Any supported target, **except for Apple targets**"; Windows (MinGW) → same.
- Verbatim: "Building final binaries for Apple targets on Linux and Windows is also not possible."
- `.klib` artifact production for Apple targets also requires a macOS host **if the project uses cinterop dependencies** (CocoaPods/C-interop).

The Kotlin/Native overview ([S2]) states: "To compile Apple targets, you need to install [Xcode](https://apps.apple.com/us/app/xcode/id497799835) and its command-line tools."

**Conclusion:** the ticket's premise is confirmed — no Linux/Windows host (including `ubuntu-latest` GitHub runners) can compile the iOS side of the CMP app. macOS is a hard requirement.

### 2. Compose Multiplatform iOS builds require a macOS host + Xcode

- The official CMP "create your first app" tutorial ([S3]): "For iOS, you'll need a macOS machine with Xcode installed. This is a general limitation of iOS development."
- In a CMP project, `iosApp` is an Xcode project; the shared Kotlin module is compiled to an iOS framework via Kotlin/Native ([S3]).
- Standard integration for a monorepo is **direct integration** ([S4][S5]): a run-script build phase in Xcode invokes `./gradlew :<shared>:embedAndSignAppleFrameworkForXcode`. This task is "designed specifically for the Xcode environment" — it embeds the Kotlin framework into the app bundle and "handles the code signing process of the embedded framework" ([S5]).
- Gradle-only alternatives (XCFramework tasks `assemble<Framework>DebugXCFramework` etc., [S6]) still compile the Kotlin/Native iOS targets, so per Finding 1 they still require a macOS host.

**Conclusion:** every route to a runnable iOS app — Xcode project build, direct integration, or XCFramework — ultimately compiles Kotlin/Native iOS targets on a macOS host with Xcode.

### 3. GitHub-hosted macOS runners: free and unlimited on this (public) repo; paid only on private repos / larger runners

The ticket's "macOS runners are paid" premise applies to **private** repos and to **larger** runners, not to standard runners on a **public** repo — and this repo is public.

- **Repo visibility:** `HarisHoulis/knowledge-base` is PUBLIC ([S24]).
- **Public repos are free and unlimited for standard GitHub-hosted runners, including macOS:** "Use of the standard GitHub-hosted runners is free and unlimited on public repositories" ([S9]); the billing doc: "GitHub Actions usage is **free** for **self-hosted runners** and for **public repositories** that use standard GitHub-hosted runners" ([S7]). The public-repo table ([S9]) lists `macos-latest`, `macos-14`, `macos-15`, `macos-26` among the standard runners, so macOS standard minutes are covered.
- **Private-repo free tier (for contrast):** GitHub Free plan = 2,000 min/month, GitHub Pro = 3,000 min/month ([S7]). On private repos macOS is billed at per-minute rates.
- **Per-minute rates for paid usage** ([S8]): standard Linux 2-core = $0.006/min; standard macOS (3/4-core M1/Intel) = $0.062/min — ≈ **10.3× the Linux 2-core rate**, matching the ticket's "10x multiplier" intuition. (The current docs express this as per-minute USD, not as an explicit multiplier.)
- **Larger runners are never free, even on public repos:** "Included minutes cannot be used for larger runners. The larger runners are not free for public repositories" ([S8]). macOS larger runners: `macos_l` (12-core) $0.077/min, `macos_xl` (5-core M2 Pro) $0.102/min — and larger runners require GitHub Team/Enterprise plans anyway ([S8]).
- **Standard macOS runner hardware** ([S9]): arm64, 3-core (M1), 7 GB RAM, 14 GB SSD. (Intel 4-core variants exist for `macos-15-intel`/`macos-26-intel`.)
- **Concurrency limits** ([S11]): GitHub Free plan = 20 concurrent jobs total, with **max 5 concurrent macOS jobs**; job execution time capped at 6 hours. The current agent-triage job uses a 30-minute step timeout, so the 6h cap is not a binding constraint.
- **Image lifecycle caveat:** `macos-14` is being deprecated (fully unsupported from Nov 2026) and `macos-latest` points at `macos-26` as of June 2026 ([S13] announcements) — use `macos-latest` rather than `macos-14`.

**Conclusion:** for this repo, option (c) costs **$0** — a GitHub-hosted macOS standard runner is free and unlimited because the repo is public. The macOS runner image ships Xcode (15.2–16.2 on `macos-14`, iOS SDKs, iOS simulators), JDK 17/21/25, Gradle, and the Android SDK preinstalled ([S13]).

### 4. Android builds on an ubuntu GitHub runner: fully feasible, toolchain preinstalled

- The **Ubuntu 24.04 runner image** ([S12]) preinstalls the entire Android toolchain: Android SDK Command Line Tools, Build-tools 34–37, Platforms `android-34`…`android-37.2-beta`, NDK 27/28/29, CMake, plus `ANDROID_HOME`/`ANDROID_SDK_ROOT` env vars; Gradle 9.7.0, Kotlin 2.4.10, and JDKs 8/11/**17 (default)**/21/25 are also preinstalled.
- **JDK/Gradle:** Gradle 9.7 requires a JVM between 17 and 26 to execute ([S15]); AGP 9.x is the tested range ([S15]). The default JDK 17 on the image satisfies the floor; `actions/setup-java` can pin any version, sets `JAVA_HOME`, and caches `~/.gradle/caches` + `~/.gradle/wrapper`, with a `cache-dependency-path` input for monorepo layout ([S14]).
- **Caching:** Actions cache storage includes 10 GB per repository free even on the Free plan ([S7]); combined with `setup-java`'s Gradle cache and `actions/cache` for `~/.gradle`/Kotlin/Native deps, repeat Android builds are fast.
- **Resources:** on public repos `ubuntu-latest` is a 4-core / 16 GB / 14 GB SSD VM ([S9]). Android SDK is preinstalled on the image (not downloaded per job), so the 14 GB disk is not consumed by the SDK; Gradle + Kotlin caches fit comfortably. Runner docs note GitHub-hosted Linux runners support **Android hardware acceleration** (KVM) for the emulator ([S9]), so even instrumented/emulator tests are possible.
- The Ktor backend is a plain JVM fat-JAR: plain `./gradlew build`/`test` under JDK 17 on the same image — no special steps ([S12][S15]).

**Conclusion:** ubuntu runners handle the Ktor backend and the Android target (compile + test, and even emulator runs) out of the box with caching. Only iOS is impossible on ubuntu (Finding 1).

### 5. opencode CLI runs locally on macOS and is the same agent used in CI

- OpenCode is an open-source local coding agent: terminal TUI, CLI, or desktop app; installed on macOS via `brew install anomalyco/tap/opencode` or `curl -fsSL https://opencode.ai/install | bash` ([S16][S22]). It runs in any project directory and uses the machine's local tools (git, gh, Xcode, Android Studio, simulators) via its bash/read/edit tools.
- Non-interactive use for automation: `opencode run "<prompt>"`; headless server: `opencode serve`; `opencode github run` runs the GitHub-agent mode used inside Actions ([S17]).
- The same repo-level agent machinery works locally: skills load from `.opencode/skills/<name>/SKILL.md` and `~/.config/opencode/skills/<name>/SKILL.md` ([S19]); custom `/commands` load from `.opencode/commands/` or config ([S20]). This repo's `auto-implement`, `auto-tdd`, `auto-commit`, etc. are defined in `.opencode/skills/` (verified in the working tree) and are therefore available to a local run identically to the CI run.
- The GitHub Actions integration is `anomalyco/opencode/github@latest` — a composite action that installs opencode and runs `opencode github run`; it has no OS restriction and works on `ubuntu-latest` today ([S21]). It uses the OpenCode GitHub App token by default, or `use_github_token: true` with a PAT/GITHUB_TOKEN; commits/branches/PRs are created by the runner ([S18]). The existing agent-triage.yml already uses this action with `use_github_token: true`.
- Git/GitHub auth on a local Mac is the developer's normal `gh`/SSH setup — no workflow file needed for local runs.

**Conclusion:** option (b) is technically sound — the exact same agent (deepseek, same skills/commands, same `/auto-implement` flow) runs on the human's Mac; the only difference is the machine and who presses "go". Local runs would have full Xcode/simulator access for free, at the cost of babysitting and losing the autonomous scheduled loop.

### 6. iOS verification without an Apple developer account: simulator builds need no signing

- Apple's doc ([S23]) describes signing/provisioning steps **only** for physical devices: "If you choose a physical device as the run destination, perform a few additional steps to create a development provisioning profile in Xcode" (sign in with Apple Developer Program or personal Apple Account, assign a team). For a simulator run destination there are no signing steps at all.
- The CMP tutorial ([S3]) likewise gates Team-ID setup behind "Run on a real iOS device"; the simulator section has none.
- In KMP builds, the framework embedding task is literally named `embedAndSignAppleFrameworkForXcode` ([S5]) — when building for the simulator, signing is a no-op or disabled; device signing is what requires a development team.

**Conclusion:** "iOS verification" = build `iosSimulatorArm64` + run the app/tests in the simulator — doable unsigned, with no Apple developer account, on any macOS host (local Mac or a GitHub-hosted macOS runner).

## Recommendation

**Recommended: option (c) — run the agent on a GitHub-hosted macOS standard runner (`macos-latest`) for app/backend tickets, with a hybrid fallback to `ubuntu-latest` for pure-Python/ingest or Ktor-only work.**

Rationale, in the ticket's own terms (free-tier-first + monorepo context):

1. **The economics premise is wrong for this repo: macOS runners are free here.** The ticket assumed "GitHub-hosted macOS runners are paid." That is true for private repos and for larger runners, but `HarisHoulis/knowledge-base` is **public**, and standard GitHub-hosted runners — including `macos-latest` — are **free and unlimited on public repositories** ([S7][S9][S24]). Option (c) is therefore $0, which is the strongest possible free-tier-first answer, and it removes the only reason (a) or (b) existed.
2. **One machine can now build *everything* in the monorepo.** `macos-latest` has Xcode + iOS SDKs + simulators ([S13]) *and* the Android SDK + JDK 17–25 + Gradle ([S12]/[S13]), so the same runner compiles Ktor (JVM), Android, and the iOS framework + simulator app. iOS verification needs no signing ([S23]), so no Apple developer account is required even in CI.
3. **It preserves the autonomous loop.** The existing agent-triage flow (schedule → claim issue → opencode implements → PR) works unchanged if the job label changes to `macos-latest`; the anomalyco action is OS-agnostic ([S21]). Options (a) and (b) both break autonomy: (a) forces a human macOS verification gate per PR, (b) requires the human to babysit the agent on their own Mac — contradicting the whole point of an agent-triage workflow.
4. **Android-on-ubuntu and backend-on-ubuntu remain valid** (Finding 4) — so if macOS queue times (5 concurrent macOS jobs on the Free plan, [S11]) or the smaller 3-core/7 GB/14 GB macOS spec ([S9]) ever bite, a job matrix that routes Python/backend/Android-only tickets to `ubuntu-latest` and only uses `macos-latest` when iOS targets are in play is a cheap, still-free refinement. (a) and (b) become fallbacks, not the primary design.

Key decision-relevant facts to carry forward:

- **Public repo ⇒ standard macOS runners are free and unlimited** — the single fact that flips this decision ([S7][S9][S24]).
- **iOS compiles only on macOS hosts; never from Linux** ([S1][S2][S3]) — so *some* macOS access is unavoidable; the question was only who pays for it (answer: nobody, on a public repo).
- **Simulator builds are unsigned** — iOS verification in CI needs no Apple developer account ([S23][S3]).
- **Avoid larger macOS runners** (`macos-xl`, `macos_l`): never free, even on public repos ([S8]).
- **Implementation details to flag:** bump/re-check the 30-minute opencode step timeout (first Kotlin/Native iOS builds on a 3-core M1 are slow; rely on Gradle + `~/.konan` caching); pin `macos-latest` rather than the deprecated `macos-14` ([S13]); watch the 10 GB cache storage and 5-concurrent-macOS-jobs caps ([S7][S11]).
