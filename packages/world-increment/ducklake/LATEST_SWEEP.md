# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-22  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d (mod 3 by increment id)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 12 (of 101 total) |
| kubeflow | org | 10 (of 48 total) |
| TeglonLabs | org | 5 (of 5 total) |
| bmorphism | user | 8 (of 105 total) |
| zubyul | user | 6 (of 49 total) |
| migalkin | social graph | 3 |
| DJedamski | social graph | 1 |
| wasita | social graph | 3 |
| kristinezheng | social graph | 1 |
| M1shaaa | social graph | 1 |
| AustinCStone | social graph | 2 |

**Total snapshots:** 52 repos across 11 sources

### GF(3) Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 18 |
| 1 | #b8bb26 | PLUS | 17 |
| -1 | #cc241d | MINUS | 17 |

### Top Repos by Stars
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/kubeflow | — | 15,739 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,157 | 2026-06-20 |
| kubeflow/spark-operator | Python | 3,127 | 2026-06-18 |
| kubeflow/trainer | Go | 2,118 | 2026-06-19 |
| kubeflow/katib | Python | 1,685 | 2026-06-20 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| plurigrid/asi | HTML | 26 | 2026-06-10 |
| plurigrid/gorj | Clojure | 0 | 2026-06-22 |

### Notable Activity (Most Recently Pushed)
- **plurigrid/gorj** — pushed 2026-06-22 (today), 735 open issues — most active plurigrid repo
- **bmorphism/Gay.jl** — pushed 2026-06-22, 187 open issues
- **kubeflow/dashboard** — pushed 2026-06-21
- **plurigrid/place** — pushed 2026-06-20
- **TeglonLabs/jank-crane** (C++, GF3 convergence maps) — pushed 2026-06-08

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 addresses queried (alice, bob, A-Z). All returned resource_not_found for
0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin> — uninitialized accounts on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes
All 5 contracts active and healthy — each requiring 2 signatures.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

### MNX Markets (testnet.mnx.fi)
Status: Unavailable — returns HTTP 401 (Vercel authentication required).
No market data extractable without credentials. mnx_snapshots table empty.

---

## DuckDB Ducklake

Path: packages/world-increment/ducklake/world-increments.duckdb

| Table | Rows |
|-------|------|
| world_increments | 52 |
| repo_snapshots | 52 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## Summary

- 52 repo snapshots ingested: plurigrid ecosystem, kubeflow, TeglonLabs, social graph
- 28 Aptos addresses probed — all uninitialized (0 APT, no CoinStore resource)
- 5/5 multisig contracts healthy, all at 2-of-N threshold
- MNX testnet inaccessible (Vercel auth wall, HTTP 401)
- GF(3) color chain: 18 ERGODIC / 17 PLUS / 17 MINUS
