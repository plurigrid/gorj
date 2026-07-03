# LATEST_SWEEP.md — 2026-07-03

## JOB 1: GitHub Social Graph Sweep

**Sweep date:** 2026-07-03T13:10 UTC  
**New world_increments:** 391  
**New repo_snapshots:** 391  

### Sources Covered

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |

*Note: plurigrid and bmorphism hit GitHub's 100-repo search cap; additional repos may exist beyond the snapshot.*

### Top Repos by Stars (this sweep)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | ★15760 | N/A | 2026-06-18 |
| kubeflow/pipelines | ★4168 | Python | 2026-07-03 |
| kubeflow/spark-operator | ★3132 | Python | 2026-07-02 |
| kubeflow/trainer | ★2129 | Go | 2026-07-02 |
| kubeflow/katib | ★1688 | Python | 2026-07-01 |
| kubeflow/examples | ★1460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | ★1028 | YAML | 2026-07-03 |
| kubeflow/arena | ★814 | Go | 2026-07-03 |
| kubeflow/kale | ★694 | Python | 2026-07-01 |
| kubeflow/mpi-operator | ★529 | Go | 2026-07-02 |
| kubeflow/fairing | ★337 | Jsonnet | 2022-04-11 |
| kubeflow/pytorch-operator | ★310 | Jsonnet | 2021-12-01 |
| kubeflow/community | ★194 | Jupyter Notebook | 2026-07-01 |
| kubeflow/website | ★184 | HTML | 2026-07-02 |
| kubeflow/kfp-tekton | ★183 | TypeScript | 2024-11-19 |

### Language Distribution (today's repos)

| Language | Count |
|----------|-------|
| Python | 82 |
| Rust | 26 |
| JavaScript | 26 |
| TypeScript | 22 |
| HTML | 17 |
| Jupyter Notebook | 15 |
| Go | 15 |
| Clojure | 13 |
| Julia | 8 |
| Jsonnet | 7 |

### GF(3) Color Chain Distribution

| Name | Color | Count | Trit |
|------|-------|-------|------|
| ERGODIC | #d3869b | 130 | 0 |
| MINUS | #cc241d | 130 | -1 |
| PLUS | #b8bb26 | 131 | 1 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses returned "Resource not found" — no `CoinStore<AptosCoin>` resource initialized on mainnet. All balances recorded as 0.0 APT.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| A | 0x8699edc096... | 0.0000 |
| B | 0x3f892ebe6e... | 0.0000 |
| C | 0x38b99e63ad... | 0.0000 |
| D | 0xf77656248f... | 0.0000 |
| E | 0xdc1d9d533b... | 0.0000 |
| F | 0x18a14b5b4b... | 0.0000 |
| G | 0x69a394c0b0... | 0.0000 |
| H | 0xce67c327a7... | 0.0000 |
| I | 0x070fe5d74e... | 0.0000 |
| J | 0x4d964db8f5... | 0.0000 |
| K | 0xa732040a6b... | 0.0000 |
| L | 0x7c2eaeafad... | 0.0000 |
| M | 0x6fed37a755... | 0.0000 |
| N | 0xe7dde6da0a... | 0.0000 |
| O | 0x73252b6011... | 0.0000 |
| P | 0x6218792de4... | 0.0000 |
| Q | 0xac40fa50b8... | 0.0000 |
| R | 0x7ce605cc8f... | 0.0000 |
| S | 0xb8753014e4... | 0.0000 |
| T | 0x35781dc0e4... | 0.0000 |
| U | 0x75860da475... | 0.0000 |
| V | 0xb59dd81703... | 0.0000 |
| W | 0x5f32aef70f... | 0.0000 |
| X | 0xa95cbbd116... | 0.0000 |
| Y | 0xd8e32848f1... | 0.0000 |
| Z | 0x7af0ef6e1b... | 0.0000 |
| alice | 0xc793acdec1... | 0.0000 |
| bob | 0x0a3c00c58f... | 0.0000 |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **HEALTHY** — `num_signatures_required = 2`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428a0... | 2 | ✓ |
| A-G | 0xf56c4a1c09... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b... | 2 | ✓ |
| S-T | 0x3b1c3ae905... | 2 | ✓ |
| V-W | 0x40fad7b423... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — No API data available**  
All probed paths (`/api/markets`, `/api/v1/markets`, `/api/v1/tickers`, `/api/tickers`) return the HTML SPA shell. No JSON market data could be extracted. Recorded as unavailable in `mnx_snapshots`.

---

## DuckDB Schema Summary

- `world_increments`: 414 rows total (cumulative across sweeps, 391 new today)
- `repo_snapshots`: 1335 rows total (391 new today)
- `aptos_snapshots`: 28 rows (this sweep)
- `multisig_probes`: 5 rows (this sweep)
- `mnx_snapshots`: 1 row (unavailable placeholder)

**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=+1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d
