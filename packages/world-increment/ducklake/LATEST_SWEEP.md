# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-04-02

---

## GitHub Repos Snapshot

### Repos by Org/User

| Org/User | Type | Repos |
|---|---|---|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 46 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 23 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| TeglonLabs | org | 0 (404 - unavailable) |

**Total repos captured: 416**

### Top 5 Recently Pushed Repos

| Repo | Pushed At | Stars | Language |
|---|---|---|---|
| plurigrid/gorj | 2026-04-02T10:29:17Z | 0 | Clojure |
| kubeflow/model-registry | 2026-04-02T08:08:02Z | 170 | Go |
| kubeflow/katib | 2026-04-02T07:08:12Z | 1674 | Python |
| kubeflow/dashboard | 2026-04-02T06:30:41Z | 16 | TypeScript |
| kubeflow/pipelines | 2026-04-02T05:55:05Z | 4118 | Python |

---

## GF(3) World Increment Summary

**Total increments:** 416

| Trit | Color | Name | Count |
|---|---|---|---|
| 1 | #b8bb26 | PLUS | 139 |
| 0 | #d3869b | ERGODIC | 138 |
| -1 | #cc241d | MINUS | 139 |

The GF(3) color chain distributes evenly across PLUS / ERGODIC / MINUS triadic states, with 416 total repo snapshot events recorded as world increments.

---

## Aptos Hamming Swarm

All 28 wallets queried against Aptos mainnet (`fullnode.mainnet.aptoslabs.com`). Resource `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` not found for any address — all balances are 0.0 APT.

| Label | Address | Balance (APT) |
|---|---|---|
| alice | 0xc793acdec1... | 0.0 |
| bob | 0x0a3c00c58f... | 0.0 |
| A | 0x8699edc096... | 0.0 |
| B | 0x3f892ebe6e... | 0.0 |
| C | 0x38b99e63ad... | 0.0 |
| D | 0xf77656248f... | 0.0 |
| E | 0xdc1d9d533b... | 0.0 |
| F | 0x18a14b5b4b... | 0.0 |
| G | 0x69a394c0b0... | 0.0 |
| H | 0xce67c327a7... | 0.0 |
| I | 0x070fe5d74e... | 0.0 |
| J | 0x4d964db8f5... | 0.0 |
| K | 0xa732040a6b... | 0.0 |
| L | 0x7c2eaeafad... | 0.0 |
| M | 0x6fed37a755... | 0.0 |
| N | 0xe7dde6da0a... | 0.0 |
| O | 0x73252b6011... | 0.0 |
| P | 0x6218792de4... | 0.0 |
| Q | 0xac40fa50b8... | 0.0 |
| R | 0x7ce605cc8f... | 0.0 |
| S | 0xb8753014e4... | 0.0 |
| T | 0x35781dc0e4... | 0.0 |
| U | 0x75860da475... | 0.0 |
| V | 0xb59dd81703... | 0.0 |
| W | 0x5f32aef70f... | 0.0 |
| X | 0xa95cbbd116... | 0.0 |
| Y | 0xd8e32848f1... | 0.0 |
| Z | 0x7af0ef6e1b... | 0.0 |

---

## Multisig Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`. All returned `["2"]`.

| Pair | Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f428a0... | 2 | true |
| A-G | 0xf56c4a1c09... | 2 | true |
| Y-Z | 0xd3ffe1812b... | 2 | true |
| S-T | 0x3b1c3ae905... | 2 | true |
| V-W | 0x40fad7b423... | 2 | true |

---

## MNX Markets

**Unavailable.** `https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/tickers` return HTML (Next.js app), not JSON. No structured market data accessible via REST API.

---

## Database

**DuckDB path:** `packages/world-increment/ducklake/world-increments.duckdb`

**Tables:**
- `world_increments` — 416 rows (GF(3) color-chained increment events)
- `repo_snapshots` — 416 rows (GitHub repo metadata)
- `aptos_snapshots` — 28 rows (Hamming swarm wallet balances)
- `multisig_probes` — 5 rows (Aptos multisig contract health)
- `mnx_snapshots` — 0 rows (unavailable)

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
