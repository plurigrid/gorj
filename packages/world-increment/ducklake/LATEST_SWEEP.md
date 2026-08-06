# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-06  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Covered

| Source | Type | Repos |
|---|---|---|
| plurigrid | org | 103 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| wasita | social | 14 |
| AustinCStone | social | 41 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| DJedamski | social | 6 |
| **Total** | | **325** |

### Notable Repos (by stars)

| Repo | Stars | Language | Last Push |
|---|---|---|---|
| kubeflow/kubeflow | 15805 | — | 2026-07-10 |
| kubeflow/pipelines | 4178 | Python | 2026-08-05 |
| kubeflow/spark-operator | 3144 | Python | 2026-08-05 |
| kubeflow/trainer | 2171 | Go | 2026-08-05 |
| plurigrid/asi | 59 | HTML | 2026-07-10 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/Gay.jl | 2 | Julia | 2026-08-06 (active today) |
| plurigrid/gorj | 1 | Clojure | 2026-08-06 (active today) |

### Most Recently Active (pushed today 2026-08-06)

- `bmorphism/Gay.jl` — Wide-gamut deterministic color sampling (GF(3) SPI)
- `kubeflow/sdk` — Universal Python SDK for AI workloads on Kubernetes
- `plurigrid/gorj` — forj Clojure REPL + GF(3) trit coloring (this repo)

### GF(3) Color Chain (by id % 3)

| id%3 | Trit | Color | Name |
|---|---|---|---|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

325 increments: 109 ERGODIC, 108 PLUS, 108 MINUS

---

## JOB 2 — Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

All 28 Hamming swarm addresses returned 0.0 APT via the CoinStore resource query. This indicates the accounts either (a) have not registered the APT CoinStore resource, (b) hold zero APT, or (c) are inactive accounts.

| World | Address (truncated) | APT Balance |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | 0x8699...–0x7af0... | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts responded healthy with `num_signatures_required = 2` (2-of-2 threshold).

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets

`testnet.mnx.fi` serves a Next.js SPA with no discoverable REST API endpoint at `/api/markets` or `/api/tickers`. Market data is rendered client-side; no structured data was extractable. Recorded as UNAVAILABLE in `mnx_snapshots`.

---

## DuckDB Tables

| Table | Rows |
|---|---|
| world_increments | 325 |
| repo_snapshots | 325 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## Key Signals

1. **bmorphism/Gay.jl** — Most active personal repo, pushed today, 188 open issues, heavy GF(3)/SPI work
2. **plurigrid/gorj** — This repo, pushed today, 1668 open issues — most active in plurigrid org
3. **kubeflow MCP server** (kubeflow/mcp-server) — 47 open issues, very recent (2026-08-04), signals new AI-agent integration work
4. **All Hamming swarm multisigs healthy** — 2-of-2 threshold confirmed on all 5 pairs
5. **wasita** social graph most active — `wasita/xoxowasita-analysis` pushed 2026-08-05, `joint-planning-lit` pushed 2026-08-04
