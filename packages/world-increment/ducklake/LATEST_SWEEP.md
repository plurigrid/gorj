# World-Increment Sweep — 2026-07-20

## Sweep Metadata
- **Date:** 2026-07-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos ledger version at query time:** 6,373,905,001 (epoch 16609)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social (zubyul graph) | 19 |
| wasita | social (zubyul graph) | 12 |
| AustinCStone | social (zubyul graph) | 20 |
| DJedamski | social (zubyul graph) | 6 |
| kristinezheng | social (zubyul graph) | 5 |
| M1shaaa | social (zubyul graph) | 8 |
| **TOTAL** | | **373** |

### Notable Repos (this sweep)
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub with GF3 convergence maps — active
- **wasita/wasita.github.io** (Svelte, pushed 2026-07-20): updated today
- **migalkin/NodePiece** (Python, 144★): knowledge graph embeddings, ICLR'22
- **migalkin/StarE** (Python, 89★): hyper-relational KG, EMNLP 2020
- **AustinCStone/TextGAN** (Python, 92★): TensorFlow text GAN
- **AustinCStone/byteruckus** (HTML, pushed 2026-07-15): new active repo

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 addresses)

**All 28 returned HTTP 404 — `CoinStore<0x1::aptos_coin::AptosCoin>` not initialized.**

These accounts are not yet funded on Aptos mainnet; CoinStore resource is
only created upon first APT receipt. All balances recorded as NULL.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

**All 5 multisig contracts respond correctly — 2-of-N threshold on all pairs.**

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Vercel deployment protection (password auth required). No market data extractable.

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Cumulative DB State

| Table | Rows |
|-------|------|
| world_increments | 346 |
| repo_snapshots | 1,267 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
