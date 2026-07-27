# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-27

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| AustinCStone | social | 30 |
| wasita | social | 12 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| DJedamski | social | 6 |
| **TOTAL** | | **383** |

### Activity Summary

Most recently pushed (2026-07-27):
- `plurigrid/gorj` (2026-07-27T09:17:16Z)
- `kubeflow/pipelines` (2026-07-27T03:53:12Z)
- `kubeflow/trainer` (2026-07-27T03:12:06Z)
- `bmorphism/Gay.jl` (2026-07-27T02:46:40Z)
- `M1shaaa/M1shaaa` (2026-07-27T02:35:41Z)

### Stars / Forks by Source

| Source | Repos | Total Stars | Max Stars | Total Forks |
|--------|-------|-------------|-----------|-------------|
| kubeflow | 49 | 34,411 | 15,791 (pipelines) | 13,781 |
| migalkin | 19 | 279 | 144 | 48 |
| bmorphism | 100 | 246 | 61 | 73 |
| AustinCStone | 30 | 108 | 92 | 36 |
| plurigrid | 100 | 103 | 51 | 49 |
| zubyul | 49 | 14 | 2 | 2 |
| wasita | 12 | 5 | 2 | 1 |
| TeglonLabs | 5 | 2 | 2 | 2 |
| DJedamski | 6 | 3 | 1 | 1 |
| kristinezheng | 5 | 0 | 0 | 0 |
| M1shaaa | 8 | 0 | 0 | 0 |

### Top Languages

| Language | Repos |
|----------|-------|
| Python | 77 |
| Rust | 26 |
| JavaScript | 24 |
| TypeScript | 22 |
| HTML | 18 |
| Go | 15 |
| Jupyter Notebook | 14 |
| Clojure | 14 |
| Julia | 9 |
| Jsonnet | 7 |

### GF(3) Color Chain Distribution

| GF3 Trit | Name | Color | Count |
|----------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 127 |
| 1 | PLUS | #b8bb26 | 128 |
| -1 | MINUS | #cc241d | 128 |

**Rule:** id%3==0 → ERGODIC (#d3869b), id%3==1 → PLUS (#b8bb26), id%3==2 → MINUS (#cc241d)

GF(3) chain covers 383 world-increments (127 ERGODIC + 128 PLUS + 128 MINUS = 42.6 full cycles)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

Method: `0x1::coin::balance` view function via POST /v1/view

| World | Balance (APT) |
|-------|--------------|
| bob | 12.657007 |
| F | 1.960516 |
| L | 1.927269 |
| J | 1.895093 |
| alice | 0.436434 |
| O | 0.210136 |
| K | 0.161961 |
| P | 0.140136 |
| M | 0.112285 |
| N | 0.106121 |
| Q | 0.103240 |
| S | 0.091788 |
| R | 0.090217 |
| T | 0.073713 |
| U | 0.055773 |
| A | 0.051767 |
| V | 0.048833 |
| Y | 0.044449 |
| X | 0.042577 |
| W | 0.040705 |
| B | 0.036256 |
| Z | 0.024268 |
| D | 0.011629 |
| C | 0.010185 |
| E | 0.009372 |
| H | 0.001681 |
| G | 0.000681 |
| I | 0.000681 |

**Total across 28 addresses: 20.3448 APT**

Notable: `bob` holds ~62% of total swarm APT (12.66 APT). `F`, `L`, `J` each hold ~1.9 APT.

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...4987003 | 2 | ✅ |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✅ |
| Y-Z | 0xd3ffe181...e75b883 | 2 | ✅ |
| S-T | 0x3b1c3ae9...ded7883 | 2 | ✅ |
| V-W | 0x40fad7b4...c80eb6d | 2 | ✅ |

All 5 multisig contracts healthy — 2-of-N signature threshold confirmed for each pair.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — site is a Next.js SPA with no accessible REST API endpoint. All HTTP requests return HTML shell; market data is rendered client-side and not extractable via curl/API.

---

## DuckDB Schema

Path: `packages/world-increment/ducklake/world-increments.duckdb`

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

| Table | Rows |
|-------|------|
| world_increments | 383 |
| repo_snapshots | 383 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

---

## Notable Highlights

- **kubeflow/pipelines**: 15,791 stars — pushed today (2026-07-27), most active kubeflow repo
- **bmorphism/Gay.jl**: pushed today — active Julia development
- **migalkin/NodePiece**: 144 stars — KG embeddings research top repo
- **plurigrid/gorj**: this repo, pushed today — most recently updated in the plurigrid org
- **TeglonLabs/jank-crane**: C++ crane-jank converged-IR hub with GF3 convergence maps — newest TeglonLabs repo (2026-06-08)
- **Hamming swarm**: total 20.34 APT across 28 Aptos mainnet wallets; bob dominates with 12.66 APT
- **All multisigs healthy**: 5/5 pairs respond with sigs_required=2
