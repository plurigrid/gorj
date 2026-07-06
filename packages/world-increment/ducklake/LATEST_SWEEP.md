# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-06  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 27 |
| kubeflow | org | 14 |
| TeglonLabs | org | 5 |
| bmorphism | user | 22 |
| zubyul | user | 11 |
| migalkin | user (social) | 5 |
| DJedamski | user (social) | 3 |
| wasita | user (social) | 6 |
| kristinezheng | user (social) | 3 |
| M1shaaa | user (social) | 3 |
| AustinCStone | user (social) | 5 |
| **TOTAL** | | **104** |

### Top Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,766 | — | 2026-07-06 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-06 |
| kubeflow/spark-operator | 3,132 | Python | 2026-07-02 |
| kubeflow/trainer | 2,129 | Go | 2026-07-06 |
| kubeflow/katib | 1,690 | Python | 2026-07-01 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |

### Most Active (Open Issues)
| Repo | Open Issues |
|------|------------|
| plurigrid/gorj | 1,018 |
| kubeflow/pipelines | 419 |
| bmorphism/Gay.jl | 187 |
| kubeflow/trainer | 151 |
| kubeflow/sdk | 145 |

### GF(3) Distribution
- **PLUS** #b8bb26 (trit=1): 35 increments
- **MINUS** #cc241d (trit=-1): 35 increments
- **ERGODIC** #d3869b (trit=0): 34 increments

### Notable Activity
- `plurigrid/gorj` pushed 2026-07-06T19:13:17Z — 1018 open issues, Clojure, GF(3) REPL orchestration
- `bmorphism/Gay.jl` pushed 2026-07-06T00:34:54Z — 187 open issues, Julia, GF(3) color engine
- `kubeflow/pipelines` active ML pipeline infra, 4169 stars, 419 open issues
- `TeglonLabs/jank-crane` pushed 2026-06-08 — C++ GF3 convergence maps, loopify pass spec
- `zubyul/nash-tui` / `zubyul/nash-web` — NASH token Rust TUIs, pushed 2026-04-13
- `bmorphism/ocaml-mcp-sdk` 61 stars — OCaml MCP SDK using Jane Street oxcaml_effect
- `wasita/wasita.github.io` pushed 2026-07-05 — active personal site (Svelte)
- `kristinezheng/kristinezheng.github.io` pushed 2026-07-01 — active portfolio

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 Hamming-swarm wallets queried 2026-07-06. All return 0.00 APT.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.00 |
| bob | 0x0a3c00... | 0.00 |
| A | 0x8699ed... | 0.00 |
| B–Z (25) | various | 0.00 each |

Note: Zero balance indicates accounts registered on-chain but unfunded, consistent with pre-deployment state.

### Multisig Contract Probes
All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | HEALTHY |
| A-G | 0xf56c4a... | 2 | HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | HEALTHY |
| S-T | 0x3b1c3a... | 2 | HEALTHY |
| V-W | 0x40fad7... | 2 | HEALTHY |

All 5 multisig contracts respond correctly; all are 2-of-N and healthy.

### MNX Markets (testnet.mnx.fi)
**Unavailable** — testnet.mnx.fi is behind Vercel deployment protection. No market data extracted. `mnx_snapshots` table empty for this sweep.

---

## DuckDB Ducklake Schema

File: `packages/world-increment/ducklake/world-increments.duckdb`

```
world_increments    104 rows  (GitHub push events, GF(3) colored)
repo_snapshots      104 rows  (full repo metadata)
aptos_snapshots      28 rows  (Hamming swarm wallets alice,bob,A-Z)
multisig_probes       5 rows  (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots         0 rows  (unavailable - Vercel auth)
```
