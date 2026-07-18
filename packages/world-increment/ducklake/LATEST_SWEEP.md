# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-18

## Sweep Metadata
- **Date:** 2026-07-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 378 |
| Total Repo Snapshots | 378 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain

378 increments, each assigned by `id % 3`:
- trit=0 → **ERGODIC** `#d3869b` (126 rows)
- trit=1 → **PLUS** `#b8bb26` (126 rows)
- trit=-1 → **MINUS** `#cc241d` `#cc241d` (126 rows)

---

## Repo Counts by Source (2026-07-18 snapshot)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 30 |
| migalkin | user | 19 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **378** |

## Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15779 | 2026-07 |
| kubeflow/pipelines | Python | 4168 | 2026-07-18 |
| kubeflow/spark-operator | Go | 3138 | 2026-07 |
| kubeflow/trainer | Go | 2151 | 2026-07-18 |
| kubeflow/katib | Go | 1691 | 2026-07 |
| plurigrid/asi | HTML | 31 | 2026-07-10 |

## Recently Active Repos

| Repo | Language | Last Push |
|------|----------|-----------|
| plurigrid/gorj | Clojure | 2026-07-18 |
| M1shaaa/M1shaaa | — | 2026-07-18 |
| kubeflow/trainer | Go | 2026-07-18 |
| kubeflow/sdk | Python | 2026-07-18 |
| wasita/wasita.github.io | Svelte | 2026-07-16 |
| bmorphism/gay-chat | Scheme | 2026-07-14 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming swarm wallets (alice, bob, A–Z) probed against `fullnode.mainnet.aptoslabs.com`.

**Result: All wallets report 0.000 APT** — no APT CoinStore resources found at these addresses on mainnet as of 2026-07-18.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

**All 5 multisig contracts healthy** — 2-of-N threshold confirmed on each.

### MNX Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` returns a Vercel authentication wall. No market data accessible from this environment.

---

## DuckDB Schema

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

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

| Table | Rows |
|-------|------|
| world_increments | 378 |
| repo_snapshots | 378 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
