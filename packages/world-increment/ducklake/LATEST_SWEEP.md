# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-26 23:09 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | ~50 |
| kubeflow | org | 30 |
| TeglonLabs | org | 5 |
| bmorphism | user | 60+ |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |

### Notable Repos (by activity, 2026-06-26)

| Repo | Lang | Stars | Forks | Issues | Last Push |
|------|------|-------|-------|--------|-----------|
| kubeflow/spark-operator | Python | 3128 | 1491 | 101 | 2026-06-26T23:02 |
| kubeflow/pipelines | Python | 4156 | 2012 | 451 | 2026-06-26T22:32 |
| kubeflow/kubeflow | — | 15746 | 2680 | 0 | 2026-06-18 |
| plurigrid/gorj | Clojure | 0 | 0 | 845 | 2026-06-26T22:14 |
| plurigrid/asi | HTML | 26 | 8 | 4 | 2026-06-26T02:57 |
| bmorphism/Gay.jl | Julia | 2 | 1 | 187 | 2026-06-26T00:41 |
| migalkin/NodePiece | Python | 144 | 21 | 0 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 16 | 1 | 2026-04-16 |
| AustinCStone/TextGAN | Python | 92 | 30 | 5 | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 0 | 2026-03-16 |

### Hot Activity Signal

- **plurigrid/gorj** (this repo): 845 open issues, pushed today — active REPL orchestration work
- **kubeflow/spark-operator**: 3128★, very recent push — Kubernetes Spark community active
- **bmorphism/Gay.jl**: 187 open issues as of today — GF(3)/SPI color work ongoing
- **TeglonLabs/jank-crane**: new repo (2026-06-08), C++ crane-jank IR hub with GF3 convergence maps

### DuckDB Table: `world_increments`

- **58 new increments** added this sweep (cumulative total: 81)
- GF(3) coloring applied across all new rows

### DuckDB Table: `repo_snapshots`

- **58 new snapshots** added (historical total: 1002 rows since 2026-04-10)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-26)

**Chain height:** 858,543,727 blocks | **Epoch:** 16321

All 28 addresses queried (alice, bob, A–Z). Result: `resource_not_found` for the `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource on every address.

**Interpretation:** These addresses have no initialized APT CoinStore — wallets exist on-chain or are pre-activation addresses with 0.0 APT.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 (uninitialized) |
| bob | 0x0a3c...512d | 0.0 (uninitialized) |
| A | 0x8699...9d7a | 0.0 (uninitialized) |
| B | 0x3f89...b13 | 0.0 (uninitialized) |
| C | 0x38b9...535e | 0.0 (uninitialized) |
| D | 0xf776...fdd1 | 0.0 (uninitialized) |
| E | 0xdc1d...8d36 | 0.0 (uninitialized) |
| F | 0x18a1...cf71 | 0.0 (uninitialized) |
| G | 0x69a3...7f32 | 0.0 (uninitialized) |
| H | 0xce67...300f | 0.0 (uninitialized) |
| I | 0x070f...1fc9 | 0.0 (uninitialized) |
| J | 0x4d96...7f54 | 0.0 (uninitialized) |
| K | 0xa732...5dc4 | 0.0 (uninitialized) |
| L | 0x7c2e...eba9 | 0.0 (uninitialized) |
| M | 0x6fed...7f2e | 0.0 (uninitialized) |
| N | 0xe7dd...1b2c | 0.0 (uninitialized) |
| O | 0x7325...a89d | 0.0 (uninitialized) |
| P | 0x6218...c948 | 0.0 (uninitialized) |
| Q | 0xac40...c89a | 0.0 (uninitialized) |
| R | 0x7ce6...6e10 | 0.0 (uninitialized) |
| S | 0xb875...0386 | 0.0 (uninitialized) |
| T | 0x3578...4588 | 0.0 (uninitialized) |
| U | 0x7586...f956 | 0.0 (uninitialized) |
| V | 0xb59d...f2c3 | 0.0 (uninitialized) |
| W | 0x5f32...c7b0 | 0.0 (uninitialized) |
| X | 0xa95c...047d | 0.0 (uninitialized) |
| Y | 0xd8e3...44c4 | 0.0 (uninitialized) |
| Z | 0x7af0...97c | 0.0 (uninitialized) |

### Multisig Contract Probes

All 5 multisig contracts successfully queried via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

**All multisigs require 2-of-N signatures and are responsive.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection (requires visitor password). No market data accessible without credentials.

---

## Summary

| Category | Count | Status |
|----------|-------|--------|
| GitHub sources swept | 11 | complete |
| Repo snapshots added | 58 | In DuckDB |
| Aptos wallets probed | 28 | All 0.0 APT (uninitialized CoinStore) |
| Multisig contracts | 5 | All healthy (2-of-N sigs required) |
| MNX markets | — | Auth required (Vercel-protected) |
| DuckDB cumulative rows | 1002+ | Accumulating since 2026-04-10 |
