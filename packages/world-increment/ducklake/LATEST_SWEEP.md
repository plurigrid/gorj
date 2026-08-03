# World-Increment Sweep + Hamming Snapshot — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 34 (+11 this sweep) |
| Total Repo Snapshots | 1,183 (+239 this sweep) |
| Aptos Snapshots | 28 (all uninitialized, 0 APT) |
| Multisig Probes | 5 (all 2-of-2, all HEALTHY) |
| MNX Snapshots | 1 (unavailable — testnet SPA) |
| Sources Covered (new) | 11 orgs/users |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Alice, Bob, A–Z)

All 28 addresses queried against Aptos mainnet. All return `Resource not found` — wallets uninitialized (no APT CoinStore registered). Balance recorded as 0.0 APT.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 (uninitialized) |
| bob | 0x0a3c...2d5d | 0.0 (uninitialized) |
| A–Z (26) | various | 0.0 (all uninitialized) |

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All contracts: 2-of-2 threshold, HEALTHY.**

### MNX Markets (testnet.mnx.fi)

- `/api/markets` → HTTP 404
- Root URL → SPA shell, no market data in static HTML
- **Status: UNAVAILABLE**

---

## GF(3) Color Chain — New Increments (IDs 13–23)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 13 | AustinCStone | +1 | `#b8bb26` | **PLUS** |
| 14 | DJedamski | -1 | `#cc241d` | **MINUS** |
| 15 | M1shaaa | 0 | `#d3869b` | **ERGODIC** |
| 16 | TeglonLabs | +1 | `#b8bb26` | **PLUS** |
| 17 | bmorphism | -1 | `#cc241d` | **MINUS** |
| 18 | kristinezheng | 0 | `#d3869b` | **ERGODIC** |
| 19 | kubeflow | +1 | `#b8bb26` | **PLUS** |
| 20 | migalkin | -1 | `#cc241d` | **MINUS** |
| 21 | plurigrid | 0 | `#d3869b` | **ERGODIC** |
| 22 | wasita | +1 | `#b8bb26` | **PLUS** |
| 23 | zubyul | -1 | `#cc241d` | **MINUS** |

GF(3) chain continues cycling: PLUS → MINUS → ERGODIC (repeating)

---

## Top Repos by Stars (2026-08-03 sweep)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,804 | — | 2026-07-10 |
| kubeflow/pipelines | 4,173 | Python | 2026-08-03 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-31 |
| kubeflow/trainer | 2,165 | Go | 2026-07-31 |
| kubeflow/katib | 1,694 | Python | 2026-08-02 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-29 |
| kubeflow/arena | 816 | Go | 2026-07-29 |
| kubeflow/kale | 699 | Python | 2026-08-01 |
| migalkin/NodePiece | 144 | Python | 2021-06 |
| migalkin/StarE | 89 | Python | 2020-09 |
| AustinCStone/TextGAN | 92 | Python | 2016-09 |
| plurigrid/asi | 58 | HTML | 2026-07-10 |

## Most Recently Active

| Repo | Pushed At |
|------|-----------|
| kubeflow/mcp-server | 2026-08-03T07:43:58Z |
| plurigrid/gorj | 2026-08-03T07:15:44Z |
| kubeflow/pipelines | 2026-08-03T03:28:32Z |
| bmorphism/Gay.jl | 2026-08-03T02:39:28Z |
| plurigrid/place | 2026-08-02T20:00:41Z |
| kubeflow/katib | 2026-08-02T10:34:06Z |

## Language Breakdown (new repos this sweep)

| Language | Count | Stars |
|----------|-------|-------|
| Python | 47 | 10,643 |
| JavaScript | 20 | 131 |
| Rust | 17 | 38 |
| Go | 13 | 4,077 |
| HTML | 13 | 269 |
| Clojure | 8 | 3 |
| Zig | 7 | 7 |
| Jsonnet | 7 | 2,218 |

## Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| plurigrid | org | 20 |
| migalkin | user | 4 |
| AustinCStone | user | 3 |
| wasita | user | 3 |
| TeglonLabs | org | 5 |
| M1shaaa | user | 2 |
| DJedamski | user | 2 |
| kristinezheng | user | 2 |
| **TOTAL** | | **239** |

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,804 stars (+239 since April) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,173 stars — pushed 2026-08-03 (active)
- **kubeflow/mcp-server**: 31 stars — pushed 2026-08-03T07:43 (newest activity in sweep)
- **bmorphism/Gay.jl**: pushed 2026-08-03 — GF(3) color library still active
- **plurigrid/gorj**: 1,595 open issues — this repo has the highest issue count in plurigrid
- **plurigrid/asi**: 58 stars (+42 since April) — fast-growing topological chemputer repo
- **All 5 multisig contracts**: 2-of-2 threshold, all HEALTHY on Aptos mainnet
- **Hamming swarm wallets**: All 28 addresses uninitialized on mainnet (0 APT each)
