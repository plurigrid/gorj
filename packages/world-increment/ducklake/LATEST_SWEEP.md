# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-11 21:35:18 UTC
**GF(3) chain:** ERGODIC #d3869b (0) → PLUS #b8bb26 (+1) → MINUS #cc241d (-1) → repeat

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Count |
|--------|------|-------|
| plurigrid | org | 98 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 99 |
| zubyul | user | 45 |
| migalkin | social-graph | 19 |
| AustinCStone | social-graph | 30 |
| wasita | social-graph | 5 |
| kristinezheng | social-graph | 3 |
| M1shaaa | social-graph | 3 |
| DJedamski | social-graph | 3 |

**Total repo snapshots in ducklake:** 827 (includes world_increment entries)

### Top Repos by Stars
```
kubeflow/kubeflow              ★15566  —  (no lang)  pushed 2026-01
kubeflow/spark-operator        ★3111   —  Python     pushed 2026-04
kubeflow/trainer               ★2080   —  Go         pushed 2026-04
kubeflow/pipelines             ★4119   —  Python     pushed 2026-04
kubeflow/katib                 ★1676   —  Python     pushed 2026-04
kubeflow/examples              ★1459   —  Jsonnet    pushed 2025-04
AustinCStone/TextGAN           ★92     —  Python     pushed 2016-10
bmorphism/anti-bullshit-mcp    ★23     —  JavaScript pushed 2026-01
migalkin/NodePiece             ★143    —  Python     pushed 2022-02
migalkin/StarE                 ★88     —  Python     pushed 2023-12
```

### Notable Recent Activity (plurigrid)
- **gorj** (Clojure) — GF(3) gay trit coloring for compositional open game REPL orchestration — pushed 2026-04-11
- **nanoclj-zig** (Zig) — NaN-boxed Clojure interpreter, interaction nets, fuel-bounded eval — pushed 2026-04-09
- **asi** (HTML) — everything is topological chemputer! ★16 — pushed 2026-04-10
- **zig-syrup** (Zig) — OCapN Syrup ★2 — pushed 2026-04-09
- **asi-skills** (Julia) — 69 skills with Galois Hole Type accessibility ★3

### Notable bmorphism Activity
- **boxxy** (Move) — pushed 2026-04-09
- **postweb** (Go) — evolved from prepostweb — pushed 2026-04-09
- **ocaml-mcp-sdk** (OCaml) — Jane Street oxcaml_effect SDK ★60 — pushed 2026-03-16
- **flox-mcp-bb** (Clojure) — open-source MCP server for Flox — pushed 2026-02-12

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

> All queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...c7b | 0.00 |
| bob   | 0x0a3c...d5d | 0.00 |
| A     | 0x8699...d7a | 0.00 |
| B     | 0x3f89...b13 | 0.00 |
| C     | 0x38b9...35e | 0.00 |
| D     | 0xf776...dd1 | 0.00 |
| E     | 0xdc1d...d36 | 0.00 |
| F     | 0x18a1...f71 | 0.00 |
| G     | 0x69a3...f32 | 0.00 |
| H     | 0xce67...00f | 0.00 |
| I     | 0x070f...c9 | 0.00 |
| J     | 0x4d96...f54 | 0.00 |
| K     | 0xa732...dc4 | 0.00 |
| L     | 0x7c2e...ba9 | 0.00 |
| M     | 0x6fed...e9 | 0.00 |
| N     | 0xe7dd...b2c | 0.00 |
| O     | 0x7325...89d | 0.00 |
| P     | 0x6218...948 | 0.00 |
| Q     | 0xac40...9a9 | 0.00 |
| R     | 0x7ce6...e10 | 0.00 |
| S     | 0xb875...386 | 0.00 |
| T     | 0x3578...588 | 0.00 |
| U     | 0x7586...956 | 0.00 |
| V     | 0xb59d...2c3 | 0.00 |
| W     | 0x5f32...7b0 | 0.00 |
| X     | 0xa95c...47d | 0.00 |
| Y     | 0xd8e3...4c4 | 0.00 |
| Z     | 0x7af0...97c | 0.00 |

**Observation:** All 28 addresses returned 0 APT — CoinStore resource not initialized or accounts unfunded on mainnet.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...003 | 2 | ✓ |
| A-G  | 0xf56c...096 | 2 | ✓ |
| Y-Z  | 0xd3ff...883 | 2 | ✓ |
| S-T  | 0x3b1c...883 | 2 | ✓ |
| V-W  | 0x40fa...b6d | 2 | ✓ |

**All 5 multisig accounts healthy — 2-of-N threshold on each.**

### MNX Markets (testnet.mnx.fi)

> Note: /api/markets returned 404. Data extracted from Next.js RSC payload on homepage.

| Ticker | Name | Category | Price | 24h Change |
|--------|------|----------|-------|-----------|
| OAI26 | OpenAI 2026 Valuation | Valuations | $527B | +0.19% |
| ANT26 | Anthropic 2026 Valuation | Valuations | $421B | -0.47% |
| USO | Oil Fund | Commodities | $124.91 | +0.43% |
| GOLD | Gold Spot | Commodities | $4,700 | +0.01% |
| TSLA | Tesla | Stocks | $351.74 | +0.98% |

---

## DuckDB Schema

Tables in `world-increments.duckdb`:
- `world_increments` — GF(3) trit-colored source events
- `repo_snapshots` — GitHub repo metadata snapshots
- `aptos_snapshots` — Hamming swarm wallet balances
- `multisig_probes` — Multisig threshold health checks
- `mnx_snapshots` — MNX prediction market data

## GF(3) Color Chain

```
id % 3 == 0  →  trit=0  ERGODIC  #d3869b  (rose/pink)
id % 3 == 1  →  trit=1  PLUS     #b8bb26  (lime/yellow)
id % 3 == 2  →  trit=-1 MINUS    #cc241d  (red)
```
