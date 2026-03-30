# World Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-03-30 21:25:08 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Fetched |
|--------|------|---------------|
| plurigrid | org | 100 (API limit, actual stored: 212 with dedup) |
| kubeflow | org | 2 |
| TeglonLabs | org | 2 |
| bmorphism | user | 100 (API limit) |
| zubyul | user | 23 |
| migalkin | user (zubyul social) | 2 |
| DJedamski | user (zubyul social) | 11 |
| wasita | user (zubyul social) | 28 |
| kristinezheng | user (zubyul social) | 18 |
| M1shaaa | user (zubyul social) | 16 |
| AustinCStone | user (zubyul social) | 2 |

**Total unique repo snapshots:** 804 rows in repo_snapshots table
**Total world_increments:** 321 rows (repos + events)
**Events captured:** bmorphism (2), zubyul (2)

### GF(3) Color Chain Summary
- trit=1 (PLUS #b8bb26): id%3==1
- trit=-1 (MINUS #cc241d): id%3==2
- trit=0 (ERGODIC #d3869b): id%3==0

### DuckDB Location
`packages/world-increment/ducklake/world-increments.duckdb`

Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`

---

## JOB 2: Hamming Swarm Aptos Snapshot

### Wallet Balances (Aptos Mainnet)

All balances queried at 2026-03-30 21:25:08 UTC. All wallets returned 0 APT (no CoinStore resource found or zero balance).

| Label | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Note:** All wallets show 0 APT. This is consistent with these being Hamming swarm addresses that may not yet be funded or use a different coin resource.

### Multisig Contract Probes

All 5 multisig contracts healthy with 2 signatures required.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

All multisig accounts require 2-of-N signatures. All contracts are live and responding on Aptos mainnet.

### MNX Markets Status

**Status: UNAVAILABLE** — `https://testnet.mnx.fi/api/markets` returns HTTP 404 (Next.js HTML page, not JSON API). The testnet MNX markets API endpoint is not available at this time.

---

## Summary

| Component | Status | Count |
|-----------|--------|-------|
| GitHub repos snapshotted | OK | 804 |
| World increments recorded | OK | 321 |
| Aptos wallets queried | OK | 28 |
| Multisig contracts probed | OK | 5/5 healthy |
| MNX markets | UNAVAILABLE | N/A |
