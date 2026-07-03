# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-03  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| DJedamski | user (zubyul graph) | 6 |
| wasita | user (zubyul graph) | 11 |
| kristinezheng | user (zubyul graph) | 5 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 30 |
| **TOTAL** | | **381** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 134 |
| +1 | `#b8bb26` | PLUS | 135 |
| -1 | `#cc241d` | MINUS | 135 |

### Top Languages

| Language | Repos |
|----------|-------|
| Python | 232 |
| Rust | 57 |
| HTML | 53 |
| JavaScript | 52 |
| Go | 51 |
| TypeScript | 46 |
| Jupyter Notebook | 40 |
| Clojure | 30 |
| Jsonnet | 23 |

### Most Starred Repos

| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,758 |
| kubeflow/pipelines | 4,167 |

### Most Recently Pushed

| Repo | Pushed At |
|------|-----------|
| kubeflow/community-distribution | 2026-07-03T08:13:35Z |
| plurigrid/gorj | 2026-07-03T08:13:33Z |
| kubeflow/dashboard | 2026-07-03T08:11:17Z |
| kubeflow/pipelines | 2026-07-03T08:06:54Z |
| M1shaaa/M1shaaa | 2026-07-03T02:37:37Z |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

Queried via `/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All 28 balances = **0.00 APT** (accounts unfunded on mainnet or CoinStore not registered)

**Total APT across swarm:** 0.00

### Multisig Contract Probes

All probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4… | 2 | YES |
| A-G | 0xf56c4a… | 2 | YES |
| Y-Z | 0xd3ffe1… | 2 | YES |
| S-T | 0x3b1c3a… | 2 | YES |
| V-W | 0x40fad7… | 2 | YES |

**All 5 multisig accounts are 2-of-N (healthy).**

### MNX Markets (testnet.mnx.fi)

**Status:** SPA — no accessible JSON API endpoint found. Market data unavailable this sweep.

---

## DuckDB Schema

```
world_increments    381 rows  GF3-tagged repo events
repo_snapshots      381 rows  GitHub repo metadata
aptos_snapshots      28 rows  Hamming swarm balances
multisig_probes       5 rows  2-of-N multisig health
mnx_snapshots         0 rows  SPA unavailable
```
