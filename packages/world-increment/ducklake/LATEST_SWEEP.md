# World-Increment Sweep + Hamming Snapshot — 2026-06-02

## Sweep Metadata
- **Date:** 2026-06-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GF(3) Color Chain Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 99 |
| zubyul | user | 48 |
| migalkin | social graph (zubyul) | 19 |
| DJedamski | social graph (zubyul) | 6 |
| wasita | social graph (zubyul) | 11 |
| kristinezheng | social graph (zubyul) | 6 |
| M1shaaa | social graph (zubyul) | 8 |
| AustinCStone | social graph (zubyul) | 40 |
| **TOTAL** | | **391** |

`world_increments`: 391 rows | `repo_snapshots`: 391 rows

### Top 10 Repos by Stars
| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,704 | — | 2026-05-24 |
| kubeflow/pipelines | 4,151 | Python | 2026-06-02 |
| kubeflow/spark-operator | 3,125 | Python | 2026-06-01 |
| kubeflow/trainer | 2,110 | Go | 2026-06-02 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,020 | YAML | 2026-06-02 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |

### Most Active (pushed within 48h of sweep)
- `plurigrid/gorj` — pushed 2026-06-02 (309 open issues — most active)
- `kubeflow/dashboard` — pushed 2026-06-02
- `kubeflow/notebooks` — pushed 2026-06-02
- `kubeflow/pipelines` — pushed 2026-06-02
- `kubeflow/manifests` — pushed 2026-06-02
- `bmorphism/world` — pushed 2026-06-02
- `bmorphism/Gay.jl` — pushed 2026-06-02 (189 open issues)
- `M1shaaa/M1shaaa` — pushed 2026-06-02
- `wasita/wasita.github.io` — pushed 2026-06-01

### Notable Finds
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street oxcaml_effect
- **bmorphism/anti-bullshit-mcp-server**: 23 stars — claim analysis + manipulation detection
- **kubeflow/mcp-apache-spark-history-server**: 173 stars — new MCP for Spark History Server
- **plurigrid/asi**: 24 stars — "everything is topological chemputer!"

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-02)
Query: `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

All 28 wallets (alice, bob, A–Z) returned **0.00 APT**.
Wallets do not have a registered APT CoinStore resource on mainnet — likely use staked/wrapped assets or have not received transfers.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...2d5d | 0.00 |
| A | 0x8699...9d7a | 0.00 |
| B | 0x3f89...b13 | 0.00 |
| C | 0x38b9...35e | 0.00 |
| D | 0xf776...dd1 | 0.00 |
| E | 0xdc1d...d36 | 0.00 |
| F | 0x18a1...f71 | 0.00 |
| G | 0x69a3...f32 | 0.00 |
| H | 0xce67...00f | 0.00 |
| I–Z (18) | various | 0.00 each |

### Multisig Contract Probes
Function: `0x1::multisig_account::num_signatures_required`

All 5 multisig contracts are **healthy** with threshold = **2**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi — 32 markets)
Fetched 2026-06-02. Market data from the MNX SPA.

| Ticker | Name | Category | Price | Δ% |
|--------|------|----------|-------|----|
| OAI26 | OpenAI Final 2026 Valuation | AI | $530B | +0.76% |
| ANT26 | Anthropic Final 2026 Valuation | AI | $417B | -1.18% |
| TSLA | Tesla Inc | Stocks | $422.43 | +1.30% |
| INTC | Intel | Compute | $107.55 | -1.72% |
| AMZN | Amazon | Stocks | $257.26 | -1.53% |
| MU | Micron Technology | Compute | $1,100 | +3.92% |
| H100 | SemiAnalysis H100 Spot Rental Index | Commodities | $2.96 | +0.34% |
| CPER | US Copper Index Fund | Commodities | $40.61 | +1.68% |
| CPI26 | US CPI Annual Inflation 2026 | Valuations | 3% | +1.41% |
| VIX | CBOE Volatility Index | Valuations | 15.82 | -1.31% |
| DPREZ | Democrat Elected President 2028 | Politics | 50% | -0.80% |
| SILVER | Silver Spot | Commodities | $75.25 | +0.40% |
| MSFT | Microsoft | Stocks | $442.45 | -3.91% |
| TSM | Taiwan Semiconductor | Compute | $446.09 | +2.13% |
| NVDA | NVIDIA | Stocks | $222.21 | -0.39% |
| GOLD | Gold Spot | Commodities | $4,500 | +0.09% |
| SFHOME26 | SF Home Price Index 2026 | Valuations | 346.2 | -0.12% |
| URA | Global X Uranium ETF | Commodities | $53.27 | +5.26% |
| GOOGL | Alphabet (Google) | Stocks | $361.62 | -4.16% |
| SPX | S&P 500 Index | Stocks | 7,605 | +0.18% |
| CRWV | CoreWeave | Compute | $119.35 | -3.85% |
| ASML | ASML Holding | Compute | $1,700 | +4.55% |
| META | Meta (Facebook) | Stocks | $600.99 | -0.26% |
| AAPL | Apple | Stocks | $314.19 | +2.66% |
| IEF | iShares 7-10yr Treasury | Financial | $94.35 | +0.08% |
| USO | US Oil Fund | Commodities | $137.57 | +1.34% |
| ECI26 | Epoch Capabilities Index 2026 | AI | 167 | -1.18% |
| ARC26 | Arc AGI 2 Highest 2026 Score | AI | 60% | +7.14% |
| TLT | iShares 20+yr Treasury | Financial | $85.54 | +0.32% |
| FMATH26 | FrontierMath Highest 2026 Score | AI | 46% | -6.12% |
| INVADE27 | China invades Taiwan before 2027 | Politics | 17% | +5.73% |
| OAITOP26 | OpenAI Top AI Model in 2026 | AI | 22% | — |

**Top 5 gainers:** ARC26 +7.14% | INVADE27 +5.73% | URA +5.26% | ASML +4.55% | MU +3.92%  
**Top 5 losers:** FMATH26 -6.12% | GOOGL -4.16% | MSFT -3.91% | CRWV -3.85% | INTC -1.72%

---

## DuckDB Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
