# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-07-26 01:11:35 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | social | 20 |
| migalkin | social | 19 |
| wasita | social | 12 |
| M1shaaa | social | 8 |
| DJedamski | social | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | social | 5 |

**Total repos indexed:** 373

### GF(3) Color Chain Applied
- `id%3==0` → trit=0 ERGODIC #d3869b (rose)
- `id%3==1` → trit=1 PLUS #b8bb26 (green)
- `id%3==2` → trit=-1 MINUS #cc241d (red)

### DuckDB Tables
- `world_increments` — GF(3)-tagged event log
- `repo_snapshots` — full repo metadata per increment
- Path: `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (26 addresses: A-Z + alice/bob)

| World | Balance (APT) | Status |
|-------|--------------|--------|
| A | 0.000000 | no CoinStore |
| B | 0.000000 | no CoinStore |
| C | 0.000000 | no CoinStore |
| D | 0.000000 | no CoinStore |
| E | 0.000000 | no CoinStore |
| F | 0.000000 | no CoinStore |
| G | 0.000000 | no CoinStore |
| H | 0.000000 | no CoinStore |
| I | 0.000000 | no CoinStore |
| J | 0.000000 | no CoinStore |
| K | 0.000000 | no CoinStore |
| L | 0.000000 | no CoinStore |
| M | 0.000000 | no CoinStore |
| N | 0.000000 | no CoinStore |
| O | 0.000000 | no CoinStore |
| P | 0.000000 | no CoinStore |
| Q | 0.000000 | no CoinStore |
| R | 0.000000 | no CoinStore |
| S | 0.000000 | no CoinStore |
| T | 0.000000 | no CoinStore |
| U | 0.000000 | no CoinStore |
| V | 0.000000 | no CoinStore |
| W | 0.000000 | no CoinStore |
| X | 0.000000 | no CoinStore |
| Y | 0.000000 | no CoinStore |
| Z | 0.000000 | no CoinStore |
| alice | 0.000000 | no CoinStore |
| bob | 0.000000 | no CoinStore |

**Note:** All 28 addresses show no CoinStore resource on Aptos mainnet (accounts may be empty or not exist).

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ |

**Result:** All 5 multisig contracts healthy, each requiring **2 signatures**.

### MNX Markets (testnet.mnx.fi)

**Status:** SPA reachable (HTTP 200) but no REST API endpoints found at common paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`). Market data unavailable.

---

## Summary

- **373 repos** snapshotted across 11 sources (3 orgs + 2 primary users + 6 social graph users)
- **28 Aptos addresses** probed: all show 0 APT balance (no active CoinStore)
- **5 multisig pairs** all healthy with 2/N signature threshold
- **MNX testnet** SPA alive but API unavailable
- DuckDB ducklake persisted to `packages/world-increment/ducklake/world-increments.duckdb`
