# World Increment Sweep + Hamming Snapshot

**Date/Time:** 2026-04-03T00:00:00Z (sweep executed)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repos Collected Per Org/User

| Org/User        | Repos (API total) | Top Stars Repo                              |
|-----------------|-------------------|---------------------------------------------|
| kubeflow        | 46                | kubeflow/kubeflow (15,552 stars)            |
| plurigrid       | 93                | plurigrid/asi (15 stars)                    |
| bmorphism       | 97                | bmorphism/ocaml-mcp-sdk (60 stars)          |
| AustinCStone    | 40                | AustinCStone/TextGAN (92 stars)             |
| migalkin        | 19                | migalkin/NodePiece (143 stars)              |
| zubyul          | 44                | zubyul/WGCNA (2 stars)                      |
| TeglonLabs      | 3                 | TeglonLabs/mathpix-gem (2 stars)            |
| DJedamski       | 6                 | DJedamski/Getting-and-Cleaning-Data (1 star)|
| wasita          | 9                 | wasita/magic-garden (1 star)                |
| kristinezheng   | 6                 | (0 stars all)                               |
| M1shaaa         | 8                 | (0 stars all)                               |

**Total curated repos ingested into repo_snapshots:** 102

### Top 15 Repos by Stars

| Rank | Repo                                     | Language | Stars  | Forks |
|------|------------------------------------------|----------|--------|-------|
| 1    | kubeflow/kubeflow                        | -        | 15,552 | 2,628 |
| 2    | kubeflow/pipelines                       | Python   | 4,118  | 1,983 |
| 3    | kubeflow/spark-operator                  | Python   | 3,110  | 1,480 |
| 4    | kubeflow/trainer                         | Go       | 2,074  | 943   |
| 5    | kubeflow/katib                           | Python   | 1,674  | 519   |
| 6    | kubeflow/examples                        | Jsonnet  | 1,459  | 755   |
| 7    | kubeflow/manifests                       | YAML     | 1,007  | 1,068 |
| 8    | kubeflow/arena                           | Go       | 809    | 190   |
| 9    | kubeflow/kale                            | Python   | 681    | 156   |
| 10   | kubeflow/mpi-operator                    | Go       | 519    | 236   |
| 11   | migalkin/NodePiece                       | Python   | 143    | 21    |
| 12   | migalkin/StarE                           | Python   | 88     | 16    |
| 13   | AustinCStone/TextGAN                     | Python   | 92     | 30    |
| 14   | bmorphism/ocaml-mcp-sdk                  | OCaml    | 60     | 2     |
| 15   | bmorphism/anti-bullshit-mcp-server       | JS       | 23     | 8     |

### GF(3) Color Chain

Increments follow GF(3) color assignment cycling on sequential IDs:
- `id % 3 == 0` trit=0 ERGODIC (#d3869b)
- `id % 3 == 1` trit=1 PLUS (#b8bb26)
- `id % 3 == 2` trit=-1 MINUS (#cc241d)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses queried against Aptos mainnet fullnode. All returned 0 APT (accounts either empty or APT CoinStore not registered).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b       | 0.0           |
| bob   | 0x0a3c...2d5d       | 0.0           |
| A     | 0x8699...9d7a       | 0.0           |
| B     | 0x3f89...b13        | 0.0           |
| C     | 0x38b9...535e       | 0.0           |
| D     | 0xf776...fdd1       | 0.0           |
| E     | 0xdc1d...8d36       | 0.0           |
| F     | 0x18a1...cf71       | 0.0           |
| G     | 0x69a3...7f32       | 0.0           |
| H     | 0xce67...300f       | 0.0           |
| I     | 0x070f...fc9        | 0.0           |
| J     | 0x4d96...7f54       | 0.0           |
| K     | 0xa732...dc4        | 0.0           |
| L     | 0x7c2e...ba9        | 0.0           |
| M     | 0x6fed...2e9        | 0.0           |
| N     | 0xe7dd...b2c        | 0.0           |
| O     | 0x7325...89d        | 0.0           |
| P     | 0x6218...948        | 0.0           |
| Q     | 0xac40...a9         | 0.0           |
| R     | 0x7ce6...e10        | 0.0           |
| S     | 0xb875...386        | 0.0           |
| T     | 0x3578...588        | 0.0           |
| U     | 0x7586...956        | 0.0           |
| V     | 0xb59d...2c3        | 0.0           |
| W     | 0x5f32...7b0        | 0.0           |
| X     | 0xa95c...47d        | 0.0           |
| Y     | 0xd8e3...4c4        | 0.0           |
| Z     | 0x7af0...97c        | 0.0           |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`. All returned 2 sigs required — healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...003        | 2             | YES     |
| A-G  | 0xf56c...096        | 2             | YES     |
| Y-Z  | 0xd3ff...883        | 2             | YES     |
| S-T  | 0x3b1c...883        | 2             | YES     |
| V-W  | 0x40fa...b6d        | 2             | YES     |

### MNX Markets

**Status: UNAVAILABLE**

`https://testnet.mnx.fi/api/markets` returned non-JSON (Next.js SPA requiring JS rendering). No parseable market data could be extracted. Recorded as unavailable in `mnx_snapshots` table (0 rows).

---

## Database Tables Summary

| Table             | Rows | Description                              |
|-------------------|------|------------------------------------------|
| repo_snapshots    | 102  | Curated repos from 11 orgs/users         |
| world_increments  | 102  | Corresponding GF(3) trit color entries   |
| aptos_snapshots   | 28   | Aptos mainnet wallet balance records     |
| multisig_probes   | 5    | Multisig contract probe results          |
| mnx_snapshots     | 0    | MNX market data (unavailable)            |
