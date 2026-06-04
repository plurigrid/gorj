# World-Increment Sweep + Hamming Snapshot

**Date:** 2026-06-04  
**GF(3) Color Chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted | Total Stars |
|--------|------|-------------------|-------------|
| kubeflow | org | 114 (20 sampled) | 100,941 |
| migalkin | user (zubyul graph) | 65 | 830 |
| bmorphism | user | 212 | 442 |
| AustinCStone | user (zubyul graph) | 89 | 319 |
| plurigrid | org | 220 | 129 |
| zubyul | user | 54 | 27 |
| DJedamski | user (zubyul graph) | 25 | 16 |
| TeglonLabs | org | 110 | 14 |
| wasita | user (zubyul graph) | 65 | 10 |
| kristinezheng | user (zubyul graph) | 39 | 0 |
| M1shaaa | user (zubyul graph) | 34 | 0 |

**Total repo_snapshots rows: 1,027**

### Top Repos by Stars

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,705 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-04 |
| kubeflow/spark-operator | 3,124 | Python | 2026-06-04 |
| kubeflow/trainer | 2,111 | Go | 2026-06-04 |
| kubeflow/katib | 1,684 | Python | 2026-06-04 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |

### Plurigrid Highlights

- **gorj** (this repo): 355 open issues, Clojure, pushed 2026-06-04
- **asi**: 25 stars — "everything is topological chemputer!"
- **nanoclj-zig**: NaN-boxed Clojure interpreter in Zig 0.15 with GF(3) trit conservation
- **nash-portal**: NASH token TUI in browser via ratzilla WASM

### Notable bmorphism Activity (as of 2026-06-04)

- **world** (pushed 2026-06-02): Local worlds launcher for SA3, jank, and world proofs
- **Gay.jl** (189 open issues): Wide-gamut color sampling with splittable determinism
- **ocaml-mcp-sdk** (61 stars): OCaml SDK for MCP using Jane Street's oxcaml_effect

### World Increments GF(3) Distribution

| GF3 Color | Name | Trit | Count |
|-----------|------|------|-------|
| #d3869b | ERGODIC | 0 | 12 |
| #b8bb26 | PLUS | +1 | 13 |
| #cc241d | MINUS | -1 | 12 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-04)

All 28 addresses (alice, bob, A-Z) queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All wallets returned 0.0 APT** — addresses exist on-chain but hold no APT in the CoinStore resource at time of snapshot.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A-Z (26) | various | 0.0 each |

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | YES |
| A-G | 0xf56c4a... | 2 | YES |
| Y-Z | 0xd3ffe1... | 2 | YES |
| S-T | 0x3b1c3a... | 2 | YES |
| V-W | 0x40fad7... | 2 | YES |

**All 5 multisigs respond healthy with 2-of-2 signature requirement.**

### MNX Testnet Markets (testnet.mnx.fi)

Snapshot from SPA initial data load (2026-06-04):

| Ticker | Name | Category | Price | Change |
|--------|------|----------|-------|--------|
| OAI26 | OpenAI 2026 | prediction | $526B | -1.50% |
| ANT26 | Anthropic 2026 | prediction | $417B | -0.95% |
| NVDA | NVIDIA | equity | $220.27 | +2.00% |
| MSFT | Microsoft | equity | $428.31 | -0.18% |
| GOOGL | Alphabet | equity | $372.61 | +3.37% |
| AMZN | Amazon | equity | $254.53 | +2.40% |
| META | Meta | equity | $626.70 | +0.63% |
| TSLA | Tesla | equity | $420.00 | -0.84% |
| AAPL | Apple | equity | $311.60 | +0.76% |
| GOLD | Gold Spot | commodity | $4,500 | +0.71% |
| SILVER | Silver Spot | commodity | $73.95 | +0.89% |
| SPX | S&P 500 | index | 7,588 | +0.34% |
| VIX | Volatility Index | index | 15.40 | -3.99% |
| USO | Oil Fund | commodity | $137.04 | -2.93% |
| DPREZ | Democrat 2028 | prediction | 50% | -1.39% |
| INVADE27 | Taiwan invasion 2027 | prediction | 17% | +1.83% |
| CPI26 | Inflation Dec 2026 | prediction | 3% | -1.74% |

**Notable moves:** VIX -3.99% (risk unwinding), GOOGL +3.37%, USO -2.93%.  
Prediction markets: Anthropic $417B, OpenAI $526B.

---

## DuckDB Schema Summary

```
world-increments.duckdb
├── world_increments    37 rows   (GF3 color chain increments)
├── repo_snapshots    1027 rows   (GitHub social graph)
├── aptos_snapshots     28 rows   (Hamming swarm wallets alice,bob,A-Z)
├── multisig_probes      5 rows   (A-B, A-G, Y-Z, S-T, V-W — all 2-of-2)
└── mnx_snapshots       17 rows   (MNX testnet markets)
```
