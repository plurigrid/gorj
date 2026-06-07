# World-Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-06-07T20:12:43Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary
| Metric | Value |
|--------|-------|
| Total repos snapshotted | 332 |
| Orgs covered | plurigrid, kubeflow, TeglonLabs |
| Users covered | bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone |
| World increments logged | 332 |

### GF(3) Color Chain Distribution
| Trit | Name | Color | Repos |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 110 |
| 1 | PLUS | #b8bb26 | 111 |
| -1 | MINUS | #cc241d | 111 |

### Top Repos by Stars
| Source | Repo | Stars | Language |
|--------|------|-------|----------|
| kubeflow | kubeflow | 15705 |  |
| kubeflow | pipelines | 4152 | Python |
| kubeflow | spark-operator | 3126 | Python |
| kubeflow | trainer | 2112 | Go |
| kubeflow | katib | 1685 | Python |
| kubeflow | examples | 1462 | Jsonnet |
| kubeflow | manifests | 1020 | YAML |
| kubeflow | arena | 811 | Go |
| kubeflow | kale | 691 | Python |
| kubeflow | mpi-operator | 528 | Go |
| kubeflow | fairing | 337 | Jsonnet |
| kubeflow | pytorch-operator | 310 | Jsonnet |
| kubeflow | community | 194 | Jupyter Notebook |
| kubeflow | website | 184 | HTML |
| kubeflow | kfp-tekton | 182 | TypeScript |
| kubeflow | kfctl | 182 | Go |
| kubeflow | hub | 175 | Go |
| kubeflow | mcp-apache-spark-history-server | 174 | Python |
| kubeflow | example-seldon | 172 | Jupyter Notebook |
| migalkin | NodePiece | 144 | Python |

### Repos by Source
| Source | Repos |
|--------|-------|
| plurigrid | 100 |
| bmorphism | 100 |
| zubyul | 49 |
| kubeflow | 48 |
| migalkin | 8 |
| wasita | 6 |
| AustinCStone | 6 |
| DJedamski | 5 |
| TeglonLabs | 4 |
| kristinezheng | 3 |
| M1shaaa | 3 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`. All balances returned 0 APT — addresses have no CoinStore resource or unfunded accounts.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| A | 0x8699edc0... | 0.0 |
| B | 0x3f892ebe... | 0.0 |
| C | 0x38b99e63... | 0.0 |
| D | 0xf7765624... | 0.0 |
| E | 0xdc1d9d53... | 0.0 |
| F | 0x18a14b5b... | 0.0 |
| G | 0x69a394c0... | 0.0 |
| H | 0xce67c327... | 0.0 |
| I | 0x070fe5d7... | 0.0 |
| J | 0x4d964db8... | 0.0 |
| K | 0xa732040a... | 0.0 |
| L | 0x7c2eaeaf... | 0.0 |
| M | 0x6fed37a7... | 0.0 |
| N | 0xe7dde6da... | 0.0 |
| O | 0x73252b60... | 0.0 |
| P | 0x6218792d... | 0.0 |
| Q | 0xac40fa50... | 0.0 |
| R | 0x7ce605cc... | 0.0 |
| S | 0xb8753014... | 0.0 |
| T | 0x35781dc0... | 0.0 |
| U | 0x75860da4... | 0.0 |
| V | 0xb59dd817... | 0.0 |
| W | 0x5f32aef7... | 0.0 |
| X | 0xa95cbbd1... | 0.0 |
| Y | 0xd8e32848... | 0.0 |
| Z | 0x7af0ef6e... | 0.0 |
| alice | 0xc793acde... | 0.0 |
| bob | 0x0a3c00c5... | 0.0 |

### Multisig Contract Probes
All 5 probes returned `sigs_required=2` — contracts are live and healthy.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f428... | 2 | true |
| A-G | 0xf56c4a1c... | 2 | true |
| Y-Z | 0xd3ffe181... | 2 | true |
| S-T | 0x3b1c3ae9... | 2 | true |
| V-W | 0x40fad7b4... | 2 | true |

### MNX Markets
`testnet.mnx.fi` — **UNAVAILABLE** at time of sweep. All API paths (/, /api/markets, /api/v1/markets, /api/tickers) returned connection errors. MNX testnet appears to be down or unreachable from this environment.

---

## Schema Reference
```
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
