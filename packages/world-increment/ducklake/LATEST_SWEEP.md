# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-07-23  
**GF(3) chain position:** increment #13 — trit=1, color=#b8bb26 (PLUS)

---

## JOB 1: GitHub Social Graph Sweep

### Orgs

| Org | Repos snapshotted | Most recently pushed |
|-----|-------------------|----------------------|
| plurigrid | 100 (of 103) | gorj (Clojure, 2026-07-23) |
| kubeflow | 49 | trainer, notebooks, mpi-operator (all 2026-07-23) |
| TeglonLabs | 5 | jank-crane (C++, 2026-06-08) |

#### plurigrid top activity (last 30 days)
- `plurigrid/gorj` — Clojure, pushed 2026-07-23 (★1)
- `plurigrid/eirobri` — Clojure, pushed 2026-07-21
- `plurigrid/place` — TeX/forester, pushed 2026-07-14 (★1)
- `plurigrid/asi` — HTML, pushed 2026-07-10 (★31)
- `plurigrid/shrimp` — pushed 2026-07-03

#### kubeflow top activity
- `kubeflow/trainer` — Go, ★2153, pushed 2026-07-23
- `kubeflow/notebooks` — pushed 2026-07-23
- `kubeflow/mpi-operator` — Go, ★530, pushed 2026-07-23
- `kubeflow/mcp-server` — Python, ★29, pushed 2026-07-23

#### TeglonLabs
- `jank-crane` — C++, "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"
- `mathpix-gem` — Ruby, ★2, 11 open issues
- `coin-flip-mcp` — JavaScript, 2 forks

### Social Graph Users

| User | Public repos | Latest |
|------|-------------|--------|
| bmorphism | 106 | Gay.jl (Julia, 2026-07-21), gay-chat (Scheme, 2026-07-14) |
| zubyul | 49 | voice-observatory (Python, 2026-04-24), wasita.github.io (Svelte, 2026-07-21) |
| migalkin | 19 | kgcourse2021 (HTML, 2026-07-10), NodePiece ★144 |
| DJedamski | 6 | kaggle_ncaa18 (2018, inactive) |
| wasita | 12 | wasita.github.io (Svelte, 2026-07-21), pnas-typst-template (2026-07-16) |
| kristinezheng | 5 | kristinezheng.github.io (HTML, 2026-07-01) |
| M1shaaa | 8 | M1shaaa profile (2026-02-04), lab-bookshelf (TypeScript) |
| AustinCStone | 41 | byteruckus (HTML, 2026-07-15) |

### DuckDB ducklake
- **DB:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Tables:** `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
- **Repo snapshots inserted:** 154 (plurigrid 100 + kubeflow 49 + TeglonLabs 5)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (via `coin::balance` view)

| World | APT Balance | Note |
|-------|------------|------|
| alice | 0.436434 | seq_num=72 |
| bob   | **12.657007** | seq_num=67 (highest) |
| A | 0.051767 | |
| B | 0.036256 | |
| C | 0.010185 | |
| D | 0.011629 | |
| E | 0.009372 | |
| F | **1.960516** | |
| G | 0.000681 | |
| H | 0.001681 | |
| I | 0.000681 | |
| J | **1.895093** | |
| K | 0.161961 | |
| L | **1.927269** | |
| M | 0.112285 | |
| N | 0.106121 | seq_num=48 |
| O | 0.210136 | |
| P | 0.140136 | |
| Q | 0.103240 | |
| R | 0.090217 | |
| S | 0.091788 | |
| T | 0.073713 | |
| U | 0.055773 | |
| V | 0.048833 | |
| W | 0.040705 | |
| X | 0.042577 | |
| Y | 0.044449 | |
| Z | 0.024268 | |

**Total swarm APT:** ~20.35 APT  
**Note:** CoinStore legacy resource returned 404 for all; balances confirmed via `0x1::coin::balance` view function.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | **2** | ✓ |
| A-G | 0xf56c4a1c... | **2** | ✓ |
| Y-Z | 0xd3ffe181... | **2** | ✓ |
| S-T | 0x3b1c3ae9... | **2** | ✓ |
| V-W | 0x40fad7b4... | **2** | ✓ |

All multisigs require 2-of-N signatures and responded successfully.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi/markets` is a Next.js SPA — no REST API endpoint yielded JSON. Recorded as unavailable in `mnx_snapshots`. Manual browser visit required to read market data.

---

## GF(3) Color Chain Summary

| Increment | Trit | Color | Name |
|-----------|------|-------|------|
| 13 (this run) | 1 | #b8bb26 | PLUS |

Previous colors in chain: ERGODIC (#d3869b) → PLUS (#b8bb26) → MINUS (#cc241d) → repeat.
