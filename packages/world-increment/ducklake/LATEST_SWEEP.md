# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-02

## Sweep Metadata
- **Date:** 2026-06-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| wasita | user (zubyul graph) | 11 |
| AustinCStone | user (zubyul graph) | 40 |
| DJedamski | user (zubyul graph) | 6 |
| kristinezheng | user (zubyul graph) | 6 |
| M1shaaa | user (zubyul graph) | 8 |
| **TOTAL** | | **391** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 130 |
| 1 | `#b8bb26` | PLUS | 131 |
| 2 | `#cc241d` | MINUS | 130 |

GF(3) rule: `id%3==0` → ERGODIC · `id%3==1` → PLUS · `id%3==2` → MINUS

### Top Repos by Stars (top 10)

| Org/User | Repo | Stars | Language | Last Push |
|----------|------|-------|----------|-----------|
| kubeflow | kubeflow | 15,700 | — | 2026-05-24 |
| kubeflow | pipelines | 4,151 | Python | 2026-06-01 |
| kubeflow | spark-operator | 3,125 | Python | 2026-06-01 |
| kubeflow | trainer | 2,109 | Go | 2026-05-30 |
| kubeflow | katib | 1,685 | Python | 2026-05-29 |
| kubeflow | examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow | manifests | 1,020 | YAML | 2026-05-29 |
| kubeflow | arena | 811 | Go | 2026-05-07 |
| kubeflow | kale | 691 | Python | 2026-06-01 |
| kubeflow | mpi-operator | 528 | Go | 2026-05-29 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-02)

All 28 Hamming-swarm wallets queried via `fullnode.mainnet.aptoslabs.com`. All returned **0 APT** — consistent with unactivated addresses (no `CoinStore<AptosCoin>` resource initialized on-chain).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793acd…4cc7b | 0.0 |
| bob | 0x0a3c00c…512d5d | 0.0 |
| A | 0x8699edc…e9d7a | 0.0 |
| B | 0x3f892eb…cb13 | 0.0 |
| C | 0x38b99e6…535e | 0.0 |
| D | 0xf776562…cfdd1 | 0.0 |
| E | 0xdc1d9d5…8d36 | 0.0 |
| F | 0x18a14b5…3cf71 | 0.0 |
| G | 0x69a394c…7f32 | 0.0 |
| H | 0xce67c32…300f | 0.0 |
| I | 0x070fe5d…1fc9 | 0.0 |
| J | 0x4d964db…7f54 | 0.0 |
| K | 0xa732040…25dc4 | 0.0 |
| L | 0x7c2eaea…eba9 | 0.0 |
| M | 0x6fed37a…7f2e9 | 0.0 |
| N | 0xe7dde6d…51b2c | 0.0 |
| O | 0x73252b6…5a89d | 0.0 |
| P | 0x621879…c948 | 0.0 |
| Q | 0xac40fa5…c89a9 | 0.0 |
| R | 0x7ce605c…6e10 | 0.0 |
| S | 0xb87530…d0386 | 0.0 |
| T | 0x35781dc…f4588 | 0.0 |
| U | 0x75860da…f9956 | 0.0 |
| V | 0xb59dd81…af2c3 | 0.0 |
| W | 0x5f32aef…cc7b0 | 0.0 |
| X | 0xa95cbbd…047d | 0.0 |
| Y | 0xd8e3284…444c4 | 0.0 |
| Z | 0x7af0ef6…197c | 0.0 |

### Multisig Contract Probes — 5/5 Healthy

All five 2-of-2 multisig accounts on Aptos mainnet responded and are healthy:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f42…87003 | 2 | ✓ |
| A-G | 0xf56c4a1…0096 | 2 | ✓ |
| Y-Z | 0xd3ffe18…b883 | 2 | ✓ |
| S-T | 0x3b1c3ae…7883 | 2 | ✓ |
| V-W | 0x40fad7b…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE.** All JSON API endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/pairs`) return HTTP 422. The site serves a Next.js SPA with no public REST API. The `mnx_snapshots` table is empty.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)  -- 391 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)  -- 391 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)  -- 0 rows (unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,700 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,151 stars — most popular ML pipeline for Kubernetes (pushed 2026-06-01)
- **kubeflow/spark-operator**: 3,125 stars — Kubernetes operator for Apache Spark (pushed 2026-06-01)
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) trit coloring
- **Hamming swarm**: 28 wallets confirmed on-chain, all unactivated (0 APT)
- **Multisig health**: 5/5 pairs confirmed 2-of-2, all healthy
