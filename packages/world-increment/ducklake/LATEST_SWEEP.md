# World-Increment Sweep + Hamming Snapshot
**Run timestamp:** 2026-08-06 16:16 UTC  
**GF3 increment #1 (merged):** trit=1 · PLUS · `#b8bb26`  
**New repos this sweep:** 396 across 11 sources

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 14 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 41 |
| **TOTAL** | | **396** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,805 | — |
| kubeflow/pipelines | 4,178 | Python |
| kubeflow/spark-operator | 3,144 | Python |
| kubeflow/trainer | 2,171 | Go |
| kubeflow/katib | 1,694 | Python |
| kubeflow/examples | 1,461 | Jsonnet |
| kubeflow/community-distribution | 1,029 | YAML |
| kubeflow/arena | 816 | Go |
| kubeflow/kale | 699 | Python |
| kubeflow/mpi-operator | 530 | Go |

**Total stars (this sweep):** 35,324

### Language Distribution (top 10)

| Language | Repos |
|----------|-------|
| Python | 94 |
| (None/unknown) | 133 |
| Rust | 43 |
| JavaScript | 27 |
| HTML | 24 |
| Clojure | 24 |
| TypeScript | 22 |
| Go | 21 |

### Notable Activity
- **wasita/xoxowasita-analysis** — pushed 2026-08-06 (today), Python
- **M1shaaa/M1shaaa** — pushed 2026-08-06 (today), profile repo
- **plurigrid/gorj** — pushed 2026-08-06 (today), Clojure — this repo
- **plurigrid/asi** — 59 stars, HTML, pushed 2026-07-10
- **TeglonLabs/jank-crane** — C++, crane-jank IR hub with GF3 convergence maps

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

**Wallets queried:** 28 (alice, bob, A–Z)  
**Wallets with registered CoinStore:** 0  
**Status:** All 28 addresses returned no CoinStore resource — either uninitialized accounts, zero-balance accounts, or testnet-only addresses that have never received APT on mainnet.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793acd... | N/A |
| bob | 0x0a3c00c... | N/A |
| A | 0x8699edc... | N/A |
| B | 0x3f892eb... | N/A |
| C | 0x38b99e6... | N/A |
| D | 0xf776562... | N/A |
| E | 0xdc1d9d5... | N/A |
| F | 0x18a14b5... | N/A |
| G | 0x69a394c... | N/A |
| H | 0xce67c32... | N/A |
| I | 0x070fe5d... | N/A |
| J | 0x4d964db... | N/A |
| K | 0xa732040... | N/A |
| L | 0x7c2eaea... | N/A |
| M | 0x6fed37a... | N/A |
| N | 0xe7dde6d... | N/A |
| O | 0x73252b6... | N/A |
| P | 0x6218792... | N/A |
| Q | 0xac40fa5... | N/A |
| R | 0x7ce605c... | N/A |
| S | 0xb875301... | N/A |
| T | 0x35781dc... | N/A |
| U | 0x75860da... | N/A |
| V | 0xb59dd81... | N/A |
| W | 0x5f32aef... | N/A |
| X | 0xa95cbbd... | N/A |
| Y | 0xd8e3284... | N/A |
| Z | 0x7af0ef6... | N/A |

### Multisig Contract Probes

**All 5 probed — All HEALTHY (2-of-N signatures required)**

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ healthy |
| A-G | 0xf56c4a1c... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✓ healthy |
| V-W | 0x40fad7b4... | 2 | ✓ healthy |

All multisig contracts are 2-of-N and responding correctly on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — the endpoint is a SPA that does not serve JSON at common API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`). No market data retrieved.

---

## DuckDB State (world-increments.duckdb)

| Table | Rows |
|-------|------|
| world_increments | 24 total increments |
| repo_snapshots | 1,340 total snapshots |
| aptos_snapshots | 28 rows (this sweep) |
| multisig_probes | 5 rows (this sweep) |
| mnx_snapshots | 0 rows |

### GF3 Color Chain (latest 5 increments)
- #12: ERGODIC `#d3869b` — bmorphism
- #11: MINUS `#cc241d` — AustinCStone  
- #10: PLUS `#b8bb26` — M1shaaa
- #1:  PLUS `#b8bb26` — plurigrid+kubeflow+TeglonLabs+social (this sweep)
