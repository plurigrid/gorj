# World Increment Sweep + Hamming Snapshot

**Run timestamp:** 2026-08-09 06:15:14 UTC
**Branch:** world-increment/sweep-2026-08-09-0615

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos | Top stars |
|--------|------|-------|-----------|
| plurigrid | org | 103 total, 10 snapshotted | asi (59 ⭐) |
| kubeflow | org | 49 total, 10 snapshotted | kubeflow/kubeflow (15,808 ⭐) |
| TeglonLabs | org | 5 total, 5 snapshotted | mathpix-gem (2 ⭐) |
| bmorphism | user | 106 total, 10 snapshotted | ocaml-mcp-sdk (61 ⭐) |
| zubyul | user | 49 total, 10 snapshotted | WGCNA (2 ⭐) |
| migalkin | user | 19 total, 5 snapshotted | NodePiece (144 ⭐) |
| DJedamski | user | 6 total, 4 snapshotted | Getting-and-Cleaning-Data (1 ⭐) |
| wasita | user | 14 total, 7 snapshotted | magic-garden (2 ⭐) |
| kristinezheng | user | 5 total, 3 snapshotted | Green-Machine (0 ⭐) |
| M1shaaa | user | 8 total, 3 snapshotted | lab-bookshelf- (0 ⭐) |
| AustinCStone | user | 41 total, 6 snapshotted | TextGAN (92 ⭐) |

### DuckDB GF(3) Color Chain (96 increments this run)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 31 |
| +1 | PLUS | #b8bb26 | 33 |
| -1 | MINUS | #cc241d | 32 |

### Notable activity

- **plurigrid/place** (TeX): 16 open issues, pushed 2026-08-08 — most recently active plurigrid repo
- **plurigrid/gorj** (Clojure): 1,736 open issues — the current repo
- **plurigrid/asi** (HTML): top-starred plurigrid repo (59 ⭐), pushed 2026-08-05
- **kubeflow/kubeflow**: 15,808 ⭐ — flagship ML toolkit, actively maintained 2026-08-09
- **kubeflow/docs-agent**: 164 open issues — high activity AI agent for Kubeflow docs
- **bmorphism/Gay.jl**: 188 open issues — wide-gamut GF(3) color library, core to this project
- **bmorphism/ocaml-mcp-sdk**: 61 ⭐ — OCaml SDK for MCP, most starred bmorphism repo
- **migalkin/NodePiece**: 144 ⭐ — top starred social graph node (knowledge graphs ICLR'22)
- **wasita/joint-planning-lit**: pushed 2026-08-04 — newest wasita activity
- **wasita/xoxowasita-analysis**: pushed 2026-08-06 — recent analysis repo

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) queried against Aptos mainnet.
**Result: All 28 wallets returned 0 APT** — the `0x1::coin::CoinStore<AptosCoin>` resource was not found on any address, indicating these accounts either do not exist on mainnet or have not been initialized with APT.

| Worlds | Total APT | Non-zero wallets |
|--------|-----------|------------------|
| 28 (alice, bob, A–Z) | 0.0 APT | 0 of 28 |

### Multisig Contract Probes (5 contracts)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | ✅ HEALTHY |

**All 5 multisig contracts are 2-of-N and responding normally.**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` returns a Next.js SPA (HTML). No public REST API endpoint was discoverable at `/api/markets` or `/api/v1/markets` — the frontend renders market data client-side. **MNX market data: UNAVAILABLE via API** (SPA only, no accessible endpoints found).

---

## DuckDB Schema Summary

Tables in `packages/world-increment/ducklake/world-increments.duckdb`:

- `world_increments`: GF(3) trit-colored increment log (96 new entries this run)
- `repo_snapshots`: GitHub repo metadata snapshots
- `aptos_snapshots`: Aptos mainnet wallet balances (28 entries this run)
- `multisig_probes`: Aptos multisig contract health checks (5 entries this run)
- `mnx_snapshots`: MNX market data (0 entries — API unavailable)

GF(3) color chain applied to increments: ERGODIC (#d3869b) / PLUS (#b8bb26) / MINUS (#cc241d) cycling by `id % 3`.
