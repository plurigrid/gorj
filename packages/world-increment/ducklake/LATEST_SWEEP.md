# World-Increment Sweep + Hamming Snapshot
**Generated:** 2026-07-23 07:12 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 103 total (top ~15 by activity captured) |
| bmorphism | user | 106 total (top ~22 by activity captured) |
| zubyul | user | 49 total (top ~10 captured) |
| TeglonLabs | org | 5 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 12 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 41 |

### DuckDB Ducklake Stats
- **Total world_increments:** 66
- **Total repo_snapshots:** 987
- **GF(3) color chain distribution:**

| GF3 Name | Color | Count |
|----------|-------|-------|
| PLUS | `#b8bb26` | 23 |
| MINUS | `#cc241d` | 22 |
| ERGODIC | `#d3869b` | 21 |

### Top Repos by Stars
| Repo | Org/User | Language | Stars | Description |
|------|----------|----------|-------|-------------|
| kubeflow/kubeflow | kubeflow | - | 15572 | Machine Learning Toolkit for Kubernetes |
| kubeflow/kubeflow | kubeflow | - | 15565 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | kubeflow | Python | 4119 | Machine Learning Pipelines for Kubeflow |
| kubeflow/pipelines | kubeflow | Python | 4119 | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | kubeflow | Python | 3114 | Kubernetes operator for managing the lifecycle of Apache Spa |
| kubeflow/spark-operator | kubeflow | Python | 3111 | Kubernetes operator for managing the lifecycle of Apache Spa |
| kubeflow/trainer | kubeflow | Go | 2082 | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| kubeflow/trainer | kubeflow | Go | 2080 | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| kubeflow/katib | kubeflow | Python | 1678 | Automated Machine Learning on Kubernetes |
| kubeflow/katib | kubeflow | Python | 1676 | Automated Machine Learning on Kubernetes |
| kubeflow/examples | kubeflow | Jsonnet | 1459 | A repository to host extended examples and tutorials |
| kubeflow/examples | kubeflow | Jsonnet | 1458 | A repository to host extended examples and tutorials |
| kubeflow/manifests | kubeflow | YAML | 1010 | Kubeflow AI Reference Platform Deployment Manifests |
| kubeflow/manifests | kubeflow | YAML | 1010 | Kubeflow AI Reference Platform Deployment Manifests |
| kubeflow/arena | kubeflow | Go | 809 | A CLI for Kubeflow.  |

### Notable Activity (2026-07-23)
- **bmorphism/Gay.jl** (Julia): 187 open issues, last pushed 2026-07-21 — most active repo
- **plurigrid/gorj** (Clojure): 1338 open issues — high issue volume
- **bmorphism/anti-bullshit-mcp-server**: 22 stars, updated 2026-07-12
- **wasita/wasita.github.io**: updated 2026-07-21 (most recent social graph activity)
- **AustinCStone/byteruckus**: new repo 2026-07-15

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice–Z, 28 addresses)
**Result:** All 28 addresses returned `resource_not_found` from Aptos mainnet.
- Addresses are not funded / have no `AptosCoin` CoinStore registered on-chain
- Balances recorded as NULL in `aptos_snapshots` table
- Total records: 28

### Multisig Contract Probes (5 pairs)
| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | `0x0da4f428a0...f4987003` | 2 | ✓ HEALTHY |
| A-G | `0xf56c4a1c09...3fbc0096` | 2 | ✓ HEALTHY |
| S-T | `0x3b1c3ae905...3ded7883` | 2 | ✓ HEALTHY |
| V-W | `0x40fad7b423...2c80eb6d` | 2 | ✓ HEALTHY |
| Y-Z | `0xd3ffe1812b...8e75b883` | 2 | ✓ HEALTHY |

**All 5 multisig pairs are healthy with 2-of-2 signature requirement.**

### MNX Markets (testnet.mnx.fi)
- All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return HTML SPA shell
- No structured market data accessible without browser execution
- Status: **SPA-only, no REST API data available**

---

## DuckDB Schema Summary
```
world_increments   — 66 rows (GF3-colored repo events)
repo_snapshots     — 987 rows (repo metadata snapshots)
aptos_snapshots    — 28 rows (28 Hamming swarm addresses)
multisig_probes    — 5 rows (5 pairs, all 2-of-2)
mnx_snapshots      — 0 rows (SPA, no API data)
```

## GF(3) Color Chain Legend
| Trit | Color | Hex | Meaning |
|------|-------|-----|---------|
| 0 | ERGODIC | `#d3869b` | id mod 3 == 0 |
| +1 | PLUS | `#b8bb26` | id mod 3 == 1 |
| -1 | MINUS | `#cc241d` | id mod 3 == 2 |
