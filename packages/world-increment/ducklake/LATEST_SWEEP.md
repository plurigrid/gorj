# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-16

## Sweep Metadata
- **Date:** 2026-06-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (This Sweep — 2026-06-16)

| Metric | Value |
|--------|-------|
| Repos Snapshotted This Sweep | 331 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| World Increments (cumulative) | 354 |
| Repo Snapshots (cumulative ducklake) | 1,275 |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source (This Sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 49 |
| zubyul | user | 19 |
| migalkin | user (zubyul graph) | 40 |
| DJedamski | user (zubyul graph) | 6 |
| wasita | user (zubyul graph) | 11 |
| kristinezheng | user (zubyul graph) | 5 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 40 |
| **TOTAL** | | **331** |

### Top Repos by Stars (This Sweep)

| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/kubeflow | — | 15,725 | 2026-06-11 |
| kubeflow/pipelines | Python | 4,154 | 2026-06-16 |
| kubeflow/spark-operator | Python | 3,127 | 2026-06-15 |
| kubeflow/trainer | Go | 2,115 | 2026-06-16 |
| kubeflow/katib | Python | 1,683 | 2026-06-15 |
| migalkin/NodePiece | Python | 144 | — |
| AustinCStone/TextGAN | Python | 92 | — |
| plurigrid/asi | HTML | 26 | 2026-06-10 |
| plurigrid/gorj | Clojure | 0 | 2026-06-16 |

### Notable Highlights
- **kubeflow/kubeflow**: 15,725 stars (+160 from last sweep) — still the ML-on-Kubernetes flagship
- **kubeflow/pipelines**: 4,154 stars, pushed 2026-06-16 — active
- **plurigrid/gorj**: This very repo (617 open issues — the ducklake is busy)
- **wasita/wasita.github.io**: pushed 2026-06-15 — recently active in social graph
- **M1shaaa/M1shaaa**: pushed 2026-06-16 03:43 UTC — most recent push in zubyul social graph

### GF(3) Color Chain (per repo increment_id)
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming-swarm wallets (alice, bob, A–Z) show **0.000000 APT**.  
`CoinStore<AptosCoin>` resource not found on any address — accounts exist on-chain but hold no native APT coin.

### Multisig Contract Probes

All 5 contracts respond with **2-of-2** threshold — healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | ✓ healthy |
| A-G | 0xf56c…0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff…b883 | 2 | ✓ healthy |
| S-T | 0x3b1c…7883 | 2 | ✓ healthy |
| V-W | 0x40fa…eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection authentication.  
All paths (`/api/markets`, `/api/v1/markets`, root) return `Authentication Required`.  
`mnx_snapshots` table is empty for this sweep.

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
