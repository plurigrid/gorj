# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-11 02:41 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GF(3) Color Chain

| Increment | Source | Type | Trit | Color | GF3 Name |
|-----------|--------|------|------|-------|----------|
| 1 | plurigrid | org | +1 | #b8bb26 | PLUS |
| 2 | kubeflow | org | -1 | #cc241d | MINUS |
| 3 | TeglonLabs | org | 0 | #d3869b | ERGODIC |
| 4 | bmorphism | user | +1 | #b8bb26 | PLUS |
| 5 | zubyul | user | -1 | #cc241d | MINUS |
| 6 | migalkin | user | 0 | #d3869b | ERGODIC |
| 7 | social_graph | user | +1 | #b8bb26 | PLUS |

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 98 |
| kubeflow | org | 12 (top active) |
| TeglonLabs | org | 4 |
| bmorphism | user | 13 (top active) |
| zubyul | user | 7 |
| migalkin | user | 4 |
| social_graph (DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) | users | 8 |
| **Total** | | **146** |

### Notable Repos (by stars)

| Repo | Language | Stars | Forks | Description |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | — | 15,565 | 2,626 | ML Toolkit for Kubernetes |
| kubeflow/pipelines | Python | 4,119 | 1,984 | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | Python | 3,111 | 1,483 | Kubernetes operator for Apache Spark |
| kubeflow/trainer | Go | 2,080 | 944 | Distributed AI Model Training |
| kubeflow/katib | Python | 1,676 | 521 | Automated ML on Kubernetes |
| plurigrid/asi | HTML | 16 | 5 | everything is topological chemputer! |
| migalkin/NodePiece | Python | 143 | 21 | Compositional KG representations (ICLR'22) |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2 | OCaml SDK for Model Context Protocol |
| AustinCStone/TextGAN | Python | 92 | 30 | Text GAN in TensorFlow |

### plurigrid Activity Highlights (most recent pushes)
- **gorj** (Clojure) — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **horse** (TeX) — 1★
- **web-browser** (Rust) — from prepostweb lineage
- **nanoclj-zig** (Zig) — NaN-boxed Clojure interpreter in Zig 0.15
- **zig-syrup** (Zig) — High-performance OCapN Syrup with CapTP optimizations
- **asi** (HTML) 16★ — everything is topological chemputer!
- **asi-skills** (Julia) 3★ — 69 skills with Galois Hole Type accessibility

### Zubyul Social Graph (bmorphism-connected)
- **migalkin** — Knowledge graph researcher; NodePiece (143★), StarE (88★)
- **wasita** — Svelte dev, wm-cv, magic-garden bot
- **kristinezheng** — Personal site, Lookit studies
- **M1shaaa** — Lab bookshelf, Yale coursework
- **AustinCStone** — TextGAN (92★), StereoVisionMRF (11★), ML/vision researcher
- **DJedamski** — NCAA ML competition (Kaggle)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-11)

All 28 wallets in the Hamming swarm queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (short) | Balance (APT) |
|-------|----------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...e9d7 | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

> All wallets report 0.0 APT — accounts may be uninitialized or have zero native balance on mainnet at this snapshot time.

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig accounts successfully probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (short) | Sigs Required | Healthy |
|------|----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All multisigs are 2-of-N threshold, operational on mainnet.

### MNX Markets (testnet.mnx.fi)

> Note: `/api/markets` returned 404. Market data extracted from SPA HTML snapshot.

| Ticker | Name | Category | Price |
|--------|------|----------|-------|
| AAPL | Apple Inc | Stocks | $260.81 |
| NVDA | NVIDIA Corp | Stocks | $188.63 |
| TSLA | Tesla Inc | Stocks | $351.56 |
| MSFT | Microsoft Corp | Stocks | $372.18 |
| AMZN | Amazon.com Inc | Stocks | $238.61 |
| SPX | S&P 500 Index | Financial | $6,813 |
| VIX | CBOE Volatility | Financial | 19.26 |
| OAI26 | OpenAI 2026 Valuation | AI | $529B |
| ANT26 | Anthropic 2026 Valuation | AI | $422B |
| GOLD | Gold Spot | Commodities | $4,746.78 |
| SILVER | Silver Spot | Commodities | $76.09 |
| CPER | US Copper Index Fund | Commodities | $35.89 |
| TLT | 20+ Year Treasury Bond ETF | Financial | $86.38 |
| TSM | Taiwan Semiconductor | Stocks | $371.37 |
| ASML | ASML Holding NV | Stocks | $1,482.98 |
| H100 | H100 GPU Index | Compute | $2.82 |

---

## DuckDB Schema

```sql
world_increments  -- 7 rows  (GF3 color-coded sweep events)
repo_snapshots    -- 146 rows (GitHub org/user repo snapshots)
aptos_snapshots   -- 28 rows  (Hamming swarm wallet balances)
multisig_probes   -- 5 rows   (multisig contract health checks)
mnx_snapshots     -- 18 rows  (MNX Markets tickers)
```
