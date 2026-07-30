# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-30  
**Run:** world-increment-sweep + hamming-swarm-snapshot agent  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**DuckDB version:** v1.5.5 (Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 103 (100 parsed) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 2 |
| wasita | user | ~12 |
| kristinezheng | user | 2 |
| M1shaaa | user | 4 |
| AustinCStone | user | ~18 |

### Star Leaders (this sweep, sampled repos)

| Org/User | Repos Sampled | Total Stars |
|----------|--------------|-------------|
| kubeflow | 10 | 30,580 |
| migalkin | 5 | 275 |
| bmorphism | 10 | 170 |
| AustinCStone | 3 | 103 |
| plurigrid | 18 | 101 |
| zubyul | 9 | 7 |
| TeglonLabs | 5 | 2 |

### Notable Repos

- **plurigrid/gorj** (this repo) — 1 star, 1503 open issues, Clojure, updated 2026-07-29
- **plurigrid/asi** — 56 stars 13 forks, HTML, `everything is topological chemputer!`, updated 2026-07-30
- **kubeflow/kubeflow** — 15,796 stars 2,689 forks, ML Toolkit for Kubernetes
- **kubeflow/pipelines** — 4,171 stars, ML Pipelines, updated 2026-07-29
- **kubeflow/spark-operator** — 3,142 stars, Kubernetes operator for Apache Spark
- **kubeflow/trainer** — 2,162 stars, Distributed AI Training (Go)
- **bmorphism/Gay.jl** — Julia wide-gamut color sampling, 188 open issues, updated 2026-07-21
- **bmorphism/ocaml-mcp-sdk** — 61 stars, OCaml MCP SDK (Jane Street oxcaml_effect)
- **bmorphism/anti-bullshit-mcp-server** — 22 stars, epistemological claim validator
- **migalkin/NodePiece** — 144 stars, Knowledge Graph representations (ICLR-22)
- **migalkin/StarE** — 89 stars, Hyper-Relational KG EMNLP 2020
- **AustinCStone/TextGAN** — 92 stars, GAN text generation (TensorFlow)
- **TeglonLabs/jank-crane** — C++, crane-jank converged-IR hub GF3 convergence maps

### GF(3) Color Chain

| Trit | Color | Name | Rule |
|------|-------|------|------|
| 0 | #d3869b | ERGODIC | id mod 3 == 0 |
| +1 | #b8bb26 | PLUS | id mod 3 == 1 |
| -1 | #cc241d | MINUS | id mod 3 == 2 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice-Z, 28 addresses)

All 28 Hamming swarm wallet addresses returned resource_not_found for
0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin> on Aptos mainnet
(ledger v6523878302). Accounts have no APT CoinStore.
Balance: 0.0 APT for all 28.

### Multisig Contract Probes

All 5 multisig contracts queried via 0x1::multisig_account::num_signatures_required:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

All 5 multisig contracts healthy - all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Status: Unavailable. https://testnet.mnx.fi returns a Next.js SPA
with no accessible REST API. No market data extracted.
Recorded as unavailable in mnx_snapshots.

---

## DuckDB Table Counts

| Table | Rows (total incl. history) | New This Run |
|-------|---------------------------|-------------|
| world_increments | 90 | 67 |
| repo_snapshots | 1011 | 67 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 1 | 1 |
