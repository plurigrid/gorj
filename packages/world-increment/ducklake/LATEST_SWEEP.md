# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-05-02  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 10 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |
| **TOTAL** | | **438** |

> Note: kubeflow was rate-limited on direct REST API, fetched via MCP search. This sweep adds to existing DB (prior total: 944 repo_snapshots → new total: 1382).

### Top Languages (This Sweep)
| Language | Repos |
|----------|-------|
| Python | 46 |
| Java | 6 |
| C | 6 |
| JavaScript | 4 |
| Matlab | 4 |
| Haskell | 2 |
| TeX | 2 |

### Top Starred Repos (This Sweep)
| Repo | Owner | Stars | Language |
|------|-------|-------|----------|
| TextGAN | AustinCStone | 92 | Python |
| StereoVisionMRF | AustinCStone | 11 | Python |
| SpectralClustering | AustinCStone | 3 | Python |
| StructureFromMotion | AustinCStone | 1 | Python |

### GF(3) Color Chain
- id%3==0 → trit=0 **ERGODIC** `#d3869b`
- id%3==1 → trit=1 **PLUS** `#b8bb26`
- id%3==2 → trit=-1 **MINUS** `#cc241d`

### Recent Events (bmorphism + zubyul)
- bmorphism: 30 recent public events captured
- zubyul: 30 recent public events captured

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
Queried 28 addresses (alice, bob, A–Z) via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793...4cc7b | 0 |
| bob | 0x0a3c...512d5d | 0 |
| A | 0x8699...9d7a | 0 |
| B | 0x3f89...cb13 | 0 |
| C | 0x38b9...535e | 0 |
| D | 0xf776...fdd1 | 0 |
| E | 0xdc1d...d36 | 0 |
| F | 0x18a1...f71 | 0 |
| G | 0x69a3...7f32 | 0 |
| H | 0xce67...00f | 0 |
| I | 0x070f...c9 | 0 |
| J | 0x4d96...f54 | 0 |
| K | 0xa732...dc4 | 0 |
| L | 0x7c2e...ba9 | 0 |
| M | 0x6fed...2e9 | 0 |
| N | 0xe7dd...b2c | 0 |
| O | 0x7325...89d | 0 |
| P | 0x6218...948 | 0 |
| Q | 0xac40...89a9 | 0 |
| R | 0x7ce6...e10 | 0 |
| S | 0xb875...386 | 0 |
| T | 0x3578...588 | 0 |
| U | 0x7586...956 | 0 |
| V | 0xb59d...2c3 | 0 |
| W | 0x5f32...7b0 | 0 |
| X | 0xa95c...47d | 0 |
| Y | 0xd8e3...4c4 | 0 |
| Z | 0x7af0...97c | 0 |

All 28 addresses report 0 APT balance (accounts have no APT coin store registered on mainnet).

### Multisig Contract Probes
All 5 probed contracts are **healthy** (respond to `num_signatures_required`).

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...003 | 2 | yes |
| A-G | 0xf56c...096 | 2 | yes |
| Y-Z | 0xd3ff...883 | 2 | yes |
| S-T | 0x3b1c...883 | 2 | yes |
| V-W | 0x40fa...b6d | 2 | yes |

All multisig accounts require **2-of-N signatures**. Consistent quorum structure across all observed pairs.

### MNX Markets Snapshot (testnet.mnx.fi)
Data extracted from SPA. No public REST API found at `/api/markets`.

| Ticker | Name | Category | Price | Change % |
|--------|------|----------|-------|---------|
| OAI26 | OpenAI 2026 | AI_valuation | 532B | +0.57% |
| ANT26 | Anthropic 2026 | AI_valuation | 418B | -0.48% |
| ARC26 | Arc AGI 2 | AI_benchmark | 60% | +5.26% |
| NVDA | NVIDIA | semiconductor | 198.39 | -0.94% |
| MSFT | Microsoft | tech_stock | 412.70 | +1.11% |
| AAPL | Apple | tech_stock | 279.89 | +1.28% |
| META | Meta | tech_stock | 608.36 | -0.71% |
| TSLA | Tesla | tech_stock | 391.87 | +2.62% |
| GOOGL | Alphabet | tech_stock | 384.83 | -0.24% |
| AMZN | Amazon | tech_stock | 268.01 | +1.63% |
| INTC | Intel | semiconductor | 100.91 | +7.80% |
| MU | Micron | semiconductor | 539.55 | +6.91% |
| TSM | Taiwan Semi | semiconductor | 397.96 | +0.87% |
| ASML | ASML | semiconductor | 1400.0 | -0.49% |
| CRWV | CoreWeave | semiconductor | 119.34 | +7.03% |
| GOLD | Gold | commodity | 4600.0 | -0.32% |
| SILVER | Silver | commodity | 75.45 | +1.49% |
| USO | Oil | commodity | 143.00 | -2.85% |
| SPX | S&P 500 | index | 7226.0 | +0.36% |
| VIX | VIX | index | 17.02 | +0.77% |
| DPREZ | 2028 Democrat | prediction | 51.0 | -0.39% |
| INVADE27 | Taiwan invasion | prediction | 16.0 | +0.63% |

---

## DB Summary
| Table | Row Count |
|-------|-----------|
| world_increments | 24 |
| repo_snapshots | 1382 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 22 |
