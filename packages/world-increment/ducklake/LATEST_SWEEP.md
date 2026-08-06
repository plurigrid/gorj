# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-06  
**Ledger Block:** 953,403,551 (Aptos mainnet, epoch 16812)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept
| Type | Source | Repos |
|------|--------|-------|
| org | plurigrid | 100 |
| org | kubeflow | 49 |
| org | TeglonLabs | 5 |
| user | bmorphism | 100 |
| user | zubyul | 49 |
| social | migalkin | 19 |
| social | wasita | 14 |
| social | AustinCStone | 41 |
| social | DJedamski | 6 |
| social | kristinezheng | 5 |
| social | M1shaaa | 8 |

**Total repo snapshots this run:** 315 increments ingested

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 112 |
| +1 | #b8bb26 | PLUS | 113 |
| -1 | #cc241d | MINUS | 113 |

### Noteworthy Recent Activity
- **plurigrid/gorj** — pushed 2026-08-06 (today); Clojure, 1 star
- **wasita/xoxowasita-analysis** — pushed 2026-08-06 (today); Python, just created 2026-08-04
- **kubeflow/trainer** — 2,171 stars, Go, pushed 2026-08-06
- **kubeflow/pipelines** — 4,178 stars, Python, pushed 2026-08-05
- **kubeflow/kubeflow** — 15,805 stars, 2,691 forks — most starred in sweep
- **bmorphism/Gay.jl** — pushed 2026-08-06 (today); Julia
- **migalkin/NodePiece** — 144 stars, ICLR'22 knowledge graph paper

### Top Starred Repos
| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15,805 | 2,691 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,178 | 2,080 | 2026-08-05 |
| kubeflow/spark-operator | Python | 3,144 | 1,511 | 2026-08-05 |
| kubeflow/trainer | Go | 2,171 | 1,015 | 2026-08-06 |
| kubeflow/katib | Python | 1,694 | 534 | 2026-08-05 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| plurigrid/asi | HTML | 59 | — | 2026-07-10 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 wallets)

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| bob | 0x0a3c...5d | 12.657007 |
| F | 0x18a1...71 | 1.960516 |
| L | 0x7c2e...a9 | 1.927269 |
| J | 0x4d96...54 | 1.895093 |
| alice | 0xc793...7b | 0.436434 |
| O | 0x7325...9d | 0.210136 |
| K | 0xa732...c4 | 0.161961 |
| P | 0x6218...48 | 0.140136 |
| M | 0x6fed...e9 | 0.112285 |
| N | 0xe7dd...2c | 0.106121 |
| Q | 0xac40...a9 | 0.103240 |
| S | 0xb875...86 | 0.091788 |
| R | 0x7ce6...10 | 0.090217 |
| T | 0x3578...88 | 0.073713 |
| U | 0x7586...56 | 0.055773 |
| A | 0x8699...7a | 0.051767 |
| V | 0xb59d...c3 | 0.048833 |
| Y | 0xd8e3...c4 | 0.044449 |
| X | 0xa95c...7d | 0.042577 |
| W | 0x5f32...b0 | 0.040705 |
| B | 0x3f89...13 | 0.036256 |
| Z | 0x7af0...7c | 0.024268 |
| D | 0xf776...d1 | 0.011629 |
| C | 0x38b9...5e | 0.010185 |
| E | 0xdc1d...36 | 0.009372 |
| H | 0xce67...0f | 0.001681 |
| I | 0x070f...c9 | 0.000681 |
| G | 0x69a3...32 | 0.000681 |

**Total APT across swarm: 20.344773 APT**  
**Dominant holders:** bob (12.66), F (1.96), L (1.93), J (1.90)

### Multisig Contract Probes (5/5 healthy)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...03 | 2 | ✅ healthy |
| A-G | 0xf56c...96 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...83 | 2 | ✅ healthy |
| S-T | 0x3b1c...83 | 2 | ✅ healthy |
| V-W | 0x40fa...6d | 2 | ✅ healthy |

All 5 multisig accounts require 2-of-N signatures. All reachable and responsive.

### MNX Markets (testnet.mnx.fi)
- `/api/markets` → HTTP 404
- Main page → SPA shell only (no SSR data)
- **Status: unavailable** — testnet SPA not serving market data via public API

---

## DuckDB Tables Updated

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 338 |
| repo_snapshots | 1,259 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

Database: `packages/world-increment/ducklake/world-increments.duckdb`
