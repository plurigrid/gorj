# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-25  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain
| trit | name | color |
|------|------|-------|
| 0 | ERGODIC | #d3869b |
| 1 | PLUS | #b8bb26 |
| -1 | MINUS | #cc241d |

Coloring: `id % 3`: 0→ERGODIC (#d3869b), 1→PLUS (#b8bb26), 2→MINUS (#cc241d)

### Repo Snapshots: 47 repos across all sources

#### plurigrid (org, 103 repos total, 14 snapped)
| repo | lang | stars | pushed_at | GF3 |
|------|------|-------|-----------|-----|
| gorj | Clojure | 1 | 2026-07-25 | PLUS (open_issues=1,387!) |
| eirobri | Clojure | 0 | 2026-07-21 | — |
| place | TeX | 1 | 2026-07-14 | — |
| asi | HTML | 31 | 2026-07-10 | — |
| shrimp | — | 0 | 2026-07-03 | — |
| nash-portal | Rust | 2 | 2026-05-19 | — |
| zig-syrup | Zig | 2 | 2026-04-30 | — |
| asi-skills | Julia | 3 | 2026-04-26 | — |
| nanoclj-zig | Zig | 1 | 2026-04-25 | — |
| vivarium | Clojure | 1 | 2026-04-08 | — |

#### kubeflow (org, 49 repos total, 8 snapped)
| repo | lang | stars | forks | pushed_at |
|------|------|-------|-------|-----------|
| kubeflow | — | 15,793 | 2,685 | 2026-07-10 |
| pipelines | Python | 4,169 | 2,059 | 2026-07-24 |
| spark-operator | Python | 3,143 | 1,505 | 2026-07-25 |
| trainer | Go | 2,153 | 995 | 2026-07-25 |
| katib | Python | 1,692 | 532 | 2026-07-22 |
| sdk | Python | 127 | 211 | 2026-07-24 |
| hub | Go | 178 | 188 | 2026-07-24 |
| mcp-server | Python | 29 | 37 | 2026-07-24 |

#### TeglonLabs (org, 5 repos total)
| repo | lang | stars | pushed_at |
|------|------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JS | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

#### bmorphism (user, 106 repos total, 6 snapped)
| repo | lang | stars | pushed_at |
|------|------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-07-21 |
| gay-chat | Scheme | 0 | 2026-07-14 |
| anti-bullshit-mcp-server | JS | 22 | 2026-07-12 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| satreadout | HTML | 0 | 2026-06-20 |
| shitcoin | Python | 5 | 2026-04-08 |

#### zubyul (user, 49 repos total, 6 snapped)
| repo | lang | stars | pushed_at |
|------|------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| gay-world | Python | 1 | 2026-04-05 |
| big-bad-plurigrid-quiz | Emacs Lisp | 0 | 2026-04-09 |
| kinesis-kb360pro | Python | 0 | 2026-03-26 |
| tilelang-kernels | Python | 0 | 2026-03-16 |
| Gay.jl (fork) | Julia | 0 | 2026-03-28 |

#### Social Graph (zubyul connections)
| user | repo | lang | stars | pushed_at |
|------|------|------|-------|-----------|
| migalkin | NodePiece | Python | 144 | 2026-05-07 |
| migalkin | kgcourse2021 | HTML | 24 | 2026-07-10 |
| migalkin | StarE | Python | 89 | 2026-04-16 |
| wasita | wasita.github.io | Svelte | 1 | 2026-07-21 |
| wasita | magic-garden | Python | 2 | 2026-04-22 |
| kristinezheng | kristinezheng.github.io | HTML | 0 | 2026-07-01 |
| AustinCStone | byteruckus | HTML | 0 | 2026-07-15 |
| DJedamski | Kaggle | — | 1 | 2023-04-21 |
| M1shaaa | M1shaaa | — | 0 | 2026-02-04 |

### Notable Signals
- **plurigrid/gorj** has **1,387 open issues** — extremely active or issue-tracker-heavy
- **kubeflow** ecosystem highly active; mcp-server (29 stars, 37 forks) trending
- **bmorphism/ocaml-mcp-sdk** at 61 stars — notable for niche OCaml MCP tooling
- **migalkin/NodePiece** (144 stars) — most-starred social-graph node, KG research
- **TeglonLabs/jank-crane** — GF3 + C++ converged-IR hub, just pushed June 2026

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)
All 28 Hamming-swarm addresses returned **0.000000 APT** from mainnet APT CoinStore.
Accounts exist on-chain but hold no native APT (assets may be in other token types).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…512d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B–Z | (25 addresses) | 0.0 each |

### Multisig Contract Probes (5 pairs)
All 5 multisig accounts are **healthy** and require **2-of-N signatures**:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|:---:|:---:|
| A-B | 0x0da4…7003 | 2 | healthy |
| A-G | 0xf56c…0096 | 2 | healthy |
| Y-Z | 0xd3ff…b883 | 2 | healthy |
| S-T | 0x3b1c…7883 | 2 | healthy |
| V-W | 0x40fa…eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
**Unavailable** — site serves a Next.js SPA; API paths (`/api/markets`, `/api/v1/markets`, `/api/ticker`) return HTML, not JSON. No market data extractable without headless browser. `mnx_snapshots` table is empty this sweep.

---

## DuckDB Tables Summary
| Table | Rows |
|-------|------|
| world_increments | 47 |
| repo_snapshots | 47 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
