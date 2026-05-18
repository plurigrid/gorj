# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-05-18  
**Branch:** world-increment/sweep-2026-05-18-2110  
**GF(3) Increment:** id=25, trit=1 PLUS `#b8bb26`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 10 |
| kubeflow | org | 10 |
| TeglonLabs | org | 4 |
| bmorphism | user | 10 |
| zubyul | user | 10 |
| migalkin | user (zubyul graph) | 8 |
| DJedamski | user (zubyul graph) | 6 |
| wasita | user (zubyul graph) | 8 |
| kristinezheng | user (zubyul graph) | 6 |
| M1shaaa | user (zubyul graph) | 5 |
| AustinCStone | user (zubyul graph) | 8 |
| **Total** | | **85 new / 1114 cumulative** |

### Top Repos by Stars (this sweep)
| Repo | Stars | Forks | Language |
|------|-------|-------|----------|
| kubeflow/pipelines | 4140 | 1993 | Python |
| kubeflow/spark-operator | 3126 | 1482 | Python |
| kubeflow/trainer | 2100 | 950 | Go |
| kubeflow/manifests | 1017 | 1064 | YAML |
| kubeflow/kale | 687 | 156 | Python |
| migalkin/NodePiece | 144 | 21 | Python |
| migalkin/StarE | 89 | 16 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml |
| plurigrid/asi | 23 | 5 | HTML |

### Active Signal (pushed today 2026-05-18)
- `plurigrid/gorj` — Clojure, 246 open issues (hot)
- `kubeflow/hub` — Go, model registry
- `kubeflow/pipelines` — Python ML pipelines
- `bmorphism/Gay.jl` — Julia, 189 open issues
- `wasita/wasita.github.io` — Svelte personal site
- `M1shaaa/M1shaaa` — profile config update

### GF(3) Chain — Increment 25
`id=25 → 25%3=1 → trit=1 PLUS #b8bb26`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)
All 28 Hamming swarm addresses (alice, bob, A–Z) queried against
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All accounts returned `resource_not_found` — no APT balances detected.  
Total APT across swarm: **0.00 APT**

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (5 pairs)
All 5 multisig accounts healthy — each requires **2-of-2 signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi) — 32 markets extracted

**Status:** `ok` — data extracted from Next.js RSC payload (REST `/api/markets` 404; homepage embeds full market state)

#### AI Benchmark Futures
| Ticker | Name | Price | 24h Chg |
|--------|------|-------|---------|
| ECI26 | Epoch Capabilities Index Max 2026 | 169.0 | -1.17% |
| ARC26 | Arc AGI 2 Highest 2026 Score | 0.59 | 0.00% |
| FMATH26 | FrontierMath Highest 2026 Score | 0.46 | **-6.12%** |

#### Valuation Futures
| Ticker | Name | Price | 24h Chg |
|--------|------|-------|---------|
| ANT26 | Anthropic Final 2026 Valuation | $426B | +0.95% |
| OAI26 | OpenAI Final 2026 Valuation | $524B | +0.38% |
| OAITOP26 | OpenAI Produces Top AI Model 2026 | 0.23 | 0.00% |

#### Compute
| Ticker | Name | Price | 24h Chg |
|--------|------|-------|---------|
| H100 | H100 Spot Rental Price Index | $2.824/hr | 0.00% |

#### Notable Equities & Commodities
| Ticker | Price | 24h Chg |
|--------|-------|---------|
| GOLD | $4,565.05 | +0.58% |
| SPX | 7,399 | -0.05% |
| NVDA | $222.48 | -0.99% |
| TSLA | $410.18 | -2.07% |
| MU | $680.75 | **-4.84%** |
| CRWV | $103.71 | -3.03% |

#### Political
| Ticker | Name | Price | 24h Chg |
|--------|------|-------|---------|
| DPREZ | Democrat Elected President 2028 | 0.506 | **+3.69%** |
| INVADE27 | China invades Taiwan before 2028 | 0.162 | -4.14% |

---

## DuckDB State (`world-increments.duckdb`)
| Table | Rows |
|-------|------|
| world_increments | 25 |
| repo_snapshots | 1114 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 32 |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
