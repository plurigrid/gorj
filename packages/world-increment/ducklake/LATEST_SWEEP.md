# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-01T00:00:00Z  
**GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Crawled

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 19 |
| kubeflow | org | 12 |
| TeglonLabs | org | 4 |
| bmorphism | user | 16 |
| zubyul | user | 9 |
| migalkin | user | 6 |
| DJedamski | user | 5 |
| wasita | user | 5 |
| kristinezheng | user | 5 |
| M1shaaa | user | 5 |
| AustinCStone | user | 5 |
| **Total** | | **91** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,695 | — | 2026-05-24 |
| kubeflow/pipelines | 4,149 | Python | 2026-06-01 |
| kubeflow/spark-operator | 3,124 | Python | 2026-05-29 |
| kubeflow/trainer | 2,109 | Go | 2026-05-30 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| kubeflow/examples | 1,463 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,019 | YAML | 2026-05-29 |
| kubeflow/arena | 811 | Go | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |

### Notable Active Repos

- `plurigrid/gorj` — Clojure, 283 open issues, 2026-05-31: *forj + Rama topology nREPL routing + GF(3) trit coloring*
- `plurigrid/eirobri` — Clojure, 28 open issues, 2026-05-26: *EiRoBri replay world*
- `bmorphism/Gay.jl` — Julia, 189 open issues, 2026-06-01: *Wide-gamut color sampling with splittable determinism*
- `kubeflow/mcp-apache-spark-history-server` — Python, 173 stars: *MCP for Spark History Server*
- `bmorphism/ocaml-mcp-sdk` — OCaml, 61 stars: *OCaml SDK for MCP via Jane Street oxcaml_effect*

### GF(3) World Increment Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 30 |
| +1 | PLUS | #b8bb26 | 31 |
| -1 | MINUS | #cc241d | 30 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-01)

28 wallets queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

All wallets (alice, bob, A–Z): **0.0 APT** — CoinStore balances empty or accounts not initialized with APT.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts healthy, all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no server-side API.** `testnet.mnx.fi` is a Next.js SPA; `/api/markets` and `/api/v1/markets` return the HTML shell, not JSON. No market data extractable via curl. `mnx_snapshots` table: 0 rows.

---

## DuckDB Schema Summary

```
world-increments.duckdb
├── world_increments   91 rows  (GF3-colored repo snapshot events)
├── repo_snapshots     91 rows  (full repo metadata: stars, forks, issues, language)
├── aptos_snapshots    28 rows  (alice, bob, A-Z balances: all 0.0 APT)
├── multisig_probes     5 rows  (A-B, A-G, Y-Z, S-T, V-W: all sigs_required=2, healthy)
└── mnx_snapshots       0 rows  (SPA, data unavailable)
```
