# YouTube Subtitle Fetcher: yt-dlp (cookies) vs youtube-transcript-api

## Investigation Date

2026-07-19

## Context

The knowledge-base pipeline at `/Users/harishoulis/knowledge-base` runs a daily GitHub Actions workflow (`ubuntu-latest`) that fetches auto-generated English subtitles from YouTube videos using yt-dlp. The pipeline currently:

1. Installs yt-dlp via `pip install -e ".[dev]"` (PyPI package, not official binary)
2. Calls `yt-dlp --write-auto-subs --sub-lang en --skip-download` with two attempts: first with `--extractor-args youtube:player_client=android`, then with default args
3. Strips WebVTT formatting from the output VTT file

The pipeline is failing due to:
- **Warning**: No JS runtime found (yt-dlp only enables `deno` by default; `node` is on the runner but not enabled)
- **Fatal error**: YouTube returns `Sign in to confirm you're not a bot`

## Primary Sources Consulted

### youtube-transcript-api

- **PyPI page**: https://pypi.org/project/youtube-transcript-api/ (v1.2.4, released 2026-01-29)
- **Source code (GitHub)**: https://github.com/jdepoix/youtube-transcript-api
  - `_api.py`: https://github.com/jdepoix/youtube-transcript-api/blob/master/youtube_transcript_api/_api.py
  - `_transcripts.py`: https://github.com/jdepoix/youtube-transcript-api/blob/master/youtube_transcript_api/_transcripts.py
  - `_settings.py`: https://github.com/jdepoix/youtube-transcript-api/blob/master/youtube_transcript_api/_settings.py
  - `_errors.py`: https://github.com/jdepoix/youtube-transcript-api/blob/master/youtube_transcript_api/_errors.py
- **Open issues**: https://github.com/jdepoix/youtube-transcript-api/issues
- **License**: MIT (LICENSE file in repository)

### yt-dlp

- **README (official docs)**: https://github.com/yt-dlp/yt-dlp#readme
- **Wiki - EJS Setup Guide**: https://github.com/yt-dlp/yt-dlp/wiki/EJS
- **Wiki - FAQ (cookies)**: https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp
- **PyPI page**: https://pypi.org/project/yt-dlp/
- **License**: Unlicense

### GitHub Actions Runner Images

- **Ubuntu 24.04 (current ubuntu-latest)**: https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2404-Readme.md
- **Ubuntu 22.04**: https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2204-Readme.md

### Existing Pipeline Code

- `/Users/harishoulis/knowledge-base/kb_pipeline/fetcher.py` (the `transcript_youtube` function)
- `/Users/harishoulis/knowledge-base/kb_pipeline/pipeline.py` (calls `transcript_youtube` via `transcript_fn`)
- `/Users/harishoulis/knowledge-base/docs/specs/daily-ingest.md` (workflow design spec)

---

## Option B: yt-dlp with added cookies and JS runtime

### How it currently works (in the pipeline)

The pipeline calls yt-dlp as a subprocess with these arguments:

```python
cmd = ["yt-dlp"]  # or ["python", "-m", "yt_dlp"]
base_args = [
    *cmd,
    "--write-auto-subs", "--sub-lang", "en",
    "--skip-download",
    "-o", f"{tmpdir}/%(id)s.%(ext)s",
    f"https://www.youtube.com/watch?v={video_id}",
]
attempts = [
    [*base_args, "--extractor-args", "youtube:player_client=android"],
    base_args,
]
```

Two issues in the current pipeline:

1. yt-dlp is installed via `pip install -e ".[dev]"`. The `[dev]` extra does NOT include the `yt-dlp-ejs` package (which ships JS challenge solver scripts). The `[default]` extra IS required for that, per the yt-dlp README.
2. No JS runtime is enabled via `--js-runtimes node`. Even though Node.js 22.23.1 is pre-installed on the GitHub Actions `ubuntu-latest` runner, yt-dlp only enables `deno` by default, and deno is NOT pre-installed on GitHub Actions runners.
3. No cookies are passed via `--cookies`.

### JS runtime requirements

Per the yt-dlp README (Dependencies section) and EJS Wiki:

- `yt-dlp-ejs` and a JS runtime are "strongly recommended" for "full YouTube support"
- Supported runtimes (priority order): `deno` (default, enabled), `node`, `quickjs`, `bun`
- Only `deno` is enabled by default
- To enable `node`: `--js-runtimes node` or `--js-runtimes node:/path/to/node`
- Minimum Node.js version: 22.0.0
- GitHub Actions `ubuntu-latest` has Node.js 22.23.1 pre-installed but NOT deno
- Without a JS runtime, yt-dlp falls back to `android_vr` client only and cannot solve JS challenges

**Fix for JS runtime**: Add `--js-runtimes node` to yt-dlp args AND ensure yt-dlp is installed with the `[default]` extra (or install `yt-dlp-ejs` separately / use `--remote-components ejs:github`).

### Cookies to fix bot detection

Per yt-dlp docs (`--cookies` option and FAQ):

- `--cookies FILE` reads a Netscape-format cookie file
- Format: first line must be `# HTTP Cookie File` or `# Netscape HTTP Cookie File`
- `--cookies-from-browser BROWSER` extracts from installed browsers (chrome, firefox, etc.)
- When logged-in cookies are passed, yt-dlp uses `tv_downgraded,web_safari` for free accounts or `tv_downgraded,web_creator` for premium
- Cookies can be exported from browser using yt-dlp itself: `yt-dlp --cookies-from-browser chrome --cookies cookies.txt`

**Cookie file management in CI**: A Netscape-format cookie file would need to be stored as a GitHub Actions secret (base64-encoded) and decoded at runtime. Cookies expire and would need periodic renewal. YouTube accounts used for cookie authentication risk permanent ban (as noted in youtube-transcript-api's own error messages).

### Alternative extractor args to bypass bot detection

Per the `--extractor-args youtube:player_client` documentation in the yt-dlp README:

Available clients: `web`, `web_safari`, `web_embedded`, `web_music`, `web_creator`, `mweb`, `ios`, `visionos`, `android`, `android_vr`, `tv`, `tv_downgraded`, `tv_simply`

Default: `android_vr,web_safari`
With no JS runtime: only `android_vr`
With cookies (free): `tv_downgraded,web_safari`
With cookies (premium): `tv_downgraded,web_creator`

The `web_embedded` client is added as a fallback for age-restricted videos if `android_vr` or `visionos` fails.

The `ios` and `tv` clients may avoid bot detection because they mimic non-browser clients. However, without cookies, these clients may still trigger bot detection from cloud IPs. The `--impersonate` option (for TLS fingerprinting, requires `curl_cffi`) can help but curl_cffi is not included in the `yt-dlp` zipimport binary.

### Failure modes

1. **Bot detection without cookies**: Cloud provider IPs (GitHub Actions) are frequently blocked by YouTube. Adding `--js-runtimes node` fixes JS challenges but does NOT fix IP-based blocking.
2. **Cookie expiration**: Browser cookies expire and must be periodically refreshed (typically every few hours to days).
3. **Account ban risk**: YouTube may permanently ban accounts used for automated extraction.
4. **Missing `yt-dlp-ejs`**: If installed via pip without `[default]`, JS challenge scripts are missing and yt-dlp cannot solve YouTube JS challenges even with a runtime.
5. **Rate limiting**: Too many requests from a single IP triggers 429 errors.
6. **Update churn**: YouTube changes its API frequently. yt-dlp releases new versions multiple times per week. The stable release is described as "often stale and prone to external breakage."

### Tradeoffs summary for Option B

| Dimension | Assessment |
|-----------|-----------|
| Auth required | Cookies strongly recommended for CI; may still work for some videos without |
| JS runtime | Required. `--js-runtimes node` works on GH Actions (Node 22 pre-installed) |
| CI compatibility | Moderate. Needs cookie management, yt-dlp-ejs install, and JS runtime config |
| Reliability | High for the tool itself (179k stars, 24k commits), but YouTube actively blocks it |
| Maintenance burden | Medium-high. Frequent yt-dlp updates needed; cookie renewal needed |
| Rate limits | Configurable retries/sleep; still subject to IP blacklisting |
| Subtitle quality | Full WebVTT with timestamps; auto-generated subs supported |
| License | Unlicense (public domain) |

---

## Option C: youtube-transcript-api Python library

### What API endpoints does it call?

From the source code (`_settings.py` and `_transcripts.py`):

1. **First request**: `GET https://www.youtube.com/watch?v={video_id}` -- fetches the video HTML page to extract the `INNERTUBE_API_KEY` from the embedded JavaScript.
2. **Second request**: `POST https://www.youtube.com/youtubei/v1/player?key={api_key}` -- sends a JSON body with the Innertube context:
   ```json
   {
     "context": {
       "client": {
         "clientName": "ANDROID",
         "clientVersion": "20.10.38"
       }
     },
     "videoId": "{video_id}"
   }
   ```
   This returns video metadata including caption tracks.
3. **Third request**: `GET {caption_baseUrl}` -- fetches the actual transcript XML from the `baseUrl` field in the caption track data. The response is XML with `<text start="0.0" dur="1.54">...</text>` elements.

### Does it require authentication / cookies?

**No.** Per the source code (`_api.py` lines 27-29):
```python
# Cookie auth has been temporarily disabled, as it is not working properly with
# YouTube's most recent changes.
# if cookie_path is not None:
#     http_client.cookies = _load_cookie_jar(cookie_path)
```

Cookie authentication code is present but commented out. The `Cookie Authentication` section of the README explicitly states: "Unfortunately, some recent changes to the YouTube API have broken the current implementation of cookie based authentication, so this feature is currently not available."

The library does NOT require any API key -- it extracts the public Innertube API key from the video page HTML.

### Does it require a JS runtime?

**No.** The library makes plain HTTP requests using the `requests` library. It does not execute any JavaScript. It parses the Innertube API response JSON directly.

### Does it work inside GitHub Actions / headless CI environments?

**Partially.** The library works by making standard HTTP requests, so technically it can run anywhere Python runs. However, the source code and error handling in `_errors.py` explicitly acknowledge:

> "YouTube is blocking requests from your IP. This usually is due to one of the following reasons: ... You are doing requests from an IP belonging to a cloud provider (like AWS, Google Cloud Platform, Azure, etc.). Unfortunately, most IPs from cloud providers are blocked by YouTube."

The `RequestBlocked` error is raised when YouTube returns "Sign in to confirm you're not a bot" or HTTP 429. GitHub Actions runners use cloud IPs (Azure), so they will likely hit this block.

Two workarounds are documented:
1. **Rotating residential proxies** (via `WebshareProxyConfig` or `GenericProxyConfig`) -- requires a paid proxy service
2. **Cookie authentication** -- listed as "NOT RECOMMENDED" because "YouTube will eventually permanently ban the account" -- and in any case, cookie auth is currently broken in the library

### Known failure modes / rate limits

From the source code (`_errors.py`) and open issues:

- **`RequestBlocked`**: YouTube's "Sign in to confirm you're not a bot" from cloud IPs
- **`IpBlocked`**: HTTP 429 Too Many Requests
- **`AgeRestricted`**: Age-restricted videos (cookie auth needed, but broken)
- **`TranscriptsDisabled`**: Video has no captions
- **`VideoUnavailable`**: Deleted/private video
- **`PoTokenRequired`**: `exp=xpe` in caption URL (open issue #592, April 2026 -- still unresolved)
- **`NoTranscriptFound`**: Requested language not available
- **`YouTubeRequestFailed`**: Generic HTTP error

The `TranscriptListFetcher._fetch_captions_json()` method has a retry mechanism for `RequestBlocked` that respects `proxy_config.retries_when_blocked`, but the default is 0 retries.

Open issue #612 (July 2026) reports that 429 retries actually fail because `urllib3.Retry` excludes POST methods by default.

### Does it fetch auto-generated captions? Can it filter by language?

**Yes.** The `TranscriptList` class has three search methods:
- `find_transcript(language_codes)` -- prefers manually created, falls back to generated
- `find_manually_created_transcript(language_codes)` -- only manual
- `find_generated_transcript(language_codes)` -- only auto-generated (ASR)

The `is_generated` field on transcript objects indicates whether the transcript was auto-generated. The `fetch()` method on `YouTubeTranscriptApi` defaults to `languages=["en"]`.

### Maintenance status

- **Last release**: v1.2.4 on 2026-01-29 (active -- less than 6 months ago)
- **License**: MIT
- **Stars**: 7.9k
- **Open issues**: 18
- **Commits**: 402

Key open issues:
- #592 (Apr 2026): `PoTokenRequired: exp=xpe` -- video-specific token requirement breaks subtitle fetching for some videos
- #437 (Jun 2025): Cookie authentication broken -- author acknowledges it and labels it "contributions welcome!"
- #612 (Jul 2026): 429 retry mechanism broken for POST requests

### Tradeoffs summary for Option C

| Dimension | Assessment |
|-----------|-----------|
| Auth required | Cookie auth is broken. No auth available for age-restricted or bot-blocked videos |
| JS runtime | Not required. Pure Python HTTP requests |
| CI compatibility | Low. GitHub Actions IPs are cloud IPs, which YouTube blocks. Workaround requires paid proxy service |
| Reliability | Moderate. 7.9k stars, actively maintained, but uses undocumented YouTube API |
| Maintenance burden | Low. Python library replaces subprocess calls. No cookie management. But depends on undocumented API that can break without warning |
| Rate limits | Built-in proxy support but retry mechanism has known bugs. No rate-limit configurability comparable to yt-dlp |
| Subtitle quality | Timestamped text snippets; `is_generated` flag available; language filtering works |
| License | MIT |

---

## Side-by-Side Comparison

| Dimension | Option B (yt-dlp + cookies) | Option C (youtube-transcript-api) |
|-----------|------------------------------|-----------------------------------|
| **Auth** | Cookies work (Netscape format file). Required for CI from cloud IPs. | Cookie auth is broken (commented out in source). No auth available. |
| **JS Runtime** | Required. `--js-runtimes node` enables Node.js (pre-installed on GH Actions). Must also install `yt-dlp-ejs` (via `pip install "yt-dlp[default]"`). | Not required. Pure Python HTTP requests. |
| **Cloud IP blocking** | Can be worked around with cookies. Without cookies, bot detection will block cloud IPs. | No working workaround for cloud IPs. `RequestBlocked` error is expected on GH Actions. Cookie auth is broken. Proxy config is only mitigation (paid service). |
| **Success probability on GH Actions** | High (with cookies + JS runtime config) | Low (cloud IP block with no fix) |
| **Implementation effort** | Medium. Add `--js-runtimes node`, install `yt-dlp[default]`, add `--cookies` with stored cookie file, update subprocess args. | Low. Replace `subprocess.run(["yt-dlp", ...])` with `YouTubeTranscriptApi().fetch(video_id)`. |
| **API stability** | Uses multiple extraction strategies (web, Innertube). Frequently updated (multiple releases/week). | Uses single undocumented Innertube API endpoint. Breaking changes break all users until library updates. |
| **Release cadence** | Multiple releases per week (nightly+stable). Very active (179k stars, 24k commits). | ~5 releases in 2025-2026. Active but much slower cadence (402 commits total). |
| **Extra dependencies** | JS runtime (node available), yt-dlp-ejs package, optional curl_cffi/certifi | `requests` library only (+ `defusedxml` for XML parsing) |
| **Rate limiting** | Built-in retry (10 default), retry-sleep, fragment retries. Highly configurable. | Minimal retry support (proxy retries only, broken for POST). No rate limit configurability. |
| **Subtitle parsing** | Outputs full WebVTT/SRT files that need stripping. Current pipeline has `_strip_subtitle_formatting()` helper. | Returns structured `FetchedTranscriptSnippet` objects with `text`, `start`, `duration`. No formatting to strip. |
| **License** | Unlicense | MIT |

## Recommendation

**Adopt Option B (yt-dlp with cookies and JS runtime).**

youtube-transcript-api (Option C) has a critical blocker for this use case: its cookie authentication is broken and the maintainer has acknowledged it needs re-implementation. Without working authentication, the library cannot bypass YouTube's bot detection from GitHub Actions cloud IPs. The library's own error messages state that cloud IPs are blocked and the only reliable workaround is rotating residential proxies (a paid service).

yt-dlp with cookies (Option B) has a clear, documented path to working in CI:

1. Install yt-dlp with `pip install "yt-dlp[default]"` (includes `yt-dlp-ejs` package)
2. Enable Node.js runtime: add `--js-runtimes node` to yt-dlp args (Node 22 is pre-installed on GH Actions `ubuntu-latest`)
3. Provide cookies: export a Netscape-format cookies file, store as a GitHub secret, decode at runtime, and pass via `--cookies cookies.txt`
4. Player client: with cookies, yt-dlp automatically uses `tv_downgraded,web_safari` which has better bot-detection avoidance

The cookie management burden is real but manageable: cookies need periodic renewal (every few weeks to months), and the YouTube account used faces a ban risk if detected. This is a maintenance cost that Option C currently cannot avoid either -- youtube-transcript-api requires proxies which also have ongoing cost and management.

yt-dlp also provides significantly better rate-limit handling, retry logic, and client rotation strategies than youtube-transcript-api. Its massive community and release frequency mean it adapts to YouTube changes faster.

### Implementation checklist for Option B

1. Change `pip install -e ".[dev]"` to `pip install -e ".[default]"` (or add `yt-dlp-ejs` to dependencies)
2. Add `--js-runtimes node` to yt-dlp arguments in `fetcher.py`
3. Export YouTube cookies as Netscape-format file: `yt-dlp --cookies-from-browser chrome --cookies cookies.txt`
4. Store `cookies.txt` as GitHub secret (base64-encoded): `base64 -i cookies.txt`
5. In the workflow, decode the secret and write to a file, pass to yt-dlp via `--cookies /path/to/cookies.txt`
6. Consider adding `--extractor-args "youtube:player_client=default"` (let yt-dlp auto-select based on cookies) or explicitly set `tv_downgraded,web_safari`
7. Keep the existing two-attempt fallback pattern; it still adds resilience

### When to revisit Option C

If the youtube-transcript-api maintainer re-implements cookie authentication (issue #437), Option C becomes viable as a simpler, dependency-lighter alternative. At that point, re-evaluate based on whether cookie auth in youtube-transcript-api is more or less reliable than the yt-dlp path.
