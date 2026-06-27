# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-27  
**Run:** world-increment-sweep + hamming-swarm-snapshot agent

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain

| id | source | type | trit | name | color |
|----|--------|------|------|------|-------|
| 1 | plurigrid | org | +1 | PLUS | #b8bb26 |
| 2 | kubeflow | org | -1 | MINUS | #cc241d |
| 3 | TeglonLabs | org | 0 | ERGODIC | #d3869b |
| 4 | bmorphism | user | +1 | PLUS | #b8bb26 |
| 5 | zubyul | user | -1 | MINUS | #cc241d |
| 6 | migalkin | user | 0 | ERGODIC | #d3869b |
| 7 | DJedamski | user | +1 | PLUS | #b8bb26 |
| 8 | wasita | user | -1 | MINUS | #cc241d |
| 9 | kristinezheng | user | 0 | ERGODIC | #d3869b |
| 10 | M1shaaa | user | +1 | PLUS | #b8bb26 |
| 11 | AustinCStone | user | -1 | MINUS | #cc241d |

### Repo Snapshot Summary

| Source | Repos | Stars |
|--------|-------|-------|
| kubeflow | 24 | 33,391 |
| migalkin | 6 | 279 |
| bmorphism | 20 | 210 |
| AustinCStone | 6 | 107 |
| plurigrid | 30 | 71 |
| zubyul | 13 | 7 |
| wasita | 6 | 5 |
| DJedamski | 5 | 3 |
| TeglonLabs | 5 | 2 |
| kristinezheng | 4 | 0 |
| M1shaaa | 3 | 0 |
| **TOTAL** | **122** | **34,085** |

### Notable Repos

**Most Stars:**
- `kubeflow/kubeflow` — 15,747 stars — Machine Learning Toolkit for Kubernetes
- `kubeflow/pipelines` — 4,156 stars — ML Pipelines for Kubeflow
- `kubeflow/spark-operator` — 3,128 stars — Kubernetes operator for Apache Spark

**Most Recently Pushed:**
- `plurigrid/gorj` — 2026-06-27T07:10:38Z — forj + Rama topology + GF(3) gay trit coloring (853 open issues)
- `plurigrid/place` — 2026-06-27T05:53:49Z
- `kubeflow/spark-operator` — 2026-06-26T23:02:30Z

**Key Zubyul Activity:**
- `zubyul/tilelang-kernels` — TileLang GPU kernels for GF(3) trit classification, targeting NVIDIA GB10 Blackwell
- `zubyul/kinesis-kb360pro` — Claude Code skill for Kinesis Advantage360 Pro with Gay.jl GF(3) analysis

**bmorphism Highlights:**
- `bmorphism/Gay.jl` — Wide-gamut splittable-determinism color sampling (187 open issues — very active)
- `bmorphism/ocaml-mcp-sdk` — OCaml SDK for MCP using Jane Street oxcaml_effect (61 stars)
- `bmorphism/penrose-mcp` — Penrose MCP server (9 stars, active recent push)

**TeglonLabs:**
- `TeglonLabs/jank-crane` — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps (C++, pushed 2026-06-08)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A-Z)

All 28 addresses returned null — accounts not found or have zero APT CoinStore on Aptos mainnet.

| World | Address prefix | Balance |
|-------|---------------|---------|
| alice | 0xc793acd... | null |
| bob | 0x0a3c00c... | null |
| A through Z | various | null (all) |

API: fullnode.mainnet.aptoslabs.com responded with resource-not-found for all CoinStore queries.

### Multisig Contract Probes

All 5 multisig accounts healthy — all require 2-of-2 signatures:

| Pair | Address prefix | Sigs Required | Healthy |
|------|---------------|--------------|---------|
| A-B | 0x0da4f428... | 2 | true |
| A-G | 0xf56c4a1c... | 2 | true |
| Y-Z | 0xd3ffe181... | 2 | true |
| S-T | 0x3b1c3ae9... | 2 | true |
| V-W | 0x40fad7b4... | 2 | true |

### MNX Markets (testnet.mnx.fi)

Status: UNAVAILABLE — site is behind Vercel deployment protection (authentication required).
No market data could be extracted.

---

## DuckDB Schema

File: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 122 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
