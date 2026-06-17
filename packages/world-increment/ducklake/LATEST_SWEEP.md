# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-06-17  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Total Repos | Latest Push | Top Stars |
|--------|------|-------------|-------------|-----------|
| kubeflow | org | 48 | 2026-06-17T15:55:00Z | 100,363 ⭐ cumulative |
| bmorphism | user | 104 | 2026-06-17T00:44:37Z | Gay.jl (1⭐), ocaml-mcp-sdk (61⭐) |
| plurigrid | org | 101 | 2026-06-17T15:16:34Z | asi (26⭐), ontology (8⭐) |
| zubyul | user | 49 | 2026-04-24T05:56:17Z | gay-world (1⭐) |
| TeglonLabs | org | 5 | 2026-06-08T19:03:03Z | mathpix-gem (2⭐) |
| migalkin | social | 19 | 2025-08-04T03:01:46Z | NodePiece (144⭐), StarE (89⭐) |
| DJedamski | social | 6 | 2018-03-07T12:36:09Z | — |
| wasita | social | 11 | 2026-06-15T20:15:02Z | magic-garden (2⭐) |
| kristinezheng | social | 5 | 2026-06-07T22:52:50Z | — |
| M1shaaa | social | 8 | 2026-06-17T15:17:37Z | — |
| AustinCStone | social | 40 | 2026-02-11T01:10:54Z | TextGAN (92⭐) |

### Notable Recent Activity (2026)

- **plurigrid/gorj** (this repo): 636 open issues, pushed today — most active plurigrid repo
- **plurigrid/place**: pushed 2026-06-15, TeX, 8 open issues
- **kubeflow/mcp-apache-spark-history-server**: pushed 2026-06-17, newest MCP integration
- **kubeflow/trainer**: 2115⭐, 970 forks — most starred active kubeflow repo
- **bmorphism/Gay.jl**: 187 open issues, pushed today — core GF(3) color library
- **bmorphism/satreadout**: Lean theorem prover, pushed 2026-06-15
- **TeglonLabs/jank-crane**: C++, jank+crane converged IR hub with GF3 convergence maps
- **M1shaaa/M1shaaa**: config repo pushed today (2026-06-17T15:17:37Z)
- **wasita/wasita.github.io**: Svelte personal site, pushed 2026-06-15
- **kristinezheng/kristinezheng.github.io**: pushed 2026-06-07

### GF(3) Color Chain Distribution (this run: 120 repo increments)

| GF(3) Trit | Color | Name | Count |
|-----------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 40 |
| 1 | `#b8bb26` | PLUS | 40 |
| -1 | `#cc241d` | MINUS | 40 |

### DuckDB Schema

```sql
-- world_increments: 143 total rows (120 this run + 23 prior)
-- repo_snapshots:   1064 total rows (120 this run + 944 prior)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`. All returned 0 APT — none have a `0x1::coin::CoinStore<AptosCoin>` resource registered, indicating unfunded/uninitialized accounts on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A–Z | 26 addresses | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`. All returned **2 signatures required** — all healthy.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...87003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` is behind Vercel deployment protection authentication. All routes (`/`, `/api/markets`, `/api/v1/markets`, `/api/tickers`) return 401 Vercel auth challenge. No market data retrievable without a bypass token.

---

## DuckDB Query Reference

```sql
-- Latest repo activity across the social graph
SELECT org_or_user, repo_name, pushed_at, stars
FROM repo_snapshots
ORDER BY pushed_at DESC LIMIT 20;

-- GF(3) color distribution
SELECT gf3_name, gf3_color, COUNT(*) 
FROM world_increments GROUP BY gf3_name, gf3_color;

-- Aptos swarm snapshot
SELECT world, address, balance_apt FROM aptos_snapshots;

-- Multisig health check
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
