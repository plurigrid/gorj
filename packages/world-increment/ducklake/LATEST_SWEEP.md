# World-Increment Sweep + Hamming Snapshot — 2026-04-29

## Sweep Metadata
- **Date:** 2026-04-29
- **Agent:** world-increment-sweep (two-job autonomous sweep)
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Status: GitHub API Rate-Limited (Unauthenticated)

The unauthenticated GitHub API rate limit was exhausted on this machine's IP address.
No `GH_TOKEN` was present in the environment. New repo snapshots could not be fetched.
The `repo_snapshots` table retains **944 rows** from prior sweeps (2026-04-10, 2026-04-14).

### Repos Snapshotted (cumulative, all sweeps)

| Source         | Type | Repos |
|----------------|------|-------|
| plurigrid      | org  |  200  |
| bmorphism      | user |  200  |
| TeglonLabs     | org  |  106  |
| kubeflow       | org  |   94  |
| AustinCStone   | user |   86  |
| migalkin       | user |   60  |
| wasita         | user |   60  |
| zubyul         | user |   48  |
| kristinezheng  | user |   36  |
| M1shaaa        | user |   32  |
| DJedamski      | user |   22  |
| **TOTAL**      |      | **944** |

### GF(3) Color Chain Stats (2026-04-29 new increments: 14 sources logged)

| GF(3) Trit | Color Name | Hex     | Count (this sweep) |
|------------|------------|---------|-------------------|
| 0          | ERGODIC    | #d3869b | 4                 |
| 1          | PLUS       | #b8bb26 | 5                 |
| 2          | MINUS      | #cc241d | 5                 |

Chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → PLUS → MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `0x1::coin::balance` view function (POST /v1/view).  
Ledger version at query time: ~5,046,716,747.  
All 28 wallets successfully queried (100% success rate).

| World | Address (truncated)              | APT Balance   |
|-------|----------------------------------|---------------|
| alice | 0xc793...4cc7b                   | 0.43643352    |
| bob   | 0x0a3c...512d5d                  | 12.65700700   |
| A     | 0x8699...e9d7a                   | 0.05176700    |
| B     | 0x3f89...cb13                    | 0.03625600    |
| C     | 0x38b9...535e                    | 0.01018500    |
| D     | 0xf776...cfdd1                   | 0.01162900    |
| E     | 0xdc1d...58d36                   | 0.00937200    |
| F     | 0x18a1...cf71                    | 1.96051600    |
| G     | 0x69a3...7f32                    | 0.00068100    |
| H     | 0xce67...5300f                   | 0.00168100    |
| I     | 0x070f...1fc9                    | 0.00068100    |
| J     | 0x4d96...7f54                    | 1.89509300    |
| K     | 0xa732...25dc4                   | 0.16196100    |
| L     | 0x7c2e...7eba9                   | 1.92726900    |
| M     | 0x6fed...f2e9                    | 0.11228500    |
| N     | 0xe7dd...51b2c                   | 0.10612100    |
| O     | 0x7325...a89d                    | 0.21013600    |
| P     | 0x6218...ec948                   | 0.14013600    |
| Q     | 0xac40...c89a9                   | 0.10324000    |
| R     | 0x7ce6...76e10                   | 0.09021700    |
| S     | 0xb875...d0386                   | 0.09178800    |
| T     | 0x3578...3f4588                  | 0.07371300    |
| U     | 0x7586...f9956                   | 0.05577300    |
| V     | 0xb59d...af2c3                   | 0.04883299    |
| W     | 0x5f32...cc7b0                   | 0.04070500    |
| X     | 0xa95c...3047d                   | 0.04257700    |
| Y     | 0xd8e3...444c4                   | 0.04444900    |
| Z     | 0x7af0...197c                    | 0.02426800    |

**Swarm total:** 20.34477251 APT  
**Swarm avg:** 0.72659902 APT  
**Largest holder:** bob (12.657007 APT)

### Multisig Contract Probes

All 5 contracts queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated)          | Sigs Required | Healthy |
|------|------------------------------|---------------|---------|
| A-B  | 0x0da4...7003                | 2             | YES     |
| A-G  | 0xf56c...0096                | 2             | YES     |
| Y-Z  | 0xd3ff...b883                | 2             | YES     |
| S-T  | 0x3b1c...7883                | 2             | YES     |
| V-W  | 0x40fa...eb6d                | 2             | YES     |

All 5/5 multisig contracts healthy, all requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE — SPA with no accessible REST API**

`testnet.mnx.fi` serves a Next.js SPA. All API paths attempted returned HTML or 404:
- `/api/markets` → SPA HTML
- `/api/v1/markets` → SPA HTML  
- `/api/tickers` → 404
- `api.testnet.mnx.fi/markets` → connection refused

No market data could be extracted programmatically. Recorded as SPA note in `mnx_snapshots`.

---

## DuckDB Table Summary

| Table             | Rows  | Notes                            |
|-------------------|-------|----------------------------------|
| world_increments  | 37+   | Multi-sweep cumulative           |
| repo_snapshots    | 944   | Prior sweeps (rate-limited today)|
| aptos_snapshots   | 28    | Fresh 2026-04-29 snapshot        |
| multisig_probes   | 5     | Fresh 2026-04-29 snapshot        |
| mnx_snapshots     | 1     | SPA unavailability note          |

---

## GF(3) Assignment Rule

- `id mod 3 == 0` → trit=0, color=ERGODIC, hex=#d3869b (pink/rose)
- `id mod 3 == 1` → trit=1, color=PLUS, hex=#b8bb26 (yellow-green)
- `id mod 3 == 2` → trit=2 (−1), color=MINUS, hex=#cc241d (red)

## Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
