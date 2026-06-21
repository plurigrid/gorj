# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-06-21  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| bmorphism | user | 100 | 248 |
| plurigrid | org | 100 | 77 |
| zubyul | user | 49 | 14 |
| kubeflow | org | 48 | 34,235 |
| AustinCStone | user | 40 | 108 |
| migalkin | user | 19 | 280 |
| wasita | user | 11 | 5 |
| M1shaaa | user | 8 | 0 |
| DJedamski | user | 6 | 3 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | user | 5 | 0 |
| **TOTAL** | | **391** | **34,972** |

### GF(3) Color Chain (id % 3)

| id | Source | Trit | Color | Name |
|----|--------|------|-------|------|
| 1 | AustinCStone | +1 | #b8bb26 | PLUS |
| 2 | DJedamski | -1 | #cc241d | MINUS |
| 3 | M1shaaa | 0 | #d3869b | ERGODIC |
| 4 | TeglonLabs | +1 | #b8bb26 | PLUS |
| 5 | bmorphism | -1 | #cc241d | MINUS |
| 6 | kristinezheng | 0 | #d3869b | ERGODIC |
| 7 | kubeflow | +1 | #b8bb26 | PLUS |
| 8 | migalkin | -1 | #cc241d | MINUS |
| 9 | plurigrid | 0 | #d3869b | ERGODIC |
| 10 | wasita | +1 | #b8bb26 | PLUS |
| 11 | zubyul | -1 | #cc241d | MINUS |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,738 | — | 2026-06-18 |
| kubeflow/pipelines | 4,155 | Python | 2026-06-20 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-18 |
| kubeflow/trainer | 2,118 | Go | 2026-06-19 |
| kubeflow/katib | 1,683 | Python | 2026-06-20 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,025 | YAML | 2026-06-18 |

### Most Recently Pushed (Today 2026-06-21)

- `M1shaaa/M1shaaa`
- `plurigrid/gorj` (this repo)
- `kubeflow/dashboard`
- `bmorphism/Gay.jl`

### Language Distribution (top 10)

Python (80), Rust (26), JavaScript (25), TypeScript (23), HTML (17),
Go (15), Jupyter Notebook (14), Clojure (14), Julia (9), Zig (7)

Notable: 14 Clojure repos (plurigrid ecosystem), 9 Julia (bmorphism), 7 Zig

### Notable Repos

- **TeglonLabs/jank-crane** (C++, 2026-06-08): GF3 convergence maps — directly relevant
- **wasita/proj-template** (2026-06-19): most recently active social node
- **kristinezheng/kristinezheng.github.io** (HTML, 2026-06-07): active personal site

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

**Result:** All 28 addresses returned HTTP errors (no CoinStore resource found).
Accounts appear uninitialized or use a non-standard coin resource on Aptos mainnet.
Stored with `balance_apt = -1` sentinel.

| World | Address (prefix) | Balance APT |
|-------|------------------|-------------|
| alice | 0xc793ac... | not found |
| bob | 0x0a3c00... | not found |
| A–Z (26) | various | not found |

### Multisig Contract Probes (5 contracts)

All 5 Aptos multisig contracts are **healthy** (2-of-N threshold):

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | YES |
| A-G | 0xf56c4a... | 2 | YES |
| Y-Z | 0xd3ffe1... | 2 | YES |
| S-T | 0x3b1c3a... | 2 | YES |
| V-W | 0x40fad7... | 2 | YES |

### MNX Markets (testnet.mnx.fi)

All probed endpoints unreachable — `testnet.mnx.fi` appears offline or SPA with no API.
No MNX market data stored this sweep.

---

## DuckDB Schema Summary

```
world_increments:  11 rows  (one per source, GF3 colored)
repo_snapshots:   391 rows  (full social graph snapshot)
aptos_snapshots:   28 rows  (Hamming swarm, all not-found)
multisig_probes:    5 rows  (all healthy, 2-of-N)
mnx_snapshots:      0 rows  (endpoint unavailable)
```

## Key Findings

1. **plurigrid/gorj** pushed today — this repo is live and active
2. **All 5 multisig contracts** on Aptos mainnet healthy (2-of-N)
3. **Hamming swarm wallets** (alice, bob, A-Z) have no CoinStore on Aptos mainnet
4. **kubeflow** dominates by stars (34,235 total); bmorphism and plurigrid at 100-repo cap
5. **MNX testnet** offline this sweep
