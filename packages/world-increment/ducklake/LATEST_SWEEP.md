# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-28  
**Sweep ID:** world-increment/hamming-swarm  
**GF(3) Color Chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 50 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | user (social graph) | 7 |
| wasita | user (social graph) | 7 |
| AustinCStone | user (social graph) | 6 |

**Total new repo snapshots this run:** 174  
**Total in ducklake (cumulative):** 1,118 repo_snapshots, 197 world_increments

### Top Repos by Stars (this sweep)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| plurigrid/asi | HTML | 52 | 2026-07-10 |
| AustinCStone/StereoVisionMRF | Python | 11 | 2026-04-01 |
| migalkin/NBFNet_mlx | Python | 10 | 2026-03-11 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |
| plurigrid/zig-syrup | Zig | 2 | 2026-07-28 |

### Most Recently Pushed (top 5)

| Repo | Pushed At |
|------|-----------|
| plurigrid/zig-syrup | 2026-07-28T13:02:13Z |
| plurigrid/gorj | 2026-07-28T12:15:15Z |
| bmorphism/Gay.jl | 2026-07-28T02:25:59Z |
| wasita/wasita.github.io | 2026-07-21T15:55:45Z |
| plurigrid/eirobri | 2026-07-21T02:24:02Z |

### GF(3) Distribution (cumulative, 197 world_increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 65 |
| 1 | #b8bb26 | PLUS | 66 |
| -1 | #cc241d | MINUS | 66 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A-Z)

**Result:** All 28 wallets returned 0.0 APT.

The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource was not found on any address, indicating these accounts have not been initialized with an APT CoinStore on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A | 0x8699...d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Total APT across swarm:** 0.0 APT

### Multisig Contract Probes

All 5 multisig contracts are **HEALTHY** (2-of-N threshold confirmed on Aptos mainnet):

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | healthy |
| A-G | 0xf56c...096 | 2 | healthy |
| Y-Z | 0xd3ff...883 | 2 | healthy |
| S-T | 0x3b1c...883 | 2 | healthy |
| V-W | 0x40fa...b6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** - testnet.mnx.fi is a Next.js SPA. All API paths probed (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return the HTML shell rather than JSON market data. No market records extractable.

---

## DuckDB Ducklake State

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 197 |
| repo_snapshots | 1,118 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## Notes

- DuckDB v1.5.5 (Variegata)
- Aptos fullnode: `fullnode.mainnet.aptoslabs.com/v1` — all 28 accounts lack APT CoinStore resource (never received APT deposit on mainnet)
- MNX testnet is a client-side Next.js SPA; REST API not publicly accessible
- Social graph users queried this run: migalkin, wasita, AustinCStone; DJedamski/kristinezheng/M1shaaa data present from prior sweeps
