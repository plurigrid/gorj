# World-Increment Sweep + Hamming Snapshot

**Date/Time:** 2026-04-05 08:31 UTC  
**DuckDB:** `/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Social Graph Snapshot

### Repos Snapshotted by Org/User

| Source         | Type | Count |
|----------------|------|-------|
| bmorphism      | user | 98    |
| plurigrid      | org  | 95    |
| kubeflow       | org  | 46    |
| zubyul         | user | 44    |
| AustinCStone   | user | 40    |
| migalkin       | user | 19    |
| wasita         | user | 9     |
| M1shaaa        | user | 8     |
| kristinezheng  | user | 6     |
| DJedamski      | user | 6     |
| TeglonLabs     | org  | 3     |
| **TOTAL**      |      | **374** |

### GF(3) Color Distribution

| GF(3) Name | Color   | Hex       | Count |
|------------|---------|-----------|-------|
| ERGODIC    | pink    | #d3869b   | 124   |
| PLUS       | yellow  | #b8bb26   | 125   |
| MINUS      | red     | #cc241d   | 125   |

Assignment rule: id%3==0 -> ERGODIC (trit=0), id%3==1 -> PLUS (trit=1), id%3==2 -> MINUS (trit=-1)

---

## Aptos Hamming Swarm Snapshot

All 28 addresses queried against Aptos mainnet. All returned resource_not_found (no APT coin store at these addresses), recorded as 0.0 APT.

| World | Address (truncated)    | Balance (APT) |
|-------|------------------------|---------------|
| alice | 0xc793...24cc7b        | 0.0           |
| bob   | 0x0a3c...12d5d        | 0.0           |
| A     | 0x8699...be9d7a        | 0.0           |
| B     | 0x3f89...7cb13        | 0.0           |
| C     | 0x38b9...1535e        | 0.0           |
| D     | 0xf776...cfdd1        | 0.0           |
| E     | 0xdc1d...58d36        | 0.0           |
| F     | 0x18a1...c3cf71        | 0.0           |
| G     | 0x69a3...cc7f32        | 0.0           |
| H     | 0xce67...5300f        | 0.0           |
| I     | 0x070f...01fc9        | 0.0           |
| J     | 0x4d96...87f54        | 0.0           |
| K     | 0xa732...425dc4        | 0.0           |
| L     | 0x7c2e...37eba9        | 0.0           |
| M     | 0x6fed...7f2e9        | 0.0           |
| N     | 0xe7dd...551b2c        | 0.0           |
| O     | 0x7325...5a89d        | 0.0           |
| P     | 0x6218...c948        | 0.0           |
| Q     | 0xac40...c89a9        | 0.0           |
| R     | 0x7ce6...76e10        | 0.0           |
| S     | 0xb875...0386        | 0.0           |
| T     | 0x3578...f4588        | 0.0           |
| U     | 0x7586...f9956        | 0.0           |
| V     | 0xb59d...af2c3        | 0.0           |
| W     | 0x5f32...cc7b0        | 0.0           |
| X     | 0xa95c...3047d        | 0.0           |
| Y     | 0xd8e3...444c4        | 0.0           |
| Z     | 0x7af0...197c        | 0.0           |

---

## Multisig Probes

All 5 pairs probed via 0x1::multisig_account::num_signatures_required on Aptos mainnet.

| Pair  | Address (truncated)    | Sigs Required | Healthy |
|-------|------------------------|---------------|---------|
| A-B   | 0x0da4...87003         | 2             | TRUE    |
| A-G   | 0xf56c...0096          | 2             | TRUE    |
| Y-Z   | 0xd3ff...b883          | 2             | TRUE    |
| S-T   | 0x3b1c...7883          | 2             | TRUE    |
| V-W   | 0x40fa...eb6d          | 2             | TRUE    |

All multisig accounts are healthy (sigs_required > 0).

---

## MNX Market Status

The MNX testnet API (https://testnet.mnx.fi/api/markets) returned a non-JSON HTML response (Next.js app). No market data could be parsed. A placeholder row has been inserted into mnx_snapshots with ticker='UNAVAILABLE'.

---

## DuckDB Table Summary

| Table              | Rows |
|--------------------|------|
| world_increments   | 374  |
| repo_snapshots     | 374  |
| aptos_snapshots    | 28   |
| multisig_probes    | 5    |
| mnx_snapshots      | 1    |
