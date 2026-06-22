# World-Increment + Hamming Swarm Snapshot

**Timestamp:** 2026-06-22T11:10:00Z
**Run date:** 2026-06-22

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 (of 101) |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (of 105) |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 40 |

**Total unique repos indexed:** 646

### Most Recently Active Repos (2026-06-22)

| Org/User | Repo | Language | Last Push |
|----------|------|----------|-----------|
| plurigrid | gorj | Clojure | 2026-06-22 |
| kubeflow | dashboard | TypeScript | 2026-06-22 |
| kubeflow | pipelines | Python | 2026-06-22 |
| bmorphism | Gay.jl | Julia | 2026-06-22 |
| M1shaaa | M1shaaa | - | 2026-06-22 |
| plurigrid | place | TeX | 2026-06-20 |
| bmorphism | satreadout | HTML | 2026-06-20 |
| wasita | proj-template | - | 2026-06-19 |
| wasita | wasita.github.io | Svelte | 2026-06-15 |
| plurigrid | asi | HTML | 2026-06-10 |

### Notable High-Star Repos

| Repo | Stars | Forks | Language |
|------|-------|-------|----------|
| kubeflow/pipelines | 4157 | - | Python |
| kubeflow/katib | 1685 | - | Python |
| AustinCStone/TextGAN | 92 | 30 | Python |
| migalkin/NodePiece | 144 | 21 | Python |
| migalkin/StarE | 89 | 16 | Python |
| plurigrid/asi | 26 | - | HTML |
| migalkin/kgcourse2021 | 25 | 9 | HTML |
| migalkin/NBFNet_mlx | 10 | 1 | Python |

### GF(3) Color Chain

- id%3==0 -> trit=0 ERGODIC #d3869b (rose)
- id%3==1 -> trit=1 PLUS #b8bb26 (green)
- id%3==2 -> trit=-1 MINUS #cc241d (red)

Total world_increments: 384 | Total repo_snapshots: 1305 (including cross-org overlaps, 646 unique)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses (alice/bob/A-Z) queried against Aptos mainnet fullnode
(`/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`).

**Result: All 28 addresses returned null**

None of these addresses hold APT in a standard CoinStore resource on mainnet.
The accounts may not be registered/funded on mainnet yet.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793... | null |
| bob   | 0x0a3c... | null |
| A     | 0x8699... | null |
| B     | 0x3f89... | null |
| C     | 0x38b9... | null |
| D     | 0xf776... | null |
| E     | 0xdc1d... | null |
| F     | 0x18a1... | null |
| G     | 0x69a3... | null |
| H     | 0xce67... | null |
| I     | 0x070f... | null |
| J     | 0x4d96... | null |
| K     | 0xa732... | null |
| L     | 0x7c2e... | null |
| M     | 0x6fed... | null |
| N     | 0xe7dd... | null |
| O     | 0x7325... | null |
| P     | 0x6218... | null |
| Q     | 0xac40... | null |
| R     | 0x7ce6... | null |
| S     | 0xb875... | null |
| T     | 0x3578... | null |
| U     | 0x7586... | null |
| V     | 0xb59d... | null |
| W     | 0x5f32... | null |
| X     | 0xa95c... | null |
| Y     | 0xd8e3... | null |
| Z     | 0x7af0... | null |

### Multisig Contract Probes

All 5 multisig contracts returned `["2"]` via `0x1::multisig_account::num_signatures_required` — all healthy.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B  | 0x0da4... | 2 | healthy |
| A-G  | 0xf56c... | 2 | healthy |
| Y-Z  | 0xd3ff... | 2 | healthy |
| S-T  | 0x3b1c... | 2 | healthy |
| V-W  | 0x40fa... | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — protected by Vercel deployment authentication (visitor password required).
Paths `/api/markets` and `/api/v1/markets` both redirect to Vercel auth challenge.
No market data could be extracted. mnx_snapshots table is empty for this run.

---

## DuckDB Schema Summary

```
packages/world-increment/ducklake/world-increments.duckdb
  world_increments    384 rows  (GF3 trit-colored event log)
  repo_snapshots     1305 rows  (646 unique full_names across 11 sources)
  aptos_snapshots      28 rows  (all null - no mainnet APT balances found)
  multisig_probes       5 rows  (all healthy, sigs_required=2)
  mnx_snapshots         0 rows  (blocked by Vercel auth)
```

## Notable Findings

1. **plurigrid/gorj** (this repo) was pushed to on 2026-06-22 — active development today.
2. **bmorphism/Gay.jl** pushed 2026-06-22 — new Julia ML library.
3. **All 5 multisig contracts healthy** with 2-of-N threshold.
4. **All 28 Hamming swarm wallets show null APT balances** on mainnet — likely testnet/unfunded.
5. **MNX testnet is Vercel-gated** — requires bypass token for automated access.
