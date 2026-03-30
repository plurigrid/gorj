# LATEST_SWEEP.md - World Increment + Hamming Swarm Snapshot

**Timestamp:** 2026-03-30 06:25:41 UTC

## GitHub Repository Sweep

### Repo Counts per Org/User

| Org/User | Repo Count |
|---|---|
| plurigrid | 93 (total on GitHub: 93) |
| kubeflow | 46 |
| TeglonLabs | 3 |
| bmorphism | 97 |
| zubyul | 44 |
| migalkin | 19 |
| DJedamski | 6 |
| wasita | 9 |
| kristinezheng | 6 |
| M1shaaa | 8 |
| AustinCStone | 40 |

**Total repos snapshot:** 371 unique repos across 11 orgs/users

### Top Repos by Stars

| Repo | Stars | Language |
|---|---|---|
| kubeflow/kubeflow | 15540 | - |
| kubeflow/pipelines | 4113 | Python |
| kubeflow/spark-operator | 3109 | Python |
| kubeflow/trainer | 2069 | Go |
| kubeflow/katib | 1673 | Python |
| kubeflow/examples | 1459 | Jsonnet |
| kubeflow/manifests | 1005 | YAML |
| migalkin/NodePiece | 143 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 88 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |
| bmorphism/anti-bullshit-mcp-server | 23 | Python |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |
| plurigrid/asi | 13 | HTML |

### GF(3) Color Chain Distribution (world_increments)

| GF3 Name | Trit | Color | Count |
|---|---|---|---|
| ERGODIC | 0 | #d3869b | ~127 |
| PLUS | +1 | #b8bb26 | ~128 |
| MINUS | -1 | #cc241d | ~128 |

---

## Aptos Wallet Balances

All 28 addresses queried via Aptos mainnet fullnode API. All balances returned 0 APT (accounts may be empty or not initialized with APT CoinStore).

| World Label | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793acde...cc7b | 0.00000000 |
| bob | 0x0a3c00c5...2d5d | 0.00000000 |
| A | 0x8699edc0...9d7a | 0.00000000 |
| B | 0x3f892ebe...cb13 | 0.00000000 |
| C | 0x38b99e63...535e | 0.00000000 |
| D | 0xf7765624...fdd1 | 0.00000000 |
| E | 0xdc1d9d53...8d36 | 0.00000000 |
| F | 0x18a14b5b...cf71 | 0.00000000 |
| G | 0x69a394c0...7f32 | 0.00000000 |
| H | 0xce67c327...300f | 0.00000000 |
| I | 0x070fe5d7...1fc9 | 0.00000000 |
| J | 0x4d964db8...7f54 | 0.00000000 |
| K | 0xa732040a...5dc4 | 0.00000000 |
| L | 0x7c2eaeaf...eba9 | 0.00000000 |
| M | 0x6fed37a7...f2e9 | 0.00000000 |
| N | 0xe7dde6da...1b2c | 0.00000000 |
| O | 0x73252b60...a89d | 0.00000000 |
| P | 0x6218792d...c948 | 0.00000000 |
| Q | 0xac40fa50...89a9 | 0.00000000 |
| R | 0x7ce605cc...6e10 | 0.00000000 |
| S | 0xb8753014...0386 | 0.00000000 |
| T | 0x35781dc0...4588 | 0.00000000 |
| U | 0x75860da4...9956 | 0.00000000 |
| V | 0xb59dd817...f2c3 | 0.00000000 |
| W | 0x5f32aef7...c7b0 | 0.00000000 |
| X | 0xa95cbbd1...047d | 0.00000000 |
| Y | 0xd8e32848...44c4 | 0.00000000 |
| Z | 0x7af0ef6e...197c | 0.00000000 |

**Note:** All APT balances are 0.0 - accounts appear to be empty or the CoinStore resource is not initialized.

---

## Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f428...7003 | 2 | YES |
| A-G | 0xf56c4a1c...0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

All 5 multisig contracts are healthy with 2-of-N signature requirements.

---

## MNX Markets (testnet.mnx.fi)

Status: **SPA (Single Page Application)** - testnet.mnx.fi returns a Next.js app. No JSON API endpoint `/api/markets` is available without authentication or browser execution. Market data could not be scraped via curl.

---

## DuckDB Tables

- **world_increments**: 371+ rows, GF(3) color-chained per repo snapshot
- **repo_snapshots**: 371 unique repos across 11 orgs/users  
- **aptos_snapshots**: 28 wallet records
- **multisig_probes**: 5 contract health checks
- **mnx_snapshots**: 1 record (SPA/unavailable status)

Database: `packages/world-increment/ducklake/world-increments.duckdb`
