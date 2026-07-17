# World-Increment Sweep — 2026-07-17

## Sweep Metadata
- **Date:** 2026-07-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 12 (IDs 13–24) |
| Total World Increments (all time) | 35 |
| New Repo Snapshots (this run) | 394 |
| Total Repo Snapshots (all time) | 865 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Wallets with APT Balance | 0 |
| Multisig Contracts Probed | 5 |
| Healthy Multisigs (sigs_required=2) | 5/5 |
| MNX Markets | Unavailable (SPA, no JSON API) |

---

## GF(3) Color Chain — New Increments (13–24)

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
| 24 | sweep (meta) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain continues: `→ PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Stars (This Sweep)

| Rank | Repo | Language | Stars | Pushed At |
|------|------|----------|-------|-----------|
| 1 | kubeflow/kubeflow | — | 15,779 | 2026-07-10 |
| 2 | kubeflow/pipelines | Python | 4,168 | 2026-07-17 |
| 3 | kubeflow/spark-operator | Python | 3,138 | 2026-07-17 |
| 4 | kubeflow/trainer | Go | 2,151 | 2026-07-17 |
| 5 | kubeflow/katib | Python | 1,690 | 2026-07-16 |
| 6 | kubeflow/examples | Jsonnet | 1,460 | 2025-04-14 |
| 7 | kubeflow/community-distribution | YAML | 1,029 | 2026-07-17 |
| 8 | kubeflow/arena | Go | 815 | 2026-07-17 |
| 9 | kubeflow/kale | Python | 696 | 2026-07-16 |
| 10 | kubeflow/mpi-operator | Go | 530 | 2026-07-13 |

---

## Repo Counts by Source (This Sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **394** |

---

## Notable Highlights (This Sweep)

### plurigrid — top 3
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |

⬆ `plurigrid/asi` grew from 16→31 stars since last sweep (2026-04-12)

### TeglonLabs — new since last sweep
| Repo | Language | Pushed At | Description |
|------|----------|-----------|-------------|
| jank-crane | C++ | 2026-06-08 | crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps |

### wasita — most recently pushed
| Repo | Language | Pushed At |
|------|----------|-----------|
| wasita.github.io | Svelte | 2026-07-16 |

### M1shaaa — profile updated today
- `M1shaaa/M1shaaa` pushed at 2026-07-17T13:19:44Z (today)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 Hamming-swarm wallets queried at 2026-07-17. All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`, indicating **zero APT balance** (accounts exist on-chain but hold no APT in the coin store).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.000000 |
| bob | 0x0a3c00... | 0.000000 |
| A–Z (26) | various | 0.000000 each |

### Multisig Contract Health — All 5 HEALTHY ✓

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3a... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7... | 2 | ✓ HEALTHY |

All multisig contracts require exactly 2 signatures — consistent with a 2-of-N Hamming-pair design.

### MNX Markets (testnet.mnx.fi)

Testnet endpoint returns an SPA shell (no JSON data API discoverable). Logged as `MNX_UNAVAILABLE` in `mnx_snapshots`. Will retry in next sweep with additional path probing.

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

## Delta vs 2026-04-12 Sweep
- plurigrid/asi: 16 → 31 stars (+15)
- kubeflow/kubeflow: 15,565 → 15,779 stars (+214)
- kubeflow/pipelines: 4,119 → 4,168 stars (+49)
- kubeflow/trainer: 2,080 → 2,151 stars (+71)
- TeglonLabs/jank-crane: **NEW** (created 2026-06-08)
- All multisig contracts: healthy, sigs_required=2 (unchanged)
- Aptos swarm: all wallets at 0 APT (unchanged)
