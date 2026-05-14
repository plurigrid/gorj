# LATEST_SWEEP — 2026-05-14 19:07 UTC

## JOB 1: GitHub Social Graph Sweep

**Sweep Date:** 2026-05-14 19:07 UTC  
**GitHub API Status:** Rate-limited (unauthenticated); 217 JSON objects parsed from raw stream; 1,161 repo snapshot rows inserted (including paginated/expanded data).

### Sources Covered
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul
- **Zubyul Social Graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone
- **Events:** bmorphism, zubyul (rate-limited before events completed)

### Repo Counts by Source
```
┌───────────────┬───────┬───────────┐
│  org_or_user  │ repos │ max_stars │
│    varchar    │ int64 │   int32   │
├───────────────┼───────┼───────────┤
│ plurigrid     │   200 │        16 │
│ bmorphism     │   200 │        60 │
│ TeglonLabs    │   159 │         2 │
│ kubeflow      │   142 │     15630 │
│ AustinCStone  │   129 │        92 │
│ wasita        │    92 │         2 │
│ migalkin      │    90 │       144 │
│ zubyul        │    48 │         2 │
│ kristinezheng │    36 │         0 │
│ DJedamski     │    33 │         2 │
│ M1shaaa       │    32 │         0 │
└───────────────┴───────┴───────────┘
  11 rows                 3 columns

```

### Top 15 Repos by Stars
```
┌─────────────┬────────────────┬───────┬──────────┬──────────────────────┐
│ org_or_user │   repo_name    │ stars │ language │      pushed_at       │
│   varchar   │    varchar     │ int32 │ varchar  │       varchar        │
├─────────────┼────────────────┼───────┼──────────┼──────────────────────┤
│ kubeflow    │ kubeflow       │ 15630 │          │ 2026-05-07T13:46:41Z │
│ kubeflow    │ kubeflow       │ 15572 │ NULL     │ 2026-01-05T13:47:10Z │
│ kubeflow    │ kubeflow       │ 15565 │          │ 2026-01-05T13:47:10Z │
│ kubeflow    │ pipelines      │  4140 │ Python   │ 2026-05-12T22:53:36Z │
│ kubeflow    │ pipelines      │  4119 │ Python   │ 2026-04-10T23:07:19Z │
│ kubeflow    │ pipelines      │  4119 │ Python   │ 2026-04-14T01:20:50Z │
│ kubeflow    │ spark-operator │  3125 │ Python   │ 2026-05-12T00:33:28Z │
│ kubeflow    │ spark-operator │  3114 │ Python   │ 2026-04-13T18:28:43Z │
│ kubeflow    │ spark-operator │  3111 │ Python   │ 2026-04-10T18:21:12Z │
│ kubeflow    │ trainer        │  2098 │ Go       │ 2026-05-13T13:05:37Z │
│ kubeflow    │ trainer        │  2082 │ Go       │ 2026-04-13T23:41:09Z │
│ kubeflow    │ trainer        │  2080 │ Go       │ 2026-04-10T13:35:59Z │
│ kubeflow    │ katib          │  1682 │ Python   │ 2026-05-09T12:21:57Z │
│ kubeflow    │ katib          │  1678 │ Python   │ 2026-04-14T01:21:37Z │
│ kubeflow    │ katib          │  1676 │ Python   │ 2026-04-02T07:08:12Z │
└─────────────┴────────────────┴───────┴──────────┴──────────────────────┘
  15 rows                                                      5 columns

```

### GF(3) Color Chain Distribution
```
┌──────────┬───────────┬───────┐
│ gf3_name │ gf3_color │ count │
│ varchar  │  varchar  │ int64 │
├──────────┼───────────┼───────┤
│ PLUS     │ #b8bb26   │    81 │
│ MINUS    │ #cc241d   │    80 │
│ ERGODIC  │ #d3869b   │    79 │
└──────────┴───────────┴───────┘

```

| Trit | Color | Name | Meaning |
|------|-------|------|---------|
| 0 | #d3869b | ERGODIC | id%3==0 |
| +1 | #b8bb26 | PLUS | id%3==1 |
| -1 | #cc241d | MINUS | id%3==2 |

---

## JOB 2: Hamming Swarm Snapshot

**Snapshot Date:** 2026-05-14 19:07 UTC  
**Total Wallets Probed:** 28 (alice, bob, A–Z)

### Aptos Wallet Balances

All 28 addresses returned **Resource Not Found** — CoinStore resource absent, indicating uninitialized/unfunded accounts on Aptos mainnet.

| World | Address (truncated) | Balance APT | Status |
|-------|---------------------|-------------|--------|
| A | 0x8699edc0...be9d7a | — | not_found |
| B | 0x3f892ebe...77cb13 | — | not_found |
| C | 0x38b99e63...91535e | — | not_found |
| D | 0xf7765624...fcfdd1 | — | not_found |
| E | 0xdc1d9d53...958d36 | — | not_found |
| F | 0x18a14b5b...c3cf71 | — | not_found |
| G | 0x69a394c0...cc7f32 | — | not_found |
| H | 0xce67c327...e5300f | — | not_found |
| I | 0x070fe5d7...0c1fc9 | — | not_found |
| J | 0x4d964db8...e87f54 | — | not_found |
| K | 0xa732040a...425dc4 | — | not_found |
| L | 0x7c2eaeaf...37eba9 | — | not_found |
| M | 0x6fed37a7...b7f2e9 | — | not_found |
| N | 0xe7dde6da...551b2c | — | not_found |
| O | 0x73252b60...25a89d | — | not_found |
| P | 0x6218792d...1ec948 | — | not_found |
| Q | 0xac40fa50...5c89a9 | — | not_found |
| R | 0x7ce605cc...d76e10 | — | not_found |
| S | 0xb8753014...9d0386 | — | not_found |
| T | 0x35781dc0...3f4588 | — | not_found |
| U | 0x75860da4...ef9956 | — | not_found |
| V | 0xb59dd817...9af2c3 | — | not_found |
| W | 0x5f32aef7...ccc7b0 | — | not_found |
| X | 0xa95cbbd1...33047d | — | not_found |
| Y | 0xd8e32848...2444c4 | — | not_found |
| Z | 0x7af0ef6e...4e197c | — | not_found |
| alice | 0xc793acde...24cc7b | — | not_found |
| bob | 0x0a3c00c5...512d5d | — | not_found |

### Multisig Contract Probes (5 of 5 HEALTHY)

All 5 multisig pairs require **2-of-2 signatures**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — Next.js SPA with no accessible REST API endpoints.  
All `/api/*` paths return HTTP 404. No market data extractable without authentication or WebSocket client.

---

## DuckDB Schema

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments    — GF(3) color-coded increment log
├── repo_snapshots      — GitHub repo metadata (1,161 rows)
├── aptos_snapshots     — Wallet balances (28 rows)
├── multisig_probes     — Multisig contract health (5 rows)
└── mnx_snapshots       — MNX market data (1 row: unavailable)
```
