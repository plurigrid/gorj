# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-24  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars | Max Stars |
|--------|------|-------|-------------|-----------|
| kubeflow | org | 48 | 34,254 | 15,742 |
| migalkin | user (social) | 19 | 280 | 144 |
| bmorphism | user | 100 | 247 | 61 |
| AustinCStone | user (social) | 40 | 108 | 92 |
| plurigrid | org | 100 | 77 | 26 |
| zubyul | user | 49 | 14 | 2 |
| wasita | user (social) | 11 | 5 | 2 |
| DJedamski | user (social) | 6 | 3 | 1 |
| TeglonLabs | org | 5 | 2 | 2 |
| M1shaaa | user (social) | 8 | 0 | 0 |
| kristinezheng | user (social) | 5 | 0 | 0 |
| **TOTAL** | | **391** | **34,990** | |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,742 | — | 2026-06-18 |
| kubeflow/pipelines | 4,157 | Python | 2026-06-24 |
| kubeflow/spark-operator | 3,128 | Python | 2026-06-24 |
| kubeflow/trainer | 2,121 | Go | 2026-06-24 |
| kubeflow/katib | 1,685 | Python | 2026-06-23 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,028 | YAML | 2026-06-24 |
| kubeflow/arena | 813 | Go | 2026-05-07 |
| kubeflow/kale | 694 | Python | 2026-06-22 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-23 |
| migalkin/NodePiece | 144 | Python | — |

### Most Recently Active (2026)

| Repo | Pushed | Stars | Language |
|------|--------|-------|----------|
| plurigrid/gorj | 2026-06-24T22:11 | 0 | Clojure |
| kubeflow/pipelines | 2026-06-24T18:51 | 4,157 | Python |
| kubeflow/spark-operator | 2026-06-24T16:53 | 3,128 | Python |
| kubeflow/notebooks | 2026-06-24T15:34 | 73 | — |
| kubeflow/community-distribution | 2026-06-24T14:23 | 1,028 | YAML |
| M1shaaa/M1shaaa | 2026-06-24T14:22 | 0 | — |
| kubeflow/hub | 2026-06-24T14:13 | 173 | Go |
| kubeflow/mcp-server | 2026-06-24T11:09 | 17 | Python |
| kubeflow/sdk | 2026-06-24T11:06 | 121 | Python |
| kubeflow/trainer | 2026-06-24T10:40 | 2,121 | Go |
| bmorphism/Gay.jl | 2026-06-24T00:35 | 2 | Julia |
| plurigrid/place | 2026-06-24T00:41 | 1 | TeX |

### Notable Observations

- **kubeflow** is the most active org — 8+ repos pushed today including new `mcp-server` (MCP for Kubeflow Tools, 17 stars)
- **plurigrid/gorj** (this repo) was the most recently pushed non-kubeflow repo at snapshot time
- **bmorphism/Gay.jl**: Wide-gamut color sampling with splittable determinism (Julia) — pushed today, Pigeons.jl SPI pattern
- **zubyul** social graph: `voice-observatory`, `nash-tui`, `nash-web` all active in Apr 2026 (49 total repos)
- **TeglonLabs/jank-crane**: C++ converged-IR hub with GF(3) convergence maps — pushed 2026-06-08
- **GF(3) trit balance**: 130 ERGODIC / 131 PLUS / 130 MINUS — near-uniform across 391 increments

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Note:** All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. Account A has `sequence_number: 58`
confirming it exists on-chain — accounts use FA (Fungible Asset) module rather than legacy
coin module. APT balances not retrievable via legacy coin endpoint.

| World | Address (prefix) | Balance APT | Status |
|-------|-----------------|-------------|--------|
| alice | 0xc793ac... | 0.0 | resource_not_found |
| bob | 0x0a3c00... | 0.0 | resource_not_found |
| A | 0x8699ed... | 0.0 | resource_not_found |
| B–Z (25 wallets) | ... | 0.0 | resource_not_found |

All 28 wallets: balance_apt = 0.0, status = resource_not_found (FA module).

### Multisig Contract Probes

All 5 probed multisig accounts healthy with **2-of-2 threshold**:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | yes |
| A-G | 0xf56c4a... | 2 | yes |
| Y-Z | 0xd3ffe1... | 2 | yes |
| S-T | 0x3b1c3a... | 2 | yes |
| V-W | 0x40fad7... | 2 | yes |

**Status: All multisig contracts healthy (5/5), all require 2 signatures.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment authentication.
All API paths return `Authentication Required`. No market data retrievable. `mnx_snapshots`
table empty for this sweep.

---

## DuckDB Ducklake Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 391 |
| repo_snapshots | 391 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

**Sources swept:** plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul,
migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone
