# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-26T07:xx UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept (11 nodes)

| Source | Type | GF3 Trit | Color | GF3 Name |
|--------|------|----------|-------|----------|
| plurigrid | org | 0 | #d3869b | ERGODIC |
| kubeflow | org | 1 | #b8bb26 | PLUS |
| TeglonLabs | org | -1 | #cc241d | MINUS |
| bmorphism | user | 0 | #d3869b | ERGODIC |
| zubyul | user | -1 | #cc241d | MINUS |
| migalkin | user | -1 | #cc241d | MINUS |
| DJedamski | user | 1 | #b8bb26 | PLUS |
| wasita | user | 1 | #b8bb26 | PLUS |
| kristinezheng | user | 0 | #d3869b | ERGODIC |
| M1shaaa | user | 0 | #d3869b | ERGODIC |
| AustinCStone | user | 1 | #b8bb26 | PLUS |

### Repo Snapshot Stats (this sweep: 254 new rows; cumulative: 1198)

| Source | Repos | Top Repo | Stars |
|--------|-------|----------|-------|
| kubeflow | 47 | kubeflow/kubeflow | 15,600 ★ |
| kubeflow | — | kubeflow/pipelines | 4,125 ★ |
| kubeflow | — | kubeflow/spark-operator | 3,120 ★ |
| bmorphism | 50 | bmorphism/Gay.jl | pushed 2026-04-26 (today!) |
| plurigrid | 50 | plurigrid/asi | pushed 2026-04-26 (today!) |
| plurigrid | — | plurigrid/gorj | pushed 2026-04-26 (today!) |
| zubyul | 48 | zubyul/voice-observatory | pushed 2026-04-24 |
| migalkin | 19 | migalkin/NodePiece | 143 ★ (ICLR'22) |
| AustinCStone | 5 | AustinCStone/TextGAN | 92 ★ |
| TeglonLabs | 4 | TeglonLabs/mathpix-gem | 2 ★ |
| wasita | 10 | wasita/wasita.github.io | pushed 2026-04-22 |
| kristinezheng | 6 | kristinezheng.github.io | pushed 2026-04-09 |
| M1shaaa | 8 | M1shaaa/M1shaaa | pushed 2026-04-26 (today!) |
| DJedamski | 6 | DJedamski/School | 1 ★ |

**Notable activity today (2026-04-26):**
- `plurigrid/asi` — "everything is topological chemputer!" (HTML)
- `plurigrid/gorj` — forj + Rama topology nREPL (Clojure) — **this repo**
- `bmorphism/Gay.jl` — Wide-gamut color sampling w/ SPI (Julia, 187 open issues!)
- `M1shaaa/M1shaaa` — profile config repo (pushed 02:28 UTC)
- `bmorphism/nanoclj-zig` — NaN-boxed Clojure interpreter in Zig, GF(3) trit conservation

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

All 28 wallets in the A–Z + alice/bob swarm returned **0.00 APT**.  
Aptos mainnet API responded correctly; CoinStore resources are uninitialized or unfunded.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...512d | 0.00 |
| A–Z | 0x8699...–0x7af0... | 0.00 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **HEALTHY** — each requires exactly **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — DNS resolution failure for `testnet.mnx.fi`. No market data retrieved.

---

## DuckDB Table Counts (cumulative)

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1,198 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

**Total stars indexed:** 103,400 across 1,198 repo snapshot records  
**GF3 trit chain:** ERGODIC(0) → PLUS(1) → MINUS(-1) cycling across 11 sources  
**Sweep date:** 2026-04-26
