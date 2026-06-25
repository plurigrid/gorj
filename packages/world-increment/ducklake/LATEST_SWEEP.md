# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-25  
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 10 (of 50+) |
| kubeflow | org | 10 (of 48) |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 |
| zubyul | user | 7 |
| migalkin | social-graph | 5 |
| DJedamski | social-graph | 3 |
| wasita | social-graph | 4 |
| kristinezheng | social-graph | 3 |
| M1shaaa | social-graph | 3 |
| AustinCStone | social-graph | 4 |

**Total repo snapshots inserted this sweep:** 64  
**Total repo_snapshots table rows (all time):** 1008  
**Total world_increments rows (all time):** 87

### Notable Active Repos (pushed within 30 days)

| Repo | Stars | Pushed | Notes |
|------|-------|--------|-------|
| plurigrid/gorj | 0 | 2026-06-25 | 816 open issues — very active |
| plurigrid/place | 1 | 2026-06-24 | TeX/forester |
| kubeflow/spark-operator | 3128 | 2026-06-25 | 1492 forks |
| kubeflow/kale | 694 | 2026-06-25 | Data science superfood |
| kubeflow/pipelines | 4156 | 2026-06-24 | ML pipelines flagship |
| kubeflow/trainer | 2121 | 2026-06-24 | Distributed training on K8s |
| wasita/wasita.github.io | 1 | 2026-06-25 | Svelte personal site |
| bmorphism/Gay.jl | 2 | 2026-06-25 | 187 open issues, wide-gamut coloring |
| migalkin/kgcourse2021 | 25 | 2026-06-08 | Knowledge graphs course |
| TeglonLabs/jank-crane | 0 | 2026-06-08 | GF3 convergence maps, C++ |

### GF(3) World Increment Distribution (this sweep)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 28 |
| 1 | #b8bb26 | PLUS | 30 |
| -1 | #cc241d | MINUS | 29 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-25)

*Balances via `0x1::coin::balance` view function. Raw values ÷ 10^8 = APT.*

| World | APT Balance | Address (prefix) |
|-------|------------|-----------------|
| bob | 12.657007 | 0x0a3c00c58fdf... |
| F | 1.960516 | 0x18a14b5b4bec... |
| L | 1.927269 | 0x7c2eaeafad97... |
| J | 1.895093 | 0x4d964db8f538... |
| alice | 0.436434 | 0xc793acdec12b... |
| O | 0.210136 | 0x73252b601... |
| K | 0.161961 | 0xa732040a6b0d... |
| P | 0.140136 | 0x6218792de4a9... |
| M | 0.112285 | 0x6fed37a7553e... |
| N | 0.106121 | 0xe7dde6da0a65... |
| S | 0.091788 | 0xb8753014e488... |
| R | 0.090217 | 0x7ce605cc8fda... |
| T | 0.073713 | 0x35781dc0e42f... |
| U | 0.055773 | 0x75860da47565... |
| A | 0.051767 | 0x8699edc0960d... |
| V | 0.048833 | 0xb59dd8170321... |
| X | 0.042577 | 0xa95cbbd11654... |
| Y | 0.044449 | 0xd8e32848f1df... |
| W | 0.040705 | 0x5f32aef70f5b... |
| B | 0.036256 | 0x3f892ebe6e45... |
| Z | 0.024268 | 0x7af0ef6e1bd7... |
| D | 0.011629 | 0xf77656248f64... |
| C | 0.010185 | 0x38b99e63ada9... |
| E | 0.009372 | 0xdc1d9d533bac... |
| G | 0.000681 | 0x69a394c0b0ac... |
| H | 0.001681 | 0xce67c327a784... |
| I | 0.000681 | 0x070fe5d74e4e... |

**Total APT in swarm:** ~20.03 APT  
**Richest:** bob (12.66 APT), F (1.96 APT), L (1.93 APT), J (1.90 APT)

### Multisig Contract Probes

All 5 multisig pairs are **healthy** (2-of-N threshold confirmed):

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | healthy |
| A-G | 0xf56c4a1c... | 2 | healthy |
| Y-Z | 0xd3ffe181... | 2 | healthy |
| S-T | 0x3b1c3ae9... | 2 | healthy |
| V-W | 0x40fad7b4... | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection requires authentication. The SPA returns an auth wall; no market data accessible without a bypass token.

---

## DuckDB Schema Summary

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 87 | GF(3)-colored event log |
| repo_snapshots | 1008 | GitHub repo metadata (all sweeps) |
| aptos_snapshots | 28 | APT wallet balances this sweep |
| multisig_probes | 5 | Multisig contract health |
| mnx_snapshots | 0 | MNX markets (unavailable) |

DB path: `packages/world-increment/ducklake/world-increments.duckdb`
