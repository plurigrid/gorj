# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-05

## Sweep Metadata
- **Date:** 2026-05-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** v1.5.2 (Variegata)
- **DB:** packages/world-increment/ducklake/world-increments.duckdb

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found | Top Repo |
|--------|------|-------------|----------|
| plurigrid | org | 100 | asi (18★) |
| kubeflow | org | 47 | kubeflow (15,622★) |
| TeglonLabs | org | 4 | mathpix-gem (2★) |
| bmorphism | user | 100 | ocaml-mcp-sdk (60★) |
| zubyul | user | 49 | gay-world (1★) |
| migalkin | user_social | 19 | NodePiece (143★) |
| DJedamski | user_social | 6 | Kaggle (1★) |
| wasita | user_social | 10 | magic-garden (2★) |
| kristinezheng | user_social | 6 | (0★) |
| M1shaaa | user_social | 8 | (0★) |
| AustinCStone | user_social | 30 | EpsteinSearch (0★) |

**Total repos across all sources this sweep:** 379

### Notable Recent Activity (pushed ≤ 7 days)

- `plurigrid/gorj` — Clojure, 72 open issues, pushed 2026-05-05 (this repo)
- `kubeflow/sdk` — Python, 111★, pushed 2026-05-05
- `kubeflow/pipelines` — Python, 4,132★, pushed 2026-05-05
- `kubeflow/trainer` — Go, 2,096★, pushed 2026-05-05
- `bmorphism/Gay.jl` — Julia, 187 open issues, pushed 2026-05-05
- `M1shaaa/M1shaaa` — pushed 2026-05-05
- `zubyul/voice-observatory` — Python, pushed 2026-04-24

### GF(3) World Increment Chain (IDs 24–34, this sweep)

| id | trit | color | name | source |
|----|------|-------|------|--------|
| 24 | 0 | `#d3869b` | ERGODIC | plurigrid |
| 25 | 1 | `#b8bb26` | PLUS | kubeflow |
| 26 | -1 | `#cc241d` | MINUS | TeglonLabs |
| 27 | 0 | `#d3869b` | ERGODIC | bmorphism |
| 28 | 1 | `#b8bb26` | PLUS | zubyul |
| 29 | -1 | `#cc241d` | MINUS | migalkin |
| 30 | 0 | `#d3869b` | ERGODIC | DJedamski |
| 31 | 1 | `#b8bb26` | PLUS | wasita |
| 32 | -1 | `#cc241d` | MINUS | kristinezheng |
| 33 | 0 | `#d3869b` | ERGODIC | M1shaaa |
| 34 | 1 | `#b8bb26` | PLUS | AustinCStone |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Query:** `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` via Aptos mainnet fullnode  
**Result:** All 28 addresses returned `resource_not_found`. CoinStore not initialized — these wallets either use the newer FA (Fungible Asset) standard or have no on-chain APT activity.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | null (no CoinStore) |
| bob | 0x0a3c...12d5 | null |
| A–Z | (26 addresses) | null |

### Multisig Contract Probes

**Query:** `0x1::multisig_account::num_signatures_required` via POST `/v1/view`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...7003 | **2** | HEALTHY |
| A-G | 0xf56c4a1c...0096 | **2** | HEALTHY |
| Y-Z | 0xd3ffe181...b883 | **2** | HEALTHY |
| S-T | 0x3b1c3ae9...7883 | **2** | HEALTHY |
| V-W | 0x40fad7b4...eb6d | **2** | HEALTHY |

All 5/5 multisig accounts require **2-of-N** signatures and responded correctly.

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — site is a Next.js SPA. `/api/markets` and `/api/tickers` return HTML, no public JSON endpoints detected.

---

## DuckDB Ducklake Cumulative State

| Table | Count |
|-------|-------|
| world_increments | 34 |
| repo_snapshots | 1,045 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |
