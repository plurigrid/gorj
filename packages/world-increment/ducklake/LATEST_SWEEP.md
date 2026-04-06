# World-Increment Sweep + Hamming Snapshot

**Sweep Date/Time:** 2026-04-06T00:00:00Z (UTC)
**DuckDB Version:** v1.5.1 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Social Graph Sweep

**Total repositories collected:** 360

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| zubyul | user | 23 |
| DJedamski | user | 11 |

**Notes:**
- kubeflow, wasita, kristinezheng, M1shaaa: rate-limited or no public repos accessible (unauthenticated GitHub API, 60 req/hr limit)

---

## Aptos Wallet Balances

Queried via: `POST https://fullnode.mainnet.aptoslabs.com/v1/view` using `0x1::coin::balance`

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| bob | 0x0a3c00c5... | 12.657007 |
| F | 0x18a14b5b... | 1.960516 |
| L | 0x7c2eaeaf... | 1.927269 |
| J | 0x4d964db8... | 1.895093 |
| alice | 0xc793acde... | 0.436434 |
| O | 0x73252b60... | 0.210136 |
| K | 0xa732040a... | 0.161961 |
| P | 0x6218792d... | 0.140136 |
| M | 0x6fed37a7... | 0.112285 |
| N | 0xe7dde6da... | 0.106121 |
| Q | 0xac40fa50... | 0.103240 |
| S | 0xb8753014... | 0.091788 |
| R | 0x7ce605cc... | 0.090217 |
| T | 0x35781dc0... | 0.073713 |
| U | 0x75860da4... | 0.055773 |
| A | 0x8699edc0... | 0.051767 |
| V | 0xb59dd817... | 0.047833 |
| Y | 0xd8e32848... | 0.044449 |
| X | 0xa95cbbd1... | 0.042577 |
| W | 0x5f32aef7... | 0.040705 |
| B | 0x3f892ebe... | 0.036256 |
| Z | 0x7af0ef6e... | 0.023268 |
| E | 0xdc1d9d53... | 0.012561 |
| D | 0xf7765624... | 0.011629 |
| C | 0x38b99e63... | 0.010185 |
| H | 0xce67c327... | 0.000681 |
| I | 0x070fe5d7... | 0.000681 |
| G | 0x69a394c0... | 0.000681 |

**Note:** All 28 accounts exist on Aptos mainnet. The CoinStore resource is not present (accounts use FA migration), so balances were retrieved via view function.

---

## Multisig Contract Probes

Endpoint: `POST https://fullnode.mainnet.aptoslabs.com/v1/view`
Function: `0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c007d... | 2 | TRUE |
| A-G | 0xf56c4a1c0906214... | 2 | TRUE |
| Y-Z | 0xd3ffe1812b2df40... | 2 | TRUE |
| S-T | 0x3b1c3ae905d44c3... | 2 | TRUE |
| V-W | 0x40fad7b423a8436... | 2 | TRUE |

All 5 multisig contracts are healthy with 2-of-N signatures required.

---

## MNX Markets Status

- **Status:** UNAVAILABLE
- `https://testnet.mnx.fi/api/markets` returns HTML (Next.js SPA, no REST API exposed at that path)
- No market data could be fetched; mnx_snapshots table contains a placeholder row

---

## GF(3) Color Chain Legend

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | #d3869b (pink) | ERGODIC |
| 1 | +1 | #b8bb26 (yellow-green) | PLUS |
| 2 | -1 | #cc241d (red) | MINUS |

GF(3) trit/color assigned per repo_id % 3 across all 360 repo snapshots.

---

## DuckDB Tables Summary

| Table | Rows |
|-------|------|
| world_increments | 7 |
| repo_snapshots | 360 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (placeholder) |

### Schema
- **world_increments**: sweep events per org/user, with GF(3) trit/color chain
- **repo_snapshots**: full GitHub repo metadata (name, language, stars, forks, issues, pushed_at, description)
- **aptos_snapshots**: APT balances for 28 labeled addresses (alice, bob, A-Z)
- **multisig_probes**: num_signatures_required for 5 on-chain multisig contracts
- **mnx_snapshots**: MNX market data (unavailable this sweep)
