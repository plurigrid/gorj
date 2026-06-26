# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-26 (UTC)
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Distinct Repos |
|--------|------|---------------|
| plurigrid | org | 108 |
| bmorphism | user | 108 |
| TeglonLabs | org | 54 |
| kubeflow | org | 48 |
| AustinCStone | user (social graph) | 43 |
| wasita | user (social graph) | 31 |
| migalkin | user (social graph) | 30 |
| zubyul | user | 28 |
| kristinezheng | user (social graph) | 18 |
| M1shaaa | user (social graph) | 16 |
| DJedamski | user (social graph) | 11 |
| **TOTAL** | **11 sources** | **495 distinct repos** |

### Top Repos by Stars

| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,745 ★ |
| kubeflow/pipelines | 4,156 ★ |
| kubeflow/spark-operator | 3,128 ★ |
| kubeflow/trainer | 2,122 ★ |
| kubeflow/katib | 1,686 ★ |
| kubeflow/examples | 1,460 ★ |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Increments |
|------|------|-------|-----------|
| 0 | ERGODIC | `#d3869b` | 36 |
| 1 | PLUS | `#b8bb26` | 39 |
| -1 | MINUS | `#cc241d` | 38 |
| **Total** | | | **113** |

Formula: `id % 3 == 0 → ERGODIC`, `id % 3 == 1 → PLUS`, `id % 3 == 2 → MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned `resource_not_found` from the Aptos mainnet `CoinStore` resource. Accounts exist on-chain but have never received APT — all balances recorded as **0.0 APT**.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0x070fe5d7... | 0.0 |
| bob | 0x0a3c00c5... | 0.0 |
| A–Z | 0x... (26 addrs) | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy**, all requiring **2 signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ |
| V-W | 0x40fad7b4...0eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi/api/markets` — SPA frontend only, no accessible public REST API endpoint. **0 rows** recorded in `mnx_snapshots`.

---

## DuckDB Tables Summary

| Table | Rows | Notes |
|-------|------|-------|
| `world_increments` | 113 | GF(3) trit-colored increment events |
| `repo_snapshots` | 1,034 | 495 distinct repos across 11 sources |
| `aptos_snapshots` | 28 | All wallets 0.0 APT (unfunded) |
| `multisig_probes` | 5 | All healthy, 2-of-N |
| `mnx_snapshots` | 0 | API unavailable |

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`
**Sequences:** `increment_seq` (→ 113), `repo_seq` (→ 1034)
