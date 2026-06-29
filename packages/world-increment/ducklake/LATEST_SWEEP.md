# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-29  **Branch:** world-increment/sweep-2026-06-29-1009

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned

| Source | Type | Repos Logged |
|--------|------|-------------|
| plurigrid | Org | 102 |
| kubeflow | Org | 50 |
| TeglonLabs | Org | 7 |
| bmorphism | User | 103 |
| zubyul | User | 51 |
| migalkin | User (zubyul social) | 21 |
| DJedamski | User (zubyul social) | 8 |
| wasita | User (zubyul social) | 13 |
| kristinezheng | User (zubyul social) | 7 |
| M1shaaa | User (zubyul social) | 10 |
| AustinCStone | User (zubyul social) | 42 |

**Total world_increments:** 414
**Total repo_snapshots:** 1,335 (646 distinct full_names)

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | #d3869b | 137 |
| PLUS | 1 | #b8bb26 | 139 |
| MINUS | -1 | #cc241d | 138 |

### Top Repos by Stars

| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,750 |
| kubeflow/pipelines | 4,160 |
| kubeflow/spark-operator | 3,129 |
| kubeflow/trainer | 2,127 |

### Language Distribution (Top 8)

| Language | Count |
|----------|-------|
| Python | 234 |
| Rust | 57 |
| JavaScript | 53 |
| HTML | 53 |
| Go | 51 |
| TypeScript | 47 |
| Jupyter Notebook | 40 |

### Notable Recent Activity
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub with GF3 convergence maps
- **TeglonLabs/mathpix-gem** (Ruby, 2 stars): Mathematical OCR gem
- **M1shaaa/M1shaaa** pushed 2026-06-29 (today)
- **wasita/wasita.github.io** (Svelte, pushed 2026-06-25): personal site

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A-Z) probed via Aptos mainnet fullnode.
**Result:** All addresses returned resource_not_found for 0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>.
These addresses have no APT coin store registered on mainnet -- balances recorded as NULL.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | NULL (no coin store) |
| bob | 0x0a3c...512d | NULL (no coin store) |
| A-Z | various | NULL (no coin store) |

### Multisig Contract Probes

All 5 multisig contracts queried via 0x1::multisig_account::num_signatures_required.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

**All 5 multisig contracts healthy -- 2-of-2 signature threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

Status: UNAVAILABLE -- Vercel authentication required. Both /api/markets and the SPA root returned authentication gates. No market data accessible.

---

## DuckDB Schema

    packages/world-increment/ducklake/world-increments.duckdb
    world_increments   (414 rows)  -- GF3 color chain, source/event metadata
    repo_snapshots     (1335 rows) -- GitHub repo stats per increment
    aptos_snapshots    (28 rows)   -- Hamming swarm wallet probes
    multisig_probes    (5 rows)    -- Multisig health checks
    mnx_snapshots      (1 row)     -- MNX market status (auth-gated)

---

Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent.
