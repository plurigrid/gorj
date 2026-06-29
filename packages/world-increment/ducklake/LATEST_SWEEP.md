# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-29
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d (id%3)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Total Stars |
|--------|------|----------------|-------------|
| plurigrid | org | 30 (of 102) | 71 |
| kubeflow | org | 20 (of 48) | 32,878 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 20 (of 105) | 203 |
| zubyul | user | 17 (of 49) | 9 |
| migalkin | user (social) | 8 (of 19) | 280 |
| AustinCStone | user (social) | 6 (of 40) | 107 |
| wasita | user (social) | 5 (of 11) | 5 |
| kristinezheng | user (social) | 4 (of 5) | 0 |
| DJedamski | user (social) | 5 (of 6) | 3 |
| M1shaaa | user (social) | 3 (of 8) | 0 |
| **TOTAL** | | **123** | **33,558** |

### Notable Repos by Activity
- plurigrid/gorj — pushed 2026-06-29, 896 open issues, GF(3) REPL orchestration
- bmorphism/Gay.jl — pushed 2026-06-29, 187 open issues, wide-gamut color sampling
- plurigrid/asi — pushed 2026-06-28, 26 stars, "everything is topological chemputer!"
- kubeflow/pipelines — pushed 2026-06-27, 4,159 stars
- kubeflow/kubeflow — 15,752 stars (largest in graph)
- migalkin/NodePiece — 144 stars, ICLR'22 knowledge graph representations
- AustinCStone/TextGAN — 92 stars, GAN for text generation
- bmorphism/ocaml-mcp-sdk — 61 stars, OCaml SDK for MCP

### DuckDB Schema
- world_increments (123 rows): GF(3) trit/color/name, source, event, snapshot hash
- repo_snapshots (123 rows): full metadata per repo

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A-Z)

All 28 wallets queried against Aptos mainnet fullnode.
Result: All wallets returned 0.0 APT (accounts not found or empty CoinStore).

| World | Balance (APT) |
|-------|---------------|
| alice | 0.0 |
| bob | 0.0 |
| A through Z (26 wallets) | 0.0 each |

### Multisig Contract Probes (5 pairs)

All probed via 0x1::multisig_account::num_signatures_required

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | 2 | HEALTHY |
| A-G | 0xf56c4a1c... | 2 | HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | HEALTHY |
| V-W | 0x40fad7b4... | 2 | HEALTHY |

All 5 multisig contracts are live and require 2-of-N signatures. No degraded multisigs detected.

### MNX Markets (testnet.mnx.fi)

Status: UNAVAILABLE — Vercel deployment protection requires authentication.
API paths /api/markets and /api/v1/markets both returned Vercel auth challenge.

---

## GF(3) Color Chain (first 10 increments)

| id | trit | color | name | repo |
|----|------|-------|------|------|
| 1 | 0 | #d3869b | ERGODIC | TeglonLabs/jank-crane |
| 2 | 1 | #b8bb26 | PLUS | TeglonLabs/mathpix-gem |
| 3 | -1 | #cc241d | MINUS | TeglonLabs/coin-flip-mcp |
| 4 | 0 | #d3869b | ERGODIC | TeglonLabs/monad-mcp-server |
| 5 | 1 | #b8bb26 | PLUS | TeglonLabs/topoi |
| 6 | -1 | #cc241d | MINUS | migalkin/kgcourse2021 |
| 7 | 0 | #d3869b | ERGODIC | migalkin/NBFNet_mlx |
| 8 | 1 | #b8bb26 | PLUS | migalkin/StarE |
| 9 | -1 | #cc241d | MINUS | migalkin/rambo |
| 10 | 0 | #d3869b | ERGODIC | migalkin/RWL |

---

## DuckDB File
packages/world-increment/ducklake/world-increments.duckdb

Tables: world_increments, repo_snapshots, aptos_snapshots, multisig_probes, mnx_snapshots
