# World-Increment Sweep + Hamming Snapshot

**Run date:** 2026-06-23  
**Branch:** world-increment/sweep-2026-06-23-1315  
**GF(3) color chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d → (repeat)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | Total Stars | Most Recent Push |
|--------|------|------:|------------:|------------------|
| plurigrid | org | 100 | 77 | 2026-06-23 (gorj, eirobri) |
| bmorphism | user | 100 | 248 | 2026-06-23 (Gay.jl) |
| zubyul | user | 49 | 14 | 2026-04-24 (voice-observatory) |
| kubeflow | org | 48 | 34,247 | 2026-06-23 (pipelines, katib) |
| migalkin | social | 10 | 280 | 2025-08-04 (kgcourse2021) |
| wasita | social | 9 | 5 | 2026-06-19 (proj-template) |
| AustinCStone | social | 9 | 107 | 2026-02-11 (EpsteinSearch) |
| M1shaaa | social | 8 | 0 | 2026-06-23 (M1shaaa profile) |
| DJedamski | social | 6 | 3 | 2018-03-07 (kaggle_ncaa18) |
| TeglonLabs | org | 5 | 2 | 2026-06-08 (jank-crane) |
| kristinezheng | social | 5 | 0 | 2026-06-07 (website) |
| **TOTAL** | | **349** | **34,983** | |

### Notable Repos

- `kubeflow/kubeflow` — 15,739 ★ — Machine Learning Toolkit for Kubernetes
- `kubeflow/pipelines` — 4,157 ★ — pushed today
- `kubeflow/spark-operator` — 3,128 ★
- `migalkin/NodePiece` — 144 ★ — Compositional KG representations (ICLR 22)
- `migalkin/StarE` — 89 ★ — Hyper-relational KG message passing (EMNLP 20)
- `AustinCStone/TextGAN` — 92 ★ — Text GAN in TensorFlow
- `plurigrid/gorj` — 765 open issues — pushed today
- `bmorphism/Gay.jl` — 187 open issues — pushed today (GF(3) color)

### GF(3) Increment Color Assignments

| ID | Source | Trit | Color | Name |
|----|--------|-----:|-------|------|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | -1 | #cc241d | MINUS |
| 3 | TeglonLabs | 0 | #d3869b | ERGODIC |
| 4 | bmorphism | 1 | #b8bb26 | PLUS |
| 5 | zubyul | -1 | #cc241d | MINUS |
| 6 | migalkin | 0 | #d3869b | ERGODIC |
| 7 | wasita | 1 | #b8bb26 | PLUS |
| 8 | kristinezheng | -1 | #cc241d | MINUS |
| 9 | M1shaaa | 0 | #d3869b | ERGODIC |
| 10 | DJedamski | 1 | #b8bb26 | PLUS |
| 11 | AustinCStone | -1 | #cc241d | MINUS |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Result: All 28 wallets (alice, bob, A-Z) returned resource_not_found.**
None hold a `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource on mainnet.
This may indicate wallets use the newer Fungible Asset standard, or have never held APT.

| World | Address | Balance APT |
|-------|---------|------------|
| alice | 0xc793...cc7b | null |
| bob | 0x0a3c...2d5d | null |
| A-Z | (26 addresses) | null (all) |

### Multisig Contract Probes

All 5 multisig accounts are live and require 2-of-N signatures:

| Pair | Address | Sigs Required | Healthy |
|------|---------|:------------:|:-------:|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel visitor-password protection active on deployment. No market data accessible without bypass token.

---

## DuckDB Schema

```
world-increments.duckdb
  world_increments   (11 rows)  GF(3) colored increment log
  repo_snapshots    (349 rows)  GitHub repo data across 11 sources
  aptos_snapshots    (28 rows)  Hamming swarm wallet balances
  multisig_probes     (5 rows)  2-of-N multisig health checks
  mnx_snapshots       (0 rows)  MNX markets (unavailable this run)
```
