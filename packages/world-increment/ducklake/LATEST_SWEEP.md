# World Increment Sweep + Hamming Snapshot
**Date:** 2026-07-06  
**Run:** world-increment-sweep + hamming-swarm-snapshot agent

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept (11)
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user (zubyul social graph) | 20 |
| wasita | user (zubyul social graph) | 11 |
| kristinezheng | user (zubyul social graph) | 5 |
| M1shaaa | user (zubyul social graph) | 8 |
| DJedamski | user (zubyul social graph) | 6 |

**Total:** 373 repos snapshotted this run

### Top Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15765 | — | 2026-06-18 |
| kubeflow/pipelines | 4169 | Python | 2026-07-06 |
| kubeflow/spark-operator | 3132 | Python | 2026-07-02 |
| kubeflow/trainer | 2129 | Go | 2026-07-03 |
| kubeflow/community-distribution | 1027 | YAML | 2026-07-05 |

### Most Recently Pushed (2026-07-06)
- `kubeflow/hub` (Go, ⭐175)
- `kubeflow/pipelines` (Python, ⭐4169)
- `plurigrid/gorj` (Clojure, ⭐0) — **this repo**
- `M1shaaa/M1shaaa` (profile README, active today)
- `bmorphism/Gay.jl` (Julia, ⭐2)

### GF(3) Color Chain Distribution
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 131 |
| +1 | PLUS | #b8bb26 | 133 |
| -1 | MINUS | #cc241d | 132 |

Well-balanced across all three GF(3) classes.

### DuckDB Schema
- `world_increments`: 396 rows (cumulative across runs)
- `repo_snapshots`: 1317 rows (cumulative across runs)
- Location: `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 addresses returned **"Resource not found"** from Aptos mainnet fullnode.
The wallets exist at the address level but hold no `0x1::aptos_coin::AptosCoin` CoinStore resource — unfunded or not yet activated on-chain.

| Metric | Value |
|--------|-------|
| Addresses queried | 28 |
| With non-zero APT | 0 |
| Total APT across swarm | 0.000000 APT |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** and responsive. Each requires 2-of-N signatures.

| Pair | Address (prefix) | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...` | 2 | ✅ |
| A-G | `0xf56c4a1c...` | 2 | ✅ |
| Y-Z | `0xd3ffe181...` | 2 | ✅ |
| S-T | `0x3b1c3ae9...` | 2 | ✅ |
| V-W | `0x40fad7b4...` | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `https://testnet.mnx.fi` is behind Vercel deployment authentication (HTTP 401). No market data could be extracted.

---

## Summary

| Job | Status | Key Finding |
|-----|--------|-------------|
| GitHub sweep | ✅ Complete | 373 repos across 11 sources; kubeflow/kubeflow leads at 15.7k⭐; plurigrid/gorj active today |
| Aptos balances | ✅ Complete | All 28 Hamming addresses unfunded (0 APT total) |
| Multisig probes | ✅ Complete | All 5 pairs healthy, 2-of-N threshold |
| MNX Markets | ⚠️ Blocked | Vercel auth wall on testnet.mnx.fi |

DuckDB ducklake updated at `packages/world-increment/ducklake/world-increments.duckdb`.
