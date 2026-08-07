# World-Increment Sweep + Hamming Swarm Snapshot

**Run timestamp:** 2026-08-07T21:18 UTC  
**Branch:** world-increment/sweep-2026-08-07-2118  
**GF3 color chain:** ERGODIC #d3869b (trit=0) → PLUS #b8bb26 (trit=1) → MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### DuckDB State After Sweep
| Table | Rows |
|---|---|
| world_increments | 165 |
| repo_snapshots | 1086 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

### Sources Swept
| Source | Type | Repos Captured |
|---|---|---|
| plurigrid | org | 230 |
| bmorphism | user | 230 |
| kubeflow | org | 124 |
| TeglonLabs | org | 111 |
| AustinCStone | user (social graph) | 90 |
| zubyul | user | 78 |
| migalkin | user (social graph) | 65 |
| wasita | user (social graph) | 63 |
| kristinezheng | user (social graph) | 37 |
| M1shaaa | user (social graph) | 34 |
| DJedamski | user (social graph) | 24 |
| **Total** | | **1086** |

### Notable Recent Activity
- **wasita/wm-cv** — pushed 2026-08-07T20:46 UTC (today, Svelte CV app)
- **wasita/xoxowasita-analysis** — pushed 2026-08-06 (Python)
- **TeglonLabs/jank-crane** — C++ crane-jank converged-IR hub with GF3 convergence maps (pushed 2026-06-08)
- **migalkin/NodePiece** — 144⭐ ICLR'22 KG representation paper
- **AustinCStone/TextGAN** — 92⭐ TensorFlow GAN for text generation
- **TeglonLabs/mathpix-gem** — 2⭐ Ruby gem for math OCR

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 wallets (alice, bob, A–Z) queried at 2026-08-07T21:18 UTC.

**Result: All wallets returned 0.000000 APT**

The Aptos mainnet fullnode responded with `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on every address. This indicates none of the Hamming swarm addresses have an active APT CoinStore resource — they may be unfunded or using a different token resource.

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...d386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes
All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy** — 2-of-2 signature threshold across all pairs.

### MNX Markets
`https://testnet.mnx.fi` returned a Next.js SPA (HTML shell). No JSON API endpoint was found at `/api/markets` or other standard paths (the site is a client-rendered app that loads market data via browser JS). MNX market data is **unavailable** via server-side fetch — recorded as 0 rows in `mnx_snapshots`.

---

## DuckDB Schema Summary

```sql
-- world-increments.duckdb
world_increments  -- GF3 color chain events (165 rows)
repo_snapshots    -- GitHub repo snapshots (1086 rows)
aptos_snapshots   -- Hamming swarm APT balances (28 rows)
multisig_probes   -- Multisig contract health (5 rows)
mnx_snapshots     -- MNX market data (0 rows - SPA only)
```

Path: `packages/world-increment/ducklake/world-increments.duckdb`
