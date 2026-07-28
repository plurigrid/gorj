# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-07-28T00:16:17Z  
**Branch:** world-increment/sweep-2026-07-28-0016  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned

| Source | Type | Repos Snapshotted | Top Repo (Stars) |
|--------|------|-------------------|------------------|
| plurigrid | org | 100 (API cap) | plurigrid/asi (52★) |
| kubeflow | org | 49 | kubeflow/kubeflow (15,793★) |
| TeglonLabs | org | 5 | TeglonLabs/mathpix-gem (2★) |
| bmorphism | user | 50 | bmorphism/ocaml-mcp-sdk (61★) |
| zubyul | user | 49 | zubyul/jonikas_lab_data_analysis_misc (2★) |
| migalkin | user | 19 | migalkin/NodePiece (144★) |
| AustinCStone | user | 41 | AustinCStone/stonks (0★, active 2026-07-15) |
| DJedamski | user | 6 | DJedamski/Kaggle (1★) |
| wasita | user | 12 | wasita/magic-garden (2★) |
| kristinezheng | user | 5 | kristinezheng/kristinezheng.github.io |
| M1shaaa | user | 8 | M1shaaa/lab-bookshelf- |

### Notable Activity (Last 30 Days)

- **plurigrid/gorj** — pushed 2026-07-27, 1,450 open issues (this repo!)
- **plurigrid/eirobri** — pushed 2026-07-21, 31 open issues, EiRoBri replay world
- **plurigrid/asi** — pushed 2026-07-10, 52★, "everything is topological chemputer"
- **kubeflow/trainer** — pushed 2026-07-27, 2,155★, distributed AI training on K8s
- **kubeflow/pipelines** — pushed 2026-07-27, 4,171★, 471 open issues
- **kubeflow/spark-operator** — pushed 2026-07-25, 3,142★
- **bmorphism/Gay.jl** — pushed 2026-07-21, wide-gamut SPI color sampling, 188 open issues
- **bmorphism/anti-bullshit-mcp-server** — pushed 2026-07-12, 22★
- **wasita/wasita.github.io** — pushed 2026-07-21, 8 open issues
- **migalkin/kgcourse2021** — pushed 2026-07-10, Knowledge Graphs course (24★)
- **TeglonLabs/jank-crane** — pushed 2026-06-08, crane-jank converged-IR hub, GF3 convergence maps

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | id%3==0 |
| 1 | `#b8bb26` | PLUS | id%3==1 |
| -1 | `#cc241d` | MINUS | id%3==2 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Timestamp:** 2026-07-28T00:16:17Z

### Wallet Balances (A-Z + alice/bob)

All 28 wallets queried against Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice | 0.0 | No CoinStore / unfunded |
| bob | 0.0 | No CoinStore / unfunded |
| A–Z | 0.0 each | No CoinStore / unfunded |

**Interpretation:** All 28 addresses returned no `0x1::coin::CoinStore<AptosCoin>` resource, 
indicating the accounts either have not been initialized on mainnet (no on-chain transactions) 
or hold zero APT. This is consistent with a fresh Hamming swarm deployment pre-funding.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ Healthy |
| A-G | 0xf56c4a1c... | 2 | ✅ Healthy |
| Y-Z | 0xd3ffe181... | 2 | ✅ Healthy |
| S-T | 0x3b1c3ae9... | 2 | ✅ Healthy |
| V-W | 0x40fad7b4... | 2 | ✅ Healthy |

All 5 multisig contracts are live on Aptos mainnet and require **2-of-N signatures**. 
All are responsive and healthy.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable as JSON** — testnet.mnx.fi returns a Next.js SPA (client-side rendered). 
No REST API endpoint at `/api/markets` or similar paths responded with structured market data.
The site loads but requires JavaScript execution to render market state.

---

## DuckDB Schema Summary

```
world_increments  — GF(3)-colored increment log
repo_snapshots    — GitHub repo metadata snapshots  
aptos_snapshots   — Aptos wallet balance records (28 wallets)
multisig_probes   — Multisig contract health checks (5 pairs)
mnx_snapshots     — MNX market data (unavailable this run)
```

| Table | Rows |
|-------|------|
| world_increments | 108 |
| repo_snapshots | 1,029 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

*Sweep complete. Next run will delta against this snapshot.*
