# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-22  
**DB:** `world-increments.duckdb`  
**GF(3) chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Most Recent Push |
|--------|------|---------------|-----------------|
| plurigrid | org | 98 | gorj 2026-07-22 |
| kubeflow | org | 49 | sdk 2026-07-22 |
| TeglonLabs | org | 5 | jank-crane 2026-06-08 |
| bmorphism | user | 100 | Gay.jl 2026-07-22 |
| zubyul | user | 49 | from-possible-worlds 2026-07-18 |
| migalkin | user | 19 | kgcourse2021 2026-07-10 |
| DJedamski | user | 6 | Kaggle 2023-04-21 |
| wasita | user | 12 | wasita.github.io 2026-07-21 |
| kristinezheng | user | 5 | kristinezheng.github.io 2026-07-01 |
| M1shaaa | user | 8 | lab-bookshelf- 2024-12-31 |
| AustinCStone | user | 41 | byteruckus 2026-07-15 |

**Total this run:** 95 new repo increments inserted  
**Total DB:** 118 world_increments · 1039 repo_snapshots

### Notable Repos (by stars)

- **kubeflow/kubeflow** — 15,789 ★ · ML Toolkit for Kubernetes
- **kubeflow/pipelines** — 4,168 ★ · ML Pipelines (active: pushed today)
- **kubeflow/spark-operator** — 3,142 ★ · Kubernetes Spark operator
- **kubeflow/trainer** — 2,152 ★ · Distributed LLM Fine-Tuning
- **kubeflow/katib** — 1,692 ★ · AutoML on Kubernetes
- **migalkin/NodePiece** — 144 ★ · KG representations (ICLR'22)
- **AustinCStone/TextGAN** — 92 ★ · TF text GAN
- **migalkin/StarE** — 89 ★ · Hyper-relational KG (EMNLP'20)
- **bmorphism/ocaml-mcp-sdk** — 61 ★ · OCaml MCP SDK
- **plurigrid/asi** — 31 ★ · topological chemputer
- **bmorphism/risc0-cosmwasm-example** — 23 ★ · zkVM + CosmWasm
- **bmorphism/anti-bullshit-mcp-server** — 22 ★ · claim validation MCP

### Most Active (open issues)

- **plurigrid/gorj** — 1,311 open issues (this repo, pushed today)
- **bmorphism/Gay.jl** — 187 open issues (pushed today)
- **kubeflow/pipelines** — 443 open issues
- **kubeflow/sdk** — 180 open issues

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-22)

Queried via `POST /v1/view` → `0x1::coin::balance<0x1::aptos_coin::AptosCoin>`

| World | Balance (APT) |
|-------|--------------|
| alice | 0.43643352 |
| bob | 12.65700700 |
| A | 0.05176700 |
| B | 0.03625600 |
| C | 0.01018500 |
| D | 0.01162900 |
| E | 0.00937200 |
| F | 1.96051600 |
| G | 0.00068100 |
| H | 0.00168100 |
| I | 0.00068100 |
| J | 1.89509300 |
| K | 0.16196100 |
| L | 1.92726900 |
| M | 0.11228500 |
| N | 0.10612100 |
| O | 0.21013600 |
| P | 0.14013600 |
| Q | 0.10324000 |
| R | 0.09021700 |
| S | 0.09178800 |
| T | 0.07371300 |
| U | 0.05577300 |
| V | 0.04883299 |
| W | 0.04070500 |
| X | 0.04257700 |
| Y | 0.04444900 |
| Z | 0.02426800 |

**Total APT across swarm:** ~20.56 APT  
**Top holders:** bob (12.66), F (1.96), L (1.93), J (1.90)  
**Note:** `CoinStore` resource endpoint returned 404 for all addresses (not initialized); corrected to `0x1::coin::balance` view function.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...87003 | 2 | ✓ |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

All 5 multisig contracts healthy: 2-of-2 threshold.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` serves a Next.js SPA with no publicly accessible JSON API endpoints. Tried `/api/markets` and `/api/v1/markets` — both returned SPA shell or 404. Market data loads client-side only. No market rows inserted.

---

## DuckDB Schema Summary

```
world_increments  (118 rows) — GF(3)-colored repo events
repo_snapshots    (1039 rows) — full repo metadata with stars/forks/issues
aptos_snapshots   (28 rows) — wallet balances 2026-07-22
multisig_probes   (5 rows) — 2-of-2 contracts, all healthy
mnx_snapshots     (1 row) — unavailable marker
```
