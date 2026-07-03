# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-07-03  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### This Run: plurigrid org (100 repos)

| repo | lang | ⭐ | forks | pushed |
|---|---|---|---|---|
| plurigrid/asi | HTML | 28 | 8 | 2026-06-29 |
| plurigrid/place | TeX | 1 | 0 | 2026-06-29 |
| plurigrid/eirobri | Clojure | 0 | 0 | 2026-06-30 |
| plurigrid/nash-portal | Rust | 2 | 3 | 2026-05-19 |
| plurigrid/gorj | Clojure | 0 | 0 | 2026-07-02 |
| plurigrid/ontology | JavaScript | 8 | 9 | 2025-05-27 |
| plurigrid/vcg-auction | Rust | 7 | 2 | 2023-03-16 |
| plurigrid/agent | Python | 5 | 1 | 2023-03-31 |
| plurigrid/StochFlow | Python | 4 | 1 | 2024-03-20 |
| plurigrid/asi-skills | Julia | 3 | 0 | 2026-04-26 |

### Cumulative DB Snapshot (all runs)

| source | repos | total ⭐ | latest push |
|---|---|---|---|
| kubeflow | 94 | 67,723 | 2026-04-14 |
| migalkin | 60 | 554 | 2025-08-04 |
| bmorphism | 200 | 262 | 2026-04-09 |
| AustinCStone | 86 | 216 | 2026-02-11 |
| plurigrid | 300 | 159 | 2026-07-02 |
| zubyul | 48 | 26 | 2026-04-09 |
| DJedamski | 22 | 14 | 2018-03-07 |
| TeglonLabs | 106 | 12 | 2026-01-16 |
| wasita | 60 | 6 | 2026-04-13 |
| M1shaaa | 32 | 0 | 2026-04-13 |
| kristinezheng | 36 | 0 | 2026-04-09 |

> Note: bmorphism, zubyul, and social-graph users (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) are present from prior sweep runs. kubeflow + TeglonLabs also from prior runs.

### GF(3) Color Chain (this run, 100 increments)

| trit | color | name | count |
|---|---|---|---|
| 1 | #b8bb26 | PLUS | 34 |
| 0 | #d3869b | ERGODIC | 33 |
| -1 | #cc241d | MINUS | 33 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-07-03)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`. All returned **0 APT** (accounts exist on-chain but hold no APT balance in CoinStore).

| world | address (truncated) | APT |
|---|---|---|
| alice | 0xc793ac…4cc7b | 0.0 |
| bob | 0x0a3c00…512d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig accounts respond healthy with `num_signatures_required = 2`.

| pair | address (truncated) | sigs_required | healthy |
|---|---|---|---|
| A-B | 0x0da4f4…87003 | 2 | ✓ |
| A-G | 0xf56c4a…0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1…b883 | 2 | ✓ |
| S-T | 0x3b1c3a…7883 | 2 | ✓ |
| V-W | 0x40fad7…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active, requires authentication token. No market data retrievable without bypass credential.

---

## DuckDB Table Summary

| table | rows |
|---|---|
| world_increments | 123 |
| repo_snapshots | 1,044 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth blocked) |
