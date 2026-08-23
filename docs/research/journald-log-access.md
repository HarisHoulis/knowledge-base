# Accessing systemd journald logs of a single service on a remote VPS

## Investigation Date

2026-08-23

## Question

A Ktor backend runs as the systemd unit `kb-backend` on a Hetzner VPS (Ubuntu/Debian, ARM, 4 GB RAM, 40 GB SSD). Its stdout/stderr are captured by journald, and there is no other log infrastructure. The owner SSHes in only occasionally and wants to read recent errors without friction. What are the options for accessing the journald logs of that single service, and what is the least-friction way for an occasional single-user operator to read recent errors — including embedding a journald excerpt into the existing `OnFailure=` GitHub-issue alert (#128)?

## Sources

- [S1] journalctl(1) — systemd man page: https://www.man7.org/linux/man-pages/man1/journalctl.1.html
- [S2] journald.conf(5) — systemd man page: https://www.man7.org/linux/man-pages/man5/journald.conf.5.html
- [S3] systemd.journal-fields(7) — systemd man page: https://www.man7.org/linux/man-pages/man7/systemd.journal-fields.7.html
- [S4] systemd.exec(5) — systemd man page: https://www.man7.org/linux/man-pages/man5/systemd.exec.5.html
- [S5] systemd.unit(5) — systemd man page: https://www.man7.org/linux/man-pages/man5/systemd.unit.5.html
- [S6] systemd.time(7) — systemd man page: https://www.man7.org/linux/man-pages/man7/systemd.time.7.html
- [S7] systemd source, `tmpfiles.d/systemd.conf.in` (creates `/var/log/journal` at boot): https://github.com/systemd/systemd/blob/main/tmpfiles.d/systemd.conf.in
- [S8] systemd v253 `man/journald.conf.xml` (historical `Storage=` default, "auto"): https://github.com/systemd/systemd/blob/v253/man/journald.conf.xml
- [S9] systemd v260 `man/journald.conf.xml` (current `Storage=` default, compile-time "persistent"): https://github.com/systemd/systemd/blob/v260/man/journald.conf.xml
- [S10] systemd commit `7af88c1e1ef9` "journald: allow default storage mode to be configured" (v259): https://github.com/systemd/systemd/commit/7af88c1e1ef9

## Findings

### 1. The service's stdout/stderr are already in the journal — nothing to build or install

journald captures the stdout/stderr of every systemd unit by default: `StandardOutput=journal` is the default for system services, `StandardError=` defaults to `inherit` (i.e. the same journal stream) [S4]. Every unit whose stdout/stderr is connected to the journal gains an automatic `After=` dependency on systemd-journald.socket [S4]. Journal records from this path carry the trusted field `_TRANSPORT=stdout`, plus `_SYSTEMD_UNIT=kb-backend.service` for the originating unit [S3]. There is therefore **no setup step**: logs are being collected today.

Access control is the only gate. The system journal is readable by root and by members of the `systemd-journal`, `adm`, and `wheel` groups; other users get only their per-user journals [S1]. A deploy user can read `kb-backend` logs by being in `adm` or `systemd-journal`, or by `sudo`. (A root-run `OnFailure=` handler sidesteps this entirely — see §4.)

### 2. Reading logs locally on the box: journalctl invocation patterns

`journalctl` prints entries from the journal; `-u/--unit=kb-backend` filters to messages from the unit via a `_SYSTEMD_UNIT=` match, plus systemd's own messages about the unit and its coredumps [S1]. Recipes for an occasional operator, all cited to [S1] unless noted:

| Goal | Command | Notes |
|------|---------|-------|
| Tail (interactive, at the newest lines) | `journalctl -u kb-backend -e` | `-e/--pager-end` jumps to the end of the journal in the pager; implies `--lines=1000` and `--boot=0` |
| Last N events | `journalctl -u kb-backend -n 50` | `-n/--lines=` limits events; default is 10 when no argument is given |
| Recent window | `journalctl -u kb-backend --since "1 hour ago"` | `-S/--since=`; relative times are `systemd.time(7)` syntax, `"… ago"` and `-`/`+` prefixes both accepted [S1][S6] |
| Follow (live) | `journalctl -u kb-backend -f` | `-f/--follow` prints new entries as appended; implies `--lines=` |
| Errors only | `journalctl -u kb-backend -p err` | `-p/--priority=`; a single level shows it **and** lower (more important) levels, i.e. err/crit/alert/emerg |
| Clean block for copy/paste or issue body | `journalctl -u kb-backend -p err --since "1 hour ago" -n 50 --no-pager -o short-precise -q` | see §4 for flag rationale |
| Full structured entry | `journalctl -u kb-backend -o verbose` | shows all fields of each entry |
| Previous boot | `journalctl -u kb-backend -b -1` | `-b/--boot=` with negative offset = boots before last |

Other useful filters: `_PID=<pid>` or any `FIELD=VALUE` match (multiple matches on different fields AND together; `+` as a separate word ORs groups) [S1]; `-g/--grep=` regex over the message [S1]; `-o short-precise` for syslog-style timestamps with microsecond precision (best for correlating stack traces with `_PID=`) [S1].

**`--user` vs system units.** `journalctl --user` shows journals of the calling user's service manager (`systemd --user`) and only works when persistent storage is enabled [S1][S2]. It is irrelevant here: `kb-backend` is a system unit, so `journalctl -u kb-backend` reads the system journal with no `--user` flag. Worth knowing only so nobody reaches for it.

### 3. Remote access patterns (SSH only)

There is no journal-specific transport needed for a one-box operator. The systemd-native options for shipping journals off-box — `systemd-journal-upload`/`systemd-journal-remote` (a central collector receiving the Journal Export Format) — exist [S2], but require a second always-on server to collect, and are ruled out as overkill for one box with one service.

Practical remote patterns:

- One-shot read: `ssh box 'journalctl -u kb-backend -p err --since "1 hour ago" --no-pager'` — non-interactive, no pager involvement.
- Interactive follow: `ssh -t box 'journalctl -u kb-backend -f'` — `-t` allocates a TTY so the pager/follow works; hit Ctrl-C to stop.
- Interactive tail: `ssh -t box 'journalctl -u kb-backend -e'`.
- A one-line alias on the laptop (`alias kberr='ssh box "journalctl -u kb-backend -p err --since 1h --no-pager"'`) makes it a single keystroke.

Log aggregators (ELK, Loki+Grafana, Prometheus+Loki) are ruled out in one line each: ELK needs a Java stack and hundreds of MB of RAM on a 4 GB box; Loki+Grafana is a whole second service stack to run and maintain; and neither is justified when journalctl already indexes and filters everything on the box.

### 4. Capturing an error excerpt in the OnFailure= GitHub-issue hook

**Mechanism.** `OnFailure=` in the `[Unit]` section lists units activated when the unit enters the "failed" state [S5]. `OnFailureJobMode=` defaults to `replace` [S5]. The documented pattern is a templated oneshot handler: create `/etc/systemd/system/failure-handler@.service` (`Type=oneshot`, `ExecStart=/usr/local/sbin/… %i`), then wire `OnFailure=failure-handler@kb-backend.service` either on the unit or — applying to all services at once — via a drop-in `/etc/systemd/system/service.d/10-onfailure.conf` containing `OnFailure=failure-handler@%N.service` [S5]. The handler runs as root (system service, no `User=`), so journal access is unrestricted.

**Excerpt command.** Inside the handler, capture the error window:

```
journalctl -u kb-backend -n 50 -p err --since "1 hour ago" \
  --no-pager -o short-precise -q
```

and pipe the output into `gh issue create --body-file -` (extending the existing #128 hook). Flag-by-flag verification against [S1]:

- `-n 50` — caps the block at 50 lines (matches the suggested count); without it the issue body can be unbounded.
- `-p err` — only err/crit/alert/emerg, so routine INFO/DEBUG noise never reaches GitHub.
- `--since "1 hour ago"` — the handler runs at failure time; the window covers the crash. Relative-time syntax is `systemd.time(7)` [S1][S6].
- `--no-pager` — output is never piped through `less`; also defensive, since paging is normally skipped when stdout is not a TTY (the handler's stdout is a journal pipe).
- `-o short-precise` — microsecond timestamps make the block sortable and grep-able.
- `-q/--quiet` — suppresses the informational `-- Journal begins at …` and `-- Reboot --` lines and warnings about inaccessible system journals [S1]; this is what keeps the issue body a clean text block.
- Do **not** add `-x/--catalog`: journalctl(1) explicitly warns against `-x` "when attaching journalctl output to bug reports" [S1].

Timing note: `SyncIntervalSec=` means journald syncs at most every 5 minutes for ERR/WARNING/INFO/DEBUG — but a message of priority CRIT/ALERT/EMERG is synchronized to disk unconditionally and immediately [S2], so the handler always sees the fatal record.

### 5. journald persistence and rotation defaults (does the log survive reboot?)

- **`Storage=` semantics.** "volatile" keeps logs only in memory (`/run/log/journal`); "persistent" writes to `/var/log/journal`; "auto" behaves like "persistent" if `/var/log/journal` exists, and "volatile" otherwise [S2]. Since systemd v259 the compiled default is "persistent" (configurable at build time) [S9][S10]; through v258 it was "auto" [S8]. Under either default, **logs survive reboot in practice**: systemd's own `tmpfiles.d/systemd.conf.in` creates `/var/log/journal` at boot via `systemd-tmpfiles-setup.service` [S7], so even "auto" resolves to persistent on every normal systemd distro (Debian/Ubuntu included). At boot, journald starts volatile and `journalctl --flush` (via `systemd-journal-flush.service`) moves data to persistent storage automatically [S2].
- **Verify once on the box:** `journalctl --disk-usage` shows the journal size, and `systemctl status systemd-journald` or the existence of `/var/log/journal/$(cat /etc/machine-id)` confirms persistence. Nothing needs to be configured.
- **Rotation defaults (40 GB disk).** `SystemMaxUse=` (persistent) and `RuntimeMaxUse=` (volatile) cap total journal space at 10% of the filesystem, capped at 4 G; `SystemKeepFree=`/`RuntimeKeepFree=` leave 15% free, and journald honours the smaller of the two limits [S2]. On this box that is ~4 GB of retained journal. Individual files are capped by `SystemMaxFileSize=` at one eighth of `SystemMaxUse=` (capped 128 M), so ~7 rotated files of history are kept; `MaxFileSec=` rotates at one month by default; `SystemMaxFiles=` defaults to 100 [S2]. A single service logging quietly for years will not fill a 40 GB SSD.
- `journalctl --user` additionally requires persistent storage [S1][S2] — not applicable here (§2).

## Recommendation

**Primary (zero-friction, recommended): ship the journald excerpt inside the existing `OnFailure=` → GitHub-issue path.** The repo already has the hook (#128); the only change is to have the failure handler run `journalctl -u kb-backend -n 50 -p err --since "1 hour ago" --no-pager -o short-precise -q` and pipe it into `gh issue create`. The operator then reads recent errors as a GitHub notification/issue — no SSH, no commands to remember, nothing to run. This matches how an occasional single-user operator already consumes the system's failures, and §4 verifies the flags yield a clean, bounded text block (the key ones being `--no-pager` + `-q` for cleanliness, `-p err` + `-n 50` for signal and size, and no `-x`).

**Secondary (when SSHing in anyway):** two muscle-memory commands, optionally aliased on the laptop:

- `journalctl -u kb-backend -e` — see the last 1000 lines of the current boot (jump-to-end) [S1]
- `journalctl -u kb-backend -p err --since "1 hour ago" --no-pager` — recent errors as a clean block [S1][S6]
- `ssh -t box 'journalctl -u kb-backend -f'` — follow live [S1]

Make the deploy user a member of `adm` or `systemd-journal` so no `sudo` is needed [S1].

**No other infrastructure.** Log aggregators (ELK, Loki/Grafana) and journal shipping (`journal-upload`/`journal-remote`) are all ruled out for a 4 GB/40 GB single-user box — journalctl already indexes and filters everything needed. Persistence needs no action: the default storage mode yields persistent logs that survive reboot on any systemd distro (§5), which a one-time `journalctl --disk-usage` check confirms.

This is research only — no config, code, or system changes were made.
