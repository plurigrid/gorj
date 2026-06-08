# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-08

## Sweep Metadata
- **Date:** 2026-06-08
- **Branch:** world-increment/sweep-2026-06-08-1308
- **DuckDB version:** v1.5.3
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this sweep) | 118 (IDs 13–130) |
| New Repo Snapshots (this sweep) | 118 (IDs 474–591) |
| Total World Increments (cumulative) | 141 |
| Total Repo Snapshots (cumulative) | 1062 |
| Aptos Wallet Snapshots | 28 |
| Multisig Probes | 5 |
| MNX Market Snapshots | 0 (unavailable) |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 21 |
| kubeflow | org | 19 |
| bmorphism | user | 18 |
| zubyul | user | 13 |
| wasita | user (social) | 11 |
| M1shaaa | user (social) | 8 |
| DJedamski | user (social) | 6 |
| AustinCStone | user (social) | 6 |
| migalkin | user (social) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (social) | 5 |
| **TOTAL** | | **118** |

### GF(3) Trit Color Chain

World increments IDs 13–130 assigned via `id % 3`:

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 40 |
| 1 | `#b8bb26` | PLUS | 40 |
| -1 | `#cc241d` | MINUS | 38 |

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried 28 addresses (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`.
All 28 addresses returned 0.0 APT — Hamming-swarm derived addresses not funded on mainnet.

| World | Balance (APT) |
|-------|---------------|
| alice | 0.0 |
| bob | 0.0 |
| A–Z (26 wallets) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts healthy, 2-of-N threshold confirmed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428...` | 2 | true |
| A-G | `0xf56c4a1c...` | 2 | true |
| Y-Z | `0xd3ffe181...` | 2 | true |
| S-T | `0x3b1c3ae9...` | 2 | true |
| V-W | `0x40fad7b4...` | 2 | true |

### MNX Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel authentication (password-protected). No market data obtainable.

---

## Database State After Sweep

```
repo_snapshots   : 1062 rows (prior: 944, new: 118)
world_increments :  141 rows (prior:  23, new: 118)
aptos_snapshots  :   28 rows (prior:   0, new:  28)
multisig_probes  :    5 rows (prior:   0, new:   5)
mnx_snapshots    :    0 rows (unavailable)
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
