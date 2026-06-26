# World-Increment Sweep — 2026-06-26

## Summary

| Table | Rows |
|---|---|
| world_increments | 433 (IDs 1–410) |
| repo_snapshots | 1354 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

## GF(3) Color Chain

| trit | name | color | count |
|---|---|---|---|
| 0 | ERGODIC | #d3869b | 143 |
| 1 | PLUS | #b8bb26 | 145 |
| −1 | MINUS | #cc241d | 145 |

Assignment rule: `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS.

## Job 1 — GitHub Social Graph Sweep

Queried repos from orgs/users: plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, and zubyul social graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone).

| source | world_increments entries |
|---|---|
| bmorphism | 103 |
| plurigrid | 102 |
| zubyul | 51 |
| kubeflow | 50 |
| AustinCStone | 42 |
| migalkin | 40 |
| wasita | 13 |
| M1shaaa | 10 |
| DJedamski | 8 |
| TeglonLabs | 7 |
| kristinezheng | 7 |
| **total** | **433** |

## Job 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

Queried 28 addresses (alice, bob, A–Z) via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: all 28 wallets returned NULL balance** — accounts exist on-chain but hold no APT in the standard CoinStore resource. Recorded as NULL in `aptos_snapshots`.

### Multisig Contract Probes (mainnet)

All 5 multisig contracts responded successfully.

| pair | address | sigs_required | healthy |
|---|---|---|---|
| A-B | 0x0da4f428...987003 | 2 | true |
| A-G | 0xf56c4a1c...c0096 | 2 | true |
| S-T | 0x3b1c3ae9...d7883 | 2 | true |
| V-W | 0x40fad7b4...0eb6d | 2 | true |
| Y-Z | 0xd3ffe181...5b883 | 2 | true |

5/5 healthy, `num_signatures_required=2` on all contracts.

### MNX Markets (testnet.mnx.fi)

**Unavailable** — testnet.mnx.fi is behind Vercel authentication. 0 rows inserted into `mnx_snapshots`.

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

## DuckDB Path

`packages/world-increment/ducklake/world-increments.duckdb`
