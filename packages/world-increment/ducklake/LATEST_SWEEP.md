# World Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-05-09  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources
- **Orgs:** plurigrid (100), kubeflow (48), TeglonLabs (4)
- **Users:** bmorphism (100), zubyul (49)
- **Zubyul social graph:** migalkin (19), DJedamski (6), wasita (11), kristinezheng (6), M1shaaa (8), AustinCStone (40)

**Total repos snapshotted:** 391

### Repo Snapshot by Source

| org_or_user   | repos | total_stars | latest_push         |
|---------------|------:|------------:|---------------------|
| plurigrid     |   100 |          71 | 2026-05-09 14:21    |
| bmorphism     |   100 |         248 | 2026-05-09 00:33    |
| zubyul        |    49 |          14 | 2026-04-24 05:56    |
| kubeflow      |    48 |       34030 | 2026-05-09 12:48    |
| AustinCStone  |    40 |         108 | 2026-02-11 01:10    |
| migalkin      |    19 |         279 | 2025-08-04 03:01    |
| wasita        |    11 |           4 | 2026-05-06 05:14    |
| M1shaaa       |     8 |           0 | 2026-05-09 13:09    |
| DJedamski     |     6 |           3 | 2018-03-07 12:36    |
| kristinezheng |     6 |           0 | 2026-04-09 17:09    |
| TeglonLabs    |     4 |           2 | 2026-01-01 12:13    |

### GF(3) Color Chain Distribution

| GF3 Name | Color   | Count |
|----------|---------|------:|
| PLUS     | #b8bb26 |   131 |
| ERGODIC  | #d3869b |   130 |
| MINUS    | #cc241d |   130 |

- `id % 3 == 0` → trit=0 ERGODIC #d3869b
- `id % 3 == 1` → trit=1 PLUS #b8bb26
- `id % 3 == 2` → trit=-1 MINUS #cc241d

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A-Z)

All 28 addresses queried against Aptos Mainnet
(`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`).

**Result:** All addresses returned `resource_not_found` at ledger ~5.2B -
no APT CoinStore registered on any of the 28 Hamming swarm wallets.
Balance recorded as **0.0 APT** for all.

| World  | Address (truncated)  | Balance (APT) |
|--------|----------------------|:-------------:|
| alice  | 0xc793...cc7b        | 0.0           |
| bob    | 0x0a3c...512d        | 0.0           |
| A-Z    | (26 addresses)       | 0.0 each      |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated)  | Sigs Required | Healthy |
|------|----------------------|:-------------:|:-------:|
| A-B  | 0x0da4...7003        | 2             | yes     |
| A-G  | 0xf56c...0096        | 2             | yes     |
| Y-Z  | 0xd3ff...b883        | 2             | yes     |
| S-T  | 0x3b1c...7883        | 2             | yes     |
| V-W  | 0x40fa...eb6d        | 2             | yes     |

**All 5 multisigs healthy** (2-of-N threshold active and responding).

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** - site is a Next.js SPA returning HTML for all routes.
No structured market data extractable via HTTP. No rows stored in `mnx_snapshots`.

---

## DuckDB Tables

| Table             | Rows | Description                              |
|-------------------|-----:|------------------------------------------|
| world_increments  |  391 | GF(3) color-chained repo events          |
| repo_snapshots    |  391 | Full repo metadata per source            |
| aptos_snapshots   |   28 | APT balances for alice, bob, A-Z         |
| multisig_probes   |    5 | Multisig threshold checks                |
| mnx_snapshots     |    0 | MNX markets (unavailable)                |
