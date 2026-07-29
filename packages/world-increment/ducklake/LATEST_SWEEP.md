# LATEST_SWEEP.md

**Sweep timestamp:** 2026-07-29 11:12 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources swept
| Source | Type | Repos sampled |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 12 (top active) |
| TeglonLabs | org | 5 |
| bmorphism | user | 6 (top) |
| zubyul | user | 4 (top) |
| migalkin | social graph | 3 |
| wasita | social graph | 2 |
| kristinezheng | social graph | 1 |
| M1shaaa | social graph | 1 |
| AustinCStone | social graph | 1 |
| DJedamski | social graph | 1 |
| **TOTAL** | | **137 repo snapshots** |

### World Increment GF(3) Chain
- **ERGODIC** `#d3869b` (trit=0): 52 increments
- **PLUS** `#b8bb26` (trit=1): 54 increments
- **MINUS** `#cc241d` (trit=-1): 54 increments
- Total world_increments recorded: 160

### Notable GitHub Activity (2026-07-29)
- `plurigrid/gorj` (Clojure) — pushed today, active sweep target
- `kubeflow/kubeflow` ⭐ 15,795 — last activity 2026-07-29
- `kubeflow/pipelines` ⭐ 4,170 — ML Pipelines, active
- `kubeflow/spark-operator` ⭐ 3,142 — Kubernetes Spark
- `bmorphism/Gay.jl` — Julia color library, 188 open issues, very active
- `zubyul/voice-observatory` — newest zubyul repo (2026-04-24)
- `TeglonLabs/jank-crane` — C++ GF3 convergence maps project
- `AustinCStone/TextGAN` ⭐ 92 — most-starred in social graph

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-29 11:12 UTC)

| World | Address (short) | Balance APT |
|-------|-----------------|-------------|
| bob    | 0x0a3c00c5...512d5d | 12.6570 |
| F      | 0x18a14b5b...c3cf71 | 1.9605 |
| L      | 0x7c2eaeaf...37eba9 | 1.9273 |
| J      | 0x4d964db8...e87f54 | 1.8951 |
| alice  | 0xc793acde...24cc7b | 0.4364 |
| O      | 0x73252b60...25a89d | 0.2101 |
| K      | 0xa732040a...425dc4 | 0.1620 |
| P      | 0x6218792d...1ec948 | 0.1401 |
| M      | 0x6fed37a7...b7f2e9 | 0.1123 |
| N      | 0xe7dde6da...551b2c | 0.1061 |
| Q      | 0xac40fa50...5c89a9 | 0.1032 |
| S      | 0xb8753014...9d0386 | 0.0918 |
| R      | 0x7ce605cc...d76e10 | 0.0902 |
| T      | 0x35781dc0...3f4588 | 0.0737 |
| U      | 0x75860da4...ef9956 | 0.0558 |
| A      | 0x8699edc0...be9d7a | 0.0518 |
| V      | 0xb59dd817...9af2c3 | 0.0488 |
| Y      | 0xd8e32848...2444c4 | 0.0444 |
| X      | 0xa95cbbd1...33047d | 0.0426 |
| W      | 0x5f32aef7...ccc7b0 | 0.0407 |
| B      | 0x3f892ebe...77cb13 | 0.0363 |
| Z      | 0x7af0ef6e...4e197c | 0.0243 |
| D      | 0xf7765624...fcfdd1 | 0.0116 |
| C      | 0x38b99e63...91535e | 0.0102 |
| E      | 0xdc1d9d53...958d36 | 0.0094 |
| H      | 0xce67c327...e5300f | 0.0017 |
| G      | 0x69a394c0...cc7f32 | 0.0007 |
| I      | 0x070fe5d7...0c1fc9 | 0.0007 |

**Total swarm APT:** 20.3448 APT

Top holders: bob (12.657 APT), F (1.961 APT), L (1.927 APT), J (1.895 APT), alice (0.436 APT)

### Multisig Contract Probes (Aptos mainnet)

| Pair | Address (short) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B   | 0x0da4f428...987003 | 2 | ✅ |
| A-G   | 0xf56c4a1c...bc0096 | 2 | ✅ |
| Y-Z   | 0xd3ffe181...75b883 | 2 | ✅ |
| S-T   | 0x3b1c3ae9...ed7883 | 2 | ✅ |
| V-W   | 0x40fad7b4...80eb6d | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-2 threshold across all pairs.**

### MNX Markets (testnet.mnx.fi)
Status: **SPA only** — all API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return HTML shell.
No market data extractable without JavaScript execution. Marked unavailable in `mnx_snapshots` table.

---

## DuckDB Ducklake Schema

Tables in `world-increments.duckdb`:
- `world_increments` — GF3-colored event log (160 rows this sweep)
- `repo_snapshots` — GitHub repo metadata snapshots (137 new rows)
- `aptos_snapshots` — Hamming swarm wallet balances (28 rows)
- `multisig_probes` — Multisig contract health (5 rows)
- `mnx_snapshots` — MNX market data (unavailable placeholder)
