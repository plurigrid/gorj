# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-16  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos Snapshotted | Total Stars | Latest Push |
|--------|------|:-----------------:|:-----------:|:-----------:|
| kubeflow | org | 48 | 34,210 | 2026-06-16 |
| plurigrid | org | 100 | 77 | 2026-06-16 |
| TeglonLabs | org | 5 | 2 | 2026-06-08 |
| bmorphism | user | 100 | 247 | 2026-06-16 |
| zubyul | user | 49 | 14 | 2026-04-24 |
| migalkin | social | 5 | 276 | 2026-05-28 |
| DJedamski | social | 3 | 2 | 2023-04-21 |
| wasita | social | 4 | 3 | 2026-06-15 |
| kristinezheng | social | 3 | 0 | 2026-06-07 |
| M1shaaa | social | 3 | 0 | 2026-02-04 |
| AustinCStone | social | 4 | 104 | 2026-04-01 |
| **TOTAL** | | **324** | **34,935** | |

### GF(3) Color Chain

| Increment | Source | GF3 Trit | Color | Name |
|:---------:|--------|:--------:|-------|------|
| 1 | plurigrid | 1 | `#b8bb26` | PLUS |
| 2 | kubeflow | -1 | `#cc241d` | MINUS |
| 3 | TeglonLabs | 0 | `#d3869b` | ERGODIC |
| 4 | bmorphism | 1 | `#b8bb26` | PLUS |
| 5 | zubyul | -1 | `#cc241d` | MINUS |
| 6 | migalkin | 0 | `#d3869b` | ERGODIC |
| 7 | DJedamski | 1 | `#b8bb26` | PLUS |
| 8 | wasita | -1 | `#cc241d` | MINUS |
| 9 | kristinezheng | 0 | `#d3869b` | ERGODIC |
| 10 | M1shaaa | 1 | `#b8bb26` | PLUS |
| 11 | AustinCStone | -1 | `#cc241d` | MINUS |

### Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|:-----:|:---------:|
| kubeflow/kubeflow | — | 15,724 | 2026-06-11 |
| kubeflow/pipelines | Python | 4,154 | 2026-06-16 |
| kubeflow/spark-operator | Python | 3,127 | 2026-06-15 |
| kubeflow/trainer | Go | 2,115 | 2026-06-16 |
| kubeflow/katib | Python | 1,683 | 2026-06-15 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| plurigrid/asi | HTML | 26 | 2026-06-10 |
| migalkin/kgcourse2021 | HTML | 25 | 2026-02-16 |

### Notable Activity

- **plurigrid/place** (TeX) pushed 2026-06-15 — most recent plurigrid push
- **plurigrid/asi** (HTML, 26 stars) pushed 2026-06-10 — top plurigrid repo
- **bmorphism/Gay.jl** (Julia) pushed 2026-06-16 — today; also fork at zubyul
- **bmorphism/satreadout** (Lean) pushed 2026-06-15 — active formal methods work
- **TeglonLabs/jank-crane** (C++) pushed 2026-06-08 — newest TeglonLabs repo; GF3 convergence maps / crane-jank IR
- **wasita/wasita.github.io** (Svelte) pushed 2026-06-15 — active personal site
- **kubeflow/mcp-apache-spark-history-server** (Python, 177 stars) — MCP integration in kubeflow ecosystem
- **kristinezheng/kristinezheng.github.io** pushed 2026-06-07 — recent activity

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

**Result:** All 28 addresses (alice, bob, A–Z) returned `resource_not_found` on  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
These accounts have no APT coin store initialized on mainnet (no balance or account not yet created).

| World | Address (prefix) | Balance APT |
|-------|-----------------|:-----------:|
| alice | 0xc793acde... | N/A |
| bob | 0x0a3c00c5... | N/A |
| A–Z (26) | various | N/A |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **HEALTHY** — responding and requiring 2-of-2 signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|:-------------:|:------:|
| A-B | 0x0da4f428a0c007da... | 2 | HEALTHY |
| A-G | 0xf56c4a1c09062143... | 2 | HEALTHY |
| Y-Z | 0xd3ffe1812b2df406... | 2 | HEALTHY |
| S-T | 0x3b1c3ae905d44c3a... | 2 | HEALTHY |
| V-W | 0x40fad7b423a84365... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status:** HTTP 401 Unauthorized — API and main page both require authentication.  
No market data available for this sweep cycle.

---

## DuckDB Tables

| Table | Rows | Description |
|-------|:----:|-------------|
| `world_increments` | 11 | GF(3) color-chain increment records per source |
| `repo_snapshots` | 324 | GitHub repo metadata snapshots |
| `aptos_snapshots` | 28 | Aptos wallet balance probes (all N/A this cycle) |
| `multisig_probes` | 5 | Multisig contract health checks (all 2-of-2 healthy) |
| `mnx_snapshots` | 0 | MNX market data (unavailable — 401) |
