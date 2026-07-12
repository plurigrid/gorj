# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-12

## Sweep Metadata
- **Date:** 2026-07-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** v1.5.4 (python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 345 |
| Total Repo Snapshots (cumulative) | 1,266 |
| New repos snapshotted this run | 322 |
| Sources covered | 3 orgs + 2 users + 6 social graph users |

### Sources Queried This Run
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 5 |
| DJedamski | social graph | 2 |
| wasita | social graph | 4 |
| kristinezheng | social graph | 2 |
| M1shaaa | social graph | 2 |
| AustinCStone | social graph | 4 |
| **TOTAL** | | **322** |

### GF(3) Color Chain Distribution (this run)
| Name | Trit | Hex | Count |
|------|------|-----|-------|
| PLUS | +1 | `#b8bb26` | 108 |
| MINUS | -1 | `#cc241d` | 107 |
| ERGODIC | 0 | `#d3869b` | 107 |

GF(3) assignment: `id mod 3 == 1 → PLUS, id mod 3 == 2 → MINUS, id mod 3 == 0 → ERGODIC`

### Top Repos by Stars (this run)
| Org/User | Repo | Language | Stars | Forks | Last Push |
|----------|------|----------|-------|-------|-----------|
| kubeflow | kubeflow | — | 15,770 | 2,685 | 2026-07-10 |
| kubeflow | pipelines | Python | 4,169 | 2,030 | 2026-07-11 |
| kubeflow | spark-operator | Python | 3,137 | 1,500 | 2026-07-12 |
| kubeflow | trainer | Go | 2,136 | 983 | 2026-07-10 |
| kubeflow | katib | Python | 1,690 | 532 | 2026-07-10 |
| migalkin | NodePiece | Python | 144 | 21 | 2026-05-07 |
| AustinCStone | TextGAN | Python | 92 | 30 | 2016 |
| migalkin | StarE | Python | 89 | 16 | 2026-04-16 |
| TeglonLabs | mathpix-gem | Ruby | 2 | 0 | 2026-01-01 |

### Notable Recent Activity (pushed since 2026-07-01)
- **kubeflow/spark-operator**: pushed 2026-07-12 — most recently active kubeflow repo
- **kubeflow/pipelines**: pushed 2026-07-11
- **migalkin/kgcourse2021**: pushed 2026-07-10 — Knowledge Graph course materials
- **wasita/wasita.github.io** (Svelte): pushed 2026-07-06 — active personal site
- **kristinezheng/kristinezheng.github.io**: pushed 2026-07-01

### TeglonLabs Highlight
- **jank-crane** (C++, pushed 2026-06-08): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow" — most recently active TeglonLabs repo

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
All 28 Hamming world addresses (alice, bob, A–Z) queried.

| Result | Count |
|--------|-------|
| 0.0000 APT (unfunded) | 28/28 |

All wallets hold 0.0000 APT. CoinStore resources exist on-chain but balances are zero.

<details>
<summary>Full address list</summary>

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793acde... | 0.0000 |
| bob | 0x0a3c00c5... | 0.0000 |
| A | 0x8699edc0... | 0.0000 |
| B | 0x3f892ebe... | 0.0000 |
| C | 0x38b99e63... | 0.0000 |
| D | 0xf7765624... | 0.0000 |
| E | 0xdc1d9d53... | 0.0000 |
| F | 0x18a14b5b... | 0.0000 |
| G | 0x69a394c0... | 0.0000 |
| H | 0xce67c327... | 0.0000 |
| I | 0x070fe5d7... | 0.0000 |
| J | 0x4d964db8... | 0.0000 |
| K | 0xa732040a... | 0.0000 |
| L | 0x7c2eaeaf... | 0.0000 |
| M | 0x6fed37a7... | 0.0000 |
| N | 0xe7dde6da... | 0.0000 |
| O | 0x73252b60... | 0.0000 |
| P | 0x62187920... | 0.0000 |
| Q | 0xac40fa50... | 0.0000 |
| R | 0x7ce605cc... | 0.0000 |
| S | 0xb8753014... | 0.0000 |
| T | 0x35781dc0... | 0.0000 |
| U | 0x75860da4... | 0.0000 |
| V | 0xb59dd817... | 0.0000 |
| W | 0x5f32aef7... | 0.0000 |
| X | 0xa95cbbd1... | 0.0000 |
| Y | 0xd8e32848... | 0.0000 |
| Z | 0x7af0ef6e... | 0.0000 |
</details>

### Multisig Contract Probes (Mainnet)
All 5 pairs healthy — 2-of-N threshold confirmed.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | healthy |
| A-G | 0xf56c4a1c... | 2 | healthy |
| Y-Z | 0xd3ffe181... | 2 | healthy |
| S-T | 0x3b1c3ae9... | 2 | healthy |
| V-W | 0x40fad7b4... | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable** — all API path probes (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/pairs`) return the SPA HTML shell. No JSON extractable without browser JS. Logged as unavailable in `mnx_snapshots`.

---

## DuckDB Tables Updated
- `world_increments` — 345 total rows
- `repo_snapshots` — 1,266 total rows
- `aptos_snapshots` — 28 new rows
- `multisig_probes` — 5 new rows
- `mnx_snapshots` — 1 row (unavailable placeholder)

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
