# World-Increment Sweep — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | This Run | Cumulative |
|--------|----------|------------|
| New World Increments | 12 | 35 |
| New Repo Snapshots | 382 | 1,326 |
| Aptos Wallets Probed | 28 | 28 |
| Multisig Contracts Probed | 5 | 5 |
| Sources Covered | 3 orgs + 8 users | — |

---

## GF(3) Color Chain — This Run's 12 Increments (IDs 13–24)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 24 | world-increment-sweep (meta) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain continues: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Stars (This Run)

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,777 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,166 | 2026-07-14 |
| kubeflow/spark-operator | Python | 3,136 | 2026-07-13 |
| kubeflow/trainer | Go | 2,140 | 2026-07-14 |
| kubeflow/katib | Python | 1,690 | 2026-07-14 |
| kubeflow/examples | Jsonnet | 1,460 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,029 | 2026-07-13 |
| kubeflow/arena | Go | 815 | 2026-07-14 |
| kubeflow/kale | Python | 695 | 2026-07-13 |
| kubeflow/mpi-operator | Go | 529 | 2026-07-14 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| DJedamski | user | 6 |
| M1shaaa | user | 8 |
| wasita | user | 1 |
| **TOTAL** | | **382** |

---

## Notable Activity (2026-07-14)

- **plurigrid/asi**: 30 stars (↑ from 16 last run) — topological chemputer, pushed 2026-07-10
- **plurigrid/gorj**: 1,168 open issues — this very repo, actively tracking
- **wasita/wm-cv**: pushed **today** 2026-07-14T03:53 — Academic CV (Svelte+Tailwind)
- **M1shaaa/M1shaaa**: profile config pushed **today** 2026-07-14T13:26
- **kubeflow/pipelines & trainer & katib**: all pushed today — active ML platform sprint
- **TeglonLabs/jank-crane**: C++, crane-jank converged-IR hub with GF3 convergence maps

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Status:** All 28 addresses have no `CoinStore<AptosCoin>` initialized on mainnet.
Aptos API returned `resource_not_found` for all addresses — wallets exist but have never
received APT (CoinStore not initialized). Balance recorded as NULL (effectively 0 APT).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | NULL (no CoinStore) |
| bob | 0x0a3c...2d5d | NULL (no CoinStore) |
| A–Z | 0x8699…7c2e | NULL × 26 (no CoinStore) |

Ledger version at query time: **6,277,550,764** (block 898,940,083, epoch 16,535)

---

### Multisig Contract Probes (5 pairs)

All 5 multisig accounts probed successfully. All healthy at **2-of-2 signatures required**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428…7003 | **2** | ✓ |
| A-G | 0xf56c4a1c…0096 | **2** | ✓ |
| Y-Z | 0xd3ffe181…b883 | **2** | ✓ |
| S-T | 0x3b1c3ae9…7883 | **2** | ✓ |
| V-W | 0x40fad7b4…eb6d | **2** | ✓ |

All pairs require unanimous 2-of-2 signing — no degradation detected.

---

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` requires Vercel visitor password authentication.
Both `/api/markets` and `/api/v1/markets` returned HTTP 401. No market data inserted.
Requires bypass token or Vercel authentication to access.

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
- **kubeflow/kubeflow**: 15,777 stars (↑212 since April) — flagship ML platform
- **kubeflow/pipelines**: 4,166 stars, pushed today — active development
- **plurigrid/asi**: 30 stars (↑14 since April) — topological chemputer surging
- **Hamming swarm**: All 5 multisig pairs healthy at 2-of-2 — no key degradation
- **Aptos wallets**: 28 addresses tracked, CoinStore not yet initialized on mainnet
- **MNX testnet**: Vercel-protected, requires bypass token for API access
- **Increment 24**: ERGODIC — sweep_complete closing 4th GF(3) cycle of this run
