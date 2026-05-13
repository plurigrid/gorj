# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-13  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| TeglonLabs | org | 4 |
| migalkin | user (zubyul social graph) | 11 |
| wasita | user (zubyul social graph) | 11 |
| AustinCStone | user (zubyul social graph) | 11 |
| M1shaaa | user (zubyul social graph) | 8 |
| kristinezheng | user (zubyul social graph) | 6 |
| DJedamski | user (zubyul social graph) | 6 |
| **Total** | | **354** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 118 |
| 1 | #b8bb26 | PLUS | 118 |
| -1 | #cc241d | MINUS | 118 |

### Top 15 Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,628 | — |
| kubeflow/pipelines | 4,140 | Python |
| kubeflow/spark-operator | 3,126 | Python |
| kubeflow/trainer | 2,098 | Go |
| kubeflow/katib | 1,682 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,017 | YAML |
| kubeflow/arena | 810 | Go |
| kubeflow/kale | 686 | Python |
| kubeflow/mpi-operator | 526 | Go |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 21 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |
| bmorphism/say-mcp-server | 20 | JavaScript |

### Notable Activity (recently pushed)

- **plurigrid/gorj** — pushed 2026-05-13 (today): forj + Rama topology nREPL + GF(3) gay trit coloring
- **bmorphism/Gay.jl** — pushed 2026-05-13: Wide-gamut color sampling with splittable determinism (188 open issues)
- **kubeflow/dashboard** — pushed 2026-05-13: Kubeflow Central Dashboard
- **wasita/wasita.github.io** — pushed 2026-05-13: personal website
- **migalkin/NodePiece** — 144 stars, Knowledge Graph compositional representations (ICLR 2022)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A-Z) returned **null** balance.
No `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource found on any address.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | null |
| bob | 0x0a3c...512d | null |
| A-Z | (26 addresses) | null |

### Multisig Contract Probes

All 5 multisig contracts responded healthy with **2 signatures required**:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All multisig pairs require 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)

Status: **SPA (Next.js) — no JSON API accessible**. HTTP 200 but client-rendered HTML only.
No `/api/markets` or `/api/v1/markets` endpoints returned structured data.
`mnx_snapshots` table is empty.

---

## DuckDB Schema Summary

```
world_increments   -- 354 rows (GF3-colored repo snapshot events)
repo_snapshots     -- 354 rows (full repo metadata)
aptos_snapshots    -- 28 rows (all null balances)
multisig_probes    -- 5 rows (all healthy, sigs_required=2)
mnx_snapshots      -- 0 rows (SPA, no API data)
```

## Quick Queries

```sql
-- Top repos by stars
SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 20;

-- GF3 color distribution
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1, 2;

-- Recently pushed repos
SELECT full_name, pushed_at FROM repo_snapshots ORDER BY pushed_at DESC LIMIT 10;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
