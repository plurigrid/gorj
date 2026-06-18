# World Increment Sweep + Hamming Snapshot

**Date:** 2026-06-18  
**DB:** `ducklake/world-increments.duckdb` (DuckDB v1.5.4)

---

## GitHub Social Graph Sweep

### Sources

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| DJedamski | user (zubyul graph) | 6 |
| wasita | user (zubyul graph) | 11 |
| kristinezheng | user (zubyul graph) | 5 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 40 |
| **TOTAL** | | **391** |

### GF(3) Color Chain

| trit | name | color | world_increments |
|------|------|-------|-----------------|
| 0 | ERGODIC | `#d3869b` | 137 |
| 1 | PLUS | `#b8bb26` | 139 |
| -1 | MINUS | `#cc241d` | 138 |

**Total world_increments:** 414  
**Total repo_snapshots rows:** 1335 (each repo triple-tagged across GF3 classes)

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15734 | — |
| kubeflow/pipelines | 4154 | Python |
| kubeflow/katib | 2376 | Go |
| kubeflow/training-operator | 1792 | Go |
| kubeflow/kfserving | 1572 | Python |

---

## Hamming Swarm Snapshot (Aptos Mainnet)

**API:** `https://fullnode.mainnet.aptoslabs.com/v1`  
**Queried:** 28 named addresses (alice, bob, A–Z)

### Wallet Balances

All 28 wallets returned **0.0 APT** (mainnet named addresses not seeded).

| Label | Address (truncated) | APT |
|-------|---------------------|-----|
| alice | `0xeaa...` | 0.0 |
| bob | `0x1c9...` | 0.0 |
| A | `0x869...` | 0.0 |
| B | `0x3f8...` | 0.0 |
| C | `0x38b...` | 0.0 |
| D | `0xf77...` | 0.0 |
| E | `0xdc1...` | 0.0 |
| … (21 more) | | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (sigs_required = 2).

| Pair | Address (truncated) | sigs_required | status |
|------|---------------------|---------------|--------|
| A-B | `0x0da...` | 2 | HEALTHY |
| A-G | `0xf56...` | 2 | HEALTHY |
| Y-Z | `0xd3f...` | 2 | HEALTHY |
| S-T | `0x3b1...` | 2 | HEALTHY |
| V-W | `0x40f...` | 2 | HEALTHY |

---

## MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — Vercel authentication wall active on testnet endpoint.  
`mnx_snapshots` table created but empty.

---

## DuckDB Tables

```
world_increments    414 rows  — GF3-tagged sweep events
repo_snapshots     1335 rows  — per-repo metadata (stars, forks, language, pushed_at)
aptos_snapshots      28 rows  — wallet balance snapshots
multisig_probes       5 rows  — multisig sig-threshold probes
mnx_snapshots         0 rows  — MNX market data (unavailable)
```

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
