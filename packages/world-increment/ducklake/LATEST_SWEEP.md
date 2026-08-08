# World-Increment Sweep + Hamming Swarm Snapshot

**Run timestamp:** 2026-08-08T15:30 UTC  
**DuckDB version:** v1.5.5 (Variegata)  
**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source Type | Name | Repos (distinct) | GF3 Trit | Color |
|-------------|------|-----------------|----------|-------|
| org | plurigrid | 107 | ERGODIC | #d3869b |
| org | kubeflow | 48 | PLUS | #b8bb26 |
| org | TeglonLabs | 5 | MINUS | #cc241d |
| user | bmorphism | 105 | ERGODIC | #d3869b |
| user | zubyul | 29 | PLUS | #b8bb26 |
| user | migalkin | 19 | MINUS | #cc241d |
| user | DJedamski | 6 | ERGODIC | #d3869b |
| user | wasita | 14 | PLUS | #b8bb26 |
| user | kristinezheng | 5 | MINUS | #cc241d |
| user | M1shaaa | 8 | ERGODIC | #d3869b |
| user | AustinCStone | 41 | PLUS | #b8bb26 |

**Total distinct repos captured: 494**  
**Total world_increments: 11**  
**Total repo_snapshot rows: 1016**

### Notable Repos by Activity (pushed_at 2026-08)

| Repo | Language | Stars | Last Push | Description |
|------|----------|-------|-----------|-------------|
| plurigrid/gorj | Clojure | 1 | 2026-08-08 | forj + Rama topology nREPL routing + GF(3) gay trit coloring |
| kubeflow/spark-operator | Python | 3145 | 2026-08-08 | Kubernetes operator for Apache Spark |
| kubeflow/trainer | Go | 2176 | 2026-08-08 | Distributed AI Model Training on Kubernetes |
| kubeflow/pipelines | Python | 4182 | 2026-08-07 | Machine Learning Pipelines for Kubeflow |
| plurigrid/place | TeX | 3 | 2026-08-08 | |
| plurigrid/eirobri | Clojure | 0 | 2026-08-04 | EiRoBri replay world |
| wasita/wm-cv | Svelte | 0 | 2026-08-07 | Academic CV as single page app |
| wasita/xoxowasita-analysis | Python | 0 | 2026-08-06 | |
| bmorphism/Gay.jl | Julia | 2 | 2026-08-07 | Wide-gamut color sampling with splittable determinism |

### Kubeflow Ecosystem (top by stars)
- **kubeflow/kubeflow**: 15,806 ⭐ — Machine Learning Toolkit for Kubernetes
- **kubeflow/pipelines**: 4,182 ⭐ — ML Pipelines
- **kubeflow/spark-operator**: 3,145 ⭐ — Spark on Kubernetes
- **kubeflow/trainer**: 2,176 ⭐ — Distributed training
- **kubeflow/katib**: 1,694 ⭐ — AutoML on Kubernetes
- **kubeflow/examples**: 1,461 ⭐ — Extended examples
- **kubeflow/arena**: 817 ⭐ — CLI for Kubeflow
- **kubeflow/kale**: 699 ⭐ — Superfood for Data Scientists

### Social Graph Activity
- **migalkin/NodePiece**: 144 ⭐ — Knowledge graph representations (ICLR'22)
- **migalkin/StarE**: 89 ⭐ — Hyper-relational KGs (EMNLP 2020)
- **AustinCStone/TextGAN**: 92 ⭐ — TF text generation GAN
- **wasita**: Active (2 new repos Aug 2026)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Queried:** 28 addresses (alice, bob, A–Z)  
**API:** `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`  

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice | 0.0 | zero |
| bob | 0.0 | zero |
| A–Z (26 wallets) | 0.0 each | all zero |

**Observation:** All 28 Hamming swarm addresses return 0.0 APT on mainnet. Accounts exist (API responds) but hold no APT coin balance at this snapshot.

### Multisig Contract Probes

**Function:** `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...7003 | 2 | ✅ |
| A-G | 0xf56c4a1c...0096 | 2 | ✅ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✅ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✅ |
| V-W | 0x40fad7b4...eb6d | 2 | ✅ |

**All 5 multisig contracts responding, all require 2-of-N signatures. Swarm structure intact.**

### MNX Markets (testnet.mnx.fi)

**Status:** Next.js SPA — no REST/JSON API accessible from server-side probe.  
Paths tried: `/api/markets`, `/api/v1/markets`, `/api/tickers` → all return HTML shell (no data).  
MNX snapshot table created but empty (SPA requires browser execution to hydrate market data).

---

## GF(3) Color Chain Summary

| id%3 | Trit | Color | Name | Count |
|------|------|-------|------|-------|
| 0 | 0 | #d3869b | ERGODIC | sources: plurigrid, bmorphism, DJedamski, M1shaaa |
| 1 | 1 | #b8bb26 | PLUS | sources: kubeflow, zubyul, wasita, AustinCStone |
| 2 | -1 | #cc241d | MINUS | sources: TeglonLabs, migalkin, kristinezheng |

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 1,016 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |
