# LATEST_SWEEP — 2026-07-10

> world-increment sweep + hamming swarm snapshot · GF(3) color chain  
> Timestamp: 2026-07-10T12:00:00Z · Ledger: Aptos mainnet v6212094467

## JOB 1: GitHub Social Graph Sweep

### World Increment Table (14 increments, GF3 color chain)

| id | GF3 trit | Color | Name | Source | Event |
|----|:--------:|-------|------|--------|-------|
| 1 | +1 | `#b8bb26` | **PLUS** | org/plurigrid | repo_snapshot |
| 2 | -1 | `#cc241d` | **MINUS** | org/kubeflow | repo_snapshot |
| 3 | +0 | `#d3869b` | **ERGODIC** | org/TeglonLabs | repo_snapshot |
| 4 | +1 | `#b8bb26` | **PLUS** | user/bmorphism | repo_snapshot |
| 5 | -1 | `#cc241d` | **MINUS** | user/zubyul | repo_snapshot |
| 6 | +0 | `#d3869b` | **ERGODIC** | social_graph/migalkin | repo_snapshot |
| 7 | +1 | `#b8bb26` | **PLUS** | social_graph/DJedamski | repo_snapshot |
| 8 | -1 | `#cc241d` | **MINUS** | social_graph/wasita | repo_snapshot |
| 9 | +0 | `#d3869b` | **ERGODIC** | social_graph/AustinCStone | repo_snapshot |
| 10 | +1 | `#b8bb26` | **PLUS** | social_graph/kristinezheng | repo_snapshot |
| 11 | -1 | `#cc241d` | **MINUS** | social_graph/M1shaaa | repo_snapshot |
| 12 | +0 | `#d3869b` | **ERGODIC** | aptos/hamming_swarm | wallet_snapshot |
| 13 | +1 | `#b8bb26` | **PLUS** | aptos/multisig_probes | contract_probe |
| 14 | -1 | `#cc241d` | **MINUS** | market/mnx_testnet | market_snapshot |

### Repo Snapshots (190 repos across 11 sources)

| Source | Repos | Total Stars |
|--------|------:|------------:|
| plurigrid | 100 | 82 |
| kubeflow | 49 | 34339 |
| bmorphism | 14 | 182 |
| zubyul | 6 | 1 |
| TeglonLabs | 5 | 2 |
| migalkin | 5 | 276 |
| wasita | 3 | 4 |
| kristinezheng | 2 | 0 |
| DJedamski | 2 | 2 |
| AustinCStone | 2 | 103 |
| M1shaaa | 2 | 0 |

**Total:** 190 repositories indexed

### Top Repos by Stars

| Repo | Lang | ⭐ Stars | Forks | Last Push |
|------|------|--------:|------:|-----------|
| [kubeflow/kubeflow](https://github.com/kubeflow/kubeflow) | — | 15771 | 2685 | 2026-07-10 |
| [kubeflow/pipelines](https://github.com/kubeflow/pipelines) | Python | 4169 | 2031 | 2026-07-10 |
| [kubeflow/spark-operator](https://github.com/kubeflow/spark-operator) | Python | 3136 | 1500 | 2026-07-08 |
| [kubeflow/trainer](https://github.com/kubeflow/trainer) | Go | 2134 | 983 | 2026-07-10 |
| [kubeflow/katib](https://github.com/kubeflow/katib) | Python | 1689 | 532 | 2026-07-09 |
| [kubeflow/examples](https://github.com/kubeflow/examples) | Jsonnet | 1460 | 756 | 2025-04-14 |
| [kubeflow/community-distribution](https://github.com/kubeflow/community-distribution) | YAML | 1029 | 1071 | 2026-07-09 |
| [kubeflow/arena](https://github.com/kubeflow/arena) | Go | 815 | 195 | 2026-07-09 |
| [kubeflow/kale](https://github.com/kubeflow/kale) | Python | 695 | 157 | 2026-07-01 |
| [kubeflow/mpi-operator](https://github.com/kubeflow/mpi-operator) | Go | 529 | 237 | 2026-07-09 |
| [kubeflow/fairing](https://github.com/kubeflow/fairing) | Jsonnet | 337 | 143 | 2022-04-11 |
| [kubeflow/pytorch-operator](https://github.com/kubeflow/pytorch-operator) | Jsonnet | 310 | 143 | 2021-12-01 |
| [kubeflow/community](https://github.com/kubeflow/community) | Jupyter Notebook | 195 | 265 | 2026-07-01 |
| [kubeflow/website](https://github.com/kubeflow/website) | HTML | 184 | 925 | 2026-07-08 |
| [kubeflow/kfp-tekton](https://github.com/kubeflow/kfp-tekton) | TypeScript | 183 | 123 | 2024-11-19 |

### Most Recently Pushed (Top 10)

| Repo | Lang | Pushed |
|------|------|--------|
| kubeflow/dashboard | TypeScript | 2026-07-10T12:15:18 |
| kubeflow/sdk | Python | 2026-07-10T11:34:03 |
| kubeflow/kubeflow | — | 2026-07-10T11:31:26 |
| kubeflow/hub | Go | 2026-07-10T10:36:14 |
| plurigrid/gorj | Clojure | 2026-07-10T10:13:45 |
| kubeflow/trainer | Go | 2026-07-10T10:02:33 |
| kubeflow/pipelines | Python | 2026-07-10T09:51:44 |
| plurigrid/asi | HTML | 2026-07-10T09:47:39 |
| kubeflow/community-distribution | YAML | 2026-07-09T21:16:37 |
| kubeflow/mpi-operator | Go | 2026-07-09T17:44:24 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Addresses probed:** 28 (alice, bob, A–Z)  
**Aptos mainnet ledger:** v6212094467  
**Result:** All 28 wallets returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

These addresses have not registered a CoinStore resource on Aptos mainnet.
Balance_apt = NULL for all nodes. This may indicate:
- Uninitialized accounts (never received APT on-chain)
- Move objects using a different coin module
- Object accounts rather than regular accounts

### Multisig Contract Probes — 5/5 HEALTHY ✓

| Pair | Address | Threshold | Status |
|------|---------|----------:|--------|
| **A-B** | `0x0da4f428a0c007da0f7629…` | 2-of-N | ✓ healthy |
| **A-G** | `0xf56c4a1c0906214f3f859c…` | 2-of-N | ✓ healthy |
| **Y-Z** | `0xd3ffe1812b2df4062281c7…` | 2-of-N | ✓ healthy |
| **S-T** | `0x3b1c3ae905d44c3a49f0de…` | 2-of-N | ✓ healthy |
| **V-W** | `0x40fad7b423a843650fddca…` | 2-of-N | ✓ healthy |

All 5 Hamming-pair multisig contracts are live on Aptos mainnet with threshold = 2 signatures.

### MNX Testnet Markets

`https://testnet.mnx.fi` — HTTP 401 Unauthorized. Authentication required; no market data available without credentials.

---

## DuckDB Schema

```
world-increments.duckdb
├── world_increments  (14 rows)   — GF(3) color-tagged sweep events
├── repo_snapshots    (190 rows)  — GitHub repos by org/user
├── aptos_snapshots   (28 rows)   — Hamming swarm wallet probes
├── multisig_probes   (5 rows)    — Aptos multisig contracts
└── mnx_snapshots     (0 rows)    — MNX market data (auth required)
```

*Generated by world-increment-sweep + hamming-swarm-snapshot · plurigrid/gorj*
