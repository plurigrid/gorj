# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-07-05 UTC  
**Branch:** world-increment/sweep-2026-07-05  
**GF(3) Color Chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 40 |
| **Total (deduped)** | | **320** |

### Top Repos by Stars

| Rank | Repo | Stars | Language |
|------|------|-------|----------|
| 1 | kubeflow/kubeflow | 15,764 | — |
| 2 | kubeflow/pipelines | 4,169 | Python |
| 3 | kubeflow/spark-operator | 3,132 | Python |
| 4 | kubeflow/trainer | 2,129 | Go |
| 5 | kubeflow/katib | 1,689 | Python |
| 6 | kubeflow/examples | 1,460 | Jsonnet |
| 7 | kubeflow/community-distribution | 1,027 | YAML |
| 8 | migalkin/NodePiece | 144 | Python |
| 9 | AustinCStone/TextGAN | 92 | Python |
| 10 | migalkin/StarE | 89 | Python |

### Notable Recent Activity

- **wasita/wasita.github.io** — pushed 2026-07-05 (today), Svelte personal site
- **TeglonLabs/jank-crane** — pushed 2026-06-08, C++ GF3 convergence maps + loopify pass spec
- **migalkin/RWL** — pushed 2026-05-28, Weisfeiler-Leman for relational graphs
- **AustinCStone/StereoVisionMRF** — pushed 2026-04-01, MRF stereo depth recovery

### GF(3) Increment Color Distribution

| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 106 |
| PLUS | #b8bb26 | +1 | 107 |
| MINUS | #cc241d | -1 | 107 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| bob | 12.657007 | 0x0a3c00...512d5d |
| F | 1.960516 | 0x18a14b...3cf71 |
| L | 1.927269 | 0x7c2eae...eba9 |
| J | 1.895093 | 0x4d964d...7f54 |
| alice | 0.436434 | 0xc793ac...cc7b |
| O | 0.210136 | 0x73252b...a89d |
| K | 0.161961 | 0xa73204...25dc4 |
| P | 0.140136 | 0x621879...c948 |
| M | 0.112285 | 0x6fed37...7f2e9 |
| N | 0.106121 | 0xe7dde6...51b2c |
| Q | 0.103240 | 0xac40fa...c89a9 |
| S | 0.091788 | 0xb87530...d0386 |
| R | 0.090217 | 0x7ce605...76e10 |
| T | 0.073713 | 0x35781d...f4588 |
| U | 0.055773 | 0x75860d...f9956 |
| A | 0.051767 | 0x8699ed...e9d7a |
| V | 0.048833 | 0xb59dd8...af2c3 |
| Y | 0.044449 | 0xd8e328...444c4 |
| X | 0.042577 | 0xa95cbb...3047d |
| W | 0.040705 | 0x5f32ae...cc7b0 |
| B | 0.036256 | 0x3f892e...cb13 |
| Z | 0.024268 | 0x7af0ef...197c |
| D | 0.011629 | 0xf77656...cfdd1 |
| C | 0.010185 | 0x38b99e...1535e |
| E | 0.009372 | 0xdc1d9d...8d36 |
| H | 0.001681 | 0xce67c3...5300f |
| G | 0.000681 | 0x69a394...7f32 |
| I | 0.000681 | 0x070fe5...1fc9 |

**Total swarm APT:** ~20.11 APT  
**Wallets with balance > 1 APT:** 4 (bob, F, L, J)

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4f4...87003 | 2 | HEALTHY |
| A-G | 0xf56c4a...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe1...b883 | 2 | HEALTHY |
| S-T | 0x3b1c3a...7883 | 2 | HEALTHY |
| V-W | 0x40fad7...eb6d | 2 | HEALTHY |

All 5 multisig contracts healthy, all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — all API paths returned HTTP 401 (authentication required).

---

## DuckDB Schema

```
packages/world-increment/ducklake/world-increments.duckdb
  world_increments     320 rows  (GF3 increment chain)
  repo_snapshots       320 rows  (GitHub repo metadata)
  aptos_snapshots       28 rows  (wallet balances)
  multisig_probes        5 rows  (multisig health)
  mnx_snapshots          1 row   (market status: unavailable)
```
