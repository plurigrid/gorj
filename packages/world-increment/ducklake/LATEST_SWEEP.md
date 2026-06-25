# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-25  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| org_or_user   | repos | stars | latest_push          |
|---------------|------:|------:|----------------------|
| plurigrid     |   100 |    77 | 2026-06-25T19:11:13Z |
| bmorphism     |   100 |   247 | 2026-06-25T00:40:37Z |
| zubyul        |    49 |    14 | 2026-04-24T05:56:17Z |
| kubeflow      |    48 | 34254 | 2026-06-25T19:47:47Z |
| AustinCStone  |    40 |   108 | 2026-02-11T01:10:54Z |
| migalkin      |    19 |   280 | 2025-08-04T03:01:46Z |
| wasita        |    11 |     5 | 2026-06-25T16:23:37Z |
| M1shaaa       |     8 |     0 | 2026-06-25T14:24:06Z |
| DJedamski     |     6 |     3 | 2018-03-07T12:36:09Z |
| TeglonLabs    |     5 |     2 | 2026-06-08T19:03:03Z |
| kristinezheng |     5 |     0 | 2026-06-07T22:52:50Z |
| **TOTAL**     | **391** | **34990** | |

### GF(3) Color Chain

- `id % 3 == 0` trit=0 ERGODIC #d3869b
- `id % 3 == 1` trit=1 PLUS #b8bb26
- `id % 3 == 2` trit=-1 MINUS #cc241d

All 391 repo snapshots stored in `repo_snapshots` with GF3 increment linkage.

### Notable Activity (2026-06-25)
- **kubeflow** active today (34k+ stars, ML infra)
- **plurigrid** and **bmorphism** both pushed today
- **wasita** (Svelte personal site) pushed at 16:23 UTC today
- **M1shaaa** profile repo updated at 14:24 UTC today

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

All 28 wallets (alice, bob, A-Z) queried against Aptos mainnet CoinStore.

**Result: All balances = 0.0 APT** (accounts not funded / CoinStore not initialized)

### Multisig Contract Probes (5 contracts) - ALL HEALTHY

| Pair | Address                                                            | Sigs Required |
|------|--------------------------------------------------------------------|---------------|
| A-B  | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2             |
| A-G  | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2             |
| Y-Z  | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883  | 2             |
| S-T  | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883  | 2             |
| V-W  | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d  | 2             |

### MNX Markets

testnet.mnx.fi returns Vercel authentication required. Status: UNAVAILABLE.

---

## DuckDB Tables

| Table             | Rows |
|-------------------|-----:|
| world_increments  |   11 |
| repo_snapshots    |  391 |
| aptos_snapshots   |   28 |
| multisig_probes   |    5 |
| mnx_snapshots     |    0 |
