# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-26T19:30:00Z  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted (GF3 Color Chain)

| id | source | type | repos | gf3_trit | gf3_name | color |
|----|--------|------|-------|----------|----------|-------|
| 1 | plurigrid | org | 30 | +1 | PLUS | `#b8bb26` |
| 2 | kubeflow | org | 30 | -1 | MINUS | `#cc241d` |
| 3 | bmorphism | user | 30 | 0 | ERGODIC | `#d3869b` |
| 4 | zubyul | user | 30 | +1 | PLUS | `#b8bb26` |
| 5 | migalkin | user_social | 19 | -1 | MINUS | `#cc241d` |
| 6 | AustinCStone | user_social | 30 | 0 | ERGODIC | `#d3869b` |
| 7 | TeglonLabs | org | 5 | +1 | PLUS | `#b8bb26` |
| 8 | DJedamski | user_social | 6 | -1 | MINUS | `#cc241d` |
| 9 | wasita | user_social | 6 | 0 | ERGODIC | `#d3869b` |
| 10 | kristinezheng | user_social | 5 | +1 | PLUS | `#b8bb26` |
| 11 | M1shaaa | user_social | 8 | -1 | MINUS | `#cc241d` |

**Total repos snapshotted:** 199

### Notable Active Repos (most recently pushed)

| repo | stars | pushed |
|------|-------|--------|
| kubeflow/pipelines | 4169 | 2026-07-26 |
| kubeflow/trainer | 2154 | 2026-07-26 |
| plurigrid/gorj | 1 | 2026-07-26 (today!) |
| bmorphism/Gay.jl | 2 | 2026-07-26 |
| M1shaaa/M1shaaa | 0 | 2026-07-26 |
| plurigrid/asi | 44 | 2026-07-10 |
| wasita/wasita.github.io | 1 | 2026-07-21 |

### Zubyul Social Graph Summary

| user | repos | focus area |
|------|-------|------------|
| migalkin | 19 | Knowledge graphs, NodePiece (144 stars), StarE (89 stars) |
| DJedamski | 6 | Data science, Kaggle competitions |
| wasita | 6 | Cognitive science, Svelte web, Typst |
| kristinezheng | 5 | Cognitive science, MIT BCS, lookit studies |
| M1shaaa | 8 | Cognitive science (Yale/MIT), lookit experiments |
| AustinCStone | 30 | Computer vision, ML, Python tooling |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 accounts)

All 28 accounts (alice, bob, A-Z) were probed for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All accounts exist on-chain (alice has sequence_number=72 confirming activity) but none hold APT via the legacy CoinStore resource. Accounts use the newer FungibleAsset (FA) framework for APT storage. Balance via legacy CoinStore: 0 APT for all 28 addresses.

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are healthy with num_signatures_required = 2:

| pair | address | sigs_required | status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | 2 | healthy |
| A-G | 0xf56c4a1c... | 2 | healthy |
| Y-Z | 0xd3ffe181... | 2 | healthy |
| S-T | 0x3b1c3ae9... | 2 | healthy |
| V-W | 0x40fad7b4... | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

testnet.mnx.fi is a Next.js SPA. The /api/markets path returns HTML (no public REST API). Market data: unavailable.

---

## Database Summary

| table | rows | notes |
|-------|------|-------|
| world_increments | 11 | GF3 color chain, 11 sources |
| repo_snapshots | 199 | distributed across 11 orgs/users |
| aptos_snapshots | 28 | alice, bob, A-Z; balance=0 via legacy CoinStore |
| multisig_probes | 5 | A-B, A-G, Y-Z, S-T, V-W; all healthy, sigs=2 |
| mnx_snapshots | 1 | SPA only, no public REST API |
