# World-Increment Sweep + Hamming Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 34 |
| Total Repo Snapshots | 1,263 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Pairs Probed | 5 |
| MNX Markets | N/A (SPA) |

---

## GF(3) Color Chain — 34 Increments

Increments follow the GF(3) ring coloring rule:

| id%3 | Trit | Color | Name |
|------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

Sources in insertion order: plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone (+ paginated sub-increments).
GF(3) chain repeats: `ERGODIC → PLUS → MINUS → ERGODIC → ...` (34 increments = 11 full cycles + 1)

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Snapshotted | Total Stars |
|--------|------|-------------------|-------------|
| plurigrid | org | 300 | 163 |
| bmorphism | user | 300 | 508 |
| kubeflow | org | 143 | 102,124 |
| TeglonLabs | org | 111 | 14 |
| zubyul | user | 97 | 40 |
| AustinCStone | social | 89 | 308 |
| migalkin | social | 64 | 821 |
| wasita | social | 63 | 9 |
| kristinezheng | social | 38 | 0 |
| M1shaaa | social | 34 | 0 |
| DJedamski | social | 24 | 15 |
| **TOTAL** | | **1,263** | **104,002** |

### Top Repos by Stars

| Repo | Stars | Language | Notes |
|------|-------|----------|-------|
| kubeflow/kubeflow | 15,789 | — | Flagship ML platform for K8s |
| kubeflow/pipelines | 4,168 | Python | ML pipeline orchestration |
| kubeflow/spark-operator | 3,142 | Python | Spark on Kubernetes |
| kubeflow/trainer | 2,152 | Go | Distributed ML training |
| migalkin/NodePiece | 144 | Python | KG embeddings (ICLR'22) |
| migalkin/StarE | 89 | Python | Hyper-relational KG (EMNLP'20) |
| AustinCStone/TextGAN | 92 | Python | Text generation with GANs |
| migalkin/kgcourse2021 | 24 | HTML | Knowledge Graphs course materials |
| migalkin/NBFNet_mlx | 10 | Python | Neural Bellman-Ford on MLX |

### Notable Recent Pushes

| Repo | Pushed | Language | Description |
|------|--------|----------|-------------|
| wasita/wasita.github.io | 2026-07-21 | Svelte | Personal site, active dev |
| AustinCStone/byteruckus | 2026-07-15 | HTML | Newest repo |
| TeglonLabs/jank-crane | 2026-06-08 | C++ | GF3 convergence maps, loopify pass |
| wasita/pnas-typst-template | 2026-07-16 | — | PNAS paper template |
| kristinezheng/kristinezheng.github.io | 2026-07-01 | HTML | Portfolio site |
| AustinCStone/EpsteinSearch | 2026-02-11 | Python | — |
| migalkin/NBFNet_mlx | 2026-03-11 | Python | Neural Bellman-Ford on Apple Silicon |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**All 28 wallets (alice, bob, A–Z) returned HTTP 404.**

The Aptos fullnode could not find `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` for any address — these accounts either have zero APT or were never initialized with an APT CoinStore. All `balance_apt` values stored as NULL.

### Multisig Contract Probes

**All 5 multisig pairs HEALTHY — each requires 2-of-2 signatures.**

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ Healthy |
| A-G | 0xf56c...096 | 2 | ✅ Healthy |
| Y-Z | 0xd3ff...883 | 2 | ✅ Healthy |
| S-T | 0x3b1c...883 | 2 | ✅ Healthy |
| V-W | 0x40fa...b6d | 2 | ✅ Healthy |

### MNX Markets (testnet.mnx.fi)

`/api/markets` → HTTP 404. Root URL returns Next.js SPA (client-side data loading).
**Status: UNAVAILABLE** — no market data ingested this sweep cycle.

---

## Database Tables

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 34 | One per source sweep |
| repo_snapshots | 1,263 | All source repos |
| aptos_snapshots | 28 | All NULL balances (404) |
| multisig_probes | 5 | All healthy |
| mnx_snapshots | 0 | SPA, no API available |

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
