# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-01
**Agent:** world-increment-sweep + hamming-swarm-snapshot
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 96 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 12 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 20 |
| **TOTAL** | | **319** |

### Notable Active Repos (pushed within 30 days of run date)
- `plurigrid/gorj` — Clojure · 1⭐ · 1567 open issues · pushed 2026-08-01 (this repo)
- `kubeflow/katib` — Python · 1694⭐ · Automated ML on Kubernetes · pushed 2026-08-01
- `kubeflow/pipelines` — Python · 4173⭐ · 2073 forks · pushed 2026-08-01
- `kubeflow/kubeflow` — 15803⭐ · flagship ML platform · pushed 2026-07-10
- `kubeflow/spark-operator` — Python · 3142⭐ · pushed 2026-07-31
- `bmorphism/Gay.jl` — Julia · 188 open issues · pushed 2026-07-21
- `bmorphism/anti-bullshit-mcp-server` — JavaScript · 22⭐ · pushed 2026-07-12
- `plurigrid/asi` — HTML · 58⭐ · "everything is topological chemputer!" · pushed 2026-07-10
- `TeglonLabs/jank-crane` — C++ · GF3 convergence maps · pushed 2026-06-08

### Top Repos by Stars (This Run)
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15803 | — |
| kubeflow/pipelines | 4173 | Python |
| kubeflow/spark-operator | 3142 | Python |
| kubeflow/trainer | 2165 | Go |
| kubeflow/katib | 1694 | Python |
| kubeflow/community-distribution | 1029 | YAML |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/NodePiece | 144 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| migalkin/StarE | 89 | Python |

### DuckDB Ducklake State
- **world_increments:** 346 rows (cumulative, GF3 color-chained)
- **repo_snapshots:** 1267 rows (cumulative across sweeps)
- **This run inserted:** 323 new increment+snapshot pairs

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 Hamming swarm addresses queried against `fullnode.mainnet.aptoslabs.com`.
**All wallets returned 0.0 APT** — CoinStore resources not initialized or unfunded.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

Full address list stored in `aptos_snapshots` table (28 rows).

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

All 5 multisig contracts are live on Aptos mainnet, requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: SPA frontend reachable, REST API unavailable.**
`/api/markets` and `/api/v1/markets` return Next.js HTML shell.
Market data is loaded client-side — not accessible via headless fetch.
`mnx_snapshots` table: 0 rows (noted as unavailable).

---

## DuckDB Schema Summary

```
world_increments  → 346 rows  (GF3 trit-colored world events, cumulative)
repo_snapshots    → 1267 rows (GitHub repo metadata across all sweeps)
aptos_snapshots   →   28 rows (Hamming swarm balances, this run)
multisig_probes   →    5 rows (A-B, A-G, Y-Z, S-T, V-W — all healthy, sigs=2)
mnx_snapshots     →    0 rows (SPA, no API endpoint found)
```

DB path: `packages/world-increment/ducklake/world-increments.duckdb`
