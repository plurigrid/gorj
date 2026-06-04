# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-06-04
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 11 |
| AustinCStone | user | 40 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| **Total** | | **391** |

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 131 |
| 1 | #b8bb26 | PLUS | 130 |
| -1 | #cc241d | MINUS | 130 |

### Notable Active Repos (recent pushes)
| Repo | Stars | Lang | Pushed |
|------|-------|------|--------|
| plurigrid/gorj | 0 | Clojure | 2026-06-04 |
| plurigrid/place | 1 | TeX | 2026-06-04 |
| plurigrid/eirobri | 0 | Clojure | 2026-06-03 |
| kubeflow/hub | 175 | Go | 2026-06-04 |
| kubeflow/pipelines | 4152 | Python | 2026-06-04 |
| kubeflow/kubeflow | 15704 | — | 2026-05-24 |
| bmorphism/Gay.jl | 1 | Julia | 2026-06-04 |
| bmorphism/world | 0 | Python | 2026-06-02 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| zubyul/voice-observatory | 0 | Python | 2026-04-24 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| wasita/wasita.github.io | 1 | Svelte | 2026-06-01 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |

### API Access Notes
GitHub public REST API was rate-limited (unauthenticated, IP-based). All data collected via MCP GitHub search tools. Events endpoint unavailable without `gh` CLI; activity inferred from `pushed_at` timestamps.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-04)
*Via `0x1::coin::balance` view function (CoinStore deprecated, accounts on fungible_asset model).*

| World | APT Balance | Octas |
|-------|-------------|-------|
| bob | **12.657007** | 1,265,700,700 |
| F | 1.960516 | 196,051,600 |
| L | 1.927269 | 192,726,900 |
| J | 1.895093 | 189,509,300 |
| alice | 0.436434 | 43,643,352 |
| O | 0.210136 | 21,013,600 |
| K | 0.161961 | 16,196,100 |
| P | 0.140136 | 14,013,600 |
| M | 0.112285 | 11,228,500 |
| N | 0.106121 | 10,612,100 |
| Q | 0.103240 | 10,324,000 |
| S | 0.091788 | 9,178,800 |
| R | 0.090217 | 9,021,700 |
| T | 0.073713 | 7,371,300 |
| U | 0.055773 | 5,577,300 |
| A | 0.051767 | 5,176,700 |
| Z | 0.024268 | 2,426,800 |
| Y | 0.044449 | 4,444,900 |
| X | 0.042577 | 4,257,700 |
| V | 0.048833 | 4,883,299 |
| W | 0.040705 | 4,070,500 |
| B | 0.036256 | 3,625,600 |
| D | 0.011629 | 1,162,900 |
| C | 0.010185 | 1,018,500 |
| E | 0.009372 | 937,200 |
| H | 0.001681 | 168,100 |
| G | 0.000681 | 68,100 |
| I | 0.000681 | 68,100 |
| **Total** | **20.345 APT** | |

### Multisig Contract Probes (Aptos mainnet)
| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | YES |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | YES |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | YES |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | YES |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | YES |

All 5 multisigs are 2-of-2. All healthy.

### MNX Markets (testnet.mnx.fi)
The site is a Next.js SPA. The API backend (`api.testnet.mnx.fi`) exposes only WebSocket endpoints (`wss://`). All REST paths return `Cannot GET /...`. No market data extractable via HTTP. Logged as unavailable in `mnx_snapshots`.

---

## DuckDB Table Summary

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 391 | One per repo, GF(3)-colored |
| repo_snapshots | 391 | Full repo metadata |
| aptos_snapshots | 28 | Wallet APT balances |
| multisig_probes | 5 | 2-of-2 multisigs, all healthy |
| mnx_snapshots | 1 | Unavailable (WS-only) |

*Sweep agent: world-increment-sweep + hamming-swarm-snapshot — 2026-06-04*
