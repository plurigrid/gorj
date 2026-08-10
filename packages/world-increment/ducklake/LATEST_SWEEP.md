# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-10  
**Run type:** Automated — world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | Org | 100 |
| kubeflow | Org | 49 |
| TeglonLabs | Org | 5 |
| bmorphism | User | 100 |
| zubyul | User | 49 |
| migalkin | Social (zubyul) | 19 |
| wasita | Social (zubyul) | 14 |
| DJedamski | Social (zubyul) | 6 |
| kristinezheng | Social (zubyul) | 5 |
| M1shaaa | Social (zubyul) | 8 |
| AustinCStone | Social (zubyul) | 20+ |
| **TOTAL** | | **312 repo snapshots** |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 104 |
| 1 | PLUS | #b8bb26 | 104 |
| -1 | MINUS | #cc241d | 104 |

### Notable Repos (by stars)

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| AustinCStone/TextGAN | 92 | Python | GAN for text generation (TensorFlow) |
| migalkin/NodePiece | 144 | Python | Parameter-Efficient KG Representations (ICLR'22) |
| migalkin/StarE | 89 | Python | Hyper-Relational KG Message Passing (EMNLP 2020) |
| plurigrid/asi | 60 | HTML | everything is topological chemputer! |
| plurigrid/gorj | 1 | Clojure | forj + Rama topology nREPL routing + GF(3) coloring |
| plurigrid/zig-syrup | 2 | Zig | OCapN Syrup with CapTP optimizations |
| TeglonLabs/mathpix-gem | 2 | Ruby | Mathematical OCR in Ruby |
| TeglonLabs/jank-crane | 0 | C++ | crane-jank converged-IR hub (pushed 2026-06-08) |
| wasita/xoxowasita-analysis | 0 | Python | Fresh push: 2026-08-10T03:48:50Z |

### Most Active (recent push)

| Repo | Pushed |
|------|--------|
| plurigrid/gorj | 2026-08-10T05:17:27Z |
| wasita/xoxowasita-analysis | 2026-08-10T03:48:50Z |
| wasita/wasita.github.io | 2026-08-10T02:27:08Z |
| plurigrid/place | 2026-08-09T01:07:33Z |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) returned **0.0 APT**.

- Likely cause: coin store resource not initialized on-chain for these addresses, or genuinely zero balance.
- All queries executed successfully against `fullnode.mainnet.aptoslabs.com`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...9a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes

All 5 multisig accounts are **healthy** (2-of-N signatures required).

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a Next.js SPA with no public REST API endpoints. The `/api/markets` path returns the SPA shell. No market data could be extracted.

---

## DuckDB Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 312 (this run) |
| repo_snapshots | 312 (this run) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
