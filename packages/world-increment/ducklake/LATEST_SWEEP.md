# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-04-11  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.1 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Database Counts

| Table | Rows |
|---|---|
| world_increments | 11 |
| repo_snapshots | 471 |

### Sources Snapshotted

| Source | Type | Repos | Total Stars | GF(3) Trit | Color |
|---|---|---|---|---|---|
| plurigrid | org | 100 | 40 | PLUS (1) | `#b8bb26` |
| kubeflow | org | 47 | 33,851 | MINUS (-1) | `#cc241d` |
| TeglonLabs | org | 53 | 6 | ERGODIC (0) | `#d3869b` |
| bmorphism | user | 100 | 131 | PLUS (1) | `#b8bb26` |
| zubyul | user | 24 | 13 | MINUS (-1) | `#cc241d` |
| migalkin | social | 30 | 277 | ERGODIC (0) | `#d3869b` |
| DJedamski | social | 11 | 7 | PLUS (1) | `#b8bb26` |
| wasita | social | 29 | 3 | MINUS (-1) | `#cc241d` |
| kristinezheng | social | 18 | 0 | ERGODIC (0) | `#d3869b` |
| M1shaaa | social | 16 | 0 | PLUS (1) | `#b8bb26` |
| AustinCStone | social | 43 | 108 | MINUS (-1) | `#cc241d` |

### GF(3) Color Chain Assignment

- **id%3==0** → trit=0, ERGODIC `#d3869b` (rose)
- **id%3==1** → trit=1, PLUS `#b8bb26` (yellow-green)
- **id%3==2** → trit=-1, MINUS `#cc241d` (red)

Balance: PLUS(4) + MINUS(4) + ERGODIC(3) = 11 increments

### Notable Repos (by stars)

| Repo | Stars | Language | Pushed |
|---|---|---|---|
| kubeflow/pipelines | 4,119 | Python | 2026-04-11 |
| kubeflow/spark-operator | 3,111 | Python | 2026-04-10 |
| kubeflow/trainer | 2,080 | Go | 2026-04-10 |
| kubeflow/katib | 1,676 | Python | 2026-04-02 |
| kubeflow/manifests | 1,010 | YAML | 2026-04-09 |
| migalkin/NodePiece | 143 | Python | 2026-03-02 |
| migalkin/StarE | 88 | Python | 2026-02-22 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| plurigrid/asi | 16 | HTML | 2026-04-10 |
| plurigrid/gorj | 0 | Clojure | 2026-04-11 |

### Most-Active Recently Pushed (plurigrid)

| Repo | Language | Pushed |
|---|---|---|
| plurigrid/gorj | Clojure | 2026-04-11T08:41:09Z |
| plurigrid/horse | TeX | 2026-04-11T07:07:06Z |
| plurigrid/web-browser | Rust | 2026-04-10T02:54:47Z |
| plurigrid/asi | HTML | 2026-04-10T02:37:44Z |
| plurigrid/nanoclj-zig | Zig | 2026-04-09T19:53:30Z |
| plurigrid/asi-skills | Julia | 2026-04-09T19:53:56Z |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at Aptos mainnet
ledger version 4,838,032,150. These wallets have no native APT coinstore
(unfunded or fungible-asset-only accounts). All balances recorded as NULL.

| World | Address | Status |
|---|---|---|
| alice | 0xc793...cc7b | resource_not_found |
| bob | 0x0a3c...512d | resource_not_found |
| A | 0x8699...9d7a | resource_not_found |
| B | 0x3f89...cb13 | resource_not_found |
| C | 0x38b9...535e | resource_not_found |
| D | 0xf776...fdd1 | resource_not_found |
| E | 0xdc1d...8d36 | resource_not_found |
| F | 0x18a1...cf71 | resource_not_found |
| G | 0x69a3...7f32 | resource_not_found |
| H | 0xce67...300f | resource_not_found |
| I | 0x070f...1fc9 | resource_not_found |
| J | 0x4d96...7f54 | resource_not_found |
| K | 0xa732...5dc4 | resource_not_found |
| L | 0x7c2e...eba9 | resource_not_found |
| M | 0x6fed...7f2e | resource_not_found |
| N | 0xe7dd...1b2c | resource_not_found |
| O | 0x7325...a89d | resource_not_found |
| P | 0x6218...c948 | resource_not_found |
| Q | 0xac40...c89a | resource_not_found |
| R | 0x7ce6...6e10 | resource_not_found |
| S | 0xb875...0386 | resource_not_found |
| T | 0x3578...4588 | resource_not_found |
| U | 0x7586...f956 | resource_not_found |
| V | 0xb59d...af2c | resource_not_found |
| W | 0x5f32...c7b0 | resource_not_found |
| X | 0xa95c...047d | resource_not_found |
| Y | 0xd8e3...44c4 | resource_not_found |
| Z | 0x7af0...197c | resource_not_found |

### Multisig Contract Probes (5 pairs, 0x1::multisig_account::num_signatures_required)

All 5 multisig contracts responded with `["2"]` — **2-of-2 required, all healthy.**

| Pair | Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f428...7003 | 2 | YES |
| A-G | 0xf56c4a1c...0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

### MNX Markets — testnet.mnx.fi ("The AI Exchange")

API endpoint `/api/markets` returns 404 (SPA routes to `api.testnet.mnx.fi`).
Market data extracted from rendered page snapshot via WebFetch.

| Ticker | Name | Category | Price | Change |
|---|---|---|---|---|
| NVDA | NVIDIA | Stocks | $188.51 | +2.90% |
| AAPL | Apple | Stocks | $260.65 | +0.42% |
| MSFT | Microsoft | Stocks | $372.18 | -0.78% |
| TSLA | Tesla Inc | Stocks | $351.53 | +1.79% |
| OAI26 | OpenAI Final 2026 Valuation | Valuations | $521B | -2.07% |
| ANT26 | Anthropic Final 2026 Valuation | Valuations | $423B | +1.68% |
| GOLD | Gold Spot | Commodities | $4,700 | -0.14% |
| VIX | CBOE Volatility Index | Financial | 19.23 | -2.34% |

MNX offers 40+ instruments across: Stocks, Valuations, Commodities,
Financial, AI benchmarks (Arc AGI, Frontier Math), Compute (H100 rental),
and Politics (2028 election, Taiwan invasion odds).

---

## Full DuckDB Schema State

```sql
world_increments  -- 11 rows  (GF3 color-chained sweep events, 11 sources)
repo_snapshots    -- 471 rows (GitHub repo metadata, 11 orgs/users)
aptos_snapshots   -- 28 rows  (Hamming swarm: alice, bob, A-Z; all NULL balance)
multisig_probes   --  5 rows  (A-B, A-G, Y-Z, S-T, V-W; all 2-of-2 healthy)
mnx_snapshots     --  8 rows  (MNX testnet tickers: NVDA, AAPL, MSFT, TSLA,
                  --           OAI26, ANT26, GOLD, VIX)
```

---

## GF(3) Assignment Rule

```
id mod 3 == 0  →  trit= 0, color=#d3869b, name=ERGODIC
id mod 3 == 1  →  trit=+1, color=#b8bb26, name=PLUS
id mod 3 == 2  →  trit=-1, color=#cc241d, name=MINUS
```

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent*  
*2026-04-11 — plurigrid/gorj*
