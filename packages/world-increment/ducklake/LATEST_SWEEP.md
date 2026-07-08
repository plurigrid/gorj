# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-08
**Run by:** world-increment-sweep + hamming-swarm-snapshot agent
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Sampled | Total Stars |
|--------|------|--------------|-------------|
| kubeflow | org | 10 | 28,663 |
| migalkin | user | 5 | 276 |
| bmorphism | user | 10 | 173 |
| AustinCStone | user | 3 | 103 |
| plurigrid | org | 10 | 48 |
| wasita | user | 3 | 4 |
| TeglonLabs | org | 5 | 2 |
| DJedamski | user | 3 | 2 |
| zubyul | user | 5 | 1 |
| M1shaaa | user | 2 | 0 |
| kristinezheng | user | 2 | 0 |
| **TOTAL** | | **58** | **29,272** |

### GF(3) Color Distribution

| GF3 Trit | Color | Name | Count |
|----------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 19 |
| 1 | `#b8bb26` | PLUS | 20 |
| -1 | `#cc241d` | MINUS | 19 |

### Notable Repos (by activity / stars)

**plurigrid** (most recently pushed):
- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF3 trit coloring (pushed 2026-07-08)
- `plurigrid/asi` ★30 — everything is topological chemputer!

**kubeflow** (highest stars):
- `kubeflow/kubeflow` ★15,768 — Machine Learning Toolkit for Kubernetes
- `kubeflow/pipelines` ★4,169 — ML Pipelines (pushed 2026-07-08)
- `kubeflow/spark-operator` ★3,135 — Kubernetes operator for Apache Spark

**bmorphism** (active):
- `bmorphism/Gay.jl` ★2, 187 open issues — Wide-gamut color sampling with splittable determinism (pushed 2026-06-20)
- `bmorphism/ocaml-mcp-sdk` ★61 — OCaml SDK for Model Context Protocol
- `bmorphism/anti-bullshit-mcp-server` ★23 — MCP for claim analysis

**migalkin** (social graph):
- `migalkin/NodePiece` ★144 — Compositional KG Representations (ICLR 2022)
- `migalkin/StarE` ★89 — Hyper-Relational Knowledge Graphs (EMNLP 2020)

**TeglonLabs**:
- `TeglonLabs/jank-crane` — crane-jank converged-IR hub, GF3 convergence maps (pushed 2026-06-08)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A-Z) queried against Aptos mainnet.

**Result:** All addresses returned 0 APT balance. The CoinStore<AptosCoin> resource was not found at any address, indicating accounts hold no APT or are not yet registered on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (5 contracts)

All 5 multisig contracts probed via 0x1::multisig_account::num_signatures_required.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

All 5 multisig contracts healthy -- 2-of-N signature threshold confirmed.

### MNX Markets (testnet.mnx.fi)

Status: UNAVAILABLE -- testnet.mnx.fi requires Vercel authentication for all endpoints.
Market data could not be extracted without credentials.

---

## DuckDB Schema Summary

| Table | Rows | Contents |
|-------|------|----------|
| world_increments | 58 | repo events with GF3 coloring |
| repo_snapshots | 58 | GitHub repo metadata |
| aptos_snapshots | 28 | alice, bob, A-Z wallet balances |
| multisig_probes | 5 | 2-of-N, all healthy |
| mnx_snapshots | 1 | unavailable marker |

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent on 2026-07-08*
