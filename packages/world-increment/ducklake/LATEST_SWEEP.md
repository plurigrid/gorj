# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-29

## Sweep Metadata
- **Date:** 2026-07-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 12 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 30 |
| **TOTAL** | | **383** |

### Top Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,794 | — | 2026-07-10 |
| kubeflow/pipelines | 4,171 | Python | 2026-07-29 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-25 |
| kubeflow/trainer | 2,160 | Go | 2026-07-27 |
| kubeflow/katib | 1,693 | Python | 2026-07-26 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 53 | HTML | 2026-07-10 |

### Notable Recent Activity (2026-07)
- **plurigrid/zig-syrup**: pushed 2026-07-28 — high-perf OCapN Syrup in Zig; 2 stars
- **plurigrid/gorj** (this repo): pushed 2026-07-29, 1479 open issues — forj + Rama + GF(3)
- **plurigrid/asi**: pushed 2026-07-10, 53 stars — topological chemputer
- **bmorphism/Gay.jl**: pushed 2026-07-29, 188 open issues — wide-gamut deterministic color
- **zubyul/from-possible-worlds**: pushed 2026-07-18
- **wasita/wasita.github.io**: pushed 2026-07-21 — personal site (Svelte)
- **kubeflow/pipelines**: pushed 2026-07-29, 4171 stars — ML pipelines (very active)
- **M1shaaa/M1shaaa**: pushed 2026-07-29 — profile config

### GF(3) Color Chain
- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC** — 123 increments
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS** — 124 increments
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS** — 124 increments

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses probed)
**Result: All 28 addresses returned "Resource not found" from Aptos mainnet.**  
Accounts (alice, bob, A–Z) are not initialized with APT CoinStore on mainnet — they may be testnet addresses, uninitialized accounts, or using non-APT resources.

### Multisig Contract Probes (5 pairs)
All 5 multisig contracts are **HEALTHY** — each requires 2 signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428a0c007da... | 2 | HEALTHY |
| A-G | 0xf56c4a1c09062143... | 2 | HEALTHY |
| Y-Z | 0xd3ffe1812b2df406... | 2 | HEALTHY |
| S-T | 0x3b1c3ae905d44c3a... | 2 | HEALTHY |
| V-W | 0x40fad7b423a84365... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — testnet.mnx.fi is a Next.js SPA with no accessible REST JSON API. The `/api/markets` path returns HTML. Market data could not be extracted this run.

---

## DuckDB Summary
```
world_increments:   371  (GF3-colored repo event log)
repo_snapshots:   1,292  (cumulative across runs, current run adds ~383)
aptos_snapshots:     28  (all balance=0.0, resource-not-found)
multisig_probes:      5  (all healthy, sigs_required=2)
mnx_snapshots:        1  (unavailable marker)
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
