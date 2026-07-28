# World Increment + Hamming Swarm Snapshot

**Timestamp:** 2026-07-28
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

**Total repos snapshotted:** 361

### Sources

| Source | Repos | Latest Push | Top Repo |
|--------|-------|-------------|----------|
| plurigrid | 100 | 2026-07-28 | asi (⭐52) |
| kubeflow | 49 | 2026-07-28 | kubeflow (⭐15794) |
| TeglonLabs | 5 | 2026-06-08 | mathpix-gem (⭐2) |
| bmorphism | 100 | 2026-07-28 | ocaml-mcp-sdk (⭐61) |
| zubyul | 49 | 2026-07-18 | jonikas_lab_data_analysis_misc (⭐2) |
| migalkin | 19 | 2025-08-04 | NodePiece (⭐144) |
| DJedamski | 6 | 2018-03-07 | Kaggle (⭐1) |
| wasita | 0 | — | — |
| kristinezheng | 5 | 2026-07-01 | kristinezheng.github.io (⭐0) |
| M1shaaa | 8 | 2026-07-28 | M1shaaa (⭐0) |
| AustinCStone | 20 | 2026-07-15 | TextGAN (⭐92) |

### GF(3) Color Chain Summary

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 120 |
| 1 | #b8bb26 | PLUS | 121 |
| -1 | #cc241d | MINUS | 120 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`, indicating **0 APT balance** on mainnet (accounts exist but hold no native APT, or have not been initialized with a coin store).

| World | Address | Balance APT |
|-------|---------|-------------|
| A | `0x8699edc0...be9d7a` | 0.0 |
| B | `0x3f892ebe...77cb13` | 0.0 |
| C | `0x38b99e63...91535e` | 0.0 |
| D | `0xf7765624...fcfdd1` | 0.0 |
| E | `0xdc1d9d53...958d36` | 0.0 |
| F | `0x18a14b5b...c3cf71` | 0.0 |
| G | `0x69a394c0...cc7f32` | 0.0 |
| H | `0xce67c327...e5300f` | 0.0 |
| I | `0x070fe5d7...0c1fc9` | 0.0 |
| J | `0x4d964db8...e87f54` | 0.0 |
| K | `0xa732040a...425dc4` | 0.0 |
| L | `0x7c2eaeaf...37eba9` | 0.0 |
| M | `0x6fed37a7...b7f2e9` | 0.0 |
| N | `0xe7dde6da...551b2c` | 0.0 |
| O | `0x73252b60...25a89d` | 0.0 |
| P | `0x6218792d...1ec948` | 0.0 |
| Q | `0xac40fa50...5c89a9` | 0.0 |
| R | `0x7ce605cc...d76e10` | 0.0 |
| S | `0xb8753014...9d0386` | 0.0 |
| T | `0x35781dc0...3f4588` | 0.0 |
| U | `0x75860da4...ef9956` | 0.0 |
| V | `0xb59dd817...9af2c3` | 0.0 |
| W | `0x5f32aef7...ccc7b0` | 0.0 |
| X | `0xa95cbbd1...33047d` | 0.0 |
| Y | `0xd8e32848...2444c4` | 0.0 |
| Z | `0x7af0ef6e...4e197c` | 0.0 |
| alice | `0xc793acde...24cc7b` | 0.0 |
| bob | `0x0a3c00c5...512d5d` | 0.0 |

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✅ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✅ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✅ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✅ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✅ |

All 5 multisig contracts are healthy with **2-of-2** signature requirement.

### MNX Markets (testnet.mnx.fi)

Site is a Next.js SPA. `GET /api/markets` returned HTML (no REST endpoint exposed). Market data **unavailable** via API probe; SPA requires browser rendering.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 361 |
| repo_snapshots | 361 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |