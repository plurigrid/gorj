# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-08-10T11:31Z  
**DuckDB:** `world-increments.duckdb` (2.3 MB)

---

## Job 1 – GitHub Social Graph Sweep

**Sources queried:** orgs `plurigrid`, `kubeflow`, `TeglonLabs`; users `bmorphism`, `zubyul`; zubyul social graph `migalkin`, `DJedamski`, `wasita`, `kristinezheng`, `M1shaaa`, `AustinCStone`

### Repository Counts by Source

| Source | Repos |
|---|---|
| bmorphism | 72 |
| plurigrid | 56 |
| AustinCStone | 30 |
| migalkin | 19 |
| kubeflow | 17 |
| zubyul | 15 |
| wasita | 14 |
| M1shaaa | 8 |
| DJedamski | 6 |
| TeglonLabs | 5 |
| kristinezheng | 5 |
| **Total** | **247** |

### GF(3) Color Chain Distribution

| Trit | Color | Hex | Count |
|---|---|---|---|
| 0 | ERGODIC | #d3869b | 82 |
| 1 | PLUS | #b8bb26 | 83 |
| -1 | MINUS | #cc241d | 82 |

### Top Repos by Stars

| Repo | Stars | Language |
|---|---|---|
| kubeflow/kubeflow | 15,809 | — |
| kubeflow/pipelines | 4,180 | Python |
| kubeflow/spark-operator | 3,146 | Python |
| kubeflow/trainer | 2,177 | Go |
| kubeflow/katib | 1,694 | Python |
| kubeflow/examples | 1,461 | Jsonnet |
| kubeflow/community-distribution | 1,030 | YAML |
| kubeflow/arena | 817 | Go |
| kubeflow/kale | 699 | Python |
| kubeflow/mpi-operator | 531 | Go |

### Most Recently Pushed (2026-08-10)

| Repo | Pushed At |
|---|---|
| bmorphism/nashator-h1 | 2026-08-10T10:57:53Z |
| bmorphism/attention-heat-capacity | 2026-08-10T10:56:32Z |
| plurigrid/gorj | 2026-08-10T10:21:39Z |
| kubeflow/sdk | 2026-08-10T10:04:21Z |
| bmorphism/oldies-clearing | 2026-08-10T09:58:45Z |

> Note: `plurigrid/gorj` has 1,765 open issues.

---

## Job 2 – Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Queried:** 28 addresses (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`

All 28 wallets: **0.0 APT** — accounts have no initialized CoinStore resource on mainnet (or genuinely zero balance).

### Multisig Contract Probes (0x1::multisig_account)

| Pair | Sigs Required | Status |
|---|---|---|
| A–B | 2 | healthy |
| A–G | 2 | healthy |
| Y–Z | 2 | healthy |
| S–T | 2 | healthy |
| V–W | 2 | healthy |

All 5 multisig contracts require **2-of-N** signatures. All healthy.

### MNX Markets (testnet.mnx.fi)

**Status: unavailable** — `testnet.mnx.fi` is a Next.js SPA with no public REST API. Routes `/api/markets` and `/api/v1/markets` return HTML, not JSON.

---

## DuckDB Schema

| Table | Rows | Description |
|---|---|---|
| `world_increments` | 247 | One row per repo; GF(3) trit + color assignment |
| `repo_snapshots` | 247 | Stars, forks, issues, pushed_at, language, description |
| `aptos_snapshots` | 28 | Mainnet wallet balances (APT) |
| `multisig_probes` | 5 | Multisig sig-count probes |
| `mnx_snapshots` | 1 | MNX testnet status |
