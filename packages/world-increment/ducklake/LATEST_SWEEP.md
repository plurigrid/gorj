# World Increment Sweep + Hamming Swarm Snapshot

Generated: 2026-07-19  
Session scope: GitHub API restricted to plurigrid/gorj; repo data from prior sweeps preserved in DB.

## JOB 1: GitHub Social Graph Sweep

| Metric | Value |
|--------|-------|
| World Increments logged (cumulative) | 23 |
| Unique repos in DB | 474 |
| Sources tracked | plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone |

### Top 10 Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15572 | N/A |
| kubeflow | pipelines | 4119 | Python |
| kubeflow | spark-operator | 3114 | Python |
| kubeflow | trainer | 2082 | Go |
| kubeflow | katib | 1678 | Python |
| kubeflow | examples | 1459 | Jsonnet |
| kubeflow | manifests | 1010 | YAML |
| kubeflow | arena | 809 | Go |
| kubeflow | kale | 683 | Python |
| kubeflow | website | 556 | HTML |

### GF(3) Color Chain
- id%3==0 → trit=0, color=#d3869b (ERGODIC)
- id%3==1 → trit=1, color=#b8bb26 (PLUS)
- id%3==2 → trit=-1, color=#cc241d (MINUS)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

| Metric | Value |
|--------|-------|
| Addresses probed | 28 |
| Active balances found | 0 |
| Not found (no CoinStore) | 28 |
| Total APT (active) | 0.0000 APT |

All 28 Hamming swarm addresses (alice, bob, A–Z) returned no CoinStore resource on Aptos mainnet,
indicating these accounts do not exist on-chain or have never received APT.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✓ |
| V-W | 0x40fad7b423a84365... | 2 | ✓ |

All 5 multisig contracts are **healthy** with a 2-of-N signature threshold.

### MNX Markets (testnet.mnx.fi)

MNX testnet endpoint responded but returned no extractable market entries. The frontend
is a SPA loading data client-side; direct API paths do not expose JSON market data.

---

## DuckDB Schema

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 23 | GF3 color-chained increment log |
| `repo_snapshots` | 474 | Unique repos tracked across sources |
| `aptos_snapshots` | 28 | Hamming swarm addresses × this sweep |
| `multisig_probes` | 5 | Pair probes, all healthy (2-sig threshold) |
| `mnx_snapshots` | 0 | MNX testnet unavailable via direct API |

DB path: `packages/world-increment/ducklake/world-increments.duckdb`

