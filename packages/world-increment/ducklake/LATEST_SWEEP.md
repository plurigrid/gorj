# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-31

## Sweep Metadata
- **Date:** 2026-07-31 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos Ledger Version:** 6541437976 (epoch 16734, block 937971139)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 343 |
| Total Repo Snapshots (cumulative) | 1264 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 pairs |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source (this run: 320 new entries)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | social_graph | 41 |
| migalkin | social_graph | 19 |
| wasita | social_graph | 12 |
| M1shaaa | social_graph | 8 |
| TeglonLabs | org | 5 |
| kristinezheng | social_graph | 5 |
| DJedamski | social_graph | 6 |
| **TOTAL this run** | | **394** |

### Notable Recent Activity
- **wasita/wasita.github.io** (Svelte, pushed 2026-07-21): active personal site, 8 open issues
- **AustinCStone/byteruckus** (HTML, pushed 2026-07-15): newest repo in social graph
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): GF3 convergence maps hub
- **migalkin/StarE** (Python, 89⭐, pushed 2026-04-16): Hyper-relational KG message passing
- **AustinCStone/StereoVisionMRF** (Python, 11⭐, pushed 2026-04-01): MRF stereo depth

### GF(3) Color Chain Distribution (cumulative)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 113 |
| +1 | #b8bb26 | PLUS | 115 |
| -1 | #cc241d | MINUS | 115 |

GF(3) assignment: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)
All 28 Hamming swarm wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
These addresses do not have a registered legacy CoinStore; APT may be held via FA (fungible asset) store or accounts may be inactive.

**All 28 wallets: 0.0 APT (no CoinStore registered)**

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes — ALL HEALTHY
All 5 multisig pairs have `num_signatures_required = 2` (2-of-2 multisig).

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Unavailable** — `testnet.mnx.fi` returns a Next.js SPA; paths `/api/markets` and `/api/v1/markets` return no structured data. `mnx_snapshots` table: 0 rows.

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
