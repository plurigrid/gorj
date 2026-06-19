# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-06-19T07:30 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 101 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 49 |
| zubyul | user | 19 |
| migalkin | user | 40 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 104 |

**Total repos snapshotted:** 391

### GF(3) Color Chain
| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | `#b8bb26` PLUS | 12 increments |
| -1 | `#cc241d` MINUS | 12 increments |
| 0 | `#d3869b` ERGODIC | 10 increments |

### Top Languages
| Language | Repos | Total Stars |
|----------|-------|------------|
| Python | 236 | 31,401 |
| Rust | 57 | 53 |
| JavaScript | 54 | 211 |
| HTML | 51 | 696 |
| Go | 51 | 11,958 |
| TypeScript | 47 | 1,004 |
| Jupyter Notebook | 41 | 992 |
| Clojure | 29 | 6 |
| Jsonnet | 23 | 7,034 |
| Julia | 19 | 10 |

### Most Recent Activity (since 2026-01-01)
| Repo | Stars | Pushed |
|------|-------|--------|
| plurigrid/gorj | 0 | 2026-06-19T07:15 |
| M1shaaa/M1shaaa | 0 | 2026-06-19T03:58 |
| kubeflow/internal-acls | 19 | 2026-06-19T01:07 |
| bmorphism/Gay.jl | 1 | 2026-06-19T00:48 |
| kubeflow/mcp-apache-spark-history-server | 177 | 2026-06-19T00:32 |
| kubeflow/pipelines | 4,154 | 2026-06-18T20:30 |
| kubeflow/spark-operator | 3,127 | 2026-06-18T15:39 |
| kubeflow/trainer | 2,116 | 2026-06-18T14:29 |
| kubeflow/kubeflow | 15,736 | 2026-06-18T11:45 |
| TeglonLabs/jank-crane | 0 | 2026-06-08T19:03 |

**Notable:** kubeflow/kubeflow tops star count at 15,736; new TeglonLabs/jank-crane (C++, GF3 convergence maps) active June 8.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A–Z + alice, bob)
All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All 28 wallets returned NULL — no CoinStore resource registered (accounts unfunded / not initialized for APT mainnet).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...2d5d | NULL |
| A–Z (26) | various | NULL |

### Multisig Contract Probes
All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed live on Aptos mainnet.**

### MNX Markets
`https://testnet.mnx.fi` requires Vercel deployment authentication (auth wall returned for all API paths tried: `/api/markets`, `/api/v1/markets`, `/api/tickers`). Status: **UNAVAILABLE** this run.

---

## DuckDB Ducklake
**Location:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 391+ |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
