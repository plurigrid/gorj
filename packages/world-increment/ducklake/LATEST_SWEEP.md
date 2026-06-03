# LATEST_SWEEP — World-Increment + Hamming Swarm Snapshot

**Timestamp:** 2026-06-03 21:13 UTC
**Sweep ID:** world-increment/sweep-2026-06-03-2110

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| source | type | repos | total_stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 155 |
| kubeflow | org | 48 | 101,898 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 100 | 508 |
| zubyul | user | 49 | 40 |
| migalkin | social | 19 | 834 |
| DJedamski | social | 6 | 3 |
| wasita | social | 11 | 7 |
| kristinezheng | social | 6 | 0 |
| M1shaaa | social | 8 | 0 |
| AustinCStone | social | 40 | 324 |
| **TOTAL (this sweep)** | | **391** | **103,771** |

> DuckDB ducklake is cumulative. This sweep added 381 repo_snapshot rows (Jun 3 2026).
> Prior sweeps on record: Apr 10 (471 rows), Apr 14 (473 rows). Cumulative DB: 1,325 rows / 643 unique repos.

### GF(3) Color Chain Distribution (this sweep, 381 increments)

| trit | color | name | count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 127 |
| 1 | `#b8bb26` | PLUS | 127 |
| -1 | `#cc241d` | MINUS | 127 |

GF(3) rule: `id % 3 == 0` → trit=0 ERGODIC, `id % 3 == 1` → trit=1 PLUS, `id % 3 == 2` → trit=-1 MINUS.

### Top Repos by Stars (this sweep)

| org/user | repo | language | stars | last_pushed |
|----------|------|----------|-------|-------------|
| kubeflow | kubeflow | Go | 15,705 | 2026-05-24 |
| kubeflow | pipelines | Python | 4,152 | 2026-06-03 |
| kubeflow | spark-operator | Python | 3,125 | 2026-06-03 |
| kubeflow | trainer | Go | 2,110 | 2026-06-03 |
| kubeflow | katib | Python | 1,685 | 2026-05-29 |
| kubeflow | examples | Jsonnet | 1,462 | 2025-04-14 |
| kubeflow | manifests | YAML | 1,020 | 2026-06-02 |
| migalkin | pykeen | Python | 453 | 2025-11-29 |
| migalkin | ultra | Python | 213 | 2025-11-18 |
| AustinCStone | various | mixed | 324 total | 2026 |
| bmorphism | various | mixed | 508 total | 2026-06 |
| plurigrid | various | mixed | 155 total | 2026-06 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
All 28 Hamming-swarm addresses returned **0.0 APT** — accounts are unfunded or not yet initialized on Aptos mainnet.

| world | address | balance_apt |
|-------|---------|-------------|
| alice | 0xc793ac...d624cc7b | 0.0 |
| bob | 0x0a3c00...05512d5d | 0.0 |
| A | 0x8699ed...ebe9d7a | 0.0 |
| B | 0x3f892e...4577cb13 | 0.0 |
| C | 0x38b99e...691535e | 0.0 |
| D | 0xf77656...d9fcfdd1 | 0.0 |
| E | 0xdc1d9d...d0958d36 | 0.0 |
| F | 0x18a14b...74c3cf71 | 0.0 |
| G | 0x69a394...dbcc7f32 | 0.0 |
| H | 0xce67c3...94e5300f | 0.0 |
| I | 0x070fe5...c00c1fc9 | 0.0 |
| J | 0x4d964d...3e87f54 | 0.0 |
| K | 0xa73204...7a425dc4 | 0.0 |
| L | 0x7c2eae...6337eba9 | 0.0 |
| M | 0x6fed37...4b7f2e9 | 0.0 |
| N | 0xe7dde6...11551b2c | 0.0 |
| O | 0x73252b...525a89d | 0.0 |
| P | 0x621879...21ec948 | 0.0 |
| Q | 0xac40fa...5e5c89a9 | 0.0 |
| R | 0x7ce605...36d76e10 | 0.0 |
| S | 0xb87530...f99d0386 | 0.0 |
| T | 0x35781d...2d3f4588 | 0.0 |
| U | 0x75860d...395ef9956 | 0.0 |
| V | 0xb59dd8...a89af2c3 | 0.0 |
| W | 0x5f32ae...a6ccc7b0 | 0.0 |
| X | 0xa95cbb...be33047d | 0.0 |
| Y | 0xd8e328...fa2444c4 | 0.0 |
| Z | 0x7af0ef...6e4e197c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts are **HEALTHY** — each requires exactly **2-of-N signatures**.

| pair | address | sigs_required | healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...fbc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...ded7883 | 2 | ✓ |
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ |

Probe method: `POST /v1/view` with `0x1::multisig_account::num_signatures_required`.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable (SPA)** — `testnet.mnx.fi` is a Next.js client-side SPA. No REST API endpoints
(`/api/markets`, `/api/v1/markets`, `/api/tickers`) are accessible server-side; all return the SPA shell HTML.
Market data requires browser-executed JavaScript. Recorded in `mnx_snapshots` as unavailable.

---

## DuckDB Ducklake State

**Location:** `packages/world-increment/ducklake/world-increments.duckdb`

| table | cumulative rows | this sweep |
|-------|-----------------|------------|
| world_increments | 404 | 381 |
| repo_snapshots | 1,325 | 381 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 1 | 1 |

Cumulative sweeps: 2026-04-10, 2026-04-14, 2026-06-03.

Sequences: `increment_seq`, `repo_seq` (DuckDB native sequences for append-safe ID generation).

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent · 2026-06-03 21:13 UTC*
