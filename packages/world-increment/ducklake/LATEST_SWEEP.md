# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-29  
**GF(3) Increment:** id=12, trit=0, color=#d3869b, name=ERGODIC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **Total** | | **391** |

### Top Repos by Stars

```
org_or_user,repo_name,stars,language
kubeflow,kubeflow,15750,NULL
kubeflow,pipelines,4160,Python
kubeflow,spark-operator,3129,Python
kubeflow,trainer,2127,Go
kubeflow,katib,1687,Python
kubeflow,examples,1460,Jsonnet
kubeflow,community-distribution,1028,YAML
kubeflow,arena,814,Go
kubeflow,kale,694,Python
kubeflow,mpi-operator,528,Go
kubeflow,fairing,337,Jsonnet
kubeflow,pytorch-operator,310,Jsonnet
kubeflow,community,194,Jupyter Notebook
kubeflow,website,184,HTML
kubeflow,kfp-tekton,183,TypeScript
```

### Language Breakdown (this run)

```
language,cnt
Python,80
Rust,26
JavaScript,25
TypeScript,23
HTML,17
Go,15
Clojure,14
Jupyter Notebook,14
Julia,9
Zig,7
Jsonnet,7
R,6
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Hamming A–Z + alice, bob)

All 28 addresses queried against Aptos mainnet (`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`).

**Result:** All 28 wallets returned **0 APT** — accounts exist on-chain but hold no liquid APT balance at time of snapshot.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | 2 | HEALTHY |
| A-G | 0xf56c4a1c... | 2 | HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | HEALTHY |
| V-W | 0x40fad7b4... | 2 | HEALTHY |

**All 5 multisig accounts are active 2-of-2 configurations.**

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — site is deployed behind Vercel authentication (deployment protection enabled). API endpoints at `/api/markets` and `/api/v1/markets` both return 401 authentication required. No market data retrievable without bypass token.

---

## DuckDB Ducklake State

| Table | Row Count |
|-------|-----------|
| world_increments | 24 |
| repo_snapshots | 1335 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

Database: `packages/world-increment/ducklake/world-increments.duckdb`
