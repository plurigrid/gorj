# World-Increment Sweep + Hamming Snapshot — 2026-07-05

## Sweep Metadata
- **Date:** 2026-07-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 102 |
| bmorphism | user | 103 |
| kubeflow | org | 51 |
| zubyul | user | 51 |
| AustinCStone | user (zubyul social) | 42 |
| migalkin | user (zubyul social) | 21 |
| wasita | user (zubyul social) | 13 |
| M1shaaa | user (zubyul social) | 10 |
| DJedamski | user (zubyul social) | 8 |
| TeglonLabs | org | 7 |
| kristinezheng | user (zubyul social) | 7 |
| **TOTAL** | | **415 increments** |

### Most Recently Active Repos (UTC 2026-07-05)
| Repo | Pushed | Stars | Language |
|------|--------|-------|----------|
| plurigrid/gorj | 2026-07-05T22:12 | 0 | Clojure |
| kubeflow/pipelines | 2026-07-05T17:30 | 4,169 | Python |
| kubeflow/community-distribution | 2026-07-05T15:30 | 1,027 | YAML |
| M1shaaa/M1shaaa | 2026-07-05T13:23 | 0 | — |
| wasita/wasita.github.io | 2026-07-05T03:54 | 1 | Svelte |
| bmorphism/Gay.jl | 2026-07-05T00:34 | 2 | Julia |

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,764 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,132 | Python |
| kubeflow/trainer | 2,129 | Go |
| kubeflow/katib | 1,689 | — |
| kubeflow/community-distribution | 1,027 | YAML |
| kubeflow/manifests | 1,010 | — |

### Notable Finds
- **TeglonLabs/jank-crane** (C++, 2026-06-08): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow" — GF(3) relevant project, NEW since last sweep
- **bmorphism/Gay.jl** (Julia): active as of today
- **plurigrid/gorj** (Clojure): most recently pushed, this very repo
- **kubeflow/kubeflow**: stars grew from 15,565 (Apr) to 15,764 (+199 since last sweep)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)
All 28 Hamming swarm addresses returned **0.0 APT** on Aptos mainnet.
Addresses are provisioned but unfunded at time of snapshot.

### Multisig Contract Probes — All 5 HEALTHY
| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ HEALTHY |

All 5 multisig accounts require 2-of-N signatures and respond normally on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)
Status: **UNAVAILABLE** — Vercel deployment protection active. All endpoints return password gate. No market data accessible without credentials.

---

## DuckDB Summary

| Table | Rows |
|-------|------|
| world_increments | 415 (this sweep) |
| repo_snapshots | 1,336 (cumulative) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

GF(3) color chain distributes ~138 entries per trit across 415 increments.
