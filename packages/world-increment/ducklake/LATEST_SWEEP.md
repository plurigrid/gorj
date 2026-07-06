# World-Increment + Hamming Swarm Snapshot — 2026-07-06

## Sweep Metadata
- **Date:** 2026-07-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 40 |
| **TOTAL** | | **392** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,765 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,132 | Python |
| kubeflow/trainer | 2,129 | Go |
| kubeflow/katib | 1,690 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| migalkin/kgcourse2021 | 25 | HTML |
| TeglonLabs/mathpix-gem | 2 | Ruby |

### Notable New Activity
- **wasita/wasita.github.io**: pushed 2026-07-05 (yesterday) — Svelte personal site active
- **kristinezheng/kristinezheng.github.io**: pushed 2026-07-01 — HTML site recently updated
- **TeglonLabs/jank-crane**: pushed 2026-06-08 — C++ crane-jank GF3 convergence maps
- **wasita/proj-template**: pushed 2026-06-19 — new project template repo

### GF(3) Color Chain Distribution (cumulative DB)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 115 |
| +1 | `#b8bb26` | PLUS | 116 |
| -1 | `#cc241d` | MINUS | 116 |

Balanced GF(3) chain across 347 total world increments.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 wallets)

**Result:** All 28 addresses returned HTTP 404 — accounts have no `CoinStore<AptosCoin>` resource initialized on Aptos mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | N/A (404) |
| bob | 0x0a3c...12d5 | N/A (404) |
| A | 0x8699...9d7a | N/A (404) |
| B–Z | 0x3f89...–0x7af0... | N/A (404) each |

All 28 wallet records stored in `aptos_snapshots` with `balance_apt = NULL`.

### Multisig Contract Probes (5 pairs)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — HTTP 401 Unauthorized on all probed endpoints. Requires authentication credentials not available to this agent. Stored as `unavailable-401` in `mnx_snapshots`.

---

## Cumulative DB State

| Table | Rows |
|-------|------|
| world_increments | 347 |
| repo_snapshots | 1,268 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

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
- `id % 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id % 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id % 3 == 2` → trit=-1, color=#cc241d, name=MINUS
