# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-04
**GF(3) color chain:** ERGODIC #d3869b (trit=0) | PLUS #b8bb26 (trit=1) | MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 30 |
| kubeflow | org | 24 |
| TeglonLabs | org | 4 |
| bmorphism | user | 20 |
| zubyul | user | 14 |
| migalkin | user (social) | 7 |
| DJedamski | user (social) | 5 |
| wasita | user (social) | 7 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 5 |
| AustinCStone | user (social) | 7 |
| **TOTAL** | | **128** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,704 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-03 |
| kubeflow/spark-operator | 3,124 | Python | 2026-06-03 |
| kubeflow/trainer | 2,110 | Go | 2026-06-04 |
| kubeflow/katib | 1,685 | Python | 2026-06-04 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 24 | HTML | 2026-04-26 |

### Most Active (recently pushed)

- `plurigrid/gorj` — 2026-06-04 (341 open issues)
- `kubeflow/trainer` — 2026-06-04
- `kubeflow/sdk` — 2026-06-04
- `bmorphism/Gay.jl` — 2026-06-04 (189 open issues)
- `M1shaaa/M1shaaa` — 2026-06-04

### Notable Clusters

**Kubeflow** (15k+ star ML platform on K8s): Active daily pushes to trainer, sdk, katib, dashboard, notebooks in 2026.

**plurigrid** (GF3/Gay.jl/forj ecosystem): gorj, nanoclj-zig, nash-portal, zig-syrup — concentrated Zig/Clojure/Rust on open games and color semantics.

**bmorphism** (MCP server farm + category theory): ocaml-mcp-sdk (61 stars), anti-bullshit-mcp-server, say-mcp-server, babashka-mcp-server. Gay.jl has 189 open issues.

**migalkin** (Knowledge Graph ML): NodePiece (144 stars ICLR'22), StarE (89 stars EMNLP'20) — leading KG representation learning researcher.

**AustinCStone** (ML/vision): TextGAN (92 stars), StereoVisionMRF (11 stars), recent bmorphism fork work.

**zubyul social graph** (wasita, kristinezheng, M1shaaa): Academic researchers, light GitHub footprint, Svelte/Python projects.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 wallets (alice, bob, A-Z) via Aptos mainnet fullnode API.

All 28 wallets returned **0.0 APT**. The CoinStore<AptosCoin> resource was present but balance is zero — wallets exist on-chain but are unfunded.

### Multisig Contract Probes

All 5 multisig pairs responded successfully from Aptos mainnet:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

All multisig accounts require 2-of-N signatures and are healthy (contract callable).

### MNX Markets (testnet.mnx.fi)

Status: **SPA unavailable via curl**. testnet.mnx.fi serves a Next.js SSR shell with no static market data. API endpoints (/api/markets, /api/tickers, /api/v1/markets) returned HTML rather than JSON. Market data requires client-side JS execution.

---

## DuckDB Schema Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 128 |
| repo_snapshots | 128 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, data unavailable) |

**GF(3) distribution:** ERGODIC #d3869b: 42 | PLUS #b8bb26: 43 | MINUS #cc241d: 43
