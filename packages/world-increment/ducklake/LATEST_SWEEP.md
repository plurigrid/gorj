# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-23  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Sampled | Most Recent Push |
|--------|------|---------------|-----------------|
| plurigrid | org | 26 | 2026-06-23 (gorj, eirobri) |
| bmorphism | user | 20 | 2026-06-23 (Gay.jl) |
| zubyul | user | 20 | 2026-04-24 (voice-observatory) |
| kubeflow | org | 15 | 2026-06-23 (spark-operator) |
| AustinCStone | user (social) | 10 | 2026-02-11 (EpsteinSearch) |
| M1shaaa | user (social) | 8 | 2026-06-23 (M1shaaa profile) |
| wasita | user (social) | 8 | 2026-06-19 (proj-template) |
| migalkin | user (social) | 7 | 2025-08-04 (kgcourse2021) |
| DJedamski | user (social) | 6 | 2018-03-07 |
| TeglonLabs | org | 5 | 2026-06-08 (jank-crane) |
| kristinezheng | user (social) | 5 | 2026-06-07 (personal site) |

**Total repo snapshots added this sweep: 130**

### Notable Activity

- **plurigrid/gorj** (this repo): 773 open issues, pushed 2026-06-23 — active
- **plurigrid/eirobri**: "EiRoBri replay world" — 30 open issues
- **bmorphism/Gay.jl**: 2 stars, 187 open issues — most active bmorphism repo today
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK gaining traction
- **kubeflow/pipelines**: 4157 stars / 2009 forks — dominant MLOps platform
- **kubeflow/spark-operator**: 3128 stars / 1491 forks
- **TeglonLabs/jank-crane**: C++ GF3 convergence maps + jank IR hub, pushed 2026-06-08
- **M1shaaa/M1shaaa** profile repo pushed 2026-06-23 (today)
- **wasita/proj-template** pushed 2026-06-19 — recent activity

### DuckDB Tables

```
repo_snapshots:  1074 total rows (cumulative across all sweeps)
world_increments: 34 total rows (cumulative)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (via `0x1::coin::balance` view function)

**Total swarm APT: 20.3448 APT across 28 wallets**

| Rank | World | Balance (APT) | Status |
|------|-------|---------------|--------|
| 1 | bob | 12.6570 | WHALE |
| 2 | F | 1.9605 | WHALE |
| 3 | L | 1.9273 | WHALE |
| 4 | J | 1.8951 | WHALE |
| 5 | alice | 0.4364 | ACTIVE |
| 6 | O | 0.2101 | ACTIVE |
| 7 | K | 0.1620 | ACTIVE |
| 8 | P | 0.1401 | ACTIVE |
| 9 | M | 0.1123 | ACTIVE |
| 10 | N | 0.1061 | ACTIVE |
| 11 | Q | 0.1032 | ACTIVE |
| 12-28 | S,R,T,U,A,V,Y,X,W,B,Z,D,C,E,H,I,G | 0.0009–0.0918 | DUST |

**Notes:**
- Legacy `CoinStore` resource not found; accounts use Fungible Asset model
- Queried via `0x1::coin::balance` view function (FA-compatible)
- `bob` holds 62.2% of total swarm APT (12.66 of 20.34 APT)

### Multisig Contract Probes

All 5 probed multisig contracts are **healthy** (2-of-N threshold each):

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | 2 | healthy |
| A-G | 0xf56c4a1c... | 2 | healthy |
| Y-Z | 0xd3ffe181... | 2 | healthy |
| S-T | 0x3b1c3ae9... | 2 | healthy |
| V-W | 0x40fad7b4... | 2 | healthy |

### MNX Markets

`testnet.mnx.fi` is **behind Vercel Authentication** — requires visitor password or trusted-source OIDC token. Market data unavailable this sweep.

---

## DuckDB Schema

```
packages/world-increment/ducklake/world-increments.duckdb
```

Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
