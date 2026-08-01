# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-08-01T15:15:00Z  
**DuckDB:** `world-increments.duckdb` (v1.5.5 Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain

| id%3 | Trit | Color | Name | Source |
|------|------|-------|------|--------|
| 0 | 0 | `#d3869b` | ERGODIC | plurigrid, bmorphism, DJedamski, M1shaaa |
| 1 | +1 | `#b8bb26` | PLUS | kubeflow, zubyul, wasita, AustinCStone |
| 2 | -1 | `#cc241d` | MINUS | TeglonLabs, migalkin, kristinezheng |

### Org Snapshots

| Org | Repos Sampled | Notable | Max Stars | Last Push |
|-----|--------------|---------|-----------|-----------|
| plurigrid | 18 | gorj (forj+GF3), zig-syrup, asi, nanoclj-zig | 58 (asi) | 2026-07-28 |
| kubeflow | 29 | kubeflow/kubeflow, pipelines, spark-operator, mcp-server | 15,803 (kubeflow) | 2026-08-01 |
| TeglonLabs | 5 | jank-crane, mathpix-gem, coin-flip-mcp, topoi | 2 (mathpix-gem) | 2026-06-08 |

### User Snapshots

| User | Repos Sampled | Notable | Max Stars | Last Push |
|------|--------------|---------|-----------|-----------|
| bmorphism | 29 | Gay.jl, ocaml-mcp-sdk, anti-bullshit-mcp, nanoclj-zig | 61 (ocaml-mcp-sdk) | 2026-07-21 |
| zubyul | 22 | voice-observatory, ghostel-emacs-worlds, tilelang-kernels | 1 (gay-world) | 2026-04-24 |
| migalkin | 10 | NodePiece (144★), StarE (89★), kgcourse2021, NBFNet_mlx | 144 (NodePiece) | 2026-07-10 |
| DJedamski | 6 | kaggle_ncaa18, Kaggle, Project_Euler | 1 | 2018-02-26 |
| wasita | 10 | wasita.github.io, wm-cv, magic-garden, send2kobo | 2 | 2026-07-21 |
| kristinezheng | 3 | kristinezheng.github.io, lookit-jenga, auditory-illusion | 0 | 2026-07-01 |
| M1shaaa | 6 | M1shaaa (profile), lab-bookshelf-, MNIST-Classifier | 0 | 2026-02-04 |
| AustinCStone | 5 | byteruckus, EpsteinSearch, bmfork | 0 | 2026-07-15 |

### Notable Activity

- **plurigrid/gorj**: Pushed 2026-07-28; 1562 open issues — highly active coordination repo
- **kubeflow/mcp-apache-spark-history-server**: 185★, pushed 2026-08-01 — hot new MCP project in kubeflow org
- **bmorphism/Gay.jl**: 188 open issues; most active personal repo in GF(3) / color-SPI space
- **zubyul/tilelang-kernels**: TileLang GPU kernels for SplitMix64 / GF(3) on Blackwell GB10
- **migalkin/NodePiece**: 144★ ICLR'22 KG representation paper — top-starred in social graph

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 worlds)

**Snapshot:** 2026-08-01 mainnet  
**All 28 addresses (alice, bob, A–Z): 0.00000000 APT**

All Hamming-swarm addresses appear unfunded on Aptos mainnet at time of sweep. The `CoinStore` resource was not found (accounts may exist but hold no APT or are not registered). This may indicate:
- Addresses not yet funded on mainnet (testnet-only activity)
- Balances held in non-APT Move objects or other coin types

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793acdec12b… | 0.0 |
| bob   | 0x0a3c00c58fdf… | 0.0 |
| A–Z   | (see DB for all 26) | 0.0 each |

### Multisig Contract Health (5 pairs)

**All 5 multisigs responsive — 2-of-2 signatures required.**

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428… | 2 | ✅ healthy |
| A-G | 0xf56c4a1c… | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181… | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9… | 2 | ✅ healthy |
| V-W | 0x40fad7b4… | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — REST API unavailable.**  
`testnet.mnx.fi` returns HTTP 200 but serves a Next.js HTML shell for all paths including `/api/markets`. No structured market data extractable via direct HTTP. `mnx_snapshots` table is empty this sweep.

---

## DuckDB Table Counts

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1005 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

*Sweep agent: world-increment-sweep + hamming-swarm-snapshot*  
*GF(3) color chain: ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d*
