# World-Increment Sweep + Hamming Snapshot — 2026-06-15

## Sweep Metadata
- **Date:** 2026-06-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 326 |
| Sources Covered | 3 orgs + 8 users |

---

### GF(3) Color Chain — All 11 Increments

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | 48 | -1 | `#cc241d` | **MINUS** |
| 3  | bmorphism | user | 100 | 0 | `#d3869b` | **ERGODIC** |
| 4  | zubyul | user | 49 | +1 | `#b8bb26` | **PLUS** |
| 5  | TeglonLabs | org | 5 | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | social_graph | 6 | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | social_graph | 3 | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | social_graph | 5 | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | social_graph | 2 | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | social_graph | 3 | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | social_graph | 5 | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`  
Distribution: ERGODIC×3, PLUS×4, MINUS×4

---

### Top Repos by Source

#### plurigrid (100 repos snapshotted)
| Repo | Language | Stars | Open Issues | Pushed At |
|------|----------|-------|-------------|-----------|
| gorj | Clojure | — | 584 | 2026-06-15 |
| eirobri | Clojure | — | 29 | 2026-06-15 |
| nanoclj-zig | Zig | — | 20 | 2026-06-15 |
| asi | HTML | 16 | — | 2026-06-10 |
| gay-rs | Rust | — | — | 2026 |

Focus areas: GF(3) color systems (Gay.jl, gay-rs, gay-go), formal topology (forester, graded-optic), REPL infrastructure (gorj), Zig/Clojure compilers.

#### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,722 | 2026-06-11 |
| pipelines | Python | 4,154 | 2026-06-14 |
| spark-operator | Python | 3,127 | 2026-06-14 |
| trainer | Go | 2,115 | 2026-06-13 |
| katib | Python | 1,683 | 2026-06-12 |
| mcp-apache-spark-history-server | Python | 177 | 2026-06-10 |

#### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026 |
| say-mcp-server | — | 20 | 2026 |
| babashka-mcp-server | — | 19 | 2026 |
| Gay.jl | Julia | 1 | 2026-06-15 |
| satreadout | Lean 4 | — | 2026-06-10 |

Focus: MCP servers (OCaml, Babashka, manifold, macOS TTS), Gay.jl wide-gamut color sampling, Lean 4 formal proofs.

#### zubyul (49 repos)
| Repo | Language | Stars |
|------|----------|-------|
| gay-world | — | 1 |
| Gay.jl | Julia | — |
| plurigrid-site | Svelte | — |
| nash-tui | — | — |
| gay-terminal-colors | — | — |

Collaborates heavily with bmorphism; shared Gay.jl repo.

#### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

jank-crane (newest): crane-jank converged-IR hub with GF3 convergence maps.

#### Zubyul Social Graph
| User | Top Repos | Specialty |
|------|-----------|-----------|
| migalkin | NodePiece (144⭐), StarE (89⭐), kgcourse2021 (25⭐) | Knowledge Graph ML research (ICLR, EMNLP) |
| AustinCStone | EpsteinSearch, bmfork variants | Python tooling, connects to bmorphism orbit |
| wasita | wasita.github.io, wm-cv, magic-garden | Svelte/TypeScript, Network Science (WiNS) |
| DJedamski | Kaggle, ncaa18 | R/Jupyter data science |
| M1shaaa | lab-bookshelf-, Lookit tools | TypeScript, cognitive science (Yale) |
| kristinezheng | lookit-jenga, auditory-illusion | MIT cognitive science (9.85, 9.35) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried 28 addresses against `fullnode.mainnet.aptoslabs.com`.

| World | Address (abbrev) | Balance (APT) | Status |
|-------|-----------------|---------------|--------|
| alice | 0xc793...cc7b | 0.0 | no CoinStore |
| bob | 0x0a3c...2d5d | 0.0 | no CoinStore |
| A–Z (26 addrs) | 0x8699...197c | 0.0 each | no CoinStore |

**All 28 addresses have 0 APT.** CoinStore resource not initialized — swarm keys not yet active on mainnet (likely testnet/devnet keys or unfunded accounts).

### Multisig Contract Probes (Mainnet)

All 5 probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (abbrev) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

All 5 multisig contracts deployed and healthy on Aptos mainnet with 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection (auth required). No market data could be extracted. `mnx_snapshots` table has 0 rows.

---

## DuckDB Schema & Row Counts

```
world-increments.duckdb
├── world_increments   11 rows   — sweep events with GF(3) color chain
├── repo_snapshots    326 rows   — full repo metadata (stars, forks, issues, pushed_at)
├── aptos_snapshots    28 rows   — Hamming swarm wallet balances (all 0.0 APT)
├── multisig_probes     5 rows   — multisig contract health (all 2-sig, all healthy)
└── mnx_snapshots       0 rows   — MNX unavailable (Vercel auth gate)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **plurigrid/gorj**: 584 open issues, pushed 2026-06-15 — highest velocity project in the graph
- **Gay.jl**: Wide-gamut GF(3) color sampling in Julia, active today (bmorphism + zubyul collaboration)
- **TeglonLabs/jank-crane**: GF3 convergence maps in C++, newest TeglonLabs repo (2026-06-08)
- **kubeflow/kubeflow**: 15,722⭐ — all major KF repos active through June 2026
- **All multisigs healthy**: 5 Aptos multisig contracts all responding with 2-sig threshold
- **Hamming swarm dormant**: All 28 mainnet wallets at 0 APT — not yet activated
