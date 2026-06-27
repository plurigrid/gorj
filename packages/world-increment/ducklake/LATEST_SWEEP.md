# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-06-27 09:10 UTC  
**GF(3) color chain:** ERGODIC `#d3869b` (trit=0) / PLUS `#b8bb26` (trit=+1) / MINUS `#cc241d` (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul
- **Zubyul social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### DuckDB Stats

**world_increments** (GF3 chain):
```
┌──────────┬───────────┬───────┐
│ gf3_name │ gf3_color │   n   │
│ varchar  │  varchar  │ int64 │
├──────────┼───────────┼───────┤
│ PLUS     │ #b8bb26   │   139 │
│ MINUS    │ #cc241d   │   138 │
│ ERGODIC  │ #d3869b   │   137 │
└──────────┴───────────┴───────┘
```

**repo_snapshots** by source:
```
┌───────────────┬───────┐
│  org_or_user  │ repos │
│    varchar    │ int64 │
├───────────────┼───────┤
│ plurigrid     │   300 │
│ bmorphism     │   300 │
│ kubeflow      │   142 │
│ AustinCStone  │   126 │
│ TeglonLabs    │   111 │
│ zubyul        │    97 │
│ migalkin      │    79 │
│ wasita        │    71 │
│ kristinezheng │    41 │
│ M1shaaa       │    40 │
│ DJedamski     │    28 │
└───────────────┴───────┘
  11 rows     2 columns
```

| Table | Rows |
|---|---|
| world_increments | 414 |
| repo_snapshots | 1,335 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-27)

> All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`. All returned 0 APT
> (CoinStore resource absent or accounts have zero balance — typical for freshly registered addresses).

| World | Balance (APT) |
|---|---|
| A | `0.000000` |
| B | `0.000000` |
| C | `0.000000` |
| D | `0.000000` |
| E | `0.000000` |
| F | `0.000000` |
| G | `0.000000` |
| H | `0.000000` |
| I | `0.000000` |
| J | `0.000000` |
| K | `0.000000` |
| L | `0.000000` |
| M | `0.000000` |
| N | `0.000000` |
| O | `0.000000` |
| P | `0.000000` |
| Q | `0.000000` |
| R | `0.000000` |
| S | `0.000000` |
| T | `0.000000` |
| U | `0.000000` |
| V | `0.000000` |
| W | `0.000000` |
| X | `0.000000` |
| Y | `0.000000` |
| Z | `0.000000` |
| alice | `0.000000` |
| bob | `0.000000` |

### Multisig Contract Probes (Aptos mainnet)

All 5 multisig contracts responded correctly: **2-of-N threshold** confirmed.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | `0x0da4f428a0c007...` | 2 | ✓ |
| A-G | `0xf56c4a1c090621...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c...` | 2 | ✓ |
| V-W | `0x40fad7b423a843...` | 2 | ✓ |

### MNX Testnet Markets

- Endpoint `https://testnet.mnx.fi/api/markets` returned 13KB SPA HTML (no JSON market data).
- Status: **unavailable** — SPA requires browser JavaScript execution to render market data.
- Recorded as empty in `mnx_snapshots` table.

---

## DuckDB Location

`packages/world-increment/ducklake/world-increments.duckdb`

```sql
-- Quick query to review latest sweep
SELECT org_or_user, COUNT(*) as repos, MAX(pushed_at) as latest_push
FROM repo_snapshots GROUP BY org_or_user ORDER BY repos DESC;
```
