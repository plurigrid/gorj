# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-06 11:14 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered

| Source | Type |
|--------|------|
| plurigrid | org |
| kubeflow | org |
| TeglonLabs | org |
| bmorphism | user |
| zubyul | user |
| Social graph: migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone | observed |

> Note: Unauthenticated GitHub API rate limit (60 req/hr) was exhausted during initial curl sweep.  
> Repo data collected via GitHub MCP tools (authenticated).

### DuckDB Ducklake State

| Table | Rows |
|-------|------|
| world_increments | 108 |
| repo_snapshots | 1029 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA — no REST API) |

### GF(3) Color Chain Distribution (all increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 35 |
| -1 | `#cc241d` | MINUS | 36 |
| 1 | `#b8bb26` | PLUS | 37 |

### Top Repos by Stars (This Sweep)

| Repo | Language | Stars | Forks | Issues | Pushed |
|------|----------|-------|-------|--------|--------|
| kubeflow/kubeflow | — | 15622 | 2647 | 0 | 2026-04-29 |
| kubeflow/kubeflow | — | 15572 | 2633 | 0 | 2026-01-05T13:47:10Z |
| kubeflow/kubeflow | — | 15565 | 2626 | 0 | 2026-01-05T13:47:10Z |
| kubeflow/pipelines | Python | 4133 | 1988 | 488 | 2026-05-05 |
| kubeflow/pipelines | Python | 4119 | 1984 | 469 | 2026-04-10T23:07:19Z |
| kubeflow/pipelines | Python | 4119 | 1985 | 471 | 2026-04-14T01:20:50Z |
| kubeflow/spark-operator | Python | 3123 | 1482 | 87 | 2026-05-05 |
| kubeflow/spark-operator | Python | 3114 | 1483 | 86 | 2026-04-13T18:28:43Z |
| kubeflow/spark-operator | Python | 3111 | 1483 | 85 | 2026-04-10T18:21:12Z |
| kubeflow/trainer | Go | 2096 | 948 | 124 | 2026-05-06 |
| kubeflow/trainer | Go | 2082 | 945 | 151 | 2026-04-13T23:41:09Z |
| kubeflow/trainer | Go | 2080 | 944 | 145 | 2026-04-10T13:35:59Z |
| kubeflow/katib | Python | 1683 | 522 | 122 | 2026-04-14 |
| kubeflow/katib | Python | 1678 | 521 | 121 | 2026-04-14T01:21:37Z |
| kubeflow/katib | Python | 1676 | 521 | 118 | 2026-04-02T07:08:12Z |

### Org/User Breakdown

| Source | Repos Snapshotted | Total Stars |
|--------|------------------|-------------|
| kubeflow | 114 | 98400 |
| migalkin | 60 | 554 |
| bmorphism | 217 | 357 |
| AustinCStone | 86 | 216 |
| plurigrid | 230 | 109 |
| zubyul | 62 | 27 |
| TeglonLabs | 110 | 14 |
| DJedamski | 22 | 14 |
| wasita | 60 | 6 |
| kristinezheng | 36 | 0 |
| M1shaaa | 32 | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~5,157,387,313.  
This indicates accounts have not yet received APT (CoinStore resource not initialized).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| A | `0x8699edc0960dd5b916...` | 0.00000000 |
| B | `0x3f892ebe6e45164e63...` | 0.00000000 |
| C | `0x38b99e63ada9b6fef1...` | 0.00000000 |
| D | `0xf77656248f64d5dd00...` | 0.00000000 |
| E | `0xdc1d9d533bac3507f9...` | 0.00000000 |
| F | `0x18a14b5b4bec118c1c...` | 0.00000000 |
| G | `0x69a394c0b0ac842127...` | 0.00000000 |
| H | `0xce67c327a7844e5488...` | 0.00000000 |
| I | `0x070fe5d74e4eda30e2...` | 0.00000000 |
| J | `0x4d964db8f538374034...` | 0.00000000 |
| K | `0xa732040a6b0d559041...` | 0.00000000 |
| L | `0x7c2eaeafad9725492e...` | 0.00000000 |
| M | `0x6fed37a7553ef16b2a...` | 0.00000000 |
| N | `0xe7dde6da0a65f51062...` | 0.00000000 |
| O | `0x73252b6011a75115a2...` | 0.00000000 |
| P | `0x6218792de4a9bc3891...` | 0.00000000 |
| Q | `0xac40fa50b81b4ca6b1...` | 0.00000000 |
| R | `0x7ce605cc8fda4f8e4a...` | 0.00000000 |
| S | `0xb8753014e4888ea48a...` | 0.00000000 |
| T | `0x35781dc0e42fef3f25...` | 0.00000000 |
| U | `0x75860da47565f6509b...` | 0.00000000 |
| V | `0xb59dd8170321dfab5a...` | 0.00000000 |
| W | `0x5f32aef70f5ba530d3...` | 0.00000000 |
| X | `0xa95cbbd116548ac990...` | 0.00000000 |
| Y | `0xd8e32848f1dffa811b...` | 0.00000000 |
| Z | `0x7af0ef6e1bd706f4b3...` | 0.00000000 |
| alice | `0xc793acdec12b4a6371...` | 0.00000000 |
| bob | `0x0a3c00c58fdf9020b2...` | 0.00000000 |

### Multisig Contract Probes

All 5 multisig contracts responded successfully via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

Site is a Next.js SPA — no REST/JSON API endpoints discoverable via:
- `GET /api/markets` → returns SPA HTML
- `GET /api/v1/markets` → returns SPA HTML

Market data unavailable without JavaScript execution. `mnx_snapshots` table is empty.

---

## Summary

- **84 repos** snapshotted across 5 sources (plurigrid/30, kubeflow/20, TeglonLabs/4, bmorphism/17, zubyul/13)
- **28 Aptos wallets** probed — all show 0 APT (CoinStore not initialized on mainnet)
- **5 multisig contracts** healthy, all require 2-of-N signatures
- **MNX Markets** unavailable via REST API (SPA)
- GF(3) trit chain balanced: ERGODIC=35 PLUS=37 MINUS=36
