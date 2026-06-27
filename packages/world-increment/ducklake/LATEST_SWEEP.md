# World-Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-06-27

---

## JOB 1: GitHub Social Graph Sweep

### Sources Captured

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | zubyul-social | 19 |
| DJedamski | zubyul-social | 6 |
| wasita | zubyul-social | 11 |
| kristinezheng | zubyul-social | 5 |
| M1shaaa | zubyul-social | 8 |
| AustinCStone | zubyul-social | 40 |
| **Total** | | **391** |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC  | #d3869b | 0 | 130 |
| PLUS     | #b8bb26 | 1 | 131 |
| MINUS    | #cc241d | -1 | 130 |

### Recently Active Repos (pushed >= 2026-05-27)

| Repo | Pushed | Language | Stars |
|------|--------|----------|-------|
| plurigrid/place | 2026-06-27 | TeX | 1 |
| plurigrid/gorj | 2026-06-27 | Clojure | 0 |
| kubeflow/pipelines | 2026-06-27 | Python | 4158 |
| kubeflow/hub | 2026-06-27 | Go | 174 |
| bmorphism/Gay.jl | 2026-06-27 | Julia | 2 |
| plurigrid/asi | 2026-06-26 | HTML | 26 |
| kubeflow/spark-operator | 2026-06-26 | Python | 3129 |
| kubeflow/trainer | 2026-06-26 | Go | 2125 |
| wasita/wasita.github.io | 2026-06-25 | Svelte | 1 |
| TeglonLabs/jank-crane | 2026-06-08 | C++ | 0 |

### Top Stars by Source

| Source | Repo | Stars |
|--------|------|-------|
| kubeflow | kubeflow/kubeflow | 15749 |
| kubeflow | kubeflow/pipelines | 4158 |
| migalkin | migalkin/NodePiece | 144 |
| AustinCStone | AustinCStone/TextGAN | 92 |
| bmorphism | bmorphism/ocaml-mcp-sdk | 61 |
| plurigrid | plurigrid/asi | 26 |
| bmorphism | bmorphism/anti-bullshit-mcp-server | 23 |
| TeglonLabs | TeglonLabs/mathpix-gem | 2 |

### Notable Activity
- **kubeflow**: pipelines, spark-operator, trainer, hub all pushed 2026-06-26/27 -- active ML platform
- **plurigrid/gorj**: pushed 2026-06-27 -- this repo
- **TeglonLabs/jank-crane**: new C++ repo 2026-06-08 -- crane-jank converged-IR hub with GF3 maps
- **bmorphism/ocaml-mcp-sdk**: highest-starred bmorphism repo (61 stars)
- **wasita/wasita.github.io**: updated 2026-06-25 (Svelte personal site)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses probed)

All 28 addresses returned resource_not_found for 0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>
at ledger version 5968769182. Accounts are unfunded or never initialized APT CoinStore.

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice-Z (all 28) | 0.0 | resource_not_found |

### Multisig Contract Probes

All 5 contracts responded, all require 2-of-N signatures -- healthy.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...4987003 | 2 | YES |
| A-G | 0xf56c4a1c...bc0096 | 2 | YES |
| Y-Z | 0xd3ffe181...75b883 | 2 | YES |
| S-T | 0x3b1c3ae9...d7883 | 2 | YES |
| V-W | 0x40fad7b4...80eb6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)

Status: UNAVAILABLE -- site requires Vercel authentication. No market data retrieved.

---

## DuckDB Schema Summary

Database: packages/world-increment/ducklake/world-increments.duckdb

| Table | Rows |
|-------|------|
| world_increments | 391 |
| repo_snapshots | 391 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
