# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-08-05 (automated sweep)
**GF(3) color chain:** ERGODIC `#d3869b` → PLUS `#b8bb26` → MINUS `#cc241d`

---

## Job 1: GitHub Social Graph Sweep

### Sources Snapshotted

| id | GF(3) | Color | Source | Type | Repos |
|----|-------|-------|--------|------|-------|
| 12 | ERGODIC | `#d3869b` | plurigrid | org | 100 |
| 13 | PLUS | `#b8bb26` | kubeflow | org | 49 |
| 14 | MINUS | `#cc241d` | TeglonLabs | org | 5 |
| 15 | ERGODIC | `#d3869b` | bmorphism | user | 100 |
| 16 | PLUS | `#b8bb26` | zubyul | user | 49 |
| 17 | MINUS | `#cc241d` | migalkin | user | 19 |
| 18 | ERGODIC | `#d3869b` | DJedamski | user | 6 |
| 19 | PLUS | `#b8bb26` | wasita | user | 14 |
| 20 | MINUS | `#cc241d` | kristinezheng | user | 5 |
| 21 | ERGODIC | `#d3869b` | M1shaaa | user | 8 |
| 22 | PLUS | `#b8bb26` | AustinCStone | user | 41 |

### Repo Stats (cumulative DuckDB)

| org/user | repos | total_stars |
|----------|-------|-------------|
| kubeflow | 94 | 67,723 |
| migalkin | 60 | 554 |
| bmorphism | 200 | 262 |
| AustinCStone | 86 | 216 |
| plurigrid | 300 | 192 |
| zubyul | 48 | 26 |
| DJedamski | 22 | 14 |
| TeglonLabs | 106 | 12 |
| wasita | 60 | 6 |
| M1shaaa | 32 | 0 |
| kristinezheng | 36 | 0 |

### Notable Activity

- **plurigrid/gorj** — Clojure, pushed 2026-08-05 (today, active)
- **plurigrid/zig-syrup** — Zig, pushed 2026-07-28
- **plurigrid/asi** — HTML, 59 stars, pushed 2026-07-10 ("everything is topological chemputer!")
- **kubeflow/pipelines** — Python, 4,177 stars, 2,079 forks
- **kubeflow/kubeflow** — 15,805 stars (flagship)
- **bmorphism/Gay.jl** — Julia, GF(3) color system, pushed 2026-07-21
- **wasita/xoxowasita-analysis** — Python, pushed 2026-08-04 (very recent)

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-08-05)

All 28 wallets queried (alice, bob, A-Z). All returned **0.0 APT** — APT coin store resource not found (accounts unfunded or unregistered on mainnet).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts responded with **2 signatures required** — all healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | yes |
| A-G | 0xf56c...0096 | 2 | yes |
| Y-Z | 0xd3ff...b883 | 2 | yes |
| S-T | 0x3b1c...7883 | 2 | yes |
| V-W | 0x40fa...eb6d | 2 | yes |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — API unavailable.** Endpoint at `/api/markets` returned a Next.js SPA shell with no parseable market data. No market records stored.

---

## DuckDB Ducklake State

| Table | Row Count |
|-------|-----------|
| world_increments | 34 |
| repo_snapshots | 1,044 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
