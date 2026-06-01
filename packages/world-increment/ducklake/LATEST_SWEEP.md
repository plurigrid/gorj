# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep:** 2026-06-01T02:12Z  
**GF(3) Color Chain:** trit=1 · PLUS · #b8bb26  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 100 | 154 |
| kubeflow | org | 48 | 101,882 |
| TeglonLabs | org | 4 | 14 |
| bmorphism | user | 100 | 509 |
| zubyul | user | 49 | 40 |
| migalkin | social graph | 19 | 834 |
| DJedamski | social graph | 6 | 17 |
| wasita | social graph | 11 | 11 |
| kristinezheng | social graph | 6 | 0 |
| M1shaaa | social graph | 8 | 0 |
| AustinCStone | social graph | 40 | 324 |
| **TOTAL** | | **391** | **103,785** |

### Notable Repos (by stars)
- `kubeflow/*` — ML pipeline framework ecosystem, 101,882 cumulative stars
- `migalkin/*` — knowledge graph / GNN research, 834 cumulative stars
- `bmorphism/*` — 100 repos, diverse research tooling
- `plurigrid/*` — 100 repos, distributed systems + AI tooling

### DuckDB Tables (current totals — accumulates across sweeps)
```
world_increments:  24 rows
repo_snapshots:  1335 rows
aptos_snapshots:    28 rows (latest sweep)
multisig_probes:     5 rows (latest sweep)
mnx_snapshots:       1 row
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses queried via `https://fullnode.mainnet.aptoslabs.com/v1/`.

**Result:** All 28 addresses return 0.0 APT — wallets are unfunded on mainnet at time of sweep.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...512d | 0.0 |
| A–Z   | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** and require **2-of-N signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — site is a Next.js SPA; `/api/markets` returns the HTML shell with no embedded market data accessible without browser JS execution.

---

## GF(3) Color Chain Reference

| id % 3 | trit | color | name |
|--------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | 1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |

*This sweep is trit=1 (PLUS, #b8bb26) — increment id 1.*
