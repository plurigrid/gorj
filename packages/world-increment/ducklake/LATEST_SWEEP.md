# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-19

## Sweep Metadata
- **Date:** 2026-06-19
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 150 |
| Total Repo Snapshots | 150 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 50 |
| +1 | PLUS | #b8bb26 | 50 |
| -1 | MINUS | #cc241d | 50 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Repo Counts by Source

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 65 |
| kubeflow | org | 20 |
| TeglonLabs | org | 5 |
| bmorphism | user | 21 |
| zubyul | user | 11 |
| migalkin | user (social) | 5 |
| wasita | user (social) | 6 |
| kristinezheng | user (social) | 3 |
| AustinCStone | user (social) | 5 |
| M1shaaa | user (social) | 3 |
| DJedamski | user (social) | 4 |
| **Total** | | **148** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,736 | – | 2026-06-18 |
| kubeflow/pipelines | 4,154 | Python | 2026-06-19 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-18 |
| kubeflow/trainer | 2,117 | Go | 2026-06-19 |
| kubeflow/katib | 1,683 | Python | 2026-06-15 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,025 | YAML | 2026-06-18 |
| kubeflow/arena | 813 | Go | 2026-05-07 |
| kubeflow/kale | 694 | Python | 2026-06-17 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |

### Notable Activity (2026)

**plurigrid:**
- **gorj** — 677 open issues (most active), forj + Rama topology nREPL + GF(3) gay trit coloring
- **eirobri** — 29 open issues, EiRoBri replay world (Clojure)
- **nanoclj-zig** — 20 open issues, NaN-boxed Clojure in Zig 0.15
- **nash-portal** — Rust, NASH token TUI (ratzilla WASM + GeckoTerminal OHLCV)
- **asi** — 26★, "everything is topological chemputer!"

**bmorphism:**
- **satreadout** — Lean 4.28, machine-checked saturating perceptual readout (2026-06-15)
- **Gay.jl** — Julia, 187 open issues, wide-gamut color sampling (2026-06-15)
- **ocaml-mcp-sdk** — 61★, Jane Street oxcaml_effect MCP SDK
- **flox-mcp-bb** — Clojure, open-source Flox MCP server (2026-06-05)

**zubyul:**
- **voice-observatory** — Passive macOS TUI observing voice-download pathways (2026-04-24)
- **tilelang-kernels** — TileLang GPU kernels for GF(3) trit classification, Sinkhorn OT

**TeglonLabs:**
- **jank-crane** — C++, crane-jank converged-IR hub with GF3 convergence maps (2026-06-08)

**migalkin (knowledge graphs):**
- **NodePiece** — 144★, compositional KG embeddings (ICLR'22)
- **StarE** — 89★, hyper-relational KG (EMNLP 2020)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm wallets (alice, bob, A–Z) returned **0 APT** on mainnet.
The `CoinStore<AptosCoin>` resource was not found at any queried address —
accounts exist but have not been funded with APT on Aptos mainnet.

| Range | Balance (APT) | Notes |
|-------|:-------------:|-------|
| alice, bob | 0.00 each | Primary pair |
| A–Z (26 wallets) | 0.00 each | Full alphabet swarm |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — each requires 2-of-N signatures.

| Pair | Contract Address (truncated) | Sigs Required | Healthy |
|------|-----------------------------:|:-------------:|:-------:|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is protected by Vercel authentication
(password-required). No market data could be extracted. `mnx_snapshots` table is empty.

---

## DuckDB Table Summary

```
world_increments : 150 rows  — GF(3)-tagged repo sweep events
repo_snapshots   : 150 rows  — GitHub repo metadata snapshots
aptos_snapshots  :  28 rows  — Hamming swarm wallet balances (all 0 APT)
multisig_probes  :   5 rows  — Aptos multisig contract health (all healthy, 2-of-N)
mnx_snapshots    :   0 rows  — MNX markets (auth-protected, unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
