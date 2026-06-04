# LATEST_SWEEP.md

**Sweep timestamp:** 2026-04-28 09:25:54 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapped | GF3 Trit | GF3 Name | GF3 Color |
|--------|------|--------------|----------|----------|-----------|
| AustinCStone | user | 40 | 1 | PLUS | #b8bb26 |
| DJedamski | user | 6 | 2 | MINUS | #cc241d |
| M1shaaa | user | 8 | 0 | ERGODIC | #d3869b |
| TeglonLabs | org | 4 | 1 | PLUS | #b8bb26 |
| bmorphism | user | 100 | 2 | MINUS | #cc241d |
| kristinezheng | user | 6 | 0 | ERGODIC | #d3869b |
| kubeflow | org | 47 | 1 | PLUS | #b8bb26 |
| migalkin | user | 19 | 2 | MINUS | #cc241d |
| plurigrid | org | 100 | 0 | ERGODIC | #d3869b |
| wasita | user | 10 | 1 | PLUS | #b8bb26 |
| zubyul | user | 49 | 2 | MINUS | #cc241d |

**Total repos snapped:** 389 across 11 sources (orgs: plurigrid, kubeflow, TeglonLabs; users: bmorphism, zubyul + social graph: migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)

### Notable Activity
- **wasita/wasita.github.io** (Svelte): pushed 2026-04-28 — most recently active
- **M1shaaa/M1shaaa** (profile): pushed 2026-04-28
- **plurigrid**: 100 repos snapped (paginated at max)
- **bmorphism**: 100 repos snapped (paginated at max)
- **kubeflow**: 47 public repos (ML platform org)
- **TeglonLabs**: 4 repos (mathpix-gem Ruby, monad-mcp-server, topoi, coin-flip-mcp)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming swarm addresses queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| A | 0x8699edc0...be9d7a | 0.00000000 |
| B | 0x3f892ebe...77cb13 | 0.00000000 |
| C | 0x38b99e63...91535e | 0.00000000 |
| D | 0xf7765624...fcfdd1 | 0.00000000 |
| E | 0xdc1d9d53...958d36 | 0.00000000 |
| F | 0x18a14b5b...c3cf71 | 0.00000000 |
| G | 0x69a394c0...cc7f32 | 0.00000000 |
| H | 0xce67c327...e5300f | 0.00000000 |
| I | 0x070fe5d7...0c1fc9 | 0.00000000 |
| J | 0x4d964db8...e87f54 | 0.00000000 |
| K | 0xa732040a...425dc4 | 0.00000000 |
| L | 0x7c2eaeaf...37eba9 | 0.00000000 |
| M | 0x6fed37a7...b7f2e9 | 0.00000000 |
| N | 0xe7dde6da...551b2c | 0.00000000 |
| O | 0x73252b60...25a89d | 0.00000000 |
| P | 0x6218792d...1ec948 | 0.00000000 |
| Q | 0xac40fa50...5c89a9 | 0.00000000 |
| R | 0x7ce605cc...d76e10 | 0.00000000 |
| S | 0xb8753014...9d0386 | 0.00000000 |
| T | 0x35781dc0...3f4588 | 0.00000000 |
| U | 0x75860da4...ef9956 | 0.00000000 |
| V | 0xb59dd817...9af2c3 | 0.00000000 |
| W | 0x5f32aef7...ccc7b0 | 0.00000000 |
| X | 0xa95cbbd1...33047d | 0.00000000 |
| Y | 0xd8e32848...2444c4 | 0.00000000 |
| Z | 0x7af0ef6e...4e197c | 0.00000000 |
| alice | 0xc793acde...24cc7b | 0.00000000 |
| bob | 0x0a3c00c5...512d5d | 0.00000000 |

**Note:** All 28 addresses returned 0.0 APT. Accounts may be uninitialized (no `CoinStore` resource registered) or genuinely empty on mainnet.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✓ |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ |
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✓ |

All 5 multisig contracts are **healthy** and configured as **2-of-2** signatures required.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable for programmatic ingestion. The endpoint returns a Next.js SPA (client-side rendered). No public REST API paths (`/api/markets`, `/api/v1/markets`) yield JSON data. MNX market data not ingested this sweep.

---

## DuckDB Schema Summary

| Table | Rows (cumulative) |
|-------|------------------|
| world_increments | 34 |
| repo_snapshots | 1333 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |

---

## GF(3) Color Legend

| Trit | Name | Hex | Meaning |
|------|------|-----|---------|
| 0 | ERGODIC | `#d3869b` | id%3==0 |
| 1 | PLUS | `#b8bb26` | id%3==1 |
| -1 | MINUS | `#cc241d` | id%3==2 |
