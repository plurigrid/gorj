# World-Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-06-23 UTC  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| bmorphism | user | ~100 |
| TeglonLabs | org | 5 |
| zubyul | user | ~49 |
| migalkin | user (social graph) | 19 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 11 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 30 |
| **Total** | | **~333** |

### Top Active Repos (by stars)

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| migalkin/NodePiece | Python | 144 | 21 | 2022-02-02 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2016-10-04 |
| migalkin/StarE | Python | 89 | 16 | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-03-16 |
| plurigrid/asi | HTML | 26 | 8 | 2026-06-10 |
| migalkin/kgcourse2021 | HTML | 25 | 9 | 2025-08-04 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 2026-01-16 |
| bmorphism/say-mcp-server | JavaScript | 20 | 9 | 2025-01-07 |
| bmorphism/babashka-mcp-server | JavaScript | 19 | 6 | 2025-01-05 |
| bmorphism/manifold-mcp-server | JavaScript | 14 | 9 | 2025-01-11 |

### Notable Recent Activity
- **TeglonLabs/jank-crane** (C++, 2026-06-08): crane-jank converged-IR hub with GF3 convergence maps
- **plurigrid/asi** (HTML, 2026-06-10): most recently pushed plurigrid repo
- **wasita/proj-template** (2026-06-19): latest social graph activity
- **M1shaaa/M1shaaa** (2026-06-23): profile README pushed TODAY
- **kristinezheng/kristinezheng.github.io** (2026-06-07): personal site active

### Social Graph Summary
- **migalkin**: KG/GNN researcher — NodePiece (★144), StarE (★89), kgcourse2021 (★25)
- **wasita**: Svelte/TypeScript developer, personal site + academic CV active
- **AustinCStone**: ML/CV — TextGAN (★92), bmfork activity 2025-05
- **M1shaaa**: Yale/MIT neuroscience research (Lookit studies), README pushed today
- **DJedamski**: Data science (R/Python, Kaggle competitions)
- **kristinezheng**: Cognitive science research tools (MIT 9.85)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — alice, bob, A–Z (28 addresses)
**Queried:** 2026-06-23 UTC via Aptos mainnet fullnode

All 28 addresses returned **0.0 APT**. Accounts appear unfunded or have not registered
the `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource on mainnet.

### Multisig Contract Probes

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428...87003 | **2-of-2** | ✅ HEALTHY |
| A-G | 0xf56c4a1c...0096 | **2-of-2** | ✅ HEALTHY |
| Y-Z | 0xd3ffe181...b883 | **2-of-2** | ✅ HEALTHY |
| S-T | 0x3b1c3ae9...7883 | **2-of-2** | ✅ HEALTHY |
| V-W | 0x40fad7b4...eb6d | **2-of-2** | ✅ HEALTHY |

All 5 multisig contracts on Aptos mainnet are live and require 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — site returns Vercel authentication wall; no API data accessible without bypass token.

---

## DuckDB Schema Summary

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Description |
|-------|-------------|
| `world_increments` | GF(3)-tagged increment events (trit, color, name per id%3) |
| `repo_snapshots` | GitHub repo snapshots (org/user, stars, forks, language, pushed_at) |
| `aptos_snapshots` | Hamming swarm APT balances |
| `multisig_probes` | Multisig 2-of-2 health checks |
| `mnx_snapshots` | MNX market data (empty — auth-walled this run) |

**GF(3) color chain in use:**
- `id % 3 == 0` → trit=0, ERGODIC, `#d3869b` (rose)
- `id % 3 == 1` → trit=1, PLUS, `#b8bb26` (lime)
- `id % 3 == 2` → trit=-1, MINUS, `#cc241d` (red)
