# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New Repo Snapshots (today) | 241 |
| Total Repo Snapshots (cumulative) | 1185 |
| Total World Increments (cumulative) | 264 |
| Sources Covered | 3 orgs + 7 users |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Pairs Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |

---

## GitHub Social Graph Sweep

### Repo Counts by Source (2026-07-10)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| bmorphism | user | 29 |
| zubyul | user | 22 |
| wasita | user | 11 |
| AustinCStone | user | 8 |
| DJedamski | user | 6 |
| migalkin | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **241** |

### Top 10 Repos by Stars (2026-07-10)

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15772 | 2026-07-10 |
| kubeflow/pipelines | Python | 4169 | 2026-07-10 |
| kubeflow/spark-operator | Python | 3136 | 2026-07-10 |
| kubeflow/trainer | Go | 2134 | 2026-07-10 |
| kubeflow/katib | Python | 1689 | 2026-07-10 |
| kubeflow/examples | Jsonnet | 1460 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1029 | 2026-07-09 |
| kubeflow/arena | Go | 815 | 2026-07-10 |
| kubeflow/kale | Python | 695 | 2026-07-10 |
| kubeflow/mpi-operator | Go | 529 | 2026-07-10 |

---

## GF(3) Color Chain — 2026-07-10 Increments

241 world increments inserted (IDs 1–241), one per repo snapshot:

| GF(3) Name | Trit | Color | Count |
|------------|------|-------|-------|
| PLUS | +1 | `#b8bb26` | 81 |
| MINUS | -1 | `#cc241d` | 80 |
| ERGODIC | 0 | `#d3869b` | 80 |

Pattern: `PLUS → MINUS → ERGODIC` repeating × 80, ending on PLUS (id 241)

## GF(3) Assignment Rule
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC

---

## Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 addresses)

All 28 Hamming swarm addresses queried via `fullnode.mainnet.aptoslabs.com`.
All balances returned 0.0 APT — accounts not funded or CoinStore not initialized.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…12d5 | 0.0 |
| A | 0x8699…e9d7 | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C | 0x38b9…535e | 0.0 |
| D | 0xf776…fdd1 | 0.0 |
| E | 0xdc1d…8d36 | 0.0 |
| F | 0x18a1…cf71 | 0.0 |
| G | 0x69a3…7f32 | 0.0 |
| H | 0xce67…300f | 0.0 |
| I | 0x070f…1fc9 | 0.0 |
| J | 0x4d96…7f54 | 0.0 |
| K | 0xa732…25dc | 0.0 |
| L | 0x7c2e…eba9 | 0.0 |
| M | 0x6fed…2e9 | 0.0 |
| N | 0xe7dd…1b2c | 0.0 |
| O | 0x7325…a89d | 0.0 |
| P | 0x6218…c948 | 0.0 |
| Q | 0xac40…89a9 | 0.0 |
| R | 0x7ce6…6e10 | 0.0 |
| S | 0xb875…0386 | 0.0 |
| T | 0x3578…4588 | 0.0 |
| U | 0x7586…9956 | 0.0 |
| V | 0xb59d…2c3 | 0.0 |
| W | 0x5f32…7b0 | 0.0 |
| X | 0xa95c…047d | 0.0 |
| Y | 0xd8e3…44c4 | 0.0 |
| Z | 0x7af0…197c | 0.0 |

### Multisig Probes (5 pairs)

All probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…7883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

All multisig contracts: 2-of-N, healthy.

### MNX Markets

**Unavailable** — `https://testnet.mnx.fi` returned Vercel deployment protection (403). No MNX snapshots recorded.

---

## DuckDB Totals (cumulative)

| Table | Rows |
|-------|------|
| world_increments | 264 |
| repo_snapshots | 1185 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,772 stars — flagship ML platform for Kubernetes (pushed 2026-07-10)
- **kubeflow/pipelines**: 4,169 stars — ML pipeline for Kubernetes (pushed 2026-07-10)
- **kubeflow/spark-operator**: 3,136 stars — Kubernetes operator for Apache Spark (pushed 2026-07-10)
- **kubeflow/trainer**: 2,134 stars — distributed training on Kubernetes (pushed 2026-07-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **GF(3) cycle**: 241 increments complete 80× full PLUS→MINUS→ERGODIC cycles + 1 trailing PLUS
