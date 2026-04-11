# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-11

## Sweep Metadata
- **Date:** 2026-04-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (DB) | 42 |
| Total Repo Snapshots (DB) | 942 |
| New Increments This Sweep | 31 |
| New Repos This Sweep | 471 |
| Sources Covered | 3 orgs + 8 users + events |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source Type | Name | Repos |
|------------|------|-------|
| org | plurigrid | 100 |
| org | kubeflow | 47 |
| org | TeglonLabs | 53 |
| user | bmorphism | 100 |
| user | zubyul | 24 |
| user | migalkin | 30 |
| user | DJedamski | 11 |
| user | wasita | 29 |
| user | kristinezheng | 18 |
| user | M1shaaa | 16 |
| user | AustinCStone | 43 |
| events | bmorphism | 10 recent |
| events | zubyul | 10 recent |

### GF(3) Color Chain — This Sweep

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1 | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2 | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3 | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4 | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5 | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6 | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7 | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8 | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9 | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |
| 12–31 | bmorphism/zubyul events | event | GF3 chain | continues... | |

GF(3) assignment: `id%3==1` → PLUS `#b8bb26`, `id%3==2` → MINUS `#cc241d`, `id%3==0` → ERGODIC `#d3869b`

### Top Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,566 | - |
| kubeflow | pipelines | 4,119 | Python |
| kubeflow | spark-operator | 3,111 | Python |
| kubeflow | trainer | 2,080 | Go |
| kubeflow | katib | 1,676 | Python |

### Language Distribution (all 942 snapshots)

| Language | Repos |
|----------|-------|
| Python | 154 |
| HTML | 36 |
| Go | 36 |
| Rust | 30 |
| JavaScript | 28 |
| Jupyter Notebook | 26 |
| TypeScript | 24 |
| Clojure | 16 |
| R | 16 |
| Jsonnet | 16 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 wallets: alice, bob, A–Z)

All wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts exist on-chain but APT CoinStore resource is not initialized (unfunded / zero balance).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

**All 5 multisig contracts are 2-of-2 and healthy.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `https://testnet.mnx.fi` serves a Next.js SPA. No `/api/markets` or `/api/v1/markets` endpoint returns structured data without browser-side JS execution. `mnx_snapshots` table has 0 rows.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 42 |
| repo_snapshots | 942 |
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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,566 stars — flagship ML toolkit for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most-used ML pipeline framework
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark
- **All 5 Hamming multisigs**: 2-of-2 signatures, all healthy on Aptos mainnet
- **28 swarm wallets**: All have zero/uninitialized APT CoinStore resources
