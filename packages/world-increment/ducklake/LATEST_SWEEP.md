# World-Increment Sweep + Hamming Snapshot — 2026-05-31

## Sweep Metadata
- **Date:** 2026-05-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 414 |
| Total Repo Snapshots | 1,335 (cumulative) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1 — GitHub Social Graph Sweep

### Sources & Repo Counts

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 48 | 101,882 |
| migalkin | user (zubyul graph) | 19 | 834 |
| bmorphism | user | 100 | 509 |
| AustinCStone | user (zubyul graph) | 40 | 324 |
| plurigrid | org | 100 | 154 |
| zubyul | user | 49 | 40 |
| DJedamski | user (zubyul graph) | 6 | 17 |
| TeglonLabs | org | 4 | 14 |
| wasita | user (zubyul graph) | 11 | 11 |
| kristinezheng | user (zubyul graph) | 6 | 0 |
| M1shaaa | user (zubyul graph) | 8 | 0 |
| **TOTAL** | | **391** | **103,785** |

### Notable Repos
| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,695 | — | 2026-05-24 |
| kubeflow/pipelines | 4,149 | Python | 2026-05-31 |
| kubeflow/spark-operator | 3,124 | Python | 2026-05-29 |
| kubeflow/trainer | 2,109 | Go | 2026-05-30 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 23 | HTML | 2026-04-26 |
| plurigrid/gorj | 0 (281 issues) | Clojure | 2026-05-31 |

### GF(3) Chain Distribution (this sweep)
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 137 |
| +1 | PLUS | #b8bb26 | 139 |
| -1 | MINUS | #cc241d | 138 |

**GF(3) rule:** `id mod 3 == 0` → ERGODIC, `mod 3 == 1` → PLUS, `mod 3 == 2` → MINUS

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (alice–Z, 28 addresses)
All 28 wallets queried via `fullnode.mainnet.aptoslabs.com/v1`. All return **0.00 APT** — accounts uninitialized or empty CoinStore at snapshot time.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | 0.00 |
| bob | 0x0a3c…2d5d | 0.00 |
| A | 0x8699…9d7a | 0.00 |
| B–Z | 0x3f89…97c | 0.00 (all) |

### Multisig Contract Probes (Aptos Mainnet)
All 5 contracts healthy — `0x1::multisig_account::num_signatures_required` returned 2 for all.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
SPA (Next.js) — no machine-readable JSON API found at `/api/markets` or `/api/v1/markets`. **Status: unavailable.**

---

## DuckDB Schema

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
