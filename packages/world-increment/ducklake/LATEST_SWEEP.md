# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-06-10  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 100 | 76 |
| kubeflow | org | 48 | 34,194 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| migalkin | user (social) | 19 | 280 |
| AustinCStone | user (social) | 40 | 108 |
| wasita | user (social) | 11 | 5 |
| kristinezheng | user (social) | 5 | 0 |
| M1shaaa | user (social) | 8 | 0 |
| DJedamski | user (social) | 6 | 3 |
| **TOTAL** | | **391** | **34,929** |

### Top Repos by Stars

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15,714 | 2,672 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,153 | 2,004 | 2026-06-10 |
| kubeflow/spark-operator | Python | 3,126 | 1,488 | 2026-06-09 |
| kubeflow/trainer | Go | 2,112 | 964 | 2026-06-10 |
| kubeflow/katib | Python | 1,685 | 525 | 2026-06-05 |
| kubeflow/examples | Jsonnet | 1,462 | 756 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,022 | 1,065 | 2026-06-09 |
| kubeflow/arena | Go | 812 | 190 | 2026-05-07 |
| bmorphism (100 repos) | various | 247 total | — | — |
| migalkin (19 repos) | Python/KG | 280 total | — | — |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 130 |
| +1 | PLUS | `#b8bb26` | 131 |
| -1 | MINUS | `#cc241d` | 130 |

Chain rule: `id % 3 == 0 → ERGODIC`, `id % 3 == 1 → PLUS`, `id % 3 == 2 → MINUS`

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com` — all returned **0.00000000 APT** for `CoinStore<AptosCoin>`.

This indicates the addresses are either not yet funded on mainnet, hold only non-APT tokens, or are not initialized with a CoinStore resource.

| World | Address | Balance (APT) |
|-------|---------|--------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required` — all **healthy**, all require **2 signatures**.

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` is protected by Vercel deployment authentication. All API paths (`/api/markets`, `/api/v1/markets`, `/api/ticker`) returned `Authentication Required`.

---

## DuckDB Schema Summary

```
world_increments  — 391 rows  (GF3 chain, one per repo snapshot)
repo_snapshots    — 391 rows  (full repo metadata)
aptos_snapshots   —  28 rows  (wallet balances, all 0 APT)
multisig_probes   —   5 rows  (all healthy, 2-of-N)
mnx_snapshots     —   1 row   (unavailable note)
```

Query example:
```sql
SELECT wi.gf3_name, wi.gf3_color, rs.full_name, rs.stars
FROM world_increments wi
JOIN repo_snapshots rs ON wi.id = rs.increment_id
ORDER BY rs.stars DESC LIMIT 10;
```
