# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-12T10:30:00Z  
**Branch:** world-increment/sweep-2026-06-12  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 38 |
| migalkin | social graph | 19 |
| wasita | social graph | 11 |
| AustinCStone | social graph | 20 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| **TOTAL** | | **310** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 103 |
| +1 | `#b8bb26` | PLUS | 104 |
| -1 | `#cc241d` | MINUS | 103 |

### Notable Repos

- **kubeflow/kubeflow** — 15,715 ★ — ML Toolkit for Kubernetes
- **kubeflow/pipelines** — 4,152 ★ — ML Pipelines
- **kubeflow/spark-operator** — 3,127 ★ — Kubernetes Spark operator
- **kubeflow/trainer** — 2,112 ★ — Distributed AI Model Training
- **bmorphism/ocaml-mcp-sdk** — 61 ★ — OCaml SDK for MCP
- **plurigrid/gorj** — 521 open issues — forj + Rama GF(3) routing (active)
- **bmorphism/Gay.jl** — 189 open issues — Wide-gamut color sampling
- **TeglonLabs/jank-crane** — C++ — crane-jank converged-IR hub, GF3 convergence maps (pushed 2026-06-08)
- **plurigrid/asi** — 25 ★ — topological chemputer (pushed 2026-06-10)

### DB Tables

```sql
world_increments  -- 310 rows, GF3 trit/color/name per repo snapshot
repo_snapshots    -- 310 rows, full metadata per repo
```

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

All 28 Hamming swarm addresses queried against Aptos mainnet
(`fullnode.mainnet.aptoslabs.com`). **All balances returned 0 APT** --
accounts either uninitialized or have no APT CoinStore resource.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...2d5d | 0.0 |
| A-Z   | (26 addresses) | 0.0 each |

*Full addresses stored in `aptos_snapshots` table.*

### Multisig Contract Probes

All 5 multisig contracts are **healthy** with `sigs_required = 2`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** -- `testnet.mnx.fi` is protected by Vercel
deployment authentication. All endpoints (`/`, `/api/markets`,
`/api/v1/markets`) return HTTP 200 with an auth-challenge page requiring
Vercel OIDC credentials. No market data could be extracted.

### DB Tables

```sql
aptos_snapshots  -- 28 rows (alice, bob, A-Z), all 0.0 APT
multisig_probes  -- 5 rows, all sigs_required=2, healthy=true
mnx_snapshots    -- 1 row, status=auth-protected
```

---

## DuckDB Schema Summary

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
