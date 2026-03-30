# World-Increment Sweep — 2026-03-30

## Sweep Metadata
- **Date:** 2026-03-30T04:30:00Z
- **Agent:** world-increment-sweep (full social graph + hamming swarm)
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 319 |
| Total Repo Snapshots | 347 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Repos per Org/User

| Source | Type | Repo Count |
|---|---|---|
| bmorphism | user | 100 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 28 |
| plurigrid | org | ~100 (25 stored) |
| kubeflow | org | ~47 (15 stored) |
| zubyul | user | 23 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| TeglonLabs | org | ~52 (10 stored) |
| DJedamski | user | 11 |

**Total repos stored in DB:** 347

### Most Recently Pushed Repos (Top 10)

| Repo | Pushed At |
|---|---|
| kubeflow/pipelines | 2026-03-30T04:01:09Z |
| plurigrid/gorj | 2026-03-30T03:24:22Z |
| kubeflow/dashboard | 2026-03-30T03:22:52Z |
| plurigrid/horse | 2026-03-30T03:05:14Z |
| M1shaaa/M1shaaa | 2026-03-30T02:08:46Z |
| plurigrid/bci-blue-share | 2026-03-30T00:58:52Z |
| plurigrid/gatomic | 2026-03-30T00:54:48Z |
| kubeflow/mcp-apache-spark-history-server | 2026-03-29T04:29:55Z |
| bmorphism/zig-syrup-1 | 2026-03-28T21:42:51Z |
| bmorphism/zig-syrup | 2026-03-28T21:42:32Z |

### Recent Events (bmorphism — 30 events)
- PushEvent → plurigrid/horse (2026-03-30T03:05:15Z)
- PushEvent → plurigrid/gatomic (2026-03-30T00:54:49Z)
- IssueCommentEvent → Textualize/textual (2026-03-29)
- PullRequestEvent → plurigrid/zig-syrup (2026-03-28)
- ForkEvent → JuliaWeb/RemoteREPL.jl (2026-03-28)
- IssuesEvent → plurigrid/gorj (2026-03-28)

### Recent Events (zubyul — 30 events)
- CreateEvent → plurigrid/gorj (2026-03-30T03:24:22Z)
- PullRequestEvent → plurigrid/gorj (2026-03-30T02:27:01Z)
- CreateEvent → plurigrid/bci-blue-share (2026-03-30T00:58:52Z)
- PullRequestEvent → plurigrid/gorj (2026-03-30T00:40:38Z)
- PushEvent → plurigrid/gorj (2026-03-30T00:33:35Z)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` from the Aptos mainnet fullnode — the CoinStore<AptosCoin> resource does not exist for any address at ledger version 4716568828. Balances stored as NULL.

| World | Address (truncated) | Balance APT |
|---|---|---|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...512d | NULL |
| A | 0x8699...9d7a | NULL |
| B | 0x3f89...b13 | NULL |
| C | 0x38b9...535e | NULL |
| D | 0xf776...fdd1 | NULL |
| E | 0xdc1d...8d36 | NULL |
| F | 0x18a1...cf71 | NULL |
| G | 0x69a3...f32 | NULL |
| H | 0xce67...300f | NULL |
| I | 0x070f...1fc9 | NULL |
| J | 0x4d96...7f54 | NULL |
| K | 0xa732...5dc4 | NULL |
| L | 0x7c2e...eba9 | NULL |
| M | 0x6fed...f2e9 | NULL |
| N | 0xe7dd...1b2c | NULL |
| O | 0x7325...a89d | NULL |
| P | 0x6218...c948 | NULL |
| Q | 0xac40...89a9 | NULL |
| R | 0x7ce6...6e10 | NULL |
| S | 0xb875...0386 | NULL |
| T | 0x3578...4588 | NULL |
| U | 0x7586...9956 | NULL |
| V | 0xb59d...f2c3 | NULL |
| W | 0x5f32...c7b0 | NULL |
| X | 0xa95c...047d | NULL |
| Y | 0xd8e3...44c4 | NULL |
| Z | 0x7af0...197c | NULL |

### Multisig Contract Probes

All 5 multisig contracts responded successfully with `sigs_required = 2`, all healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

---

## MNX Markets

**Status: Unavailable** — All three endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) at `testnet.mnx.fi` returned HTML (Next.js SPA) rather than JSON market data. The REST API is not publicly accessible via direct curl requests.

---

## GF(3) Color Chain Stats

Sequential GF(3) trit coloring applied to all 319 world_increment records:

| Trit | Color | Name | Count |
|---|---|---|---|
| 0 | #d3869b | ERGODIC | 106 |
| 1 | #b8bb26 | PLUS | 107 |
| -1 | #cc241d | MINUS | 106 |

Assignment rule:
- `id % 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id % 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id % 3 == 2` → trit=-1, color=#cc241d, name=MINUS

Distribution is nearly uniform (balanced ternary), as expected for sequential assignment modulo 3.

---

## Database Summary

- **Path:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Tables:** world_increments (319), repo_snapshots (347), aptos_snapshots (28), multisig_probes (5), mnx_snapshots (0)
- **DuckDB version:** v1.5.1 (Variegata)

## Notable Highlights
- **kubeflow/pipelines**: 4,113 stars — most popular ML pipeline for Kubernetes (pushed 2026-03-30)
- **kubeflow/spark-operator**: 3,109 stars — Kubernetes operator for Apache Spark
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **plurigrid/asi**: 13 stars — topological chemputer (pushed 2026-03-28)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- All 5 multisig contracts healthy (2-of-N signature threshold)
