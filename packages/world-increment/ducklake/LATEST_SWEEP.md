# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-06T01:16Z  
**Branch:** world-increment/sweep-2026-06-06-0109  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 103 |
| zubyul | user | 49 |
| AustinCStone | user (social) | 40 |
| migalkin | user (social) | 19 |
| wasita | user (social) | 11 |
| M1shaaa | user (social) | 8 |
| DJedamski | user (social) | 6 |
| kristinezheng | user (social) | 5 |
| **TOTAL** | | **393** |

### Notable Repos

**plurigrid** — top by stars:
- `plurigrid/asi` ★25 — "everything is topological chemputer!"
- `plurigrid/ontology` ★8 — "autopoietic ergodicity and embodied gradualism"
- `plurigrid/vcg-auction` ★7 — Rust VCG auction contract
- `plurigrid/agent` ★5 — Framework for agency amplification
- `plurigrid/gorj` — 383 open issues (this repo)

**kubeflow** — top by stars:
- `kubeflow/kubeflow` ★15,706 — ML Toolkit for Kubernetes
- `kubeflow/pipelines` ★4,152 — ML Pipelines
- `kubeflow/spark-operator` ★3,125 — recently active (2026-06-04)
- `kubeflow/trainer` ★2,111 — Distributed AI Training on Kubernetes
- `kubeflow/katib` ★1,685 — AutoML on Kubernetes

**bmorphism** — top by stars:
- `bmorphism/ocaml-mcp-sdk` ★61 — OCaml SDK for Model Context Protocol
- `bmorphism/anti-bullshit-mcp-server` ★23 — claim analysis MCP server
- `bmorphism/risc0-cosmwasm-example` ★23 — CosmWasm + zkVM
- `bmorphism/say-mcp-server` ★20 — macOS TTS MCP server
- `bmorphism/babashka-mcp-server` ★19 — Babashka MCP
- `bmorphism/Gay.jl` ★1, 189 open issues — active today

**zubyul** — terminal/world tooling, Gay.jl integration, nash-tui/web

**migalkin** — knowledge graph research: `NodePiece` ★144, `StarE` ★89

### GF(3) Color Chain

| ID % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

Total world_increments: **34** across **11** sources.

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Snapshot time:** 2026-06-06T01:16Z  
**Total APT across 28 wallets:** 20.3448 APT

| World | APT Balance |
|-------|------------|
| bob | 12.65700700 |
| F | 1.96051600 |
| L | 1.92726900 |
| J | 1.89509300 |
| alice | 0.43643352 |
| O | 0.21013600 |
| K | 0.16196100 |
| P | 0.14013600 |
| M | 0.11228500 |
| N | 0.10612100 |
| Q | 0.10324000 |
| S | 0.09178800 |
| R | 0.09021700 |
| T | 0.07371300 |
| U | 0.05577300 |
| A | 0.05176700 |
| V | 0.04883299 |
| Y | 0.04444900 |
| X | 0.04257700 |
| W | 0.04070500 |
| B | 0.03625600 |
| Z | 0.02426800 |
| D | 0.01162900 |
| C | 0.01018500 |
| E | 0.00937200 |
| H | 0.00168100 |
| I | 0.00068100 |
| G | 0.00068100 |

Note: All 28 addresses resolved via `0x1::coin::balance` view function (CoinStore endpoint returned 404 — accounts use newer Aptos account model).

### Multisig Contract Probes

All 5 multisig accounts healthy — each requires **2-of-N** signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...4987003` | 2 | healthy |
| A-G | `0xf56c4a1c...bc0096` | 2 | healthy |
| Y-Z | `0xd3ffe181...5b883` | 2 | healthy |
| S-T | `0x3b1c3ae9...d7883` | 2 | healthy |
| V-W | `0x40fad7b4...0eb6d` | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi/api/markets` and `/api/v1/markets` both return HTTP 401 (Vercel deployment authentication required). No public market data accessible without credentials.

---

## DuckDB Schema Summary

```
world_increments  — 34 rows   (GF(3) color-chained source events)
repo_snapshots    — 1334 rows (all org/user repos with metadata)
aptos_snapshots   — 28 rows   (Hamming swarm wallet balances)
multisig_probes   — 5 rows    (contract health checks)
mnx_snapshots     — 1 row     (unavailable marker)
```
