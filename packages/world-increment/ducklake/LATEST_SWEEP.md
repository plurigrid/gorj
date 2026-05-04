# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-04

## Sweep Metadata
- **Date:** 2026-05-04 (UTC)
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Total Stars |
|--------|------|----------------|-------------|
| plurigrid | org | 100 | 145 |
| kubeflow | org | 47 | 101,718 |
| TeglonLabs | org | 4 | 14 |
| bmorphism | user | 100 | 509 |
| zubyul | user | 49 | 40 |
| migalkin | social graph (zubyul) | 19 | 832 |
| DJedamski | social graph (zubyul) | 6 | 17 |
| wasita | social graph (zubyul) | 10 | 10 |
| kristinezheng | social graph (zubyul) | 6 | 0 |
| M1shaaa | social graph (zubyul) | 8 | 0 |
| AustinCStone | social graph (zubyul) | 40 | 324 |

**Total repos snapshotted:** 389 unique (1,333 rows cumulative in DB)

### GF(3) Color Chain — 11 Increments This Run
| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1 | plurigrid | 1 | `#b8bb26` | PLUS |
| 2 | kubeflow | -1 | `#cc241d` | MINUS |
| 3 | bmorphism | 0 | `#d3869b` | ERGODIC |
| 4 | zubyul | 1 | `#b8bb26` | PLUS |
| 5 | TeglonLabs | -1 | `#cc241d` | MINUS |
| 6 | DJedamski | 0 | `#d3869b` | ERGODIC |
| 7 | migalkin | 1 | `#b8bb26` | PLUS |
| 8 | wasita | -1 | `#cc241d` | MINUS |
| 9 | kristinezheng | 0 | `#d3869b` | ERGODIC |
| 10 | M1shaaa | 1 | `#b8bb26` | PLUS |
| 11 | AustinCStone | -1 | `#cc241d` | MINUS |

### Notable Repos
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform
- **kubeflow/pipelines**: 4,119 stars — ML pipelines for Kubernetes
- **migalkin/NodePiece**: 143 stars — knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK
- **AustinCStone/TextGAN**: 92 stars — text generation GANs
- **TeglonLabs/mathpix-gem**: Ruby gem for MathML/LaTeX OCR (pushed 2026-01-01)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses probed against `fullnode.mainnet.aptoslabs.com`.
All returned `resource_not_found` — accounts have no on-chain APT CoinStore
(unfunded / never initialized).

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793…4cc7b | unfunded |
| bob | 0x0a3c…512d5d | unfunded |
| A | 0x8699…9d7a | unfunded |
| B | 0x3f89…cb13 | unfunded |
| C | 0x38b9…535e | unfunded |
| D–Z | (22 more) | all unfunded |

**28/28 addresses unfunded on Aptos mainnet.**

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428… | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c… | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181… | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9… | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4… | 2 | ✓ HEALTHY |

**5/5 multisig contracts healthy — all 2-of-2 threshold.**

### MNX Markets (testnet.mnx.fi)

MNX testnet is a Next.js SPA. No JSON API endpoints were accessible at
`/api/markets` or `/api/v1/markets`. Market data is client-side only.
**Status: UNAVAILABLE** (SPA, no public REST API)

---

## DuckDB Table Counts
```
world_increments:  34 rows (cumulative, GF3 color-coded)
repo_snapshots:  1333 rows (cumulative history)
aptos_snapshots:    28 rows (all balance_apt = NULL, unfunded)
multisig_probes:     5 rows (all healthy, 2-of-2)
mnx_snapshots:       0 rows (API unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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
