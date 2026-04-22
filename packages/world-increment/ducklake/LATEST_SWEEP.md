# World Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-04-22T22:20:13Z

---

## JOB 1: GitHub Social Graph Sweep

### Repos Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | rate-limited (unauthenticated) |
| TeglonLabs | org | rate-limited (unauthenticated) |
| zubyul | user | rate-limited (unauthenticated) |
| migalkin | user (social graph) | rate-limited |
| DJedamski | user (social graph) | rate-limited |
| wasita | user (social graph) | rate-limited |
| kristinezheng | user (social graph) | rate-limited |
| M1shaaa | user (social graph) | rate-limited |
| AustinCStone | user (social graph) | rate-limited |

**Total repos snapshotted: 200** (rate limit hit after plurigrid+bmorphism; unauthenticated GitHub API allows 60 req/hr)

### Notable plurigrid repos (top by recency)
- `gorj` (Clojure) - forj + Rama topology nREPL routing + GF(3) gay trit coloring
- `nanoclj-zig` (Zig) - NaN-boxed Clojure interpreter in Zig 0.15
- `zig-syrup` (Zig) - High-performance OCapN Syrup implementation

### GF(3) Color Chain Stats

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 66 |
| 1 | PLUS | #b8bb26 | 67 |
| -1 | MINUS | #cc241d | 67 |

**Total world_increments:** 200 (balanced trit distribution across GF(3))

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Balances queried via `0x1::coin::balance` view function on `fullnode.mainnet.aptoslabs.com`.

| World | Address | Balance (APT) |
|-------|---------|--------------|
| bob | 0x0a3c00c5...512d5d | **12.65700700** |
| F | 0x18a14b5b...3cf71 | 1.96051600 |
| L | 0x7c2eaeaf...7eba9 | 1.92726900 |
| J | 0x4d964db8...7f54 | 1.89509300 |
| alice | 0xc793acde...4cc7b | 0.43643352 |
| O | 0x73252b60...5a89d | 0.21013600 |
| K | 0xa732040a...25dc4 | 0.16196100 |
| P | 0x62187929...c948 | 0.14013600 |
| M | 0x6fed37a7...7f2e9 | 0.11228500 |
| N | 0xe7dde6da...51b2c | 0.10612100 |
| Q | 0xac40fa50...c89a9 | 0.10324000 |
| S | 0xb8753014...d0386 | 0.09178800 |
| R | 0x7ce605cc...6e10 | 0.09021700 |
| T | 0x35781dc0...f4588 | 0.07371300 |
| U | 0x75860da4...f9956 | 0.05577300 |
| A | 0x8699edc0...be9d7a | 0.05176700 |
| V | 0xb59dd817...9af2c3 | 0.04883299 |
| Y | 0xd8e32848...2444c4 | 0.04444900 |
| X | 0xa95cbbd1...33047d | 0.04257700 |
| W | 0x5f32aef7...cc7b0 | 0.04070500 |
| B | 0x3f892ebe...cb13 | 0.03625600 |
| Z | 0x7af0ef6e...e197c | 0.02426800 |
| D | 0xf77656248...fcfdd1 | 0.01162900 |
| C | 0x38b99e63...1535e | 0.01018500 |
| E | 0xdc1d9d53...958d36 | 0.00937200 |
| H | 0xce67c327...5300f | 0.00168100 |
| I | 0x070fe5d7...c1fc9 | 0.00068100 |
| G | 0x69a394c0...c7f32 | 0.00068100 |

**Total APT across 28 wallets:** ~18.73 APT

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...87003 | 2 | YES |
| A-G | 0xf56c4a1c...0096 | 2 | YES |
| Y-Z | 0xd3ffe181...5b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

All multisig accounts require **2-of-N** signatures. All healthy (contract state queryable).

### MNX Market Status

**Status: UNAVAILABLE**
- Endpoint: `https://testnet.mnx.fi/api/markets`
- Error: DNS cache overflow (network sandbox restriction)
- Recorded in `mnx_snapshots` table with status note.

---

## DuckDB Database

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 200 |
| repo_snapshots | 200 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

GF(3) color chain: `id%3==0` -> trit=0 ERGODIC `#d3869b` | `id%3==1` -> trit=1 PLUS `#b8bb26` | `id%3==2` -> trit=-1 MINUS `#cc241d`
