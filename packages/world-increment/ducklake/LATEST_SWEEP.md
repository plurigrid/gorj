# World-Increment Sweep + Hamming Snapshot — 2026-04-19

**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.2 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned (this run)

| Source | Type | Repos | Total Stars |
|---|---|---|---|
| plurigrid | org | 100 | 64 |
| kubeflow | org | 47 | 33,901 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 100 | 246 |
| zubyul | user | 47 | 14 |
| migalkin | user (social) | 7 | 277 |
| AustinCStone | user (social) | 5 | 103 |
| wasita | user (social) | 4 | 1 |
| kristinezheng | user (social) | 2 | 0 |
| M1shaaa | user (social) | 2 | 0 |
| DJedamski | user (social) | 2 | 1 |
| **TOTAL** | | **320** | **34,609** |

### GF(3) Color Chain Distribution (this sweep)

| Trit | Color | Name | Count |
|---|---|---|---|
| 0 | #d3869b | ERGODIC | 106 |
| +1 | #b8bb26 | PLUS | 107 |
| -1 | #cc241d | MINUS | 107 |

### Notable Repos

- **kubeflow/kubeflow**: 15,565 stars — ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — pushed 2026-04-10
- **kubeflow/spark-operator**: 3,111 stars — pushed 2026-04-10
- **migalkin/NodePiece**: 143 stars — ICLR'22 KG representations
- **migalkin/StarE**: 89 stars — EMNLP 2020 hyper-relational KGs
- **AustinCStone/TextGAN**: 92 stars — TensorFlow text generation GAN
- **bmorphism**: 100 repos, 246 total stars

### TeglonLabs Repos (all 4)

| Repo | Language | Pushed | Stars |
|---|---|---|---|
| mathpix-gem | Ruby | 2026-01-01 | 2 |
| monad-mcp-server | — | 2025-05-14 | 0 |
| topoi | Python | 2025-01-24 | 0 |
| coin-flip-mcp | JavaScript | 2025-09-21 | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet fullnode)

| World | Address (truncated) | APT Balance |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

All 28 wallets show 0.0 APT (`CoinStore` resource not initialized or unfunded on mainnet). Multisig activity confirms these addresses are live on-chain.

### Multisig Contract Probes

Probed via `0x1::multisig_account::num_signatures_required` (POST /v1/view):

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f4...7003 | 2 | ✓ |
| A-G | 0xf56c4a...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ |
| S-T | 0x3b1c3a...7883 | 2 | ✓ |
| V-W | 0x40fad7...eb6d | 2 | ✓ |

All 5 multisig contracts healthy — 2-of-N threshold confirmed.

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — Next.js SPA renders client-side only. No `/api/markets` endpoint accessible server-side. No market data extracted.

---

## DuckDB Table Counts (cumulative)

| Table | Rows |
|---|---|
| world_increments | 343 |
| repo_snapshots | 1,264 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, #d3869b, ERGODIC
- `id mod 3 == 1` → trit=+1, #b8bb26, PLUS
- `id mod 3 == 2` → trit=-1, #cc241d, MINUS
