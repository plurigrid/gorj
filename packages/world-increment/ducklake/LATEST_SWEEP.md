# World-Increment Sweep — 2026-07-20

## Sweep Metadata
- **Date:** 2026-07-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Prior sweep:** 2026-04-12 (12 increments, 471 repos)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 34 |
| New Increments This Sweep | 11 |
| Total Repo Snapshots (cumulative) | 1278 |
| New Repos Snapshotted | 807 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (testnet.mnx.fi offline) |

---

## GF(3) Color Chain — New Increments (IDs 13–23)

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 13 | plurigrid | org | 100 | 0 | `#d3869b` | **ERGODIC** |
| 14 | kubeflow | org | 49 | +1 | `#b8bb26` | **PLUS** |
| 15 | TeglonLabs | org | 5 | -1 | `#cc241d` | **MINUS** |
| 16 | bmorphism | user | 100 | 0 | `#d3869b` | **ERGODIC** |
| 17 | zubyul | user | 49 | +1 | `#b8bb26` | **PLUS** |
| 18 | migalkin | user | 5 | -1 | `#cc241d` | **MINUS** |
| 19 | wasita | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 20 | AustinCStone | user | 5 | +1 | `#b8bb26` | **PLUS** |
| 21 | kristinezheng | user | 5 | -1 | `#cc241d` | **MINUS** |
| 22 | M1shaaa | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 23 | DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |

---

## JOB 1: GitHub Social Graph Sweep

### Orgs

#### plurigrid (103 repos total, 100 indexed)
Top repos by activity:
- `plurigrid/shepherd` (Scheme) — pushed 2026-01-23
- `plurigrid/duck-kanban` (Rust, ★1) — pushed 2025-09-26
- `plurigrid/aptos-wallet-ruby` (Ruby, ★1)

#### kubeflow (49 repos)
Top repos:
- `kubeflow/trainer` (Go, ★2152) — pushed 2026-07-19 **(active)**
- `kubeflow/spark-operator` (Python, ★3139) — pushed 2026-07-17 **(active)**
- `kubeflow/testing` (Python, ★60) — pushed 2025-02-14

#### TeglonLabs (5 repos)
- `TeglonLabs/jank-crane` (C++) — pushed 2026-06-08, crane-jank converged-IR hub, GF3 convergence maps
- `TeglonLabs/mathpix-gem` (Ruby, ★2) — pushed 2026-01-01, math OCR gem
- `TeglonLabs/coin-flip-mcp` (JS, 2 forks) — MCP coin flip server

### Users

#### bmorphism (106 repos total, 100 indexed)
Notable:
- `bmorphism/world` (Python) — pushed 2026-06-02, local worlds launcher for SA3/jank
- `bmorphism/manifold-mcp-server` (JS, ★14, 9 forks) — Manifold prediction markets MCP
- `bmorphism/signal-mcp` (Rust) — O(n)→O(1) chromatic mode collapse via Galois connection
- `bmorphism/zeldar` (Python, ★1) — Burning Man Art Robot

#### zubyul (49 repos)
Notable:
- `zubyul/gay-world` (Python, ★1, 1 fork) — pushed 2026-03-26, goblin world builder with MLX
- `zubyul/toad-warpify-extension` (Python) — pushed 2026-01-17, ACP agent control extension
- `zubyul/quantum-telephone` (Jupyter) — entangled message passing world

### Zubyul Social Graph

#### migalkin (19 repos) — ML/KG researcher
- `migalkin/NodePiece` (Python, ★144, 21 forks) — ICLR'22 KG embeddings
- `migalkin/StarE` (Python, ★89, 16 forks) — Hyper-relational KG, EMNLP 2020
- `migalkin/kgcourse2021` (HTML, ★24, 8 forks) — updated 2026-07-10

#### wasita (12 repos)
Active: `wasita/wasita.github.io` pushed 2026-07-16; `wasita/pnas-typst-template` pushed 2026-07-16

#### AustinCStone (41 repos)
- `AustinCStone/byteruckus` (HTML) — pushed 2026-07-15 **(brand new)**
- `AustinCStone/TextGAN` (Python, ★92, 30 forks) — GAN text generation

#### kristinezheng (5 repos)
`kristinezheng/kristinezheng.github.io` — pushed 2026-07-01

#### M1shaaa (8 repos)
`M1shaaa/M1shaaa` — pushed 2026-02-04

#### DJedamski (6 repos)
Stats/data science repos (R, Jupyter). Last activity 2023.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) returned **not_found** from Aptos mainnet.
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource absent on all.
These accounts have not been initialized with APT on mainnet.

### Multisig Contract Probes (5 contracts) — ALL HEALTHY

All 5 multisig contracts respond with `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...4987003` | 2 | healthy |
| A-G | `0xf56c4a1c...bc0096` | 2 | healthy |
| Y-Z | `0xd3ffe181...5b883` | 2 | healthy |
| S-T | `0x3b1c3ae9...d7883` | 2 | healthy |
| V-W | `0x40fad7b4...0eb6d` | 2 | healthy |

### MNX Markets

`https://testnet.mnx.fi` — **unavailable** (no API response on `/api/markets` or `/api/v1/markets`).

---

## Notable Signals

- **kubeflow/trainer** + **kubeflow/spark-operator** both pushed within 48h — ML infra actively maintained
- **TeglonLabs/jank-crane** (C++) pushed June 2026 — GF3 convergence/IR work ongoing
- **bmorphism/world** pushed June 2026 — worlds launcher connecting SA3 + jank ecosystem
- **wasita** pushing daily (2026-07-16) — pnas-typst + personal site active
- **AustinCStone/byteruckus** created 2026-07-15 — brand new repo
- **migalkin/kgcourse2021** updated 2026-07-10 — KG course still maintained
- All Hamming swarm wallets uninitialized on Aptos mainnet
- All 5 multisig 2-of-N contracts responding correctly
