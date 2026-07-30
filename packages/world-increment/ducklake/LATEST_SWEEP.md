# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-30

## Sweep Metadata
- **Date:** 2026-07-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (this run)

| Metric | Value |
|--------|-------|
| New World Increments | 11 (ids 12–22) |
| New Repo Snapshots | 142 |
| Cumulative Repo Snapshots | 1,086 |
| Sources Covered | 3 orgs + 8 users = 11 |

---

### GF(3) Color Chain — This Run's Increments

| ID | Source | Type | GF3 Trit | Color | Name | Repos |
|----|--------|------|-----------|-------|------|-------|
| 12 | plurigrid | org | 0 | `#d3869b` | **ERGODIC** | 30 |
| 13 | TeglonLabs | org | 1 | `#b8bb26` | **PLUS** | 5 |
| 14 | kubeflow | org | -1 | `#cc241d` | **MINUS** | 20 |
| 15 | bmorphism | user | 0 | `#d3869b` | **ERGODIC** | 30 |
| 16 | zubyul | user | 1 | `#b8bb26` | **PLUS** | 17 |
| 17 | migalkin | user | -1 | `#cc241d` | **MINUS** | 7 |
| 18 | wasita | user | 0 | `#d3869b` | **ERGODIC** | 6 |
| 19 | AustinCStone | user | 1 | `#b8bb26` | **PLUS** | 8 |
| 20 | DJedamski | user | -1 | `#cc241d` | **MINUS** | 6 |
| 21 | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** | 5 |
| 22 | M1shaaa | user | 1 | `#b8bb26` | **PLUS** | 8 |

GF(3) chain continues: `…ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

### Top Repos by Source (2026-07-30)

#### plurigrid (30 new snapshots)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 1 | 2026-07-30 |
| asi | HTML | 56 | 2026-07-10 |
| zig-syrup | Zig | 2 | 2026-07-28 |
| eirobri | Clojure | 0 | 2026-07-21 |
| vcg-auction | Rust | 7 | 2023-03-16 |

#### kubeflow (20 new snapshots)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15798 | 2026-07-10 |
| pipelines | Python | 4171 | 2026-07-29 |
| spark-operator | Python | 3142 | 2026-07-30 |
| trainer | Go | 2163 | 2026-07-30 |
| katib | Python | 1694 | 2026-07-26 |

#### TeglonLabs (5 new snapshots)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

#### bmorphism (30 new snapshots, MCP theme dominant)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |
| Gay.jl | Julia | 2 | 2026-07-30 🔥 (188 open issues) |

#### Social Graph
| User | Notable repos |
|------|---------------|
| migalkin | NodePiece (144★), StarE (89★), kgcourse2021 (24★) — KG research |
| wasita | wasita.github.io (Svelte), magic-garden bot, send2kobo |
| AustinCStone | TextGAN (92★), StereoVisionMRF (11★), bmfork/bmforkupdate (AustinC connection to bmorphism) |
| DJedamski | Kaggle/R data science, mostly archived |
| kristinezheng | MIT/lookit cognitive science studies |
| M1shaaa | Yale lab work, Lookit studies |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — 28 addresses (2026-07-30)

| world | address (prefix) | balance_apt |
|-------|------------------|-------------|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A–Z (26 wallets) | various | 0.0 each |

**Total APT across 28 swarm wallets: 0.0 APT**  
All wallets return empty `CoinStore<AptosCoin>` — accounts uninitialized or zero balance.

### Multisig Contract Health — 5 pairs (2026-07-30)

| pair | address (prefix) | sigs_required | healthy |
|------|------------------|---------------|---------|
| A-B | 0x0da4f4… | 2 | ✓ |
| A-G | 0xf56c4a… | 2 | ✓ |
| Y-Z | 0xd3ffe1… | 2 | ✓ |
| S-T | 0x3b1c3a… | 2 | ✓ |
| V-W | 0x40fad7… | 2 | ✓ |

**All 5 multisig contracts HEALTHY** — each requires 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: SPA unavailable** — site returns Next.js bundle, no REST API endpoints (`/api/markets`, `/api/v1/markets`) yielded JSON. Recorded as `unavailable` in `mnx_snapshots`.

---

## DuckDB Table State

| table | rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1,086 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
