# World-Increment Sweep + Hamming Snapshot

**Generated:** 2026-05-31  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| bmorphism | user | 100 |
| plurigrid | org | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user (zubyul social) | 8 |
| DJedamski | user (zubyul social) | 6 |
| kristinezheng | user (zubyul social) | 6 |
| TeglonLabs | org | 4 |

**Total unique repos:** 391

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 130 |
| 1 | `#b8bb26` | PLUS | 131 |
| -1 | `#cc241d` | MINUS | 130 |

### Top Languages

| Language | Repos |
|----------|-------|
| Python | 81 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| Go | 15 |
| HTML | 15 |
| Clojure | 14 |
| Jupyter Notebook | 14 |
| Julia | 9 |
| Jsonnet | 7 |

### Most Starred Repos

| Repo | Stars | Forks | Last Push |
|------|-------|-------|-----------|
| kubeflow/kubeflow | 15,693 | 2,665 | 2026-05-24 |
| kubeflow/pipelines | 4,149 | 2,002 | 2026-05-30 |
| kubeflow/spark-operator | 3,124 | 1,488 | 2026-05-29 |
| kubeflow/trainer | 2,107 | 963 | 2026-05-30 |
| kubeflow/katib | 1,685 | 524 | 2026-05-29 |
| kubeflow/examples | 1,463 | 755 | 2025-04-14 |
| kubeflow/manifests | 1,019 | 1,064 | 2026-05-29 |
| kubeflow/arena | 811 | 191 | 2026-05-07 |
| kubeflow/kale | 691 | 155 | 2026-05-29 |
| kubeflow/mpi-operator | 528 | 235 | 2026-05-29 |

**Repos active in 2026:** 106 (pushed_at >= 2026-01-01)

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A-Z) returned HTTP 404 on the
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource endpoint --
these accounts have no registered APT coin store on mainnet at time of query.

**Balance recorded:** 0.000 APT for all 28 worlds  
**Snapshot timestamp:** 2026-05-31

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | YES |
| A-G | 0xf56c4a1c... | 2 | YES |
| Y-Z | 0xd3ffe181... | 2 | YES |
| S-T | 0x3b1c3ae9... | 2 | YES |
| V-W | 0x40fad7b4... | 2 | YES |

All 5 multisig contracts healthy -- 2-of-N threshold confirmed.

### MNX Markets (testnet.mnx.fi)

API endpoint /api/markets returned 404. SPA fetched directly:

| Ticker | Name | Category | Price |
|--------|------|----------|-------|
| NVDA | NVIDIA | Stocks | $212.75 |
| MSFT | Microsoft | Stocks | $449.70 |
| TSLA | Tesla | Stocks | $434.93 |
| AMZN | Amazon | Stocks | $270.30 |
| SPX | S&P 500 | Indices | $7,575 |
| GOLD | Gold | Commodities | $4,500 |
| USO | Oil ETF | Commodities | $129.17 |
| CPER | Copper ETF | Commodities | $38.92 |
| OPENAI-2026 | OpenAI 2026 Valuation | AI | $523B |
| ANTHROPIC | Anthropic Valuation | AI | $425B |
| DEM2028 | Democrat 2028 Win | Politics | 49% |
| TAIWAN | Taiwan Invasion Probability | Politics | 16% |

---

## DuckDB Schema

```
world_increments  (391 rows)  -- GF3 color-chained repo events
repo_snapshots    (391 rows)  -- full repo metadata
aptos_snapshots   ( 28 rows)  -- hamming swarm wallet balances
multisig_probes   (  5 rows)  -- 2-of-N contract health
mnx_snapshots     ( 12 rows)  -- prediction market prices
```

GF(3) color encoding: id%3==0 => trit=0 ERGODIC #d3869b (pink),
id%3==1 => trit=1 PLUS #b8bb26 (green), id%3==2 => trit=-1 MINUS #cc241d (red).
