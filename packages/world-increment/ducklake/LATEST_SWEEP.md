# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-30  
**GF(3) Color Chain:** ERGODIC #d3869b (trit=0) → PLUS #b8bb26 (trit=1) → MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Summary by Source

| Source | Type | Repos | Total Stars | Last Push |
|--------|------|-------|-------------|-----------|
| kubeflow | org | 48 | 34,147 | 2026-05-29 |
| migalkin | user | 9 | 280 | 2026-05-28 |
| bmorphism | user | 100 | 247 | 2026-05-30 |
| AustinCStone | user (social) | 7 | 106 | 2026-04-01 |
| plurigrid | org | 100 | 74 | 2026-05-30 |
| zubyul | user | 49 | 14 | 2026-04-24 |
| wasita | user (social) | 7 | 5 | 2026-05-20 |
| DJedamski | user (social) | 6 | 3 | 2023-04-21 |
| TeglonLabs | org | 4 | 2 | 2026-01-01 |
| kristinezheng | user (social) | 5 | 0 | 2026-05-14 |
| M1shaaa | user (social) | 4 | 0 | 2026-02-04 |

**Total repos snapshotted:** 339

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,686 | — | 2026-05-24 |
| kubeflow/pipelines | 4,150 | Python | 2026-05-29 |
| kubeflow/spark-operator | 3,124 | Python | 2026-05-29 |
| kubeflow/trainer | 2,107 | Go | 2026-05-29 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| kubeflow/examples | 1,463 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,019 | YAML | 2026-05-29 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |

### Notable Plurigrid / bmorphism Activity

- `plurigrid/gorj` (this repo): 258 open issues, pushed 2026-05-30 — GF(3) trit coloring for open game REPL
- `bmorphism/Gay.jl`: 189 open issues, most active; wide-gamut color sampling with GF(3) trits
- `plurigrid/eirobri`: 28 open issues — EiRoBri replay world (Clojure)
- `bmorphism/anti-bullshit-mcp-server`: 23 stars — claim analysis via epistemological frameworks
- `bmorphism/say-mcp-server`: 20 stars — macOS TTS MCP server

### GF(3) Distribution (this sweep)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 113 |
| 1 | PLUS | #b8bb26 | 113 |
| -1 | MINUS | #cc241d | 113 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming-alphabet wallets (alice, bob, A-Z) were queried against the Aptos mainnet `CoinStore<AptosCoin>` resource. All returned `0 APT` — indicating either unfunded accounts or that the `CoinStore` resource has not been registered for these addresses on mainnet.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 probed multisig contracts responded healthy with 2 signatures required:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA — no REST API endpoints (`/api/markets`, `/api/tickers`) are accessible server-side. Market data is rendered client-side and unavailable via curl. Marked as unavailable in `mnx_snapshots` table.

---

## DuckDB Schema

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (this sweep) |
|-------|-------------------|
| `world_increments` | 339 |
| `repo_snapshots` | 339 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 1 (sentinel) |
