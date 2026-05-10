# LATEST_SWEEP — 2026-05-10 12:21:30 UTC

## JOB 1: GitHub Social Graph Sweep

### Sources Crawled
| Source           | Type  | Repos |
|-----------------|-------|-------|
| plurigrid        | org   |  100  |
| bmorphism        | user  |  100  |
| kubeflow         | org   |   48  |
| zubyul           | user  |   49  |
| AustinCStone     | user  |   40  |
| migalkin         | user  |   19  |
| wasita           | user  |   11  |
| M1shaaa          | user  |    8  |
| DJedamski        | user  |    6  |
| kristinezheng    | user  |    6  |
| TeglonLabs       | org   |    4  |

**Total repos snapshotted: 391** (100 from plurigrid, 100 from bmorphism, 49 zubyul, 48 kubeflow + zubyul social graph)

### Top Repos by Stars
| Repo                         | Stars | Language |
|-----------------------------|-------|----------|
| kubeflow/kubeflow            | 15628 | —        |
| kubeflow/pipelines           |  4137 | Python   |
| kubeflow/spark-operator      |  3125 | Python   |
| kubeflow/trainer             |  2097 | Go       |
| kubeflow/katib               |  1683 | Python   |

### GF(3) Color Chain Distribution
| trit | name    | color   | hex     |
|------|---------|---------|---------|
|  0   | ERGODIC | pink    | #d3869b |
|  1   | PLUS    | yellow  | #b8bb26 |
| -1   | MINUS   | red     | #cc241d |

| trit | count |
|------|-------|
| 0 (ERGODIC #d3869b) | 130 |
| 1 (PLUS #b8bb26)    | 131 |
| -1 (MINUS #cc241d)  | 130 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, APT)
| World | Address (prefix)  | Balance (APT) |
|-------|------------------|---------------|

| bob   | 0x0a3c00c58f... |    12.657007 |
| F     | 0x18a14b5b4b... |     1.960516 |
| L     | 0x7c2eaeafad... |     1.927269 |
| J     | 0x4d964db8f5... |     1.895093 |
| alice | 0xc793acdec1... |     0.436434 |
| O     | 0x73252b6011... |     0.210136 |
| K     | 0xa732040a6b... |     0.161961 |
| P     | 0x6218792de4... |     0.140136 |
| M     | 0x6fed37a755... |     0.112285 |
| N     | 0xe7dde6da0a... |     0.106121 |
| Q     | 0xac40fa50b8... |     0.103240 |
| S     | 0xb8753014e4... |     0.091788 |
| R     | 0x7ce605cc8f... |     0.090217 |
| T     | 0x35781dc0e4... |     0.073713 |
| U     | 0x75860da475... |     0.055773 |
| A     | 0x8699edc096... |     0.051767 |
| V     | 0xb59dd81703... |     0.048833 |
| Y     | 0xd8e32848f1... |     0.044449 |
| X     | 0xa95cbbd116... |     0.042577 |
| W     | 0x5f32aef70f... |     0.040705 |
| B     | 0x3f892ebe6e... |     0.036256 |
| Z     | 0x7af0ef6e1b... |     0.024268 |
| D     | 0xf77656248f... |     0.011629 |
| C     | 0x38b99e63ad... |     0.010185 |
| E     | 0xdc1d9d533b... |     0.009372 |
| H     | 0xce67c327a7... |     0.001681 |
| G     | 0x69a394c0b0... |     0.000681 |
| I     | 0x070fe5d74e... |     0.000681 |

### Multisig Contract Probes
| Pair  | Address (prefix)     | Sigs Required | Status  |
|-------|---------------------|---------------|---------|

| A-B   | 0x0da4f428a0c007... | 2 | HEALTHY |
| A-G   | 0xf56c4a1c090621... | 2 | HEALTHY |
| Y-Z   | 0xd3ffe1812b2df4... | 2 | HEALTHY |
| S-T   | 0x3b1c3ae905d44c... | 2 | HEALTHY |
| V-W   | 0x40fad7b423a843... | 2 | HEALTHY |

All 5 multisig contracts probed healthy (2-of-N threshold).

### MNX Markets (testnet.mnx.fi)
Status: **UNAVAILABLE** — site is a Next.js SPA with no accessible REST API endpoints.
All `/api/*` paths redirect to the SPA shell. Market data not retrievable without browser JS execution.

---

## DuckDB Schema (ducklake/world-increments.duckdb)
- `world_increments` — 391 rows (GF3 chain over repo events)
- `repo_snapshots` — 391 rows (full repo metadata)
- `aptos_snapshots` — 28 rows (A–Z + alice + bob wallet balances)
- `multisig_probes` — 5 rows (A-B, A-G, Y-Z, S-T, V-W)
- `mnx_snapshots` — 1 row (unavailability marker)
