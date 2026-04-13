# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-04-13  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=2)  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 12 |
| kubeflow | org | 9 |
| TeglonLabs | org | 4 |
| bmorphism | user | 6 |
| zubyul | user | 6 |
| migalkin | social (zubyul graph) | 4 |
| DJedamski | social (zubyul graph) | 2 |
| wasita | social (zubyul graph) | 4 |
| kristinezheng | social (zubyul graph) | 2 |
| M1shaaa | social (zubyul graph) | 2 |
| AustinCStone | social (zubyul graph) | 3 |
| **Total** | | **54 repos** |

### Top Repos by Stars

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15,569 | 2,629 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,119 | 1,985 | 2026-04-12 |
| kubeflow/spark-operator | Python | 3,114 | 1,482 | 2026-04-11 |
| kubeflow/trainer | Go | 2,081 | 945 | 2026-04-10 |
| kubeflow/katib | Python | 1,678 | 521 | 2026-04-12 |
| kubeflow/manifests | YAML | 1,010 | 1,069 | 2026-04-11 |
| kubeflow/arena | Go | 808 | 190 | 2026-04-10 |
| kubeflow/mpi-operator | Go | 523 | 236 | 2026-04-08 |
| migalkin/NodePiece | Python | 143 | 21 | 2026-03-02 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| migalkin/StarE | Python | 88 | 16 | 2026-02-22 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 2026-01-16 |

### Active Frontier (pushed 2026-04-12 or later)

| Repo | Description |
|------|-------------|
| plurigrid/nash-portal | NASH token TUI in the browser — ratzilla WASM + GeckoTerminal OHLCV candlesticks |
| plurigrid/gorj | forj + Rama topology nREPL routing + GF(3) gay trit coloring |
| plurigrid/asi | everything is topological chemputer! |
| zubyul/nash-tui | NASH token TUI: real-time candles via GeckoTerminal |
| zubyul/nash-web | NASH token browser TUI via ratzilla WASM |
| wasita/wasita.github.io | personal website (Svelte) |
| kubeflow/pipelines | Machine Learning Pipelines for Kubeflow |
| kubeflow/katib | Automated Machine Learning on Kubernetes |

### GF(3) Color Distribution (world_increments)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 18 |
| 1 | PLUS | #b8bb26 | 18 |
| 2 | MINUS | #cc241d | 18 |

54 world_increments minted, balanced across all three GF(3) trits.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (coin::balance view function)

**Total swarm APT: 20.344773 APT**

| World | Address (short) | Balance (APT) |
|-------|-----------------|---------------|
| bob | 0x0a3c...512d | **12.657007** |
| F | 0x18a1...cf71 | **1.960516** |
| L | 0x7c2e...ba9 | **1.927269** |
| J | 0x4d96...f54 | **1.895093** |
| alice | 0xc793...cc7b | 0.436434 |
| O | 0x7325...89d | 0.210136 |
| K | 0xa732...dc4 | 0.161961 |
| P | 0x6218...948 | 0.140136 |
| M | 0x6fed...2e9 | 0.112285 |
| N | 0xe7dd...b2c | 0.106121 |
| Q | 0xac40...89a | 0.103240 |
| S | 0xb875...386 | 0.091788 |
| R | 0x7ce6...e10 | 0.090217 |
| T | 0x3578...588 | 0.073713 |
| U | 0x7586...956 | 0.055773 |
| A | 0x8699...97a | 0.051767 |
| V | 0xb59d...2c3 | 0.048833 |
| Y | 0xd8e3...4c4 | 0.044449 |
| X | 0xa95c...47d | 0.042577 |
| W | 0x5f32...7b0 | 0.040705 |
| B | 0x3f89...b13 | 0.036256 |
| Z | 0x7af0...97c | 0.024268 |
| D | 0xf776...dd1 | 0.011629 |
| C | 0x38b9...35e | 0.010185 |
| E | 0xdc1d...d36 | 0.009372 |
| H | 0xce67...00f | 0.001681 |
| G | 0x69a3...f32 | 0.000681 |
| I | 0x070f...fc9 | 0.000681 |

Note: `0x1::coin::CoinStore` legacy resource not initialized on these addresses; balances retrieved via `0x1::coin::balance` view function.

### Multisig Contract Probes (num_signatures_required)

All 5 multisig contracts healthy — 2-of-N threshold confirmed on all pairs.

| Pair | Address (short) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | healthy |
| A-G | 0xf56c...096 | 2 | healthy |
| Y-Z | 0xd3ff...883 | 2 | healthy |
| S-T | 0x3b1c...883 | 2 | healthy |
| V-W | 0x40fa...6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi — The AI Exchange)

Extracted from Next.js SPA preloaded HTML payload. Full market list (40+ assets) requires wallet connection; 7 assets captured from static preload.

| Ticker | Name | Category | Price | 24h Change |
|--------|------|----------|-------|------------|
| AMZN | Amazon | Stocks | $235.51 | -1.36% |
| NVDA | NVIDIA | Stocks | $186.50 | -1.06% |
| OAI26 | OpenAI Final 2026 Valuation | Valuations | $530B | +0.19% |
| ANT26 | Anthropic Final 2026 Valuation | Valuations | $416B | -0.48% |
| USO | United States Oil Fund | Commodities | $133.89 | +7.19% |
| DPREZ | Democrat Elected President 2028 | Politics | 50% | +1.61% |
| INVADE27 | China invades Taiwan by 2027 | Politics | 17% | +5.59% |

---

## DuckDB Schema Summary

```
world_increments   -- 54 rows: one per repo snapshot, GF(3)-colored
repo_snapshots     -- 54 rows: GitHub repo metadata (stars, forks, language, pushed_at)
aptos_snapshots    -- 28 rows: Hamming swarm APT balances (alice, bob, A-Z)
multisig_probes    -- 5 rows: multisig sig thresholds
mnx_snapshots      -- 7 rows: MNX market tickers
```

```sql
-- Top repos by stars
SELECT full_name, language, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- Swarm APT leaderboard
SELECT world, balance_apt FROM aptos_snapshots ORDER BY balance_apt DESC;

-- GF(3) color balance
SELECT gf3_name, gf3_color, count(*) FROM world_increments GROUP BY gf3_name, gf3_color;

-- Active multisigs
SELECT pair, sigs_required FROM multisig_probes WHERE healthy = true;
```
