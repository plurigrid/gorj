# World-Increment Sweep + Hamming Swarm Snapshot
**Sweep date:** 2026-06-23  
**GF(3) increment id:** 1 — trit=1 PLUS #b8bb26  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources snapshotted
| Source | Type | Unique Repos | Total Stars |
|---|---|---|---|
| kubeflow | org | 50 | 101,969 |
| migalkin | user (social graph) | 30 | 830 |
| bmorphism | user | 168 | 503 |
| AustinCStone | user (social graph) | 43 | 319 |
| plurigrid | org | 168 | 157 |
| zubyul | user | 59 | 40 |
| DJedamski | user (social graph) | 11 | 16 |
| TeglonLabs | org | 54 | 14 |
| wasita | user (social graph) | 31 | 10 |
| kristinezheng | user (social graph) | 18 | 0 |
| M1shaaa | user (social graph) | 16 | 0 |

**Total unique repos indexed:** ~648 across 11 orgs/users

### Notable repos (by stars)
- `kubeflow/kubeflow` — 15,740 stars
- `kubeflow/pipelines` — 4,157 stars
- `AustinCStone/TextGAN` — 92 stars, TF text GAN
- `migalkin/NodePiece` — 144 stars, ICLR'22 KG paper
- `TeglonLabs/jank-crane` — C++ GF3 IR hub, pushed 2026-06-08

### Recent activity (most recent pushes)
- `wasita/proj-template` pushed 2026-06-19
- `wasita/wasita.github.io` pushed 2026-06-15
- `TeglonLabs/jank-crane` pushed 2026-06-08
- `kristinezheng/kristinezheng.github.io` pushed 2026-06-07

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)
All 28 addresses (alice, bob, A-Z) queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result: All balances = 0 APT** (no CoinStore resource initialized or zero balance)

### Multisig Contract Probes — ALL 5 HEALTHY

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

### MNX Markets
`testnet.mnx.fi` blocked by Vercel deployment protection. Status: UNAVAILABLE.

---

## DuckDB Tables
- `world_increments` — GF3 color-chain sweep log
- `repo_snapshots` — GitHub repo snapshots per org/user
- `aptos_snapshots` — 28 Hamming swarm wallet balances
- `multisig_probes` — 5 multisig sigs_required probes
- `mnx_snapshots` — MNX market data (unavailable)
