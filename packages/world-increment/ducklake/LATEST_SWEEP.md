# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-06

## Sweep Metadata
- **Date:** 2026-06-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 413 |
| Total Repo Snapshots | 1334 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts | 5 (all healthy) |
| MNX Markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 137 |
| PLUS | +1 | `#b8bb26` | 138 |
| MINUS | -1 | `#cc241d` | 138 |

GF(3) rule: `id%3==0` → ERGODIC `#d3869b` · `id%3==1` → PLUS `#b8bb26` · `id%3==2` → MINUS `#cc241d`

---

## GitHub Social Graph: Repo Snapshots by Source

| Source | Type | Snapshots |
|--------|------|-----------|
| plurigrid | org | 300 |
| bmorphism | user | 300 |
| kubeflow | org | 142 |
| AustinCStone | user | 126 |
| TeglonLabs | org | 110 |
| zubyul | user | 97 |
| migalkin | user | 79 |
| wasita | user (social) | 71 |
| kristinezheng | user (social) | 41 |
| M1shaaa | user (social) | 40 |
| DJedamski | user (social) | 28 |
| **TOTAL** | | **1334** |

### Top Repositories by Stars

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15,706 | 2,671 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,152 | 2,005 | 2026-06-06 |
| kubeflow/spark-operator | Python | 3,125 | 1,488 | 2026-06-04 |
| kubeflow/trainer | Go | 2,112 | 964 | 2026-06-05 |
| kubeflow/katib | Python | 1,685 | 525 | 2026-06-05 |
| kubeflow/examples | Jsonnet | 1,462 | 756 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,020 | 1,065 | 2026-06-05 |

### Top Languages

| Language | Repos |
|----------|-------|
| Python | 236 |
| Rust | 57 |
| JavaScript | 53 |
| HTML | 51 |
| Go | 51 |
| TypeScript | 47 |
| Jupyter Notebook | 40 |
| Clojure | 30 |
| Jsonnet | 23 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

28 wallets queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<AptosCoin>`.
All wallets returned **0.0 APT** — CoinStore resources are uninitialized/empty on mainnet as of this sweep.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (`0x1::multisig_account::num_signatures_required`)

All 5 contracts are **on-chain, responsive, and healthy**. All require **2-of-N signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Protected by Vercel deployment authentication gate.
Both `/api/markets` and `/api/v1/markets` return auth HTML. `mnx_snapshots` table has 0 rows this sweep.
Retry requires Vercel bypass token or trusted-source OIDC configuration.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,706 stars (+141 from Apr sweep) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,152 stars — active development, pushed 2026-06-06 (today)
- **Hamming swarm wallets**: All 28 at 0.0 APT — swarm unpopulated on Aptos mainnet
- **All multisig contracts**: 2-of-N threshold confirmed on-chain, all pairs healthy
- **MNX testnet**: SPA behind Vercel auth — requires deployment bypass token
- **GF(3) balance**: ERGODIC=137, PLUS=138, MINUS=138 — near-perfect trit distribution
