# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-25

## Sweep Metadata
- **Date:** 2026-07-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 (of 103) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (of 106) |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 12 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 30+ |

### Notable Activity (last 7 days, as of 2026-07-25)
- **plurigrid/gorj** — pushed 2026-07-25 (this repo, 1395 open issues) — active
- **plurigrid/eirobri** — pushed 2026-07-21 (EiRoBri replay world)
- **kubeflow/pipelines** — pushed 2026-07-25 (4170 ⭐)
- **kubeflow/kale** — pushed 2026-07-25 (697 ⭐, Kubeflow's superfood for Data Scientists)
- **kubeflow/dashboard** — pushed 2026-07-25 (TypeScript, Central Dashboard)
- **bmorphism/Gay.jl** — pushed 2026-07-25 (188 open issues, highly active)
- **zubyul/from-possible-worlds** — pushed 2026-07-18
- **wasita/wasita.github.io** — pushed 2026-07-21
- **migalkin/kgcourse2021** — pushed 2026-07-10

### GF(3) Color Chain Distribution (this sweep — 84 new increments)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 28 |
| 1 | #b8bb26 | PLUS | 28 |
| -1 | #cc241d | MINUS | 28 |

### Top Repos by Stars (this sweep)
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,793 | — | 2026-07-10 |
| kubeflow/pipelines | 4,170 | Python | 2026-07-25 |
| kubeflow/spark-operator | 3,143 | Python | 2026-07-25 |
| kubeflow/trainer | 2,153 | Go | 2026-07-25 |
| kubeflow/katib | 1,692 | Python | 2026-07-22 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| plurigrid/asi | 31 | HTML | 2026-07-10 |

### DuckDB State (cumulative across all sweeps)
- `world_increments`: 107 rows total (84 inserted this sweep)
- `repo_snapshots`: 1028 rows (historical accumulation)
- GF(3) distribution this sweep: ERGODIC=28, PLUS=28, MINUS=28 (perfect balance)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)
**28 addresses probed via `fullnode.mainnet.aptoslabs.com`**

All 28 addresses returned `null` from the `0x1::coin::CoinStore<AptosCoin>` resource endpoint.
The accounts are either uninitialized (CoinStore not registered) or unfunded on mainnet.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793acd... | null |
| bob   | 0x0a3c00c... | null |
| A     | 0x8699edc... | null |
| B     | 0x3f892eb... | null |
| C     | 0x38b99e6... | null |
| D     | 0xf776562... | null |
| E     | 0xdc1d9d5... | null |
| F     | 0x18a14b5... | null |
| G     | 0x69a394c... | null |
| H     | 0xce67c32... | null |
| I     | 0x070fe5d... | null |
| J     | 0x4d964db... | null |
| K     | 0xa732040... | null |
| L     | 0x7c2eaea... | null |
| M     | 0x6fed37a... | null |
| N     | 0xe7dde6d... | null |
| O     | 0x73252b6... | null |
| P     | 0x621879 2... | null |
| Q     | 0xac40fa5... | null |
| R     | 0x7ce605c... | null |
| S     | 0xb875301... | null |
| T     | 0x35781dc... | null |
| U     | 0x75860da... | null |
| V     | 0xb59dd81... | null |
| W     | 0x5f32aef... | null |
| X     | 0xa95cbbd... | null |
| Y     | 0xd8e3284... | null |
| Z     | 0x7af0ef6... | null |

### Multisig Contract Probes (5 pairs)
All 5 multisig contracts are **healthy** (2-of-2 signatures required).

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B  | 0x0da4f428... | 2 | ✓ healthy |
| A-G  | 0xf56c4a1c... | 2 | ✓ healthy |
| Y-Z  | 0xd3ffe181... | 2 | ✓ healthy |
| S-T  | 0x3b1c3ae9... | 2 | ✓ healthy |
| V-W  | 0x40fad7b4... | 2 | ✓ healthy |

### MNX Testnet Markets (`testnet.mnx.fi`)
Site is a Next.js SPA — no REST API endpoint exposed market data via curl.
**Status: unavailable.** No mnx_snapshots inserted.

### DuckDB Tables Updated
- `aptos_snapshots`: 28 rows inserted (all null balance)
- `multisig_probes`: 5 rows inserted (all 2-of-2, healthy)
- `mnx_snapshots`: 0 rows (SPA, no data accessible)

---

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
