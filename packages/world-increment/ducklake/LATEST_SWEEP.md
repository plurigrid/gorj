# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-08  
**Run:** world-increment-sweep + hamming-swarm-snapshot  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos | Notable |
|--------|------|-------|---------|
| plurigrid | org | 100 | asi (30★), gorj (pushed today) |
| kubeflow | org | 49 | kubeflow/kubeflow (15,769★), pipelines (4,169★) |
| TeglonLabs | org | 5 | jank-crane (GF3 maps, C++) |
| bmorphism | user | 100 | ocaml-mcp-sdk (61★), Gay.jl (pushed today) |
| zubyul | user | 49 | voice-observatory, nash-tui |
| migalkin | user | 19 | NodePiece (144★, ICLR'22) |
| DJedamski | user | 6 | data science / Kaggle |
| wasita | user | 11 | wasita.github.io (pushed 2026-07-06) |
| kristinezheng | user | 5 | MIT neuro research |
| M1shaaa | user | 8 | Yale/Lookit research |
| AustinCStone | user | 20 | TextGAN (92★), bmfork/bitmind work |

**Total repos in this sweep:** 372

### Most Recently Pushed (2026-07-08)

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow/pipelines | Python | 4,169 | 2026-07-08T02:04 |
| bmorphism/Gay.jl | Julia | 2 | 2026-07-08T00:29 |
| plurigrid/gorj | Clojure | 1 | 2026-07-08T01:15 |
| kubeflow/trainer | Go | 2,130 | 2026-07-08T00:12 |

### Notable Repos Across the Social Graph

| Repo | Stars | Signal |
|------|-------|--------|
| kubeflow/kubeflow | 15,769 | flagship ML-on-K8s platform |
| kubeflow/pipelines | 4,169 | pushed today |
| kubeflow/spark-operator | 3,133 | active K8s/Spark |
| kubeflow/trainer | 2,130 | distributed training |
| migalkin/NodePiece | 144 | ICLR'22 KG embeddings |
| AustinCStone/TextGAN | 92 | TF GAN for text |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml MCP SDK (Jane Street) |
| migalkin/StarE | 89 | EMNLP'20 hyper-relational KGs |
| plurigrid/asi | 30 | topological chemputer |
| bmorphism/anti-bullshit-mcp-server | 23 | MCP server |
| TeglonLabs/jank-crane | 0 | crane-jank IR hub, GF3 convergence maps (C++) |
| plurigrid/gorj | 1 | this repo — Clojure REPL + forj |

### GF(3) Color Chain

Each repo increment is tagged by `id % 3`:

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 113 |
| +1 | `#b8bb26` | PLUS | 115 |
| -1 | `#cc241d` | MINUS | 115 |

Chain pattern: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses via `https://fullnode.mainnet.aptoslabs.com`.  
All 28 wallets returned **0 APT** — no `CoinStore<AptosCoin>` resource registered,  
or accounts have zero balance.

| World | Address (truncated) | APT |
|-------|---------------------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes

All 5 multisig accounts are **healthy** — 2-of-N sigs required.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ healthy |
| A-G | 0xf56c...096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ healthy |
| S-T | 0x3b1c...883 | 2 | ✓ healthy |
| V-W | 0x40fa...b6d | 2 | ✓ healthy |

### MNX Markets (`testnet.mnx.fi`)

**Unavailable** — site requires Vercel visitor password authentication.  
No market data could be extracted. `mnx_snapshots` table is empty.

---

## DuckDB Schema

```
world-increments.duckdb
├── world_increments    — GF3-tagged activity log (id, trit, color, source, repo, hash)
├── repo_snapshots      — GitHub repo metadata (stars, forks, issues, pushed_at)
├── aptos_snapshots     — Hamming swarm wallet balances (all 0.0 APT this sweep)
├── multisig_probes     — Contract health checks (5/5 healthy, sigs_required=2)
└── mnx_snapshots       — MNX market data (empty — Vercel auth required)
```

---

*Generated 2026-07-08 by world-increment-sweep + hamming-swarm-snapshot*
