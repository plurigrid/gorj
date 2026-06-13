# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-13

## Sweep Metadata
- **Date:** 2026-06-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 331 |
| Total Repo Snapshots | 331 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | `#b8bb26` | **PLUS** | 111 |
| -1 | `#cc241d` | **MINUS** | 110 |
| 0 | `#d3869b` | **ERGODIC** | 110 |

Near-uniform distribution across 331 repo increments (111/110/110).
Rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS.

---

## Top Repos by Stars (this sweep)

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15,720 | 2,673 | 2026-06-11 |
| kubeflow/pipelines | Python | 4,153 | 2,006 | 2026-06-12 |
| kubeflow/spark-operator | Python | 3,128 | 1,490 | 2026-06-12 |
| kubeflow/trainer | Go | 2,114 | 967 | 2026-06-13 |
| kubeflow/katib | Python | 1,683 | 527 | 2026-06-12 |
| kubeflow/examples | Jsonnet | 1,461 | 756 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,023 | 1,065 | 2026-06-12 |
| migalkin/NodePiece | Python | 144 | 21 | 2021-06-14 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2016-09-19 |
| migalkin/StarE | Python | 89 | 16 | 2020-09-17 |

## Repo Counts by Source (this sweep)

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 48 | 34,205 |
| bmorphism | user | 100 | 241 |
| migalkin | social graph | 7 | 280 |
| AustinCStone | social graph | 5 | 106 |
| plurigrid | org | 100 | 77 |
| zubyul | user | 49 | 14 |
| wasita | social graph | 6 | 5 |
| DJedamski | social graph | 4 | 3 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | social graph | 3 | 0 |
| M1shaaa | social graph | 4 | 0 |
| **TOTAL** | | **331** | **34,933** |

## Notable Activity (since last sweep)

- **kubeflow/kubeflow**: +155 stars since 2026-04-12 (15,720 vs 15,565)
- **kubeflow/pipelines**: +34 stars (4,153 vs 4,119), pushed 2026-06-12
- **TeglonLabs/jank-crane** (C++, new): pushed 2026-06-08 — crane-jank converged-IR hub with GF3 convergence maps
- **kristinezheng/kristinezheng.github.io**: pushed 2026-06-07 (very recent activity)
- **kubeflow/trainer**: pushed 2026-06-13 (active today)

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming-world wallets (alice, bob, A–Z) returned **0.0 APT**.
The Aptos fullnode returned no `CoinStore` resource — these accounts have no on-chain APT balance.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26) | (see DuckDB) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts are live and require **2 signatures** (2-of-N):

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Vercel deployment authentication required. All API paths return auth-gate HTML. `mnx_snapshots` table is empty pending access credentials.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,720 stars — flagship ML platform for Kubernetes (growing)
- **kubeflow/trainer**: Go, pushed 2026-06-13 — training operators (active today)
- **migalkin/NodePiece**: 144 stars — parameter-efficient KG representations (ICLR'22)
- **bmorphism** (100 repos): active personal graph including forks of gorj ecosystem
- **AustinCStone/bmfork**: Python, pushed 2025-05-09 — direct fork connection to bmorphism
- **Hamming swarm**: 28 addresses, all at 0 APT; 5/5 multisig contracts healthy at 2-of-N
- **MNX**: deployment-protected, monitoring recommended for future access
