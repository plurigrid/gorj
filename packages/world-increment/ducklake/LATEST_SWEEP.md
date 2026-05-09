# World-Increment Sweep + Hamming Swarm Snapshot

**Swept:** 2026-05-09  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 43 |
| kubeflow | org | 15 |
| TeglonLabs | org | 4 |
| bmorphism | user | 13 |
| zubyul | user | 11 |
| migalkin | social graph | 4 |
| DJedamski | social graph | 2 |
| wasita | social graph | 3 |
| kristinezheng | social graph | 1 |
| M1shaaa | social graph | 2 |
| AustinCStone | social graph | 3 |

**Total world_increments this run:** 122 rows  
**Total repo_snapshots (cumulative):** 1,043 rows

### Top Repos by Stars (this sweep)

| Repo | Lang | Stars | Forks | Open Issues | Last Push |
|------|------|-------|-------|-------------|-----------|
| kubeflow/kubeflow | — | 15,628 | 2,647 | 2 | 2026-05-07 |
| kubeflow/pipelines | Python | 4,137 | 1,989 | 494 | 2026-05-08 |
| kubeflow/spark-operator | Python | 3,125 | 1,480 | 89 | 2026-05-08 |
| kubeflow/trainer | Go | 2,096 | 948 | 112 | 2026-05-09 |
| kubeflow/katib | Python | 1,683 | 522 | 124 | 2026-05-09 |
| kubeflow/examples | Jsonnet | 1,462 | 756 | 111 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,015 | 1,063 | 27 | 2026-05-08 |
| kubeflow/arena | Go | 810 | 190 | 63 | 2026-05-07 |
| kubeflow/kale | Python | 685 | 156 | 59 | 2026-05-09 |
| kubeflow/mpi-operator | Go | 524 | 235 | 100 | 2026-05-05 |
| migalkin/NodePiece | Python | 144 | 21 | 0 | 2026-05-07 |
| kubeflow/sdk | Python | 114 | 174 | 129 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 5 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 16 | 1 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 0 | 2026-03-16 |

### Notable Activity
- **gorj** (this repo): 129 open issues, pushed 2026-05-09 — most active in plurigrid
- **bmorphism/Gay.jl**: 187 issues, pushed 2026-05-09 — very active
- **kubeflow/trainer**: new MCP-Apache-Spark-History-Server (167⭐) — active ML infra
- **zubyul/nash-tui + nash-web**: NASH token TUI in Rust, both pushed 2026-04-13
- **bmorphism/zig-syrup**: matches plurigrid/zig-syrup — cross-account active dev

### GF(3) Distribution (this sweep)
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 40 |
| 1 | PLUS | #b8bb26 | 41 |
| -1 | MINUS | #cc241d | 41 |

---

## JOB 2 — Hamming Swarm Snapshot (Aptos Mainnet)

**Method:** `0x1::coin::balance` view function (FA-compatible, bypasses legacy CoinStore 404s)  
**Ledger version at sweep:** ~5,200,904,988

### Wallet Balances (APT)

| World | Balance (APT) | Address |
|-------|---------------|---------|
| bob | **12.657007** | 0x0a3c...512d |
| F | 1.960516 | 0x18a1...cf71 |
| L | 1.927269 | 0x7c2e...eba9 |
| J | 1.895093 | 0x4d96...7f54 |
| alice | 0.436434 | 0xc793...cc7b |
| O | 0.210136 | 0x7325...a89d |
| K | 0.161961 | 0xa732...dc4 |
| P | 0.140136 | 0x6218...c948 |
| M | 0.112285 | 0x6fed...f2e9 |
| N | 0.106121 | 0xe7dd...1b2c |
| Q | 0.103240 | 0xac40...c89a9 |
| S | 0.091788 | 0xb875...0386 |
| R | 0.090217 | 0x7ce6...6e10 |
| T | 0.073713 | 0x3578...4588 |
| U | 0.055773 | 0x7586...9956 |
| A | 0.051767 | 0x8699...9d7a |
| V | 0.048833 | 0xb59d...af2c3 |
| Y | 0.044449 | 0xd8e3...44c4 |
| X | 0.042577 | 0xa95c...047d |
| W | 0.040705 | 0x5f32...c7b0 |
| B | 0.036256 | 0x3f89...cb13 |
| Z | 0.024268 | 0x7af0...197c |
| D | 0.011629 | 0xf776...cfdd1 |
| C | 0.010185 | 0x38b9...535e |
| E | 0.009372 | 0xdc1d...8d36 |
| H | 0.001681 | 0xce67...300f |
| G | 0.000681 | 0x69a3...cf32 |
| I | 0.000681 | 0x070f...1fc9 |

**Total APT across swarm:** ~20.69 APT  
**Top holder:** bob (12.66 APT = 61% of swarm)  
**Dust accounts (< 0.01 APT):** E, H, G, I

### Multisig Contract Probes (2-of-N)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts healthy — each requires 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Status: **SPA only** — Next.js app served as HTML shell, no public JSON API endpoints accessible via curl. Market data loads client-side; `mnx_snapshots` table remains empty this sweep.

---

## DuckDB Schema Summary

| Table | Rows |
|-------|------|
| world_increments | 122 (this sweep) |
| repo_snapshots | 1,043 (cumulative) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, unavailable) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
