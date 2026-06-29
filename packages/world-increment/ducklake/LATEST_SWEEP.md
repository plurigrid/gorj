# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-29

## Sweep Metadata
- **Date:** 2026-06-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 361 |
| Total Repo Snapshots | 361 |
| Sources Covered | 3 orgs + 9 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution (361 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 120 |
| +1 | `#b8bb26` | PLUS | 121 |
| -1 | `#cc241d` | MINUS | 120 |

GF(3) assignment: `id%3==0` → ERGODIC · `id%3==1` → PLUS · `id%3==2` → MINUS

---

## JOB 1: GitHub Social Graph Sweep

### Source Counts

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 78 |
| kubeflow | org | 48 | 34,277 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| AustinCStone | social-graph user | 40 | 108 |
| DJedamski | social-graph user | 6 | 3 |
| wasita | social-graph user | 11 | — |
| kristinezheng | social-graph user | 5 | 0 |
| M1shaaa | social-graph user | 8 | 0 |
| **TOTAL** | | **361** | **34,729** |

### Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,750 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,160 | 2026-06-29 |
| kubeflow/spark-operator | Python | 3,129 | 2026-06-26 |
| kubeflow/trainer | Go | 2,127 | 2026-06-26 |
| kubeflow/katib | Python | 1,687 | 2026-06-23 |
| kubeflow/examples | Jsonnet | 1,460 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,028 | 2026-06-29 |
| kubeflow/arena | Go | 814 | 2026-06-29 |
| kubeflow/kale | Python | 694 | 2026-06-25 |
| kubeflow/mpi-operator | Go | 528 | 2026-06-25 |

### Notable Recent Activity (2026)

- **M1shaaa/M1shaaa**: pushed today (2026-06-29)
- **kubeflow/pipelines**, **kubeflow/arena**, **kubeflow/community-distribution**: all active today
- **TeglonLabs/jank-crane** (C++): pushed 2026-06-08 — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"
- **kristinezheng/kristinezheng.github.io**: pushed 2026-06-07
- **wasita/wasita.github.io** (Svelte): personal site pushed 2026-06-25

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-06-29)

Queried via `fullnode.mainnet.aptoslabs.com` with 1s sleep between calls.

| Status | Count |
|--------|-------|
| Addresses probed | 28 |
| Addresses with APT balance > 0 | 0 |
| Addresses with no CoinStore initialized | 28 |

All 28 addresses (alice, bob, A–Z) return 0 APT. No `CoinStore<0x1::aptos_coin::AptosCoin>` resource is initialized on any address — accounts exist on-chain but hold no liquid APT.

### Multisig Contract Probes — ALL HEALTHY

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ healthy |

All 5 multisig accounts are live and respond to `0x1::multisig_account::num_signatures_required`. All require 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` is Vercel-hosted behind authentication. The `/api/markets` and `/api/v1/markets` endpoints redirect to a Vercel auth wall requiring OIDC token or bypass token. Market data unavailable without credentials.

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
