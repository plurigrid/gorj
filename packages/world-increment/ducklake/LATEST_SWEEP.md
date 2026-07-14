# World-Increment Sweep — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 34 |
| New Increments This Run | 11 |
| Total Repo Snapshots (cumulative) | 1041 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Vercel auth required) |

---

## GF(3) Color Chain — This Run (Increments #24–34)

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 24 | plurigrid (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 25 | kubeflow (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 26 | TeglonLabs (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 27 | bmorphism (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 28 | zubyul (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 29 | migalkin (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 30 | DJedamski (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 31 | wasita (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 32 | kristinezheng (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 33 | M1shaaa (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 34 | AustinCStone (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |

---

## GitHub Social Graph Snapshot

### Orgs

| Org | Repos Sampled | Top Repo | Stars |
|-----|---------------|----------|-------|
| plurigrid | 20 | asi | 30 |
| kubeflow | 20 | kubeflow/kubeflow | 15,777 |
| TeglonLabs | 5 | mathpix-gem | 2 |

### Users

| User | Repos Sampled | Top Repo | Stars |
|------|---------------|----------|-------|
| bmorphism | 15 | ocaml-mcp-sdk | 61 |
| zubyul | 10 | Gay.jl (fork) | 0 |
| migalkin | 6 | NodePiece | 144 |
| DJedamski | 4 | Kaggle | 1 |
| wasita | 5 | magic-garden | 2 |
| kristinezheng | 3 | (no stars) | 0 |
| M1shaaa | 3 | (no stars) | 0 |
| AustinCStone | 6 | TextGAN | 92 |

### Notable Activity (last pushed ≤ 2026-07-14)
- `plurigrid/gorj` — pushed 2026-07-14 (1,162 open issues, active)
- `plurigrid/place` — pushed 2026-07-14
- `plurigrid/eirobri` — pushed 2026-07-14
- `bmorphism/Gay.jl` — pushed 2026-07-14 (187 open issues)
- `kubeflow/sdk` — pushed 2026-07-14
- `wasita/wm-cv` — pushed 2026-07-14

---

## Hamming Swarm Snapshot — Aptos Mainnet

### Wallet Balances (alice, bob, A–Z)

All 28 addresses returned **0.00 APT** from the mainnet CoinStore resource.
This indicates accounts either have no deposited APT or the CoinStore has not been initialized on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...b9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cfdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...25dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

**Total APT across all 28 worlds: 0.0**

---

## Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts probed successfully. All return **2 signatures required**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

All multisig contracts healthy. 2-of-2 threshold consistent across all probed pairs.

---

## MNX Markets

**Status:** UNAVAILABLE — `testnet.mnx.fi` is behind Vercel deployment protection (authentication required). No market data could be extracted from the SPA. Agent will require a Vercel bypass token or trusted source configuration to access this endpoint.

---

## DuckDB Table Summary

| Table | Row Count |
|-------|-----------|
| world_increments | 34 |
| repo_snapshots | 1041 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
