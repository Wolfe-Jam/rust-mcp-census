# The Rust MCP Census

Every server in the official [MCP Registry](https://registry.modelcontextprotocol.io) that ships a **cargo** (crates.io) package, counted each week.

## 30 October 2026: 104 servers

- **104** active servers list a cargo package, out of 52,348 active servers in the registry (53,046 entries, deprecated included). 2 more cargo servers are deprecated.
- **90** owners: 55 people and 33 organisations on GitHub, 2 elsewhere.
- Cargo has been accepted in production since registry v1.8.0 (2026-07-13). The first cargo server arrived on 2026-07-13; the latest on 2026-10-30 (109 days).
- **+10** new in the last 7 days (2026-10-24 to 2026-10-30).

## By week

Weeks start on Monday.

| Week of | New | Total |
|---|---|---|
| 2026-07-13 | 9 | 9 |
| 2026-07-20 | 1 | 10 |
| 2026-07-27 | 7 | 17 |
| 2026-08-03 | 7 | 24 |
| 2026-08-10 | 2 | 26 |
| 2026-08-17 | 4 | 30 |
| 2026-08-24 | 5 | 35 |
| 2026-08-31 | 6 | 41 |
| 2026-09-07 | 7 | 48 |
| 2026-09-14 | 6 | 54 |
| 2026-09-21 | 7 | 61 |
| 2026-09-28 | 7 | 68 |
| 2026-10-05 | 5 | 73 |
| 2026-10-12 | 14 | 87 |
| 2026-10-19 | 10 | 97 |
| 2026-10-26 (so far) | 7 | 104 |

## By month

| Month | New | Total |
|---|---|---|
| Jul 2026 | 15 | 15 |
| Aug 2026 | 20 | 35 |
| Sep 2026 | 27 | 62 |
| Oct 2026 | 42 | 104 |

## How they ship

| Packages | Servers |
|---|---|
| `cargo` | 73 |
| `cargo` + `npm` | 12 |
| `cargo` + `oci` | 5 |
| `cargo` + `npm` + `pypi` | 5 |
| `cargo` + `mcpb` | 4 |
| `cargo` + `npm` + `oci` | 2 |
| `cargo` + `mcpb` + `npm` | 2 |
| `cargo` + `pypi` | 1 |

Many Rust MCP servers list another way (npm, an MCP bundle or a container) and don't appear here. This census counts servers that list a cargo package.

## New in the last 7 days (10)

| First cargo | Server | What it does |
|---|---|---|
| 2026-10-30 | [`io.github.dot-ASH/umbriel-mcp`](https://github.com/dot-ASH/umbriel-mcp) | Control the Umbriel Wayland compositor: windows, workspaces, input, screenshots, clipboard. |
| 2026-10-29 | `science.transaction.wai/quantum` | OpenQASM 3 programs run, checked against their intent and signed on this machine. |
| 2026-10-29 | [`io.github.kinkirill/bevy-manual-mcp`](https://github.com/kinkirill/bevy_manual_mcp) | Version-accurate Bevy API docs, Book, migration guides and examples for AI agents. |
| 2026-10-27 | [`io.github.ermoluk/mcp-warden`](https://github.com/ermoluk/mcp-warden) | Local credential broker: agents call APIs, SSH and DBs via scoped presets; secrets stay in keychain. |
| 2026-10-27 | [`io.github.emanuele-em/kanzo`](https://github.com/emanuele-em/kanzo) | Self-hosted kanban for humans and agents. One 4 MB binary, starts in 2 ms, zero setup. |
| 2026-10-27 | [`io.github.devops-infinity/ownsearch`](https://github.com/devops-infinity/ownsearch) | Quality-ranked SearXNG search over MCP with local fleet state, scoring, and merged results. |
| 2026-10-26 | [`io.github.godot-pty/gpty`](https://github.com/godot-pty/gpty) | Spawn panes, inject input and read output in a tiling terminal workspace |
| 2026-10-24 | [`io.github.semlith/semlith`](https://github.com/semlith/semlith) | Local search over your code and documents for AI agents. |
| 2026-10-24 | [`io.github.oxygenframe/oxframe`](https://github.com/oxygenframe/oxframe-cli) | Make videos from code: check scenes frame by frame, inspect nodes, render a frame, search the docs. |
| 2026-10-24 | [`io.github.MikkoParkkola/nab`](https://github.com/MikkoParkkola/nab) | Token-optimized HTTP client for LLMs: fetches any URL as clean markdown. CLI and MCP server. |

## All 104

| # | First cargo | Server | Crate | Packages | ★ | What it does |
|---|---|---|---|---|---|---|
| 1 | 2026-07-13 | [`io.github.VoidNullable/lific`](https://github.com/VoidNullable/lific) | [lific](https://crates.io/crates/lific) | `cargo` | 83 | Local-first, lightweight issue tracker. Single binary, SQLite-backed, MCP-native. |
| 2 | 2026-07-14 | [`io.github.ltspace/dowse`](https://github.com/ltspace/dowse) | [dowse](https://crates.io/crates/dowse) | `cargo` | 39 | Fast local full-text search for Windows files (tantivy + jieba), exposed to AI agents over MCP. |
| 3 | 2026-07-14 | [`io.github.ojhermann-org/ferric-fred-mcp`](https://github.com/ojhermann-org/ferric-fred) | [ferric-fred-mcp](https://crates.io/crates/ferric-fred-mcp) | `cargo` | 0 | MCP server for FRED (Federal Reserve Economic Data): full read API plus GeoFRED, 34 tools. |
| 4 | 2026-07-17 | [`io.github.Liohtml/matomo-mcp`](https://github.com/Liohtml/matomo-mcp) | [matomo-mcp](https://crates.io/crates/matomo-mcp) | `cargo` + `oci` | 0 | Curated read-only Matomo Analytics tools: traffic, pages, referrers, e-commerce, real-time & more. |
| 5 | 2026-07-17 | [`io.github.Liohtml/sistrix-mcp`](https://github.com/Liohtml/sistrix-mcp) | [sistrix-mcp](https://crates.io/crates/sistrix-mcp) | `cargo` + `oci` | 0 | Curated SISTRIX SEO tools: visibility, rankings, keywords, backlinks, AI visibility, Amazon data. |
| 6 | 2026-07-18 | [`io.github.singhpratech/notepatra-mcp`](https://github.com/singhpratech/notepatra) | [notepatra-mcp](https://crates.io/crates/notepatra-mcp) | `cargo` | 6 | Notepatra editor MCP server — 35 tools; every write human-approved in the editor; local-only. |
| 7 | 2026-07-18 | [`one.faf/rust-faf-mcp`](https://github.com/Wolfe-Jam/rust-faf-mcp) | [rust-faf-mcp](https://crates.io/crates/rust-faf-mcp) | `cargo` + `npm` | 4 | Persistent project context — Rust-native MCP server. IANA-registered .faf format. |
| 8 | 2026-07-19 | [`io.github.brechanbech/sec-mcp`](https://github.com/brechanbech/sec-mcp) | [sec-mcp](https://crates.io/crates/sec-mcp) | `cargo` | 0 | Rust MCP server for SEC EDGAR data — company filings, financial concepts, and company info |
| 9 | 2026-07-19 | [`io.github.brechanbech/xojo-mcp`](https://github.com/brechanbech/xojo-mcp) | [xojo-mcp](https://crates.io/crates/xojo-mcp) | `cargo` | 0 | MCP server for controlling the Xojo IDE on macOS |
| 10 | 2026-07-20 | [`io.github.patchloom/patchloom`](https://github.com/patchloom/patchloom) | [patchloom](https://crates.io/crates/patchloom) | `cargo` + `npm` | 20 | Agent-safe structured edits: JSON/YAML/TOML/md/AST, dry-run, batch/tx. Not a filesystem MCP. |
| 11 | 2026-07-28 | [`io.github.lacs-project/sysknife`](https://github.com/lacs-project/sysknife) | [sysknife-cli](https://crates.io/crates/sysknife-cli) | `cargo` | 104 | Administers Linux via typed, approval-gated actions with an Ed25519-signed audit trail. |
| 12 | 2026-07-28 | [`io.github.protostatis/unbrowser`](https://github.com/protostatis/unbrowser) | [unbrowser](https://crates.io/crates/unbrowser) | `cargo` + `pypi` | 17 | Chrome-free MCP web access for agents with low-token page maps and browser escalation hints. |
| 13 | 2026-07-29 | [`io.github.Wolfe-Jam/mcp-better`](https://github.com/Wolfe-Jam/mcp-better) | [mcp-better](https://crates.io/crates/mcp-better) | `cargo` + `npm` | 2 | AAIF-verified modern MCP setup optimised to the 2026-07-28 model (BETTER textbook). |
| 14 | 2026-07-29 | [`io.github.klNuno/fast-mcp-ssh`](https://github.com/klNuno/fast-mcp-ssh) | [fast-mcp-ssh](https://crates.io/crates/fast-mcp-ssh) | `cargo` | 5 | SSH, SFTP, PTY shells, host-to-host copies and remote screenshots for AI agents. One Rust binary. |
| 15 | 2026-07-31 | [`io.github.Mapika/portview`](https://github.com/Mapika/portview) | [portview](https://crates.io/crates/portview) | `cargo` | 61 | See what's on your ports, the processes behind them, and diagnose conflicts and leaks. |
| 16 | 2026-08-01 | [`io.github.morluto/leantoken`](https://github.com/morluto/leantoken) | [leantoken](https://crates.io/crates/leantoken) | `cargo` | 134 | Token-bounded repository context for coding agents over MCP. |
| 17 | 2026-08-02 | [`io.github.smbcloudXYZ/xcrs`](https://github.com/smbcloudXYZ/smbcloud-cli) | [xcrs](https://crates.io/crates/xcrs) | `cargo` | 12 | MCP tools for testing mobile and TV apps on iOS simulators, Android phones, and Apple/Android TV. |
| 18 | 2026-08-05 | [`io.github.koshak01/tidex6-mcp-local`](https://github.com/koshak01/tidex6) | [tidex6-mcp-local](https://crates.io/crates/tidex6-mcp-local) | `cargo` | 1 | Private USDC/USDT payments on Solana: hidden amounts, unlinkable, optional auditor. |
| 19 | 2026-08-05 | [`io.github.mahabubul470/gpp`](https://github.com/mahabubul470/gpp) | [gpp-cli](https://crates.io/crates/gpp-cli) | `cargo` | 2 | Project knowledge graph with history-checked belief staleness, changeset proposals, cost reporting |
| 20 | 2026-08-06 | [`io.github.aurumflux20/effectfence`](https://github.com/aurumflux20/effectfence) | [effectfence](https://crates.io/crates/effectfence) | `cargo` + `npm` | 0 | Stops agents double-firing side effects: 1,000 racing duplicates, exactly one execution. |
| 21 | 2026-08-07 | [`io.github.tenequm/pond`](https://github.com/tenequm/pond) | [pond-db](https://crates.io/crates/pond-db) | `cargo` | 89 | Lossless archive and search for AI agent sessions across clients, exposed to agents over MCP. |
| 22 | 2026-08-08 | [`io.github.MauricioPerera/kite-lite`](https://github.com/MauricioPerera/kite-lite) | [kite-lite](https://crates.io/crates/kite-lite) | `cargo` | 0 | Fetch, parse, screenshot and browse pages via MCP without a real browser -- no JS execution. |
| 23 | 2026-08-08 | [`io.github.NexQL-OSS/nexql-mcp`](https://github.com/NexQL-OSS/mcp) | [nexql-mcp](https://crates.io/crates/nexql-mcp) | `cargo` + `npm` | 0 | Standalone Postgres MCP server — schema-aware, read-only by default, installable everywhere. |
| 24 | 2026-08-09 | [`io.github.sandbanks/agentic_ssh`](https://github.com/sandbanks/agentic_ssh) | [agentic_ssh](https://crates.io/crates/agentic_ssh) | `cargo` | 6 | High-performance (Rust), token-efficient, and asynchronous SSH orchestrations for AI agents. |
| 25 | 2026-08-11 | [`io.github.asanabrial/leteo`](https://github.com/asanabrial/leteo) | [leteo](https://crates.io/crates/leteo) | `cargo` + `npm` | 4 | Persistent memory for AI coding agents: one Rust binary, one local SQLite database. |
| 26 | 2026-08-14 | [`io.github.deed-lang/deed`](https://github.com/deed-lang/deed) | [deed-lang](https://crates.io/crates/deed-lang) | `cargo` | 9 | Contract-first language and MCP server for capability-aware code and patch review. |
| 27 | 2026-08-19 | [`io.github.verivus-oss/sqry`](https://github.com/verivus-oss/sqry) | [sqry-mcp](https://crates.io/crates/sqry-mcp) | `cargo` + `oci` | 31 | AST-based semantic code search: 39 tools over 37 languages. Call tracing and impact analysis. |
| 28 | 2026-08-21 | [`io.github.tombaldwin/ebman`](https://github.com/tombaldwin/ebman) | [ebman](https://crates.io/crates/ebman) | `cargo` | 1 | MCP server for AWS Elastic Beanstalk: read the fleet; --allow-writes adds two-phase writes. |
| 29 | 2026-08-23 | [`io.github.nhatvu148/video-transcriber-mcp`](https://github.com/nhatvu148/video-transcriber-mcp-rs) | [video-transcriber-mcp](https://crates.io/crates/video-transcriber-mcp) | `cargo` | 19 | Transcribe videos from 1000+ platforms or local files offline, and search across every transcript |
| 30 | 2026-08-23 | [`io.github.ojuschugh1/sqz`](https://github.com/ojuschugh1/sqz) | [sqz-mcp](https://crates.io/crates/sqz-mcp) | `cargo` | 673 | Pre-injection context compression for coding agents. Zero LLM calls, zero telemetry, offline-safe. |
| 31 | 2026-08-26 | [`io.github.oxyplay/wyd`](https://github.com/oxyplay/wyd) | [wyd](https://crates.io/crates/wyd) | `cargo` | 4 | Local runtime provenance for coding agents. Inspect sessions and explain which one owns a process. |
| 32 | 2026-08-27 | [`io.github.QAtlasHub/doiget`](https://github.com/QAtlasHub/doiget) | [doiget-cli](https://crates.io/crates/doiget-cli) | `cargo` + `mcpb` | 2 | OA-first paper fetcher: DOIs/arXiv IDs to local PDFs + metadata via Open Access APIs. |
| 33 | 2026-08-27 | [`io.github.husk-security/husk`](https://github.com/husk-security/husk) | [husk-sec](https://crates.io/crates/husk-sec) | `cargo` + `npm` | 6 | Local-first defensive scanner for vulnerable dependencies, leaked secrets, and risky agent configs |
| 34 | 2026-08-28 | [`io.github.MatthewSherlin/mushroomdb`](https://github.com/MatthewSherlin/mushroomdb) | [mushroomdb-cli](https://crates.io/crates/mushroomdb-cli) | `cargo` + `npm` | 5 | Embedded graph database for agents: declare association rules once, edges maintain themselves. |
| 35 | 2026-08-28 | [`io.github.underpass-ai/kmp`](https://github.com/underpass-ai/kmp) | [kmp-mcp](https://crates.io/crates/kmp-mcp) | `cargo` + `mcpb` | 0 | Local-first agent memory that preserves what happened, when and why |
| 36 | 2026-09-02 | [`io.github.joshiii-xyz/basalt`](https://github.com/joshiii-xyz/basalt) | [basalt-db](https://crates.io/crates/basalt-db) | `cargo` | 1 | Local SQL workspaces with bounded, recoverable writes for coding agents. |
| 37 | 2026-09-04 | [`io.github.AbduljabbarBXR/cornea`](https://github.com/AbduljabbarBXR/cornea) | [cornea](https://crates.io/crates/cornea) | `cargo` | 1 | Deterministic visual inspection for AI agents. Overlap, overflow, contrast, quality. |
| 38 | 2026-09-04 | [`si.sigit/cli`](https://github.com/getsigit/si) | [sigit-si-cli](https://crates.io/crates/sigit-si-cli) | `cargo` | 6 | Run sigit.si locally: browse repos, search code, manage PRs, issues, and Cloud Sessions. |
| 39 | 2026-09-05 | [`io.github.adrianov/abcop`](https://github.com/adrianov/abcop) | [abcop](https://crates.io/crates/abcop) | `cargo` | 2 | ABC complexity gate for AI-written code with an MCP inspection tool. |
| 40 | 2026-09-05 | [`io.github.adrianov/rrubocop`](https://github.com/adrianov/rrubocop) | [rrubocop](https://crates.io/crates/rrubocop) | `cargo` | 2 | Fast RuboCop-compatible Ruby linter with MCP inspect and autocorrect tools. |
| 41 | 2026-09-05 | [`io.github.ugur-murat-alt/agz-rust-coder`](https://github.com/ugur-murat-alt/agz-rust-coder) | [agz-rust-coder](https://crates.io/crates/agz-rust-coder) | `cargo` | 2 | Bounded, source-write-free Rust correctness tools grounded in Cargo and rustc output. |
| 42 | 2026-09-07 | [`io.github.daffa2555/razor`](https://github.com/daffa2555/Tokenectomy) | [tokenectomy](https://crates.io/crates/tokenectomy) | `cargo` | 6 | Autonomous log surgery & secret redaction MCP server for AI coding agents. |
| 43 | 2026-09-07 | [`io.github.tarides/sudo-proxy`](https://github.com/tarides/sudo-proxy) | [sudo-proxy](https://crates.io/crates/sudo-proxy) | `cargo` + `mcpb` | 0 | Privileged command execution proxy with human approval via pkexec or sudo |
| 44 | 2026-09-08 | [`io.github.4lador/leantime-mcp`](https://github.com/4lador/leantime-mcp) | [leantime-mcp](https://crates.io/crates/leantime-mcp) | `cargo` | 0 | Unofficial MCP server for Leantime: 42 agent-first tools, backup/restore, dry-run validation |
| 45 | 2026-09-09 | [`tech.melodium/melodium-mcp`](https://gitlab.com/melodium/melodium) | [melodium-mcp](https://crates.io/crates/melodium-mcp) | `cargo` |  | MCP server exposing Mélodium program validation and reference lookup |
| 46 | 2026-09-10 | [`dev.ilien.svipall/mcp`](https://github.com/ilien-dev/svipall) | [svipall](https://crates.io/crates/svipall) | `cargo` + `npm` + `oci` | 20 | Read any page past its anti-bot wall, crawl sites, search without an API key, solve captchas locally |
| 47 | 2026-09-11 | [`io.github.ugur-murat-alt/agz-rust-mcp`](https://github.com/ugur-murat-alt/agz-rust-mcp) | [agz-rust-mcp](https://crates.io/crates/agz-rust-mcp) | `cargo` | 2 | Bounded, source-write-free Rust correctness tools grounded in Cargo and rustc output. |
| 48 | 2026-09-12 | [`io.github.ECD5A/tkach-security`](https://github.com/ECD5A/Tkach-Security) | [tkach-mcp](https://crates.io/crates/tkach-mcp) | `cargo` | 1 | Fail-closed MCP adapter for untrusted model output over a local Tkach runtime. |
| 49 | 2026-09-14 | [`io.github.factum-project/factum`](https://github.com/factum-project/factum) | [factum-mcp](https://crates.io/crates/factum-mcp) | `cargo` | 3 | Auditable memory for AI agents: provenance, cascade retraction, conflict refusal |
| 50 | 2026-09-16 | [`io.github.jolars/deixis`](https://github.com/jolars/deixis) | [deixis](https://crates.io/crates/deixis) | `cargo` | 2 | Typed LSP operations for MCP clients. |
| 51 | 2026-09-17 | [`io.github.gridhra/atx-mcp`](https://github.com/gridhra/atx-mcp) | [atx-mcp](https://crates.io/crates/atx-mcp) | `cargo` + `npm` + `oci` | 0 | Deterministic, non-generative image transform MCP server: reproducible recipes, immutable originals. |
| 52 | 2026-09-18 | [`io.github.eabz/tirith`](https://github.com/eabz/tirith) | [tirith-mcp](https://crates.io/crates/tirith-mcp) | `cargo` | 4 | Coordination server for parallel coding agents: claims, contracts, notices, and memory notes. |
| 53 | 2026-09-19 | [`io.github.grayclayton/aetre-mcp`](https://github.com/grayclayton/aetre) | [aetre-mcp](https://crates.io/crates/aetre-mcp) | `cargo` + `oci` | 0 | Decision-theoretic triage and fail-closed agent gating: 32 tools over stdio. |
| 54 | 2026-09-20 | [`io.github.croviatrust/causari`](https://github.com/croviatrust/causari) | [causari](https://crates.io/crates/causari) | `cargo` | 9 | Records the prompt, model and files an agent declared for a line. It does not prove who typed it. |
| 55 | 2026-09-21 | [`app.mochify/mochify`](https://github.com/getmochify/mochify-cli) | [mochify](https://crates.io/crates/mochify) | `cargo` | 1 | Image and PDF toolkit: convert to AVIF/WebP/JXL, resize, crop, remove backgrounds, optimize PDFs. |
| 56 | 2026-09-24 | [`io.github.devops-infinity/ownpg`](https://github.com/devops-infinity/ownpg-releases) | [ownpg](https://crates.io/crates/ownpg) | `cargo` + `mcpb` | 0 | PostgreSQL DBA tools over MCP, scoped to one database and one schema. |
| 57 | 2026-09-24 | [`io.github.naw103/foremerge`](https://github.com/naw103/foremerge) | [foremerge](https://crates.io/crates/foremerge) | `cargo` | 529 | Coordinate parallel coding agents, above Git |
| 58 | 2026-09-26 | [`io.github.damejeras/agentchan`](https://github.com/damejeras/agentchan) | [agentchan](https://crates.io/crates/agentchan) | `cargo` | 0 | Lets one coding agent talk to another: Claude Code, Codex or Grok |
| 59 | 2026-09-26 | [`io.github.fluxgit-hq/fluxgit-mcp-server`](https://github.com/fluxgit-hq/fluxgit-mcp-server) | [fluxgit-mcp-sidecar](https://crates.io/crates/fluxgit-mcp-sidecar) | `cargo` | 0 | Safety-first Git MCP server: rich read tools plus human-approved FluxGit operation proposals. |
| 60 | 2026-09-27 | [`io.github.brechanbech/forgejo-mcp-rs`](https://github.com/brechanbech/forgejo-mcp-rs) | [forgejo-mcp-rs](https://crates.io/crates/forgejo-mcp-rs) | `cargo` | 1 | Model Context Protocol server for Forgejo, Codeberg and Gitea, in Rust |
| 61 | 2026-09-27 | [`io.github.harisnopen/diavlos`](https://github.com/harisnopen/diavlos) | [diavlos](https://crates.io/crates/diavlos) | `cargo` | 3 | Signed messages between AI agents. Dangerous actions wait for a human-signed approval. |
| 62 | 2026-09-28 | [`io.github.JAAvila-Of/vivac`](https://github.com/JAAvila-Of/vivac) | [vivac](https://crates.io/crates/vivac) | `cargo` | 1 | Provenance tree for coding agents: where you are, why, and what was already decided |
| 63 | 2026-10-01 | [`io.github.damejeras/agentgrasp`](https://github.com/damejeras/agentgrasp) | [agentgrasp](https://crates.io/crates/agentgrasp) | `cargo` | 0 | Yes/no questions about local files, and relevant-file search, with TypeSafe Jev |
| 64 | 2026-10-02 | [`io.github.MykytaStel/repopilot`](https://github.com/MykytaStel/repopilot) | [repopilot](https://crates.io/crates/repopilot) | `cargo` + `npm` | 24 | Local, deterministic review of Git changes: weakened tests and CI gates, risky flows, blast radius. |
| 65 | 2026-10-02 | [`io.github.joowani/tree-sitter-mcp-server`](https://github.com/joowani/tree-sitter-mcp-server) | [tree-sitter-mcp-server](https://crates.io/crates/tree-sitter-mcp-server) | `cargo` + `npm` | 0 | Parse code into Tree-sitter ASTs to see node kinds, field names, and positions |
| 66 | 2026-10-03 | [`io.github.openreadout/openreadout`](https://github.com/openreadout/openreadout) | [openreadout](https://crates.io/crates/openreadout) | `cargo` + `mcpb` + `npm` | 10 | Read raw lab-instrument files offline: metadata, previews, integrity checks, open-format export. |
| 67 | 2026-10-04 | [`io.github.aleksUIX/pixellint`](https://github.com/aleksUIX/pixellint) | [pixellint-mcp](https://crates.io/crates/pixellint-mcp) | `cargo` | 1 | Validate pixels, postbacks, conversion API payloads, and tracking URLs with spec-backed findings. |
| 68 | 2026-10-04 | [`io.github.craftbag/craftbag-mcp`](https://github.com/craftbag/craftbag) | [craftbag-mcp](https://crates.io/crates/craftbag-mcp) | `cargo` | 2 | MCP server to list, load, explain, and validate Agent Skills. |
| 69 | 2026-10-06 | [`io.github.Tavrin/saccade`](https://github.com/Tavrin/saccade) | [saccade](https://crates.io/crates/saccade) | `cargo` | 0 | Perceptual visual regression, image evidence inspection and bounded decision proposals. |
| 70 | 2026-10-10 | [`io.github.yrangana/fm-mcp`](https://github.com/yrangana/fm-mcp) | [fm-mcp](https://crates.io/crates/fm-mcp) | `cargo` | 5 | Delegate summarising, extraction, classification and OCR to the macOS 27 on-device model. |
| 71 | 2026-10-11 | [`io.github.moreno-omar/mcp-obsidian`](https://github.com/moreno-omar/mcp_obsidian) | [mcp-obsidian](https://crates.io/crates/mcp-obsidian) | `cargo` | 0 | Search an Obsidian vault by tag, term and wikilink graph. Read-only, deterministic, no embeddings. |
| 72 | 2026-10-11 | [`io.github.nrupala/codetopo`](https://github.com/nrupala/codetopo) | [codetopo-mcp](https://crates.io/crates/codetopo-mcp) | `cargo` | 1 | Domain-blind code graphs for AI agents: symbols, calls, blast radius, proof-checked snapshots. |
| 73 | 2026-10-11 | [`io.github.smbcloudXYZ/ascapi`](https://github.com/smbcloudXYZ/smbcloud-ascapi) | [smbcloud-ascapi-cli](https://crates.io/crates/smbcloud-ascapi-cli) | `cargo` | 8 | Forget Fastlane, this is the app stores coolest API. |
| 74 | 2026-10-12 | [`io.github.scrapertweeter3-prog/flatrate-math`](https://github.com/scrapertweeter3-prog/mcp-flatratemath) | [flatrate-math](https://crates.io/crates/flatrate-math) | `cargo` | 0 | Benchmark math for flat-rate software subscriptions against a fully loaded senior hire. |
| 75 | 2026-10-13 | [`io.github.Blackcat-Informatics/purrassist`](https://github.com/Blackcat-Informatics/purrassist) | [purrassist-cli](https://crates.io/crates/purrassist-cli) | `cargo` | 0 | Recovers intent from imperfect AI output: JSON, tool calls, names, paths and Markdown edits. |
| 76 | 2026-10-14 | [`io.github.est57/echoproof`](https://github.com/est57/echoproof) | [echoproof](https://crates.io/crates/echoproof) | `cargo` | 0 | Replay real HTTP traffic against base and changed builds; flag behavior changes the intent omits. |
| 77 | 2026-10-14 | [`io.github.leidarljos/ljos`](https://github.com/leidarljos/ljos) | [ljos](https://crates.io/crates/ljos) | `cargo` | 1 | Local memory, a work tracker and a shell-command guard shared by coding agents on one machine. |
| 78 | 2026-10-15 | [`org.renyi-lang/renyi`](https://github.com/renyi-lang/renyi) | [renyi](https://crates.io/crates/renyi) | `cargo` | 3 | Check, format, run and test Renyi programs; the project map with effects, diffs and chunks. |
| 79 | 2026-10-17 | [`io.github.arifulislamat/database-mcp-libsql`](https://github.com/arifulislamat/database-mcp) | [database-mcp-rs-libsql](https://crates.io/crates/database-mcp-rs-libsql) | `cargo` + `npm` + `pypi` | 5 | MCP server for libSQL/Turso, local or remote. Read-only by default, row caps, timeouts. |
| 80 | 2026-10-17 | [`io.github.arifulislamat/database-mcp-mariadb`](https://github.com/arifulislamat/database-mcp) | [database-mcp-rs-mariadb](https://crates.io/crates/database-mcp-rs-mariadb) | `cargo` + `npm` + `pypi` | 5 | MCP server for MariaDB. Read-only by default, row caps, timeouts, secrets never logged. |
| 81 | 2026-10-17 | [`io.github.arifulislamat/database-mcp-mysql`](https://github.com/arifulislamat/database-mcp) | [database-mcp-rs-mysql](https://crates.io/crates/database-mcp-rs-mysql) | `cargo` + `npm` + `pypi` | 5 | MCP server for MySQL. Read-only by default, row caps, statement timeouts, secrets never logged. |
| 82 | 2026-10-17 | [`io.github.arifulislamat/database-mcp-postgres`](https://github.com/arifulislamat/database-mcp) | [database-mcp-rs-postgres](https://crates.io/crates/database-mcp-rs-postgres) | `cargo` + `npm` + `pypi` | 5 | MCP server for PostgreSQL. Read-only by default, row caps, timeouts, secrets never logged. |
| 83 | 2026-10-17 | [`io.github.arifulislamat/database-mcp-sqlite`](https://github.com/arifulislamat/database-mcp) | [database-mcp-rs-sqlite](https://crates.io/crates/database-mcp-rs-sqlite) | `cargo` + `npm` + `pypi` | 5 | MCP server for SQLite databases. Read-only by default, row caps, statement timeouts. |
| 84 | 2026-10-17 | [`io.github.asanabrial/estigia`](https://github.com/asanabrial/estigia) | [estigia](https://crates.io/crates/estigia) | `cargo` + `npm` | 1 | Guardrails for AI coding agents: verified claims, reviews bound to exact commits, gated merges. |
| 85 | 2026-10-17 | [`io.github.fatsearch/fats`](https://github.com/fatsearch/fatsearch) | [fatsearch](https://crates.io/crates/fatsearch) | `cargo` | 50 | Web pages, PDFs and documents as small, clean, cached Markdown for AI agents |
| 86 | 2026-10-18 | [`io.github.4DA-Systems/victauri`](https://github.com/4DA-Systems/victauri) | [victauri-cli](https://crates.io/crates/victauri-cli) | `cargo` | 4 | In-process MCP server for Tauri apps: DOM, IPC with bodies, Rust state, SQLite. Debug builds only. |
| 87 | 2026-10-18 | [`io.github.Ezra-Black/rekey`](https://github.com/Ezra-Black/rekey) | [rekey](https://crates.io/crates/rekey) | `cargo` | 2 | Rotate API keys across AWS, GitLab, Cloudflare, OpenAI & more. Secrets never reach the model. |
| 88 | 2026-10-19 | [`io.github.G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) | [moodle-mcp](https://crates.io/crates/moodle-mcp) | `cargo` | 27 | Moodle LMS for LLM agents — courses, assignments, files, submissions in one static binary. |
| 89 | 2026-10-20 | [`io.github.AppachiTech/suvadu`](https://github.com/AppachiTech/suvadu) | [suvadu](https://crates.io/crates/suvadu) | `cargo` | 124 | Local shell history and AI agent sessions over MCP: search commands, failures, risk and git changes |
| 90 | 2026-10-20 | [`io.github.emmanuel-defreitas/gpui-agentation`](https://github.com/emmanuel-defreitas/gpui-agentation) | [gpui-agentation](https://crates.io/crates/gpui-agentation) | `cargo` | 3 | Read and manage development annotations from a local GPUI app. |
| 91 | 2026-10-20 | [`io.github.marcomq/mq-bridge`](https://github.com/marcomq/mq-bridge) | [mq-bridge-app](https://crates.io/crates/mq-bridge-app) | `cargo` + `oci` | 25 | Move data between 15+ databases, queues and files at high throughput, without it entering context |
| 92 | 2026-10-23 | [`io.github.PSCatLabs/pscat`](https://github.com/PSCatLabs/pscat) | [pscat](https://crates.io/crates/pscat) | `cargo` | 2 | Render and debug PostScript to PNG, SVG or PDF, write handwritten notes, and make generative art |
| 93 | 2026-10-23 | [`io.github.abelreqma/oxiploitability-mcp`](https://github.com/abelreqma/oxiploitability-mcp) | [oxiploitability-mcp](https://crates.io/crates/oxiploitability-mcp) | `cargo` | 0 | Sourced, evidence-aware CVE research for CVEs, products, SBOMs and images via NVD, EPSS, KEV, OSV. |
| 94 | 2026-10-23 | [`io.github.triplexanalytics/triplex-mcp`](https://github.com/triplexanalytics/triplex) | [triplex-mcp](https://crates.io/crates/triplex-mcp) | `cargo` | 0 | Infer and validate schema contracts on local CSV, TSV and JSON Lines files. No network access. |
| 95 | 2026-10-24 | [`io.github.MikkoParkkola/nab`](https://github.com/MikkoParkkola/nab) | [nab](https://crates.io/crates/nab) | `cargo` | 17 | Token-optimized HTTP client for LLMs: fetches any URL as clean markdown. CLI and MCP server. |
| 96 | 2026-10-24 | [`io.github.oxygenframe/oxframe`](https://github.com/oxygenframe/oxframe-cli) | [oxframe-cli](https://crates.io/crates/oxframe-cli) | `cargo` | 2 | Make videos from code: check scenes frame by frame, inspect nodes, render a frame, search the docs. |
| 97 | 2026-10-24 | [`io.github.semlith/semlith`](https://github.com/semlith/semlith) | [semlith](https://crates.io/crates/semlith) | `cargo` | 7 | Local search over your code and documents for AI agents. |
| 98 | 2026-10-26 | [`io.github.godot-pty/gpty`](https://github.com/godot-pty/gpty) | [gpty](https://crates.io/crates/gpty) | `cargo` | 78 | Spawn panes, inject input and read output in a tiling terminal workspace |
| 99 | 2026-10-27 | [`io.github.devops-infinity/ownsearch`](https://github.com/devops-infinity/ownsearch) | [ownsearch](https://crates.io/crates/ownsearch) | `cargo` + `npm` | 0 | Quality-ranked SearXNG search over MCP with local fleet state, scoring, and merged results. |
| 100 | 2026-10-27 | [`io.github.emanuele-em/kanzo`](https://github.com/emanuele-em/kanzo) | [kanzo](https://crates.io/crates/kanzo) | `cargo` | 190 | Self-hosted kanban for humans and agents. One 4 MB binary, starts in 2 ms, zero setup. |
| 101 | 2026-10-27 | [`io.github.ermoluk/mcp-warden`](https://github.com/ermoluk/mcp-warden) | [mcp-warden](https://crates.io/crates/mcp-warden) | `cargo` + `mcpb` + `npm` | 10 | Local credential broker: agents call APIs, SSH and DBs via scoped presets; secrets stay in keychain. |
| 102 | 2026-10-29 | [`io.github.kinkirill/bevy-manual-mcp`](https://github.com/kinkirill/bevy_manual_mcp) | [bevy-manual-mcp](https://crates.io/crates/bevy-manual-mcp) | `cargo` | 16 | Version-accurate Bevy API docs, Book, migration guides and examples for AI agents. |
| 103 | 2026-10-29 | `science.transaction.wai/quantum` | [wai-quantum-cli](https://crates.io/crates/wai-quantum-cli) | `cargo` |  | OpenQASM 3 programs run, checked against their intent and signed on this machine. |
| 104 | 2026-10-30 | [`io.github.dot-ASH/umbriel-mcp`](https://github.com/dot-ASH/umbriel-mcp) | [umbriel-mcp](https://crates.io/crates/umbriel-mcp) | `cargo` | 0 | Control the Umbriel Wayland compositor: windows, workspaces, input, screenshots, clipboard. |

## Deprecated (2)

Marked deprecated in the registry, so not counted above.

- `io.github.Wolfe-Jam/rust-faf-mcp` (first cargo 2026-07-17)
- `io.github.marcomq/mq-bridge-app` (first cargo 2026-07-31)

## Method

- **Source:** the registry API (`/v0/servers?version=latest`, then `/v0/servers/{name}/versions` for the first version with a cargo package). Owner and stars from the GitHub API. Snapshot taken 2026-10-30.
- **Counted:** active servers whose latest version lists a package with `registryType: cargo`. Servers that list only `npm`, `pypi`, `oci` or `mcpb` are not counted, whatever language they are written in. A server that listed cargo in an earlier version but not its latest is not counted.
- **Dates** are the registry's `publishedAt`, in UTC.
- **What it does** is each author's own description from the registry, unedited.
- **Stars** are shown, not ranked. Nothing here judges a server.
- **Data:** [`data/2026-10-30.json`](data/2026-10-30.json) and [`data/2026-10-30.csv`](data/2026-10-30.csv). One snapshot per day; earlier days are never overwritten.
- **Run it yourself:** `python3 src/census.py` (Python 3, standard library; `gh` for owner and stars). One crawl a week (Sundays, 23:00 UTC, by [a GitHub Action](.github/workflows/weekly.yml)), with the User-Agent `rust-mcp-census`.
- Cargo support in the registry: [modelcontextprotocol/registry#1207](https://github.com/modelcontextprotocol/registry/pull/1207).

## Background

[An MCP Story about Rust](https://wolfejam.dev/blog/rust-mcp-story): how cargo got into the registry.
