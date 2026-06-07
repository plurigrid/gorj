# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-06-07 (UTC)
**Branch:** world-increment/sweep
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 35 |
| kubeflow | org | 20 |
| TeglonLabs | org | 4 |
| bmorphism | user | 57 |
| zubyul | user | 27 |
| migalkin | user | 7 |
| DJedamski | user | 6 |
| wasita | user | 6 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 10 |
| **TOTAL** | | **185** |

### GF(3) Color Chain (world_increments)
| Color | Hex | GF(3) Trit | Count |
|-------|-----|-----------|-------|
| ERGODIC | `#d3869b` | 0 | 4 |
| PLUS | `#b8bb26` | +1 | 5 |
| MINUS | `#cc241d` | -1 | 5 |

### Notable Recent Activity
- **plurigrid/gorj** (this repo): 414 open issues, pushed 2026-06-07
- **bmorphism/Gay.jl**: 189 open issues, active as of 2026-06-07
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK
- **kubeflow/kubeflow**: 15,706 stars — ML Toolkit for Kubernetes
- **kubeflow/pipelines**: 4,153 stars — ML Pipelines
- **kubeflow/spark-operator**: 3,125 stars — Kubernetes Spark Operator
- **migalkin/NodePiece**: 144 stars — Compositional KG representations (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — GAN for text generation
- **bmorphism/anti-bullshit-mcp-server**: 23 stars — Claim validation MCP
- **plurigrid/asi**: 25 stars — everything is topological chemputer!
- **zubyul/nash-tui**: Real-time NASH token TUI with GeckoTerminal OHLCV

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
All 28 wallets (alice, bob, A-Z) queried via fullnode.mainnet.aptoslabs.com.

| Result | Count |
|--------|-------|
| Wallets with 0.0 APT (unfunded/empty) | 28 |
| Wallets with APT balance | 0 |

All 28 addresses returned 0 APT on mainnet as of this sweep.

### Multisig Contract Probes (Aptos)
All 5 multisig contracts probed via 0x1::multisig_account::num_signatures_required.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | HEALTHY |
| A-G | 0xf56c4a1c... | 2 | HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | HEALTHY |
| V-W | 0x40fad7b4... | 2 | HEALTHY |

All multisig pairs require 2-of-N signatures and are structurally healthy.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — testnet.mnx.fi is behind Vercel deployment protection.
No market data could be fetched. 0 rows in mnx_snapshots.

---

## DuckDB Schema
- world_increments   -- 14 rows (GF3-colored sweep events)
- repo_snapshots     -- 185 rows (GitHub repo metadata)
- aptos_snapshots    -- 28 rows (Hamming swarm wallet balances)
- multisig_probes    -- 5 rows (multisig contract health)
- mnx_snapshots      -- 0 rows (MNX unavailable)

## Data Files
- world-increments.duckdb -- DuckDB ducklake
- populate.py             -- Main population script
- populate_bmorphism.py   -- bmorphism supplement
- LATEST_SWEEP.md         -- This file
