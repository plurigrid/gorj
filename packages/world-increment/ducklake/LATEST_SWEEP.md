# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-24

## Sweep Metadata
- **Date:** 2026-06-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 40 |

**Total repos discovered:** 391 public repos across 11 sources  
**New world-increments this sweep:** 112 (IDs assigned sequentially, GF3 color chain applied)

### Most Recently Pushed Repos

| Repo | Stars | Lang | Pushed |
|------|-------|------|--------|
| kubeflow/spark-operator | 3128 | Python | 2026-06-24 |
| kubeflow/pipelines | 4157 | Python | 2026-06-24 |
| plurigrid/gorj | 0 | Clojure | 2026-06-24 |
| M1shaaa/M1shaaa | 0 | — | 2026-06-24 |
| bmorphism/Gay.jl | 2 | Julia | 2026-06-24 |
| plurigrid/place | 1 | TeX | 2026-06-24 |
| wasita/proj-template | 0 | — | 2026-06-19 |

### Top Repos by Stars (This Sweep)

| Repo | Stars | Forks | Lang |
|------|-------|-------|------|
| kubeflow/kubeflow | 15742 | 2680 | — |
| kubeflow/pipelines | 4157 | 2009 | Python |
| kubeflow/spark-operator | 3128 | 1492 | Python |
| kubeflow/trainer | 2119 | 972 | Go |
| kubeflow/katib | 1685 | 527 | Python |
| kubeflow/examples | 1460 | 756 | Jsonnet |
| kubeflow/arena | 813 | 191 | Go |
| kubeflow/mpi-operator | 528 | 236 | Go |
| migalkin/NodePiece | 144 | 21 | Python |
| AustinCStone/TextGAN | 92 | 30 | Python |
| migalkin/StarE | 89 | 16 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml |

### Notable New/Active Repos

- **plurigrid/gorj** (this repo) — pushed 2026-06-24, 793 open issues — active forj + Rama + GF(3) REPL routing
- **plurigrid/eirobri** — pushed 2026-06-23, 30 open issues — EiRoBri replay world
- **bmorphism/Gay.jl** — Julia, 187 open issues — wide-gamut color sampling, Pigeons.jl SPI
- **kubeflow/mcp-server** — Python, 17 stars — MCP server for AI-assisted kubeflow development
- **kubeflow/mcp-apache-spark-history-server** — Python, 178 stars — debug Spark from AI agents
- **TeglonLabs/jank-crane** — C++, pushed 2026-06-08 — crane-jank converged-IR hub with GF3 convergence maps

### GF(3) Color Chain (112 new increments)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 38 |
| 1 | PLUS | #b8bb26 | 37 |
| -1 | MINUS | #cc241d | 37 |

Sequence cycles: `ERGODIC → PLUS → MINUS → ERGODIC → ...` (37 full cycles + 1 partial)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 hamming swarm addresses (alice, bob, A–Z) probed via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All addresses returned 0 APT** — no CoinStore resource initialized on any of these accounts on Aptos mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a | 0.0 |
| B | 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 | 0.0 |
| C | 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e | 0.0 |
| D | 0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1 | 0.0 |
| E–Z | (22 addresses) | 0.0 each |

### Multisig Contract Health (5 pairs)

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

**Result: All 5 contracts healthy — 2-of-2 threshold.**

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ healthy |

### MNX Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` requires Vercel deployment authentication. The site serves an authentication-required page for all endpoints (`/api/markets`, `/api/tickers`, `/`). No market data accessible without a Vercel bypass token or trusted source OIDC configuration.

---

## DuckDB Table Summary

```
world_increments  – 135 total rows (112 added this sweep)
repo_snapshots    – 1056 total rows (includes all historical sweeps)
aptos_snapshots   – 28 rows (this sweep)
multisig_probes   – 5 rows (this sweep)
mnx_snapshots     – 0 rows (unavailable)
```

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
