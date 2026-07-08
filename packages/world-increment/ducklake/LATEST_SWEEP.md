# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-08

**Run date:** 2026-07-08  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 50 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 40 |

**Total:** 292 repos snapshotted this run (1157 cumulative in DB)

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,770 | — | 2026-07-08 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-08 |
| kubeflow/spark-operator | 3,135 | Python | 2026-07-02 |
| kubeflow/trainer | 2,133 | Go | 2026-07-08 |
| kubeflow/katib | 1,689 | Python | 2026-07-08 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| plurigrid/asi | 30 | HTML | 2026-06-29 |
| migalkin/kgcourse2021 | 25 | HTML | 2026-02-16 |

### Notable Activity
- **plurigrid/gorj** (this repo, Clojure): pushed **today** 2026-07-08 — actively developed
- **TeglonLabs/jank-crane** (C++): GF3 convergence maps + crane-jank converged-IR hub, pushed 2026-06-08
- **bmorphism/Gay.jl** (Julia): pushed 2026-07-08 (today)
- **wasita/wasita.github.io** (Svelte): pushed 2026-07-06
- **kristinezheng/kristinezheng.github.io** (HTML): pushed 2026-07-01

### GF(3) Color Chain (this run, 213 new increments)
- **ERGODIC** (trit=0, #d3869b): 71 increments
- **PLUS** (trit=1, #b8bb26): 71 increments
- **MINUS** (trit=-1, #cc241d): 71 increments

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-08)

> Method: `0x1::coin::balance` view function (accounts use FA module, not legacy CoinStore)

| World | Balance (APT) | Address |
|-------|--------------|---------|
| bob | 12.6570 | 0x0a3c00c5... |
| F | 1.9605 | 0x18a14b5b... |
| L | 1.9273 | 0x7c2eaeaf... |
| J | 1.8951 | 0x4d964db8... |
| alice | 0.4364 | 0xc793acde... |
| O | 0.2101 | 0x73252b60... |
| K | 0.1620 | 0xa732040a... |
| P | 0.1401 | 0x6218792d... |
| M | 0.1123 | 0x6fed37a7... |
| N | 0.1061 | 0xe7dde6da... |
| Q | 0.1032 | 0xac40fa50... |
| S | 0.0918 | 0xb8753014... |
| R | 0.0902 | 0x7ce605cc... |
| T | 0.0737 | 0x35781dc0... |
| U | 0.0558 | 0x75860da4... |
| A | 0.0518 | 0x8699edc0... |
| V | 0.0488 | 0xb59dd817... |
| X | 0.0426 | 0xa95cbbd1... |
| Y | 0.0444 | 0xd8e32848... |
| W | 0.0407 | 0x5f32aef7... |
| B | 0.0363 | 0x3f892ebe... |
| Z | 0.0243 | 0x7af0ef6e... |
| D | 0.0116 | 0xf7765624... |
| C | 0.0102 | 0x38b99e63... |
| E | 0.0094 | 0xdc1d9d53... |
| H | 0.0017 | 0xce67c327... |
| G | 0.0007 | 0x69a394c0... |
| I | 0.0007 | 0x070fe5d7... |

**Total APT across Hamming swarm: 20.3448 APT**

**Richest:** bob (12.66 APT) — accounts for 62.2% of swarm total

### Multisig Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✅ |
| A-G | 0xf56c4a1c... | 2 | ✅ |
| Y-Z | 0xd3ffe181... | 2 | ✅ |
| S-T | 0x3b1c3ae9... | 2 | ✅ |
| V-W | 0x40fad7b4... | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

```
Status: UNAVAILABLE
All API paths returned HTTP 401 Unauthorized.
The testnet requires authenticated access — no public market data accessible.
```

---

## DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 236 |
| repo_snapshots | 1157 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (placeholder) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
