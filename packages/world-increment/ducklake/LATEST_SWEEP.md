# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-04-20  
**GF(3) Color Chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 101 (top 11 indexed) |
| zubyul | user | 47 (top 6 indexed) |
| migalkin | social-graph | 19 (top 4 indexed) |
| AustinCStone | social-graph | 40 (top 2 indexed) |
| wasita | social-graph | 10 (top 3 indexed) |
| kristinezheng | social-graph | 6 (top 1 indexed) |
| M1shaaa | social-graph | 8 (top 1 indexed) |
| DJedamski | social-graph | 6 (top 1 indexed) |

**Total world_increments:** 202  
**GF(3) distribution:** ERGODIC=66, PLUS=68, MINUS=68

### Notable Repos (by stars)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,587 | — | 2026-04-18 |
| kubeflow/pipelines | 4,125 | Python | 2026-04-18 |
| kubeflow/spark-operator | 3,116 | Python | 2026-04-17 |
| kubeflow/trainer | 2,085 | Go | 2026-04-17 |
| kubeflow/katib | 1,680 | Python | 2026-04-16 |
| migalkin/NodePiece | 143 | Python | 2026-03-02 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-28 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2026-03-19 |
| bmorphism/babashka-mcp-server | 18 | JavaScript | 2026-03-26 |
| bmorphism/manifold-mcp-server | 14 | JavaScript | 2026-04-15 |
| bmorphism/penrose-mcp | 10 | JavaScript | 2026-04-12 |

### Recently Active (plurigrid)

| Repo | Language | Last Pushed |
|------|----------|-------------|
| plurigrid/gorj | Clojure | 2026-04-20 |
| plurigrid/bci-blue-share | HTML | 2026-04-19 |
| plurigrid/nanoclj-zig | Zig | 2026-04-18 |
| plurigrid/reafference | HTML | 2026-04-16 |
| plurigrid/nash-portal | Rust | 2026-04-15 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-04-20)

All 28 wallets queried via Aptos fullnode mainnet. All returned **0 APT** (accounts not initialized / CoinStore resource absent).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793… | 0.00000000 |
| bob | 0x0a3c… | 0.00000000 |
| A–Z (26) | various | 0.00000000 each |

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required`. All **healthy**.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4… | 2 | healthy |
| A-G | 0xf56c… | 2 | healthy |
| Y-Z | 0xd3ff… | 2 | healthy |
| S-T | 0x3b1c… | 2 | healthy |
| V-W | 0x40fa… | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: 503 Unavailable** — testnet returns "DNS cache overflow". No market data extractable.

---

## DuckDB Schema

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 202 |
| repo_snapshots | 1,123 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

## GF(3) Trit Legend

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |
