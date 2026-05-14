# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep Date:** 2026-05-14 00:20 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered

| Source | Type | Repos This Run | Notes |
|--------|------|---------------|-------|
| plurigrid | org | 100 | 100 returned (API max per page) |
| kubeflow | org | 48 | |
| TeglonLabs | org | 53 | |
| bmorphism | user | 100 | Via GitHub MCP search |
| zubyul | user | 49 | Via GitHub MCP search |
| migalkin | user (zubyul-graph) | 7 | KG research, NodePiece ⭐144 |
| DJedamski | user (zubyul-graph) | 4 | |
| wasita | user (zubyul-graph) | 5 | Svelte/network-science |
| kristinezheng | user (zubyul-graph) | 4 | MIT/cog-sci |
| M1shaaa | user (zubyul-graph) | 4 | |
| AustinCStone | user (zubyul-graph) | 6 | TextGAN ⭐92 |

**Total repos ingested this run: 380**

### GF(3) Color Chain Assignment

| Source | Increment ID | Trit | Color | Name |
|--------|-------------|------|-------|------|
| plurigrid | id%3=1 | 1 | #b8bb26 | PLUS |
| kubeflow | id%3=2 | -1 | #cc241d | MINUS |
| TeglonLabs | id%3=0 | 0 | #d3869b | ERGODIC |
| bmorphism | id%3=1 | 1 | #b8bb26 | PLUS |
| zubyul | id%3=2 | -1 | #cc241d | MINUS |
| migalkin | id%3=0 | 0 | #d3869b | ERGODIC |
| DJedamski | id%3=1 | 1 | #b8bb26 | PLUS |
| wasita | id%3=2 | -1 | #cc241d | MINUS |
| kristinezheng | id%3=0 | 0 | #d3869b | ERGODIC |
| M1shaaa | id%3=1 | 1 | #b8bb26 | PLUS |
| AustinCStone | id%3=2 | -1 | #cc241d | MINUS |

### DuckDB Ducklake State

```
world_increments : 34 rows (historical + this run)
repo_snapshots   : 1324 rows (historical + this run)
```

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) were queried against Aptos mainnet.
**All returned 0 APT** — accounts either unfunded or no CoinStore resource initialized on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793...4cc7b | 0.00 |
| bob | 0x0a3c...512d5d | 0.00 |
| A | 0x8699...9d7a | 0.00 |
| B | 0x3f89...cb13 | 0.00 |
| C | 0x38b9...535e | 0.00 |
| D | 0xf776...fdd1 | 0.00 |
| E | 0xdc1d...8d36 | 0.00 |
| F | 0x18a1...cf71 | 0.00 |
| G | 0x69a3...7f32 | 0.00 |
| H | 0xce67...300f | 0.00 |
| I | 0x070f...1fc9 | 0.00 |
| J | 0x4d96...7f54 | 0.00 |
| K | 0xa732...25dc4 | 0.00 |
| L | 0x7c2e...eba9 | 0.00 |
| M | 0x6fed...7f2e9 | 0.00 |
| N | 0xe7dd...51b2c | 0.00 |
| O | 0x7325...a89d | 0.00 |
| P | 0x6218...c948 | 0.00 |
| Q | 0xac40...c89a9 | 0.00 |
| R | 0x7ce6...6e10 | 0.00 |
| S | 0xb875...d386 | 0.00 |
| T | 0x3578...4588 | 0.00 |
| U | 0x7586...f9956 | 0.00 |
| V | 0xb59d...af2c3 | 0.00 |
| W | 0x5f32...c7b0 | 0.00 |
| X | 0xa95c...047d | 0.00 |
| Y | 0xd8e3...444c4 | 0.00 |
| Z | 0x7af0...197c | 0.00 |

### Multisig Contract Probes

All 5 multisig contracts healthy — each requires **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets

**Status: Unavailable via REST.** `https://testnet.mnx.fi/api/markets` returns 404. 
The CSP headers reveal the actual API at `wss://api.testnet.mnx.fi` (WebSocket-only). 
No REST market data endpoint is exposed publicly.

---

## DuckDB Schema Summary

```sql
world_increments  -- GF(3) color chain per source
repo_snapshots    -- repo metadata per increment
aptos_snapshots   -- wallet balance snapshots (28 addresses)
multisig_probes   -- multisig health checks (5 pairs)
mnx_snapshots     -- MNX market data (unavailable this run)
```

**Ducklake path:** `packages/world-increment/ducklake/world-increments.duckdb`
