# World-Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-07-25  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Notes |
|--------|------|---------------|-------|
| plurigrid | org | 50 | gorj pushed today (2026-07-25), 1389 issues |
| kubeflow | org | 49 | pipelines (4169★), trainer (2153★), spark-operator (3143★) |
| TeglonLabs | org | 5 | jank-crane (GF3 convergence maps), mathpix-gem, coin-flip-mcp |
| bmorphism | user | 50 | Gay.jl top (188 issues), ocaml-mcp-sdk (61★) |
| zubyul | user | 49 | from-possible-worlds pushed 2026-07-18 |
| migalkin | user (social) | 5 | NodePiece (144★), StarE (89★), KG research |
| wasita | user (social) | 4 | wasita.github.io Svelte site active |
| AustinCStone | user (social) | 3 | TextGAN (92★) |
| DJedamski | user (social) | 2 | Kaggle/NCAA data science |
| kristinezheng | user (social) | 2 | MIT neuroscience lookit studies |
| M1shaaa | user (social) | 2 | lab bookshelf TypeScript |
| **TOTAL** | | **221** | |

### GF(3) Color Chain Distribution
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 73 |
| +1 | PLUS | #b8bb26 | 74 |
| -1 | MINUS | #cc241d | 74 |

### Notable Activity
- **plurigrid/gorj** — pushed 2026-07-25T10:13:42Z, 1389 open issues (most active repo)
- **plurigrid/asi** — 31★, 10 forks, pushed 2026-07-10 "everything is topological chemputer!"
- **kubeflow/pipelines** — 4169★ pushed 2026-07-24
- **kubeflow/trainer** — 2153★ pushed 2026-07-25
- **bmorphism/Gay.jl** — 188 issues, pushed 2026-07-25 (most active in bmorphism)
- **zubyul/from-possible-worlds** — TeX, pushed 2026-07-18
- **TeglonLabs/jank-crane** — C++, "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A-Z)
**All 28 addresses returned 0 APT** — CoinStore resource not found, indicating unfunded or inactive accounts on Aptos mainnet.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A-Z (26) | various | 0.0 each |

### Multisig Contract Probes (5 pairs)
All 5 multisig contracts are **healthy** and responsive, all requiring **2-of-N signatures**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
**Status: SPA only** — testnet.mnx.fi serves a Next.js SPA; /api/markets and /api/tickers both return HTML shell (no public JSON API endpoints). No market data extracted.

---

## DuckDB Schema Summary

```
world_increments  — 221 rows (repo events with GF3 color chain)
repo_snapshots    — 221 rows (per-repo metadata: lang, stars, forks, issues, push timestamp)
aptos_snapshots   —  28 rows (all balances 0 APT)
multisig_probes   —   5 rows (all healthy, sigs_required=2)
mnx_snapshots     —   0 rows (API unavailable, SPA only)
```
