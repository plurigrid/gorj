# LATEST_SWEEP — World Increment + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-05 05:10:16 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**Total world_increments:** 330 | **GF3 distribution:** 110 ERGODIC (#d3869b) / 110 PLUS (#b8bb26) / 110 MINUS (#cc241d)

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 49 |
| zubyul | user | 100 |
| migalkin | social | 7 |
| DJedamski | social | 4 |
| wasita | social | 6 |
| kristinezheng | social | 3 |
| M1shaaa | social | 3 |
| AustinCStone | social | 6 |
| **TOTAL** | | **330** |

### Notable Repositories by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| AustinCStone/StereoVisionMRF | 11 | Python | 2026-04-01 |
| migalkin/kgcourse2021 | 25 | HTML | 2026-02-16 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |

### GF3 Color Chain (first 9)

| Increment ID | Trit | Color | Hex |
|-------------|------|-------|-----|
| 1 | 1 (PLUS) | PLUS | #b8bb26 |
| 2 | 2 (MINUS) | MINUS | #cc241d |
| 3 | 0 (ERGODIC) | ERGODIC | #d3869b |
| 4 | 1 (PLUS) | PLUS | #b8bb26 |
| 5 | 2 (MINUS) | MINUS | #cc241d |
| 6 | 0 (ERGODIC) | ERGODIC | #d3869b |
| 7 | 1 (PLUS) | PLUS | #b8bb26 |
| 8 | 2 (MINUS) | MINUS | #cc241d |
| 9 | 0 (ERGODIC) | ERGODIC | #d3869b |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets (alice, bob, A–Z) queried via Aptos fullnode mainnet API.  
**Result: All accounts return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — balance recorded as 0.0 APT for all.**  
This indicates these addresses either have not been initialized with APT or hold zero balance.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26 wallets) | 0x8699...→ 0x7af0... | 0.0 each |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

**All multisigs require 2-of-N signatures. All probes returned successfully.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a Vercel-protected deployment requiring authentication.  
Attempted paths: `/`, `/api/markets`, `/api/v1/markets` — all return HTTP 401 with Vercel auth wall.  
No market data could be extracted without credentials.

---

## DuckDB Tables Summary

| Table | Row Count | Description |
|-------|-----------|-------------|
| world_increments | 330 | GF3-tagged repo snapshot events |
| repo_snapshots | 330 | Full repo metadata (stars, forks, language, push date) |
| aptos_snapshots | 28 | Wallet balances for alice/bob/A-Z |
| multisig_probes | 5 | Multisig contract signature requirements |
| mnx_snapshots | 0 | Empty (auth-gated, unavailable) |

