# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-11T19:22:22Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.1 Variegata)  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 98 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 99 |
| zubyul | user | 45 |
| migalkin | user (zubyul graph) | 19 |
| DJedamski | user (zubyul graph) | 6 |
| wasita | user (zubyul graph) | 9 |
| kristinezheng | user (zubyul graph) | 6 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 40 |
| **TOTAL** | | **381** |

**repo_snapshots in DuckDB:** 669 rows (includes prior sweep data)  
**GF(3) distribution (new inserts):** ERGODIC=69 · PLUS=70 · MINUS=70

### Notable Recent Activity (pushed ≤ 7 days ago)

- `bmorphism/boxxy` (Move) — pushed 2026-04-09
- `zubyul/big-bad-plurigrid-quiz` (Emacs Lisp) — pushed 2026-04-09
- `bmorphism/postweb` (Go) — pushed 2026-04-09
- `kristinezheng/kristinezheng.github.io` — pushed 2026-04-09
- `wasita/wm-cv` (Svelte) — pushed 2026-04-08
- `bmorphism/shitcoin` (Python) — pushed 2026-04-08
- `zubyul/gay-world` (Python) — pushed 2026-04-05

### Top Starred Repos in Sweep

| Repo | Stars | Language |
|------|-------|----------|
| migalkin/NodePiece | 143 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 88 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |
| migalkin/kgcourse2021 | 25 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |
| bmorphism/say-mcp-server | 20 | JavaScript |
| bmorphism/babashka-mcp-server | 18 | JavaScript |
| bmorphism/manifold-mcp-server | 13 | JavaScript |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — 28 wallets (A–Z + alice + bob)

All 28 probes completed via `fullnode.mainnet.aptoslabs.com`.  
**Result: All 28 wallets show 0.0 APT** (accounts exist on-chain with empty CoinStore).

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C | 0x38b9…535e | 0.0 |
| D | 0xf776…fdd1 | 0.0 |
| E | 0xdc1d…8d36 | 0.0 |
| F | 0x18a1…cf71 | 0.0 |
| G | 0x69a3…7f32 | 0.0 |
| H | 0xce67…300f | 0.0 |
| I | 0x070f…1fc9 | 0.0 |
| J | 0x4d96…7f54 | 0.0 |
| K | 0xa732…5dc4 | 0.0 |
| L | 0x7c2e…eba9 | 0.0 |
| M | 0x6fed…f2e9 | 0.0 |
| N | 0xe7dd…1b2c | 0.0 |
| O | 0x7325…a89d | 0.0 |
| P | 0x6218…c948 | 0.0 |
| Q | 0xac40…c89a9 | 0.0 |
| R | 0x7ce6…6e10 | 0.0 |
| S | 0xb875…0386 | 0.0 |
| T | 0x3578…4588 | 0.0 |
| U | 0x7586…f9956 | 0.0 |
| V | 0xb59d…f2c3 | 0.0 |
| W | 0x5f32…c7b0 | 0.0 |
| X | 0xa95c…047d | 0.0 |
| Y | 0xd8e3…44c4 | 0.0 |
| Z | 0x7af0…197c | 0.0 |

### Multisig Contract Probes — 5 pairs

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Contract (prefix) | Sigs Required | Healthy |
|------|------------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — uniform 2-of-N threshold.**

### MNX Prediction Markets (testnet.mnx.fi) — 32 markets

SPA with server-side hydrated data. No REST API exposed. Markets extracted from embedded Next.js state.

| Ticker | Name | Category | Price | Δ24h |
|--------|------|----------|-------|------|
| FMATH26 | FrontierMath Highest 2026 Score | AI | 50% | +6.38% |
| ARC26 | Arc AGI 2 Highest 2026 Score | AI | 60% | +1.69% |
| CPI26 | U.S. CPI Annual Inflation Rate Dec 2026 | Financial | 2.59% | +1.57% |
| TSLA | Tesla Inc | Stocks | $351.77 | +1.56% |
| ECI26 | Epoch Capabilities Index Max 2026 | AI | 169 | +1.20% |
| DPREZ | Democrat Elected President 2028 | Politics | 50% | +1.01% |
| GOOGL | Alphabet (Google) | Stocks | $318.07 | +0.31% |
| MSFT | Microsoft | Stocks | $372.15 | +0.35% |
| OAI26 | OpenAI Final 2026 Valuation | Valuations | $526B | +0.38% |
| AAPL | Apple | Stocks | $260.67 | +0.39% |
| H100 | SemiAnalysis H100 Spot Rental | Compute | $2.82 | +0.46% |
| META | Meta (Facebook) | Stocks | $630.27 | +0.67% |
| OAITOP26 | OpenAI Top AI Model 2026 | AI | 23% | 0.00% |
| AMZN | Amazon | Stocks | $238.61 | +0.08% |
| TLT | iShares 20+ Year Treasury Bond ETF | Financial | $86.43 | +0.03% |
| SPX | S&P 500 Index | Financial | 6,813 | -0.01% |
| IEF | iShares 7-10 Year Treasury Bond ETF | Financial | $95.33 | -0.02% |
| URA | Global X Uranium ETF | Commodities | $50.93 | -0.12% |
| ANT26 | Anthropic Final 2026 Valuation | Valuations | $422B | -1.17% |
| CRWV | CoreWeave | Stocks | $102.84 | -1.57% |
| NVDA | NVIDIA | Stocks | $188.51 | -0.24% |
| CPER | United States Copper Index Fund | Commodities | $35.89 | -0.19% |
| USO | United States Oil Fund | Commodities | $124.91 | -0.49% |
| INTC | Intel | Stocks | $62.47 | -0.70% |
| MU | Micron Technology | Stocks | $420.10 | -0.74% |
| ASML | ASML Holding | Stocks | $1,483.00 | -0.37% |
| GOLD | Gold Spot | Commodities | $4,747.39 | -0.45% |
| TSM | Taiwan Semiconductor | Stocks | $371.17 | -0.56% |
| SILVER | Silver Spot | Commodities | $76.10 | -0.59% |
| SFHOME26 | S&P Case-Shiller SF Home Index 2026 | Financial | 380.5 | -0.63% |
| VIX | CBOE Volatility Index | Financial | 19.26 | -2.87% |
| INVADE27 | China Invades Taiwan before 2027 | Politics | 16% | -9.50% |

**Signal:** AI benchmarks (ARC26, FMATH26, ECI26) all up. INVADE27 -9.5% (geopolitical risk declining). ANT26 $422B vs OAI26 $526B.

---

## DuckDB Schema

```
world-increments.duckdb
├── world_increments   — GF(3) color-chained event log (209 rows)
├── repo_snapshots     — GitHub repo metadata (669 rows, cumulative)
├── aptos_snapshots    — Hamming swarm wallet balances (28 rows)
├── multisig_probes    — Multisig contract health (5 rows)
└── mnx_snapshots      — Prediction market data (32 rows)
```

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent · plurigrid/gorj · 2026-04-11*
