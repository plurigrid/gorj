# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-05-30T19:13:11Z
**Database:** `world-increments.duckdb` (DuckDB v1.5.3)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted
| Source | Type | Repos |
|---|---|---|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 6 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 40 |
| **TOTAL** | | **391** |

### GF(3) Color Chain Distribution
| Name | Color | Count |
|---|---|---|
| ERGODIC | #d3869b | 130 |
| PLUS | #b8bb26 | 131 |
| MINUS | #cc241d | 130 |

### Top Repos by Stars (Top 20)
```

```

### Language Breakdown (Top 15)
```
language,cnt
Python,81
Rust,26
JavaScript,25
TypeScript,23
Go,15
HTML,15
Jupyter Notebook,14
Clojure,14
Julia,9
Zig,7
Jsonnet,7
Java,6
Svelte,6
R,6
TeX,5
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (APT on Mainnet)
All 28 addresses returned **0.0 APT** — wallets are unfunded or not initialized on Aptos mainnet CoinStore.

| World | Address (truncated) | APT Balance |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | 0x86..–0x7af... | 0.0 each |

### Multisig Contract Probes (Aptos Mainnet)
All 5 contracts are healthy, requiring **2-of-N signatures**:

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi — 32 markets live)
**Top 15 by Price:**
```
ticker,name,category,price,chg_pct
SPX,S&P 500 Index,Financial,7569.0,-0.053
GOLD,Gold Spot,Commodities,4537.28,-0.21
ASML,ASML Holding,Stocks,1614.22,0.346
MU,Micron Technology,Stocks,963.57,1.115
META,Meta (Facebook),Stocks,633.02,0.968
OAI26,OpenAI Final 2026 Valuation,Valuations,525.0,-1.13
MSFT,Microsoft,Stocks,449.66,1.423
TSLA,Tesla Inc,Stocks,434.93,-0.644
ANT26,Anthropic Final 2026 Valuation,Valuations,422.0,0.238
TSM,Taiwan Semiconductor,Stocks,418.75,0.146
GOOGL,Alphabet (Google),Stocks,380.41,-0.565
SFHOME26,S&P CoreLogic Case-Shiller CA-San Francisco Home Price Index 2026 Year-End,Financial,380.2,10.299
AAPL,Apple,Stocks,310.93,0.443
AMZN,Amazon,Stocks,270.32,-0.151
NVDA,NVIDIA,Stocks,212.62,-1.692
```

**Notable prediction markets:**
- `FMATH26` — FrontierMath Highest 2026 Score: **0.49** (49%)
- `INVADE27` — China invades Taiwan before end of 2027: **0.162** (16.2%)
- `DPREZ` — Democrat elected President in 2028: **0.506** (50.6%)
- `OAI26` — OpenAI Final 2026 Valuation: **$525B**
- `ANT26` — Anthropic Final 2026 Valuation: **$422B**

---

## DuckDB Schema
```sql
world_increments   (391 rows) — GF(3)-colored increment ledger
repo_snapshots     (391 rows) — GitHub repo metadata
aptos_snapshots    (28 rows)  — Aptos wallet APT balances
multisig_probes    (5 rows)   — Aptos multisig contract health
mnx_snapshots      (32 rows)  — MNX prediction market prices
```
