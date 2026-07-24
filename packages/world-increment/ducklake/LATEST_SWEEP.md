# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 37 (IDs 1–26, this run added 13–26) |
| Total Repo Snapshots | 1,283 (+339 this run) |
| Aptos Addresses Snapshotted | 28 |
| Multisig Probes | 5 (all healthy) |
| MNX Markets | 0 (SPA, no REST API) |

---

## GF(3) Color Chain — This Sweep (IDs 13–26)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow (org) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs (org) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin (social) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski (social) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita (social) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng (social) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa (social) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone (social) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 24 | hamming_swarm (aptos) | balance_sweep | 0 | `#d3869b` | **ERGODIC** |
| 25 | multisig (aptos) | probe_sweep | +1 | `#b8bb26` | **PLUS** |
| 26 | testnet.mnx.fi (mnx) | market_sweep | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## JOB 1: GitHub Social Graph — Top Repos This Sweep

| Repo | Stars | Forks | Language | Last Push |
|------|-------|-------|----------|-----------|
| kubeflow/kubeflow | 15,791 | 2,686 | — | 2026-07-10 |
| kubeflow/pipelines | 4,169 | 2,056 | Python | 2026-07-24 |
| kubeflow/spark-operator | 3,143 | 1,504 | Python | 2026-07-17 |
| kubeflow/trainer | 2,153 | 994 | Go | 2026-07-24 |
| kubeflow/katib | 1,692 | 532 | Python | 2026-07-22 |
| migalkin/NodePiece | 144 | 21 | Python | 2026-05-07 |
| migalkin/StarE | 89 | 16 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | 30 | Python | 2025-03-03 |
| TeglonLabs/mathpix-gem | 2 | 0 | Ruby | 2026-01-01 |
| TeglonLabs/jank-crane | 0 | 0 | C++ | 2026-06-08 |

### Repo Counts by Source (this sweep)

| Source | Type | Repos (this sweep) |
|--------|------|--------------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | social | 8 |
| wasita | social | 7 |
| migalkin | social | 7 |
| TeglonLabs | org | 5 |
| kristinezheng | social | 5 |
| DJedamski | social | 5 |
| M1shaaa | social | 4 |
| **TOTAL** | | **339** |

### Notable Activity
- **kubeflow**: pipelines, trainer, community-distribution all pushed 2026-07-23/24 — active
- **plurigrid** & **bmorphism** both at 100-repo cap, latest pushes 2026-07-24
- **wasita**: active Svelte/TypeScript portfolio (wasita.github.io, wm-cv), pushed 2026-07-21
- **TeglonLabs/jank-crane**: new C++ converged-IR hub (crane-jank + GF3 loopify pass) — 2026-06-08

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (ID 24 — ERGODIC #d3869b)

28 addresses queried (alice, bob, A–Z). All returned **0.0 APT** via mainnet fullnode — accounts not holding `0x1::aptos_coin::AptosCoin` resources (uninitialized or empty).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B–Z | (24 addresses) | 0.0 each |

### Multisig Contract Probes (ID 25 — PLUS #b8bb26)

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy. 2-of-N threshold confirmed across all pairs.**

### MNX Markets (ID 26 — MINUS #cc241d)

`testnet.mnx.fi` returned HTTP 200 but serves a Next.js SPA. No `/api/markets` JSON endpoint available headlessly. **mnx_snapshots: 0 rows.**

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
