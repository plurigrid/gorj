# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-07 (automated sweep)
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

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
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 14 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 41 |
| **Total** | | **396** |

### DuckDB Tables

- `world_increments`: 341 rows — GF(3) color-chained event log
  - ERGODIC (#d3869b, trit=0): 113 entries
  - PLUS (#b8bb26, trit=1): 114 entries
  - MINUS (#cc241d, trit=-1): 114 entries
- `repo_snapshots`: 1262 rows (two passes per repo: increment + snapshot)

### Notable Recent Activity

- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub with GF3 convergence maps
- **wasita/xoxowasita-analysis** (Python, pushed 2026-08-06): most recently pushed repo in the sweep
- **migalkin/NodePiece** (Python, ★144): top-starred social graph repo — compositional KG embeddings (ICLR'22)
- **AustinCStone/TextGAN** (Python, ★92): generative adversarial network for text
- **migalkin/StarE** (Python, ★89): hyper-relational KG message passing (EMNLP 2020)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 addresses queried via `0x1::coin::balance` view function.
**Total swarm balance: 20.3448 APT**

| World | Balance (APT) |
|-------|--------------|
| bob | 12.657007 |
| F | 1.960516 |
| L | 1.927269 |
| J | 1.895093 |
| alice | 0.436434 |
| O | 0.210136 |
| K | 0.161961 |
| P | 0.140136 |
| M | 0.112285 |
| N | 0.106121 |
| Q | 0.103240 |
| S | 0.091788 |
| R | 0.090217 |
| T | 0.073713 |
| U | 0.055773 |
| A | 0.051767 |
| V | 0.048833 |
| Y | 0.044449 |
| X | 0.042577 |
| W | 0.040705 |
| B | 0.036256 |
| Z | 0.024268 |
| D | 0.011629 |
| C | 0.010185 |
| E | 0.009372 |
| H | 0.001681 |
| G | 0.000681 |
| I | 0.000681 |

> Note: Legacy `CoinStore` resource not present on these accounts. Balances retrieved via `0x1::coin::balance` view function (returns unified coin+FA balance).

### Multisig Contract Probes

All 5 multisig contracts healthy — 2-of-N signatures required.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

Status: **SPA only — no public REST API available.** The testnet returns a Next.js client-rendered app (HTTP 200). Endpoints `/api/markets` and `/api/v1/markets` return the same SPA HTML shell. No market data extractable without browser execution.

---

## GF(3) Color Chain Legend

| Mod | Trit | Color | Name |
|-----|------|-------|------|
| id%3==0 | 0 | #d3869b | ERGODIC |
| id%3==1 | +1 | #b8bb26 | PLUS |
| id%3==2 | -1 | #cc241d | MINUS |
