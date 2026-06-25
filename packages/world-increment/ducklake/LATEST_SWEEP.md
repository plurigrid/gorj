# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-25  
**Sweep Branch:** world-increment/sweep-2026-06-25

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos This Sweep |
|--------|------|-----------------|
| plurigrid | org | 43 |
| kubeflow | org | 15 |
| TeglonLabs | org | 5 |
| bmorphism | user | 15 |
| zubyul | user | 11 |
| migalkin | user (social graph) | 7 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 6 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 5 |
| **Total** | | **126** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 48 |
| 1 | `#b8bb26` | PLUS | 50 |
| -1 | `#cc241d` | MINUS | 50 |

### Notable Repos (Top by Stars, This Sweep)

| Repo | Stars | Forks | Language |
|------|-------|-------|----------|
| kubeflow/kubeflow | 15,742 | 2,680 | — |
| kubeflow/pipelines | 4,157 | 2,009 | Python |
| kubeflow/spark-operator | 3,128 | 1,492 | Python |
| kubeflow/trainer | 2,121 | 972 | Go |
| kubeflow/katib | 1,685 | 527 | Python |
| AustinCStone/TextGAN | 92 | 30 | Python |
| migalkin/NodePiece | 144 | 21 | Python |
| migalkin/StarE | 89 | 16 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml |
| plurigrid/gorj | 0 | 0 | Clojure (800 open issues!) |

### Hot Activity (Pushed Last 7 Days)

- `bmorphism/Gay.jl` — pushed 2026-06-25 (187 open issues, Julia)
- `plurigrid/gorj` — pushed 2026-06-25 (our own repo!)
- `M1shaaa/M1shaaa` — pushed 2026-06-24
- `kubeflow/pipelines` — pushed 2026-06-24
- `zubyul/voice-observatory` — pushed 2026-04-24

### DuckDB ducklake State

| Table | Rows |
|-------|------|
| world_increments | 148 |
| repo_snapshots | 1,069 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos)

### Wallet Balances (A–Z + alice/bob)

All 28 addresses queried against Aptos mainnet CoinStore endpoint.  
**Result: All addresses returned HTTP 404 — wallets not initialized on mainnet.**

This indicates the Hamming swarm addresses (alice, bob, A–Z) have not yet been funded or their accounts have not been created on Aptos mainnet. Addresses are tracked for future sweeps.

### Multisig Contracts

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428...` | 2 | ✓ |
| A-G | `0xf56c4a1c...` | 2 | ✓ |
| Y-Z | `0xd3ffe181...` | 2 | ✓ |
| S-T | `0x3b1c3ae9...` | 2 | ✓ |
| V-W | `0x40fad7b4...` | 2 | ✓ |

**All 5 multisig contracts healthy — all require 2-of-N signatures.**

### MNX Testnet Markets

`https://testnet.mnx.fi` — **HTTP 401 Unauthorized** on all probed API paths:
- `/api/markets`
- `/api/v1/markets`
- `/api/tickers`

MNX testnet appears to require authentication. No market data captured this sweep.

---

## Sweep Metadata

- **GF(3) color chain seed:** id % 3 → trit ∈ {0, 1, -1}
- **Colors:** ERGODIC=#d3869b, PLUS=#b8bb26, MINUS=#cc241d
- **DuckDB version:** v1.5.4 (Variegata)
- **DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
