# LATEST_SWEEP — World-Increment + Hamming Swarm Snapshot

**Sweep date:** 2026-04-12  
**Branch:** world-increment/sweep-2026-04-12  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 98 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 99 |
| zubyul | user | 45 |
| migalkin | user (zubyul social graph) | 19 |
| DJedamski | user (zubyul social graph) | 6 |
| wasita | user (zubyul social graph) | 10 |
| kristinezheng | user (zubyul social graph) | 6 |
| M1shaaa | user (zubyul social graph) | 8 |
| AustinCStone | user (zubyul social graph) | 40 |

### DuckDB — repo_snapshots (50 representative rows inserted)

**GF(3) color chain:**
- trit=0 ERGODIC `#d3869b` — id % 3 == 0
- trit=1 PLUS `#b8bb26` — id % 3 == 1
- trit=-1 MINUS `#cc241d` — id % 3 == 2

**Top repos by stars:**

| full_name | lang | stars | forks | issues | pushed |
|-----------|------|-------|-------|--------|--------|
| kubeflow/kubeflow | — | 15568 | 2629 | 0 | 2026-01-05 |
| kubeflow/pipelines | Python | 4119 | 1985 | 465 | 2026-04-12 |
| kubeflow/spark-operator | Python | 3112 | 1482 | 82 | 2026-04-11 |
| kubeflow/trainer | Go | 2080 | 945 | 147 | 2026-04-10 |
| kubeflow/examples | Jsonnet | 1459 | 756 | 111 | 2025-04-14 |
| kubeflow/katib | Python | 1677 | 521 | 119 | 2026-04-12 |
| migalkin/NodePiece | Python | 143 | 21 | 0 | 2026-03-02 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2 | 0 | 2026-03-28 |
| migalkin/StarE | Python | 88 | 16 | 1 | 2026-02-22 |
| AustinCStone/TextGAN | Python | 92 | 30 | 5 | 2025-03-03 |
| bmorphism/say-mcp-server | JavaScript | 20 | 8 | 2 | 2026-03-19 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 1 | 2026-02-05 |
| plurigrid/gorj | Clojure | 0 | 0 | 163 | 2026-04-12 |

**Most active (pushed today 2026-04-12):**
- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) coloring
- `kubeflow/pipelines` — ML Pipelines
- `bmorphism/penrose-mcp` — Penrose server for Infinity-Topos
- `wasita/wasita.github.io` — personal site

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets, mainnet)

Queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**All 28 wallets returned 0 APT balance.** The hamming-swarm addresses (alice, bob, A–Z) are not currently funded on Aptos mainnet. These are precomputed addresses tracked for future activity.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | 0x8699...–0x7af0... | 0.0 each |

### Multisig Probes (5 pairs)

All 5 multisig accounts responded **healthy** with `num_signatures_required = 2`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All multisig accounts require 2-of-N signatures — standard hamming pair configuration.

### MNX Markets (testnet.mnx.fi — "The AI Exchange")

Successfully fetched 19 market tickers.

**AI/Tech Valuations:**

| Ticker | Name | Price/Value | Change |
|--------|------|-------------|--------|
| OAI26 | OpenAI 2026 | $529B | -0.38% |
| ANT26 | Anthropic 2026 | $420B | +0.48% |
| ARC26 | Arc AGI 2 Score | 59% | +3.51% |
| ECI26 | Epoch Capabilities Index | 171 | +3.01% |

**Compute:**

| Ticker | Name | Price | Change |
|--------|------|-------|--------|
| H100 | GPU Rental Index | $2.81 | -0.46% |
| CRWV | CoreWeave | $103.11 | +0.19% |

**Stocks (spot):**

| Ticker | Price | Change |
|--------|-------|--------|
| NVDA | $188.49 | -0.01% |
| MSFT | $371.92 | -0.07% |
| GOOGL | $318.07 | -0.01% |
| TSLA | $351.53 | -0.06% |
| META | $629.96 | -0.18% |
| AAPL | $260.67 | — |
| AMZN | $238.61 | — |

**Commodities:**

| Ticker | Price | Change |
|--------|-------|--------|
| GOLD | $4,700 | +0.00% |
| SILVER | $76.04 | -0.07% |
| URA (Uranium) | $50.89 | -0.02% |
| USO (Oil) | $124.91 | -0.06% |

**Political:**

| Ticker | Name | Probability | Change |
|--------|------|-------------|--------|
| DPREZ | Democrat 2028 | 51% | -1.74% |
| INVADE27 | China-Taiwan 2027 | 17% | +3.13% |

---

## DuckDB Summary

```
Tables:
  world_increments  — 50 rows (GitHub repo events, GF3 color-chained)
  repo_snapshots    — 50 rows (11 orgs/users, 2026-04-12 snapshot)
  aptos_snapshots   — 28 rows (alice, bob, A–Z wallets)
  multisig_probes   —  5 rows (A-B, A-G, Y-Z, S-T, V-W pairs)
  mnx_snapshots     — 19 rows (AI/tech/stocks/commodities/political)
```

**Notable signals:**
- `plurigrid/gorj` has 163 open issues — most active repo in sweep
- All Hamming swarm wallets (A–Z) have 0 APT — swarm unfunded on mainnet
- All 5 multisig pairs healthy, 2-of-N threshold uniform across swarm
- ANT26 (Anthropic) trending up +0.48%, OAI26 trending down -0.38%
- Arc AGI 2 score at 59%, up +3.51% — AGI progress signal
- INVADE27 (China-Taiwan) at 17%, up +3.13% — geopolitical risk ticking up
