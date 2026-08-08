# World Increment Sweep + Hamming Snapshot
**Date:** 2026-08-08  
**Run type:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 (of 103) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (of 106) |
| zubyul | user | 49 |
| migalkin | social graph | 7 |
| DJedamski | social graph | 5 |
| wasita | social graph | 5 |
| kristinezheng | social graph | 3 |
| M1shaaa | social graph | 2 |
| AustinCStone | social graph | 13 |
| **Total** | | **338** |

### GF(3) Color Chain
- `id % 3 == 0` → trit=0, ERGODIC `#d3869b`
- `id % 3 == 1` → trit=1, PLUS `#b8bb26`
- `id % 3 == 2` → trit=-1, MINUS `#cc241d`

### Top Repos by Stars (Latest Sweep)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,806 | — |
| kubeflow/pipelines | 4,181 | Python |
| kubeflow/spark-operator | 3,145 | Python |
| kubeflow/trainer | 2,175 | Go |
| kubeflow/katib | 1,694 | Python |
| kubeflow/examples | 1,461 | Jsonnet |
| kubeflow/community-distribution | 1,030 | YAML |
| kubeflow/arena | 817 | Go |
| kubeflow/kale | 699 | Python |
| plurigrid/asi | 59 | HTML |

### Notable plurigrid Activity (pushed today 2026-08-08)
- `plurigrid/place` — pushed 10:48 UTC (18 open issues)
- `plurigrid/gorj` — pushed 12:18 UTC (1719 open issues — active development)

### Notable bmorphism Repos
- `bmorphism/ocaml-mcp-sdk` — 61 stars, OCaml SDK for MCP
- `bmorphism/anti-bullshit-mcp-server` — 23 stars
- `bmorphism/risc0-cosmwasm-example` — 23 stars
- `bmorphism/Gay.jl` — 2 stars but **188 open issues** (very active)

### TeglonLabs
5 repos: `jank-crane` (C++, GF3 convergence maps), `mathpix-gem` (Ruby, 2★), `coin-flip-mcp` (JS, 2 forks), `monad-mcp-server`, `topoi` (Python)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets queried (alice, bob, A–Z). All returned **0.0 APT** — accounts do not exist on mainnet or hold no APT coins at this time.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts responded successfully. All require **2-of-2 signatures**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | ✓ |
| A-G | 0xf56c4a... | 2 | ✓ |
| Y-Z | 0xd3ffe1... | 2 | ✓ |
| S-T | 0x3b1c3a... | 2 | ✓ |
| V-W | 0x40fad7... | 2 | ✓ |

All multisig contracts healthy. 2-of-2 threshold enforced across all pairs.

### MNX Markets (testnet.mnx.fi)

The site is a Next.js SPA. API paths `/api/markets` and `/api/v1/markets` return the SPA HTML rather than JSON. **No structured market data extractable from this endpoint at sweep time.** Status: SPA redirect, data unavailable without browser JS execution.

---

## DuckDB Tables Summary

| Table | Rows This Sweep |
|-------|----------------|
| world_increments | +353 |
| repo_snapshots | +353 |
| aptos_snapshots | +28 |
| multisig_probes | +5 |
| mnx_snapshots | 0 (SPA, no API) |

Database: `packages/world-increment/ducklake/world-increments.duckdb`
