# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-30 (sweep run)
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 145 |
| kubeflow | org | 47 | 101,696 |
| TeglonLabs | org | 4 | 14 |
| bmorphism | user | 100 | 508 |
| zubyul | user | 49 | 40 |
| migalkin | social graph | 19 | 832 |
| AustinCStone | social graph | 46 | 324 |
| wasita | social graph | 24 | 10 |
| kristinezheng | social graph | ~14 | 0 |
| M1shaaa | social graph | ~14 | 0 |
| DJedamski | social graph | ~28 | 17 |

**Total this sweep:** 389 new repo snapshots inserted
**Cumulative DB:** 1333 repo_snapshots, 412 world_increments

### Notable Recent Activity (plurigrid)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| plurigrid/zig-syrup | Zig | 2 | 2026-04-30 |
| plurigrid/gorj | Clojure | 0 | 2026-04-30 |
| plurigrid/horse | TeX | 1 | 2026-04-29 |
| plurigrid/asi | HTML | 17 | 2026-04-26 |
| plurigrid/nanoclj-zig | Zig | 1 | 2026-04-25 |

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | #d3869b | 136 |
| PLUS | +1 | #b8bb26 | 138 |
| MINUS | -1 | #cc241d | 138 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm wallets (alice, bob, A–Z) were probed via Aptos mainnet fullnode.
All balances returned **0.0 APT** — CoinStore resources absent or accounts not yet funded on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes

All 5 multisig accounts responded with `sigs_required = 2`. All **HEALTHY**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4...003 | 2 | HEALTHY |
| A-G | 0xf56c...096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | HEALTHY |
| S-T | 0x3b1c...883 | 2 | HEALTHY |
| V-W | 0x40fa...b6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

`/api/markets` endpoint returned **404 Not Found**. `testnet.mnx.fi` is a Next.js SPA ("The AI Exchange") — market data requires authenticated/WebSocket access. **Status: UNAVAILABLE via unauthenticated REST.**

---

## DuckDB Tables Summary

| Table | Rows |
|-------|------|
| world_increments | 412 |
| repo_snapshots | 1333 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |
