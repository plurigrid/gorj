# World Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-08-01  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos found |
|--------|------|-------------|
| plurigrid | org | 50+ (sampled top 38) |
| kubeflow | org | 49 (sampled 7) |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 (sampled 10) |
| zubyul | user | 49 (sampled 8) |
| migalkin | social | 19 (sampled 3) |
| DJedamski | social | 6 (sampled 1) |
| wasita | social | 12 (sampled 2) |
| kristinezheng | social | 5 (sampled 1) |
| M1shaaa | social | 8 (sampled 1) |
| AustinCStone | social | 41 (sampled 1) |

### Most Recently Active Repos
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/hub | 180 | Go | 2026-07-31 |
| kubeflow/spark-operator | 3141 | Python | 2026-07-31 |
| kubeflow/pipelines | 4172 | Python | 2026-07-31 |
| kubeflow/trainer | 2165 | Go | 2026-07-31 |
| plurigrid/asi | 56 | HTML | 2026-07-30 |
| plurigrid/gorj | 1 | Clojure | 2026-07-29 |
| plurigrid/zig-syrup | 2 | Zig | 2026-07-28 |
| bmorphism/Gay.jl | 2 | Julia | 2026-07-21 |
| wasita/wasita.github.io | 1 | Svelte | 2026-07-21 |
| AustinCStone/byteruckus | 0 | HTML | 2026-07-15 |
| bmorphism/gay-chat | 0 | Scheme | 2026-07-14 |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript | 2026-07-12 |
| migalkin/kgcourse2021 | 24 | HTML | 2026-07-10 |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 |

### World Increments Written
- 13 increments recorded with GF(3) color chain
- 37 repo snapshots stored in this run

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice + bob + A-Z = 28 wallets)
**All 28 wallets returned `resource_not_found` for `0x1::coin::CoinStore<aptos_coin::AptosCoin>` at ledger ~6,554,698,614.**

None of the Hamming swarm addresses have initialized an APT CoinStore on mainnet. All balances recorded as 0.0 APT.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A-Z (26) | 0x8699ed...–0x7af0ef... | 0.0 each |

### Multisig Contract Probes (5/5 healthy)
All 5 multisig contracts responded with `sigs_required = 2`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | HEALTHY |
| A-G | 0xf56c4a... | 2 | HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | HEALTHY |
| S-T | 0x3b1c3a... | 2 | HEALTHY |
| V-W | 0x40fad7... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Status: SPA — no JSON API accessible.**  
Next.js SPA. `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/v1/markets` all 404. `/markets` returns the SPA HTML shell only. `mnx_snapshots` table left empty this run.

---

## DuckDB State
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Cumulative Rows |
|-------|----------------|
| world_increments | 36 |
| repo_snapshots | 982 |
| aptos_snapshots | 28 (this run) |
| multisig_probes | 5 (this run) |
| mnx_snapshots | 0 (unavailable) |
