# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 344 |
| Total Repo Snapshots (cumulative) | 1,265 |
| Repos Ingested This Run | 321 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried This Run

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 100 | 163 |
| kubeflow | org | 49 | 102,126 |
| TeglonLabs | org | 5 | 14 |
| bmorphism | user | 100 | 508 |
| zubyul | user | 49 | 40 |
| migalkin | social | 19 | 829 |
| wasita | social | 12 | 10 |
| AustinCStone | social | 30 | 319 |
| DJedamski | social | 6 | 3 |
| kristinezheng | social | 5 | 0 |
| M1shaaa | social | 8 | 0 |
| **TOTAL** | | **321** | **103,012** |

### Top Repos by Stars (this sweep)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,788 | — | 2026-07-10 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-22 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-17 |
| kubeflow/trainer | 2,153 | Go | 2026-07-22 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/StereoVisionMRF | 11 | Python | 2026-04-01 |

### Most Recently Pushed (this sweep)

| Repo | Pushed At |
|------|-----------|
| kubeflow/pipelines | 2026-07-22 |
| kubeflow/trainer | 2026-07-22 |
| wasita/wasita.github.io | 2026-07-21 |
| kubeflow/spark-operator | 2026-07-17 |
| AustinCStone/byteruckus | 2026-07-15 |
| wasita/pnas-typst-template | 2026-07-16 |

### Notable Activity
- **kubeflow/pipelines** and **kubeflow/trainer** pushed today (2026-07-22)
- **wasita/wasita.github.io** (Svelte personal site) pushed 2026-07-21 — most recent social graph activity
- **TeglonLabs/jank-crane** (C++, GF3 convergence maps) last pushed 2026-06-08
- **migalkin/kgcourse2021** last updated 2026-07-10 — Knowledge Graph course material still active

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count (cumulative) |
|------|-------|------|--------------------|
| 0 | `#d3869b` | ERGODIC | 114 |
| 1 | `#b8bb26` | PLUS | 115 |
| -1 | `#cc241d` | MINUS | 115 |

GF(3) Assignment: `id%3==0 → ERGODIC` | `id%3==1 → PLUS` | `id%3==2 → MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 hamming-swarm addresses (alice, bob, A–Z) queried via
`fullnode.mainnet.aptoslabs.com`. All return `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — **0 APT held** in native coin store.
Accounts may hold other Aptos tokens or be used for non-coin activity.

| World | Address (truncated) | Balance |
|-------|---------------------|---------|
| alice | `0xc793ac...` | 0.00 APT |
| bob | `0x0a3c00...` | 0.00 APT |
| A–Z | (26 addresses) | 0.00 APT each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts **healthy** — all configured at **2-of-N signatures required**.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | `0x0da4f428...` | 2 | ✓ Healthy |
| A-G | `0xf56c4a1c...` | 2 | ✓ Healthy |
| Y-Z | `0xd3ffe181...` | 2 | ✓ Healthy |
| S-T | `0x3b1c3ae9...` | 2 | ✓ Healthy |
| V-W | `0x40fad7b4...` | 2 | ✓ Healthy |

### MNX Markets (testnet.mnx.fi)

MNX testnet is a Next.js SPA. HTTP 200 returned for `/markets` and `/api`
routes but no JSON market data is accessible server-side. `/api/markets`
returns 404. **Market data: unavailable** (client-rendered SPA — no REST API exposed).

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
