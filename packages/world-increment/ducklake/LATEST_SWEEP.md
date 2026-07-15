# LATEST_SWEEP.md

**Timestamp:** 2026-07-15T17:30:00Z
**DuckDB:** world-increments.duckdb (226 world_increments, 1147 repo_snapshots cumulative)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept
| Source | Type | Repos |
|--------|------|-------|
| bmorphism | org/user | 51 |
| plurigrid | org/user | 50 |
| zubyul | org/user | 49 |
| kubeflow | org/user | 49 |
| TeglonLabs | org/user | 5 |

### GF(3) Color Chain Distribution (this run)
| GF3 Name | Color | Count |
|----------|-------|-------|
| PLUS | #b8bb26 | 76 |
| MINUS | #cc241d | 75 |
| ERGODIC | #d3869b | 75 |

### Top Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| AustinCStone/Connectomics | 0 | TeX | 2014-05-11 |
| AustinCStone/ConvNet | 0 | Python | 2015-09-08 |
| AustinCStone/DigitRecognition | 0 | Matlab | 2015-02-02 |
| AustinCStone/Eigenface-Recognition | 0 | Matlab | 2014-05-11 |
| AustinCStone/EpsteinSearch | 0 | Python | 2026-02-11 |
| AustinCStone/FlaskBlog | 0 | Python | 2014-12-17 |
| AustinCStone/Founderati-Server | 0 | Python | 2015-08-25 |
| AustinCStone/Founderati-client | 0 | JavaScript | 2015-08-25 |
| AustinCStone/Genetic-Algorithm-Sorting-Network | 0 | Python | 2015-05-12 |
| AustinCStone/HTTPCache | 0 | Java | 2015-02-05 |

### Notable Activity
- **plurigrid/gorj**: 1183 open issues, pushed 2026-07-15 (active today)
- **plurigrid/asi**: 30 stars, HTML, pushed 2026-07-10
- **TeglonLabs/jank-crane**: C++ GF3 convergence maps, pushed 2026-06-08
- **kubeflow/kubeflow**: 15,778 stars — most-starred repo in sweep

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) returned **0.0 APT** (`resource_not_found` on CoinStore).
These accounts are uninitialized on Aptos mainnet at the time of this sweep.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| Z | 0x7af0ef6e...4e197c | 0.00000000 |
| Y | 0xd8e32848...2444c4 | 0.00000000 |
| X | 0xa95cbbd1...33047d | 0.00000000 |
| W | 0x5f32aef7...ccc7b0 | 0.00000000 |
| V | 0xb59dd817...9af2c3 | 0.00000000 |
| U | 0x75860da4...ef9956 | 0.00000000 |
| T | 0x35781dc0...3f4588 | 0.00000000 |
| S | 0xb8753014...9d0386 | 0.00000000 |
| R | 0x7ce605cc...d76e10 | 0.00000000 |
| Q | 0xac40fa50...5c89a9 | 0.00000000 |
| P | 0x6218792d...1ec948 | 0.00000000 |
| O | 0x73252b60...25a89d | 0.00000000 |
| N | 0xe7dde6da...551b2c | 0.00000000 |
| M | 0x6fed37a7...b7f2e9 | 0.00000000 |
| L | 0x7c2eaeaf...37eba9 | 0.00000000 |
| K | 0xa732040a...425dc4 | 0.00000000 |
| J | 0x4d964db8...e87f54 | 0.00000000 |
| I | 0x070fe5d7...0c1fc9 | 0.00000000 |
| H | 0xce67c327...e5300f | 0.00000000 |
| G | 0x69a394c0...cc7f32 | 0.00000000 |
| F | 0x18a14b5b...c3cf71 | 0.00000000 |
| E | 0xdc1d9d53...958d36 | 0.00000000 |
| D | 0xf7765624...fcfdd1 | 0.00000000 |
| C | 0x38b99e63...91535e | 0.00000000 |
| B | 0x3f892ebe...77cb13 | 0.00000000 |
| A | 0x8699edc0...be9d7a | 0.00000000 |
| bob | 0x0a3c00c5...512d5d | 0.00000000 |
| alice | 0xc793acde...24cc7b | 0.00000000 |

### Multisig Contract Probes (5 pairs)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✓ |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✓ |
| A-B | 0x0da4f428...987003 | 2 | ✓ |

**All 5 multisig contracts are healthy** (2-of-2 signature threshold).

### MNX Testnet Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` returns Vercel authentication gate (visitor password required).
No market data could be extracted without credentials.

---

## DuckDB Schema Summary

```
world_increments   — GF(3) trit-colored event log
repo_snapshots     — GitHub repo state (stars, forks, language, pushed_at)
aptos_snapshots    — Wallet APT balances (Hamming swarm)
multisig_probes    — Multisig sigs_required health checks
mnx_snapshots      — MNX market data (empty this run — auth required)
```
