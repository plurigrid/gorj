# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-08  
**Increment ID:** 13  
**GF(3):** trit=1 · color=#b8bb26 · name=PLUS  
**Hash:** `2f24eeb2d8e226f3cc47822c987e9cbd`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 15 |
| kubeflow | org | 13 |
| TeglonLabs | org | 5 |
| bmorphism | user | 14 |
| zubyul | user | 10 |
| migalkin | social graph | 5 |
| DJedamski | social graph | 3 |
| wasita | social graph | 6 |
| AustinCStone | social graph | 6 |
| kristinezheng | social graph | 4 |
| M1shaaa | social graph | 4 |
| **Total** | | **85 this run / 1,029 cumulative** |

### Notable Activity (pushed 2026-08-08)

| Repo | Stars | Open Issues | Notes |
|------|-------|-------------|-------|
| plurigrid/gorj | 1 | 1721 | Active today — forj + Rama topology nREPL routing |
| plurigrid/place | 3 | 18 | Active today |
| kubeflow/spark-operator | 3,145 | 122 | Active today — Kubernetes Spark operator |
| kubeflow/trainer | 2,175 | 146 | Active today — Distributed AI Model Training |
| wasita/wm-cv | 0 | 0 | Active today — Academic CV |
| wasita/xoxowasita-analysis | 0 | 0 | Active today |

### Top Repos by Stars (this sweep)

| Repo | Stars | Forks |
|------|-------|-------|
| kubeflow/kubeflow | 15,806 | 2,691 |
| kubeflow/pipelines | 4,182 | 2,084 |
| kubeflow/spark-operator | 3,145 | 1,512 |
| kubeflow/trainer | 2,175 | 1,018 |
| kubeflow/katib | 1,694 | 535 |
| kubeflow/arena | 817 | 196 |
| kubeflow/community-distribution | 1,030 | 1,070 |
| plurigrid/asi | 59 | 13 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 |
| AustinCStone/TextGAN | 92 | 30 |
| migalkin/NodePiece | 144 | 21 |

### DuckDB Ducklake State

```
packages/world-increment/ducklake/world-increments.duckdb
  world_increments:   25 rows (sweeps)
  repo_snapshots:  1,029 rows (cumulative)
  aptos_snapshots:    28 rows
  multisig_probes:     5 rows
  mnx_snapshots:       0 rows
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

**Status:** All 28 addresses queried. APT CoinStore resource not found on any address
(accounts exist on mainnet but do not hold APT via the legacy `0x1::coin::CoinStore` module —
likely using Aptos Fungible Asset v2 standard or unfunded at query time).

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...c7b | NULL (account exists, seq=72) |
| bob | 0x0a3c...d5d | NULL |
| A–Z (26 addresses) | ... | NULL (all) |

### Multisig Contract Probes (5/5 healthy)

All 5 multisig contracts responded with `num_signatures_required = 2` (2-of-2).

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status:** SPA unavailable — `testnet.mnx.fi` returns a Next.js HTML shell with no
REST API endpoints accessible (`/api/markets`, `/api/v1/markets`, `/api/tickers` all
return the same HTML). Market data not extractable without browser JS execution.
No data inserted into `mnx_snapshots`.

---

## GF(3) Color Chain Legend

| id mod 3 | trit | color | name |
|----------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | 1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |

*This sweep: id=13, 13 mod 3 = 1 → PLUS (#b8bb26)*
