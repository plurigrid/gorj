# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-07-07  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| kubeflow | org | 49 | 34,330 |
| bmorphism | user | 100 (of 105) | 247 |
| plurigrid | org | 100 (of 103) | 82 |
| zubyul | user | 49 | 14 |
| migalkin | social graph | 7 sampled | 279 |
| AustinCStone | social graph | 7 sampled | 107 |
| wasita | social graph | 11 | 5 |
| DJedamski | social graph | 6 | 3 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | social graph | 5 | 0 |
| M1shaaa | social graph | 8 | 0 |

**Total repo snapshots:** 347  
**Total world_increments:** 347 (GF3 color-chained by id%3)

### GF3 Color Chain
- `id%3==0` → trit=0, ERGODIC `#d3869b`
- `id%3==1` → trit=+1, PLUS `#b8bb26`
- `id%3==2` → trit=-1, MINUS `#cc241d`

### Notable Repos
- **kubeflow/kubeflow**: flagship ML platform (~17k stars)
- **migalkin/NodePiece**: KG representation learning, ICLR'22 (144 stars)
- **migalkin/StarE**: Hyper-relational KG message passing, EMNLP'20 (89 stars)
- **AustinCStone/TextGAN**: TensorFlow text GAN (92 stars)
- **TeglonLabs/jank-crane**: crane-jank converged-IR hub with GF3 convergence maps (C++)
- **wasita/wasita.github.io**: personal site, active (pushed 2026-07-06)

### Events
- bmorphism repo bmfork/bmforkupdate visible via AustinCStone social link
- wasita.github.io most recently pushed (2026-07-06T23:51:09Z)
- TeglonLabs/jank-crane most recent TeglonLabs push (2026-06-08)

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses probed)
Endpoint: https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>
Ledger version at query time: ~6,166,865,634

Result: All 28 addresses (alice, bob, A-Z) returned HTTP 404 resource_not_found. No APT CoinStore resource exists at these addresses on mainnet. All balances recorded as 0.00 APT.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.0 (no resource) |
| bob   | 0x0a3c00... | 0.0 (no resource) |
| A-Z   | various...   | 0.0 (no resource) |

### Multisig Contract Probes (5 pairs)
Endpoint: POST https://fullnode.mainnet.aptoslabs.com/v1/view
Function: 0x1::multisig_account::num_signatures_required

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B  | 0x0da4f4...     | 2             | yes     |
| A-G  | 0xf56c4a...     | 2             | yes     |
| Y-Z  | 0xd3ffe1...     | 2             | yes     |
| S-T  | 0x3b1c3a...     | 2             | yes     |
| V-W  | 0x40fad7...     | 2             | yes     |

All 5 multisig contracts are healthy and require 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)
testnet.mnx.fi is a password-protected Vercel deployment (HTTP 401, authentication required).
No market data accessible without a bypass token. Recorded as MNX_UNAVAILABLE in mnx_snapshots.

---

## DuckDB Schema Summary
```
world_increments   347 rows  -- GF3-tagged event log
repo_snapshots     347 rows  -- GitHub repo metadata
aptos_snapshots     28 rows  -- Hamming swarm wallet balances (all 0.0 APT)
multisig_probes      5 rows  -- All 2-of-2, all healthy
mnx_snapshots        1 row   -- MNX_UNAVAILABLE (auth required)
```
