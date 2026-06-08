# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-08  
**Branch:** world-increment/sweep-2026-06-08-1005  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 11 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 40 |
| **Total** | | **391** |

### GF(3) Color Chain Distribution
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 55 |
| +1 | PLUS | #b8bb26 | 56 |
| -1 | MINUS | #cc241d | 56 |

### Top Repos by Stars

| Repo | Stars | Language | Source |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,708 | — | org:kubeflow |
| kubeflow/pipelines | 4,152 | Python | org:kubeflow |
| kubeflow/spark-operator | 3,126 | Python | org:kubeflow |
| kubeflow/trainer | 2,112 | Go | org:kubeflow |
| kubeflow/katib | 1,685 | Python | org:kubeflow |
| kubeflow/examples | 1,462 | Jsonnet | org:kubeflow |
| kubeflow/manifests | 1,020 | YAML | org:kubeflow |
| kubeflow/arena | 812 | Go | org:kubeflow |
| AustinCStone/TextGAN | 92 | Python | user:AustinCStone |
| migalkin/NodePiece | 144 | Python | user:migalkin |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | user:bmorphism |
| plurigrid/asi | 25 | HTML | org:plurigrid |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | user:bmorphism |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | user:bmorphism |
| bmorphism/say-mcp-server | 20 | JavaScript | user:bmorphism |

### Notable Findings

- **plurigrid/gorj** (this repo): 439 open issues — forj + Rama nREPL + GF(3) trit coloring for compositional open game REPL orchestration
- **TeglonLabs/jank-crane**: created 2026-06-08 (today!), C++ — crane-jank converged-IR hub with GF3 convergence maps, simonw workflow
- **bmorphism/Gay.jl**: 189 open issues — Wide-gamut color sampling with splittable determinism (Pigeons.jl SPI)
- **bmorphism MCP universe** (2024–2026 era): say-mcp-server (20★), babashka-mcp-server (19★), manifold-mcp-server (14★), penrose-mcp (10★), anti-bullshit-mcp-server (23★), nats-mcp-server (7★), hypernym-mcp-server (6★)
- **zubyul social graph themes**: GF(3) trit GPU kernels (tilelang-kernels, Blackwell CUDA 13.0), NASH TUI on GeckoTerminal OHLCV, BCI/OpenBCI work, Gay.jl color world

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice through Z, 28 addresses)

All 28 Hamming swarm addresses queried against `fullnode.mainnet.aptoslabs.com`.  
**Result: All 28 addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.**

The swarm wallets (alice, bob, A–Z) have not initialized their APT CoinStore resource on Aptos mainnet. Accounts may exist at the address derivation level but have not been funded with native APT through the standard coin module.

| Worlds | Status |
|--------|--------|
| alice, bob, A–Z (28 total) | CoinStore uninitialized on mainnet |

### Multisig Contract Probes

All 5 multisig contracts are **HEALTHY** — each requires exactly **2 signatures**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4...7003` | 2 | healthy |
| A-G | `0xf56c...0096` | 2 | healthy |
| Y-Z | `0xd3ff...b883` | 2 | healthy |
| S-T | `0x3b1c...7883` | 2 | healthy |
| V-W | `0x40fa...eb6d` | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — All routes on `testnet.mnx.fi` return Vercel deployment protection auth page. No market data extracted.

---

## DuckDB Tables

```
world_increments  167 rows   — GF(3)-colored sweep events (ERGODIC/PLUS/MINUS)
repo_snapshots    1088 rows  — temporal repo snapshots (391 unique repos)
aptos_snapshots   28 rows    — Hamming swarm wallet probes (all uninitialized)
multisig_probes   5 rows     — 2-of-N multisig contracts, all healthy
mnx_snapshots     0 rows     — MNX unavailable (Vercel auth required)
```

## Sweep Metadata
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** v1.5.3 Variegata
- **GitHub access:** via GitHub MCP server (plurigrid/gorj scope)
- **Aptos API:** fullnode.mainnet.aptoslabs.com/v1 — reachable, curl exit 0
- **Network policy:** external curl available for Aptos; GitHub MCP for social graph
