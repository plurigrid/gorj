# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-17T12:10Z  
**Run:** world-increment-sweep + hamming-swarm-snapshot agent  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|---|---|---|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |
| **Total** | | **391** |

### Most Recently Pushed Repos (Top sources)

| Org/User | Latest Push | Most Active Repo |
|---|---|---|
| kubeflow | 2026-06-17T11:54Z | (latest of 48) |
| plurigrid | 2026-06-17T11:13Z | (latest of 100) |
| M1shaaa | 2026-06-17T03:43Z | M1shaaa/M1shaaa (profile) |
| bmorphism | 2026-06-17T00:44Z | (latest of 100) |
| wasita | 2026-06-15T20:15Z | wasita/wasita.github.io (Svelte) |
| TeglonLabs | 2026-06-08T19:03Z | TeglonLabs/jank-crane (C++) |
| kristinezheng | 2026-06-07T22:52Z | kristinezheng.github.io |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|---|---|---|---|
| 0 | ERGODIC | #d3869b | 130 |
| 1 | PLUS | #b8bb26 | 131 |
| -1 | MINUS | #cc241d | 130 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses (alice, bob, A-Z) queried against Aptos mainnet fullnode.

**Result:** All 28 addresses returned `resource_not_found` for `CoinStore<AptosCoin>`. Accounts have not been initialized with APT on mainnet (no funded CoinStore present).

| World | Balance (APT) | Status |
|---|---|---|
| alice, bob, A-Z (all 28) | 0.0 | resource_not_found |

### Multisig Contract Probes

All 5 multisig accounts are **healthy** with exactly 2 signatures required:

| Pair | Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | `0x0da4f428...987003` | 2 | true |
| A-G | `0xf56c4a1c...c0096` | 2 | true |
| Y-Z | `0xd3ffe181...b883` | 2 | true |
| S-T | `0x3b1c3ae9...7883` | 2 | true |
| V-W | `0x40fad7b4...eb6d` | 2 | true |

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — `testnet.mnx.fi` returns HTTP 401 (Vercel authentication required). No market data accessible without visitor password or bypass token.

---

## DuckDB Tables Written

| Table | Rows |
|---|---|
| world_increments | 391 |
| repo_snapshots | 391 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth-gated) |

---

## Notable Signals

- **kubeflow** and **plurigrid** had pushes within the last hour of sweep time (active today)
- **M1shaaa** profile repo was pushed today at 03:43 UTC — profile config update
- **TeglonLabs/jank-crane** (newest TeglonLabs repo, 2026-06-08): C++, GF3 convergence maps, simonw workflow
- **wasita/wasita.github.io** (Svelte, 2026-06-15): most recently active personal repo in social graph
- All 5 Hamming swarm multisigs use consistent 2-of-N quorum threshold
- Aptos wallets (alice/bob/A-Z): no APT CoinStore initialized on mainnet
