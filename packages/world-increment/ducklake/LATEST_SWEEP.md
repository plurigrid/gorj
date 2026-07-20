# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-20

## Sweep Metadata
- **Date:** 2026-07-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 141 |
| Total Repo Snapshots | 118 |
| Aptos Snapshots | 28 |
| Multisig Probes | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 32 | 77 |
| kubeflow | org | 20 | 32,827 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 20 | 197 |
| zubyul | user | 14 | 8 |
| migalkin | social graph | 7 | 278 |
| AustinCStone | social graph | 5 | 104 |
| wasita | social graph | 6 | 4 |
| M1shaaa | social graph | 3 | 0 |
| DJedamski | social graph | 3 | 2 |
| kristinezheng | social graph | 3 | 0 |
| **TOTAL** | | **118** | **33,499** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,783 | — | 2026-07-10 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-19 |
| kubeflow/spark-operator | 3,140 | Python | 2026-07-17 |
| kubeflow/trainer | 2,152 | Go | 2026-07-19 |
| kubeflow/katib | 1,691 | Python | 2026-07-16 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-19 |
| kubeflow/arena | 815 | Go | 2026-07-17 |
| kubeflow/kale | 696 | Python | 2026-07-16 |
| kubeflow/mpi-operator | 530 | Go | 2026-07-13 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2023-02-13 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |

### Notable Activity

- **plurigrid/gorj** (this repo!): 1,268 open issues, pushed 2026-07-20
- **plurigrid/eirobri**: 30 open issues — EiRoBri replay world, pushed 2026-07-14
- **plurigrid/asi**: 31 stars — everything is topological chemputer!
- **kubeflow/mcp-server**: 28 stars, 35 forks — new MCP Server for Kubeflow AI dev tools
- **bmorphism/Gay.jl**: 187 open issues — Wide-gamut color sampling with GF(3) trits
- **zubyul/from-possible-worlds**: TeX, pushed 2026-07-18 — active academic writing
- **TeglonLabs/jank-crane**: C++ GF3 convergence maps + simonw workflow, pushed 2026-06-08
- **kubeflow/hub**: Model Registry, pushed 2026-07-20 (today)

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 47 |
| 1 | `#b8bb26` | PLUS | 47 |
| -1 | `#cc241d` | MINUS | 47 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (26 worlds + alice/bob)

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~6,362,757,581.

**Result:** All returned `resource_not_found` — accounts exist on-chain but hold no APT via legacy CoinStore. Consistent with Aptos Fungible Asset (FA) migration or unfunded accounts. Balance recorded as NULL.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | NULL (no CoinStore) |
| bob | 0x0a3c...512d | NULL (no CoinStore) |
| A | 0x8699...9d7a | NULL |
| B | 0x3f89...b13 | NULL |
| C | 0x38b9...535e | NULL |
| D | 0xf776...fdd1 | NULL |
| E | 0xdc1d...8d36 | NULL |
| F | 0x18a1...cf71 | NULL |
| G | 0x69a3...7f32 | NULL |
| H | 0xce67...300f | NULL |
| I | 0x070f...1fc9 | NULL |
| J | 0x4d96...7f54 | NULL |
| K | 0xa732...5dc4 | NULL |
| L | 0x7c2e...eba9 | NULL |
| M | 0x6fed...f2e9 | NULL |
| N | 0xe7dd...1b2c | NULL |
| O | 0x7325...a89d | NULL |
| P | 0x6218...c948 | NULL |
| Q | 0xac40...c89a9 | NULL |
| R | 0x7ce6...6e10 | NULL |
| S | 0xb875...0386 | NULL |
| T | 0x3578...4588 | NULL |
| U | 0x7586...f9956 | NULL |
| V | 0xb59d...af2c3 | NULL |
| W | 0x5f32...c7b0 | NULL |
| X | 0xa95c...3047d | NULL |
| Y | 0xd8e3...444c4 | NULL |
| Z | 0x7af0...197c | NULL |

### Multisig Contract Probes

All probes via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisigs healthy** — 2-of-2 threshold across all pairs.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel authentication wall blocks unauthenticated access. No market data extractable from `testnet.mnx.fi/api/markets` or `testnet.mnx.fi/api/v1/markets`.

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
