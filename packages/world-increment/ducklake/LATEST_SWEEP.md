# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-28

## Sweep Metadata
- **Date:** 2026-06-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | Stars | Latest Push |
|--------|------|-------|-------|-------------|
| kubeflow | org | 48 | 34,272 | 2026-06-27 |
| migalkin | social | 19 | 280 | 2025-08-04 |
| bmorphism | user | 100 | 247 | 2026-06-28 |
| AustinCStone | social | 40 | 108 | 2026-02-11 |
| plurigrid | org | 100 | 77 | 2026-06-28 |
| zubyul | user | 49 | 14 | 2026-04-24 |
| wasita | social | 11 | 5 | 2026-06-25 |
| DJedamski | social | 6 | 3 | 2018-03-07 |
| TeglonLabs | org | 5 | 2 | 2026-06-08 |
| kristinezheng | social | 5 | 0 | 2026-06-07 |
| M1shaaa | social | 8 | 0 | 2026-06-28 |
| **TOTAL** | | **391** | **35,008** | |

### Top Repos by Stars

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15,750 | 2,680 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,158 | 2,013 | 2026-06-27 |
| kubeflow/spark-operator | Python | 3,129 | 1,491 | 2026-06-26 |
| kubeflow/trainer | Go | 2,125 | 972 | 2026-06-26 |
| kubeflow/katib | Python | 1,687 | 527 | 2026-06-23 |
| kubeflow/examples | Jsonnet | 1,460 | 756 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,028 | 1,065 | 2026-06-25 |
| kubeflow/arena | Go | 814 | 192 | 2026-06-26 |
| kubeflow/kale | Python | 694 | 156 | 2026-06-25 |
| kubeflow/mpi-operator | Go | 528 | 236 | 2026-06-25 |
| migalkin/NodePiece | Python | 144 | 21 | 2022-02-02 |
| TeglonLabs/jank-crane | C++ | 0 | 0 | 2026-06-08 |

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | #d3869b | 130 |
| PLUS | 1 | #b8bb26 | 131 |
| MINUS | -1 | #cc241d | 130 |

### Notable Highlights
- **kubeflow/kubeflow**: 15,750 stars (+185 since Apr sweep) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,158 stars (+39) — ML pipeline framework, pushed 2026-06-27
- **kubeflow/spark-operator**: 3,129 stars (+18) — Apache Spark on Kubernetes, pushed 2026-06-26
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **plurigrid**: still most-active org with pushes today (2026-06-28)
- **M1shaaa/M1shaaa**: profile repo pushed 2026-06-28 13:38 UTC (active today)
- **TeglonLabs/jank-crane**: new C++ repo since April — GF3 convergence maps + jank compiler

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

All 28 Hamming-space wallet addresses queried against Aptos mainnet
(`fullnode.mainnet.aptoslabs.com`). None have a `CoinStore<AptosCoin>`
resource — these are **unfunded / inactive** accounts on-chain.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...c7b | 0 |
| bob | 0x0a3c...5d | 0 |
| A | 0x8699...9d7a | 0 |
| B | 0x3f89...b13 | 0 |
| C | 0x38b9...35e | 0 |
| D | 0xf776...dd1 | 0 |
| E | 0xdc1d...d36 | 0 |
| F | 0x18a1...f71 | 0 |
| G | 0x69a3...f32 | 0 |
| H | 0xce67...00f | 0 |
| I | 0x070f...fc9 | 0 |
| J | 0x4d96...f54 | 0 |
| K | 0xa732...dc4 | 0 |
| L | 0x7c2e...ba9 | 0 |
| M | 0x6fed...2e9 | 0 |
| N | 0xe7dd...b2c | 0 |
| O | 0x7325...89d | 0 |
| P | 0x6218...948 | 0 |
| Q | 0xac40...a9 | 0 |
| R | 0x7ce6...e10 | 0 |
| S | 0xb875...386 | 0 |
| T | 0x3578...588 | 0 |
| U | 0x7586...956 | 0 |
| V | 0xb59d...2c3 | 0 |
| W | 0x5f32...7b0 | 0 |
| X | 0xa95c...47d | 0 |
| Y | 0xd8e3...4c4 | 0 |
| Z | 0x7af0...97c | 0 |

**Total swarm liquidity:** 0 APT (all accounts inactive on mainnet)

### Multisig Contract Probes

All 5 multisig accounts on Aptos mainnet healthy — `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...003 | 2 | ✓ |
| A-G | 0xf56c4a1c...096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...883 | 2 | ✓ |
| V-W | 0x40fad7b4...6d | 2 | ✓ |

All multisig contracts healthy — consistent 2-of-N threshold across swarm.

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — `testnet.mnx.fi` and all probed API paths
(`/api/markets`, `/api/v1/markets`, `/api/tickers`) return Vercel
authentication gate. No market data extractable without bypass token.
`mnx_snapshots` table: 0 rows.

---

## DuckDB Schema

```sql
-- 391 rows: one per GitHub repo snapshotted, with GF(3) color chain
world_increments (id, timestamp, gf3_trit, gf3_color, gf3_name,
                  source_type, source_name, event_type, repo_name,
                  actor, snapshot_hash)

-- 391 rows: full repo metadata
repo_snapshots (id, timestamp, increment_id, org_or_user, repo_name,
                full_name, language, stars, forks, open_issues,
                pushed_at, description)

-- 28 rows: Aptos Hamming swarm wallet balances
aptos_snapshots (timestamp, world, address, balance_apt)

-- 5 rows: Aptos multisig contract probes
multisig_probes (timestamp, pair, address, sigs_required, healthy)

-- 0 rows: MNX market data (unavailable — Vercel auth gate)
mnx_snapshots (timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
