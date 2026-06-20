# World-Increment Sweep + Hamming Swarm Snapshot
**Run date:** 2026-06-20T17:10 UTC  
**Branch:** world-increment/sweep-2026-06-20  
**GF(3) Color Chain:** id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Cumulative Repo Snapshots in Ducklake

| Source | Type | Total Snapshots |
|--------|------|-----------------|
| plurigrid | org | 300 |
| bmorphism | user | 300 |
| kubeflow | org | 142 |
| AustinCStone | user (zubyul graph) | 126 |
| TeglonLabs | org | 111 |
| zubyul | user | 97 |
| migalkin | user (zubyul graph) | 79 |
| wasita | user (zubyul graph) | 71 |
| kristinezheng | user (zubyul graph) | 41 |
| M1shaaa | user (zubyul graph) | 40 |
| DJedamski | user (zubyul graph) | 28 |

**Total accumulated repo snapshots:** 1,335 | **World increments:** 414

### Notable repos captured this run (active 2026)
- **plurigrid/gorj** (Clojure, 699 open issues, pushed 2026-06-20) — this very repo: forj + Rama topology nREPL + GF(3)
- **plurigrid/place** (TeX, pushed 2026-06-20) — bci.place forester
- **plurigrid/eirobri** (Clojure, 29 issues, pushed 2026-06-03) — EiRoBri replay world
- **bmorphism/Gay.jl** (Julia ★2, 187 open issues, pushed 2026-06-20) — wide-gamut GF(3) color sampling
- **bmorphism/satreadout** (HTML, pushed 2026-06-20) — machine-checked saturating non-Riemannian perceptual readout
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08) — crane-jank converged-IR hub with GF3 convergence maps
- **kubeflow/pipelines** (Python ★4155, 2008 forks, pushed 2026-06-20) — ML Pipelines for Kubeflow
- **kubeflow/mcp-apache-spark-history-server** (Python ★177) — MCP for Spark
- **M1shaaa/M1shaaa** — profile repo pushed 2026-06-20 (active today)
- **wasita/wasita.github.io** (Svelte ★1, pushed 2026-06-15) — personal website

### DuckDB ducklake
- Path: `packages/world-increment/ducklake/world-increments.duckdb`
- Tables: `world_increments` (414 rows), `repo_snapshots` (1335 rows), `aptos_snapshots` (28 rows), `multisig_probes` (5 rows), `mnx_snapshots` (0 rows)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
**Queried:** 28 wallets (alice, bob, A–Z)  
**Result:** All 28 wallets returned 0 APT — CoinStore resources not found or accounts uninitialized on mainnet.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...c7b | 0 |
| bob | 0x0a3c...d5d | 0 |
| A | 0x8699...9d7a | 0 |
| B–Z | (see aptos_snapshots table) | 0 each |

All 28 entries in `aptos_snapshots`. No APT holdings detected on mainnet for any address.

### Multisig Contract Probes
All 5 multisig contracts **HEALTHY** — `num_signatures_required` returns 2.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | HEALTHY |
| A-G | 0xf56c...096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | HEALTHY |
| S-T | 0x3b1c...883 | 2 | HEALTHY |
| V-W | 0x40fa...b6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)
- **Status: UNAVAILABLE** — All API endpoints returned errors; root returns HTTP 401 (Vercel, requires auth)
- `/api/markets`, `/api/v1/markets`, `/api/tickers` → all failed
- `mnx_snapshots` table: 0 rows (no public market data accessible)

---

## GF(3) Trit Distribution (this run's increments)
- **Trit 0 / ERGODIC / #d3869b:** every 3rd increment (TeglonLabs, kubeflow-even, etc.)
- **Trit 1 / PLUS / #b8bb26:** every 3rd+1 increment
- **Trit -1 / MINUS / #cc241d:** every 3rd+2 increment

```sql
-- Query to reproduce
SELECT gf3_trit, gf3_color, gf3_name, count(*) as n
FROM world_increments GROUP BY gf3_trit, gf3_color, gf3_name ORDER BY gf3_trit;
```
