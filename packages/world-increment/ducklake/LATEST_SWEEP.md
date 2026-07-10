# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-10  **GF(3) color chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found | Most Recent Push |
|--------|------|-------------|-----------------|
| plurigrid | org | 103 | 2026-07-07 (gorj, asi) |
| kubeflow | org | 49 | 2026-07-10 (kubeflow/kubeflow) |
| TeglonLabs | org | 5 | 2026-06-08 (jank-crane) |
| bmorphism | user | 105 | 2026-06-20 (Gay.jl, satreadout) |
| zubyul | user | 49 | 2026-04-24 (voice-observatory) |
| migalkin | user | 19 | 2026-05-28 (RWL) |
| DJedamski | user | 6 | 2023-04-21 (Kaggle) |
| wasita | user | 11 | 2026-07-06 (wasita.github.io) |
| kristinezheng | user | 5 | 2026-07-01 (kristinezheng.github.io) |
| M1shaaa | user | 8 | 2024-12-31 (lab-bookshelf) |
| AustinCStone | user | 40 | 2026-04-01 (StereoVisionMRF) |

**Total repos discovered:** ~400 across 11 sources  
**Notable activity:** plurigrid/gorj (this repo, 1096 open issues), kubeflow main 15.7k stars, bmorphism/Gay.jl 187 open issues

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,771 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,136 | Python |
| kubeflow/trainer | 2,134 | Go |
| kubeflow/katib | 1,689 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| plurigrid/asi | 30 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |

### Active Orgs / Users

- **plurigrid**: gorj (GF3 REPL), asi, nash-portal, nanoclj-zig, zig-syrup all recently active
- **kubeflow**: Active ML infra; new MCP servers, docs-agent, sdk launched 2025
- **bmorphism**: Heavy Gay.jl/GF3 work, OCaml/Zig/Move, 105 repos total
- **zubyul**: BCI/brain-world, Gay.jl, TileLang kernels, voice-observatory

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 hamming-swarm addresses (alice, bob, A–Z) probed via Aptos mainnet fullnode.

**Result: All balances 0.0 APT** — APT CoinStore resource absent or empty for every address.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A–Z (26 addresses) | various | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts live and responsive. **All require 2-of-N signatures.**

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | YES |
| A-G | 0xf56c4a... | 2 | YES |
| Y-Z | 0xd3ffe1... | 2 | YES |
| S-T | 0x3b1c3a... | 2 | YES |
| V-W | 0x40fad7... | 2 | YES |

**Multisig health: 5/5 contracts healthy, all 2-of-N.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — behind Vercel deployment protection (password-required). No market data could be extracted.

---

## DuckDB Ducklake State

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Row Count |
|-------|-----------|
| world_increments | 36 |
| repo_snapshots | 1,029 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

**GF(3) increment chain this sweep:** 13 new increments (11 GitHub sources + 1 Aptos + 1 multisig)
