# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (2026-07-10 run)

| Metric | Value |
|--------|-------|
| Repos snapshotted this run | 321 |
| World increments (cumulative DB) | 344 |
| Repo snapshots (cumulative DB) | 1,265 |
| Sources covered | 3 orgs + 8 users |
| Aptos wallets probed | 28 |
| Multisig contracts probed | 5 |

**GF(3) this-run distribution:** ERGODIC 114 · PLUS 115 · MINUS 115

---

## JOB 1: GitHub Social Graph

### Sources

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 49 |
| kubeflow | org | 100 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 40 |
| **TOTAL** | | **392** |

### Top Repos by Stars

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,771 | 2,685 |
| kubeflow/pipelines | Python | 4,169 | 2,031 |
| kubeflow/spark-operator | Python | 3,136 | 1,500 |
| kubeflow/trainer | Go | 2,134 | 983 |
| migalkin/NodePiece | Python | 144 | 21 |
| AustinCStone/TextGAN | Python | 92 | 30 |
| migalkin/StarE | Python | 89 | 16 |

### Notable Activity
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub with GF3 convergence maps
- **wasita/wasita.github.io** (Svelte, pushed 2026-07-06): most recently active social node
- **kristinezheng/kristinezheng.github.io** (pushed 2026-07-01)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-10)

28 addresses probed via `fullnode.mainnet.aptoslabs.com`. **All returned 0.0 APT** — accounts are unfunded or unregistered on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes — All Healthy ✓

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts confirmed active with 2-of-2 threshold.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — Vercel password-protection active (HTTP 401 on all API paths). No market data accessible without credentials.

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
