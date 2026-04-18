# World-Increment Sweep + Hamming Snapshot — 2026-04-18

## Sweep Metadata
- **Date:** 2026-04-18T07:10 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 31 |
| Total Repo Snapshots (cumulative) | 1,004 |
| Repos This Sweep | 60 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Healthy | 5/5 |

---

## GF(3) Color Chain (This Sweep)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | **ERGODIC** | 9 |
| +1 | `#b8bb26` | **PLUS** | 11 |
| -1 | `#cc241d` | **MINUS** | 11 |

GF(3) rule: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

---

## JOB 1: GitHub Social Graph Sweep

### Recent Events (bmorphism + zubyul)

| Event | Repo | Actor | Timestamp |
|-------|------|-------|-----------|
| PullRequestEvent | plurigrid/gorj | zubyul | 2026-04-18T06:18:28Z |
| CreateEvent | plurigrid/gorj | zubyul | 2026-04-18T06:18:16Z |
| PullRequestEvent | plurigrid/gorj | zubyul | 2026-04-18T04:39:58Z |
| CreateEvent | plurigrid/gorj | zubyul | 2026-04-18T04:39:45Z |
| PullRequestEvent | plurigrid/gorj | zubyul | 2026-04-18T02:14:03Z |
| PushEvent | plurigrid/reafference | bmorphism | 2026-04-15T12:43:38Z |
| CommitCommentEvent | plurigrid/nash-portal | bmorphism | 2026-04-15T08:37:24Z |
| PushEvent | plurigrid/nash-portal | bmorphism | 2026-04-15T05:39:52Z |

### Repos This Sweep by Source

| Org/User | Type | Repos | Total Stars |
|----------|------|-------|-------------|
| kubeflow | org | 14 | 14,297 |
| migalkin | user | 3 | 124 |
| bmorphism | user | 5 | 66 |
| plurigrid | org | 20 | 25 |
| TeglonLabs | org | 7 | 5 |
| zubyul | user | 4 | 1 |
| wasita | user | 2 | 1 |
| kristinezheng | user | 1 | 0 |
| M1shaaa | user | 2 | 0 |
| DJedamski | user | 1 | 0 |
| AustinCStone | user | 1 | 0 |
| **TOTAL** | | **60** | **14,519** |

### Top Repos by Stars (This Sweep)

| Repo | Language | Stars | Forks | Pushed |
|------|----------|-------|-------|--------|
| kubeflow/pipelines | Python | 4,121 | 1,985 | 2026-04-17 |
| kubeflow/spark-operator | Python | 3,117 | 1,481 | 2026-04-16 |
| kubeflow/trainer | Go | 2,085 | 945 | 2026-04-17 |
| kubeflow/katib | Python | 1,679 | 521 | 2026-04-14 |
| kubeflow/manifests | YAML | 1,010 | 1,067 | 2026-04-11 |
| kubeflow/arena | Go | 810 | 190 | 2026-04-16 |
| kubeflow/kale | Python | 682 | 156 | 2026-04-16 |
| kubeflow/model-registry | Go | 172 | 180 | 2026-04-17 |
| kubeflow/mcp-apache-spark-history-server | Python | 151 | 52 | 2026-04-17 |
| migalkin/StarE | Python | 89 | 16 | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2 | 2026-03-16 |
| plurigrid/asi | HTML | 17 | 5 | 2026-04-13 |

### Notable plurigrid Activity
- **gorj** (this repo): zubyul active with 3 PRs + 2 branch creates today (2026-04-18)
- **nash-portal**: bmorphism pushing + commenting 2026-04-15
- **reafference**: new repo created 2026-04-15

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet — Wallet Balances

All 28 Hamming swarm addresses probed via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. All returned `resource_not_found` — addresses exist on chain but hold no APT in the standard coin store (may hold other assets or be unfunded).

**Swarm total: 0.0 APT across 28 addresses (alice, bob, A–Z)**

### Multisig Contract Probes

All 5 multisig pairs resolved via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | **2** | ✓ healthy |
| A-G | 0xf56c4a1c... | **2** | ✓ healthy |
| Y-Z | 0xd3ffe181... | **2** | ✓ healthy |
| S-T | 0x3b1c3ae9... | **2** | ✓ healthy |
| V-W | 0x40fad7b4... | **2** | ✓ healthy |

**5/5 multisig contracts healthy — all require 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` serves a Next.js SPA. No public JSON API endpoints respond without JS execution. Market data unavailable — recorded as `N/A` in mnx_snapshots.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
