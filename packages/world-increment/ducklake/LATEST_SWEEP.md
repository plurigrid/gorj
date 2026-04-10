# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-10

## Sweep Metadata
- **Date:** 2026-04-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all time) | 514 |
| Total Repo Snapshots (all time) | 895 |
| New Increments This Sweep | 11 |
| New Repo Snapshots This Sweep | 286 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain — Sweep Increments (IDs 470–480)

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|----------|-------|------|
| 470 | plurigrid | org | 100 | -1 | `#cc241d` | **MINUS** |
| 471 | kubeflow | org | 0 | 0 | `#d3869b` | **ERGODIC** |
| 472 | TeglonLabs | org | 0 | 1 | `#b8bb26` | **PLUS** |
| 473 | bmorphism | user | 100 | -1 | `#cc241d` | **MINUS** |
| 474 | zubyul | user | 0 | 0 | `#d3869b` | **ERGODIC** |
| 475 | migalkin | user | 30 | 1 | `#b8bb26` | **PLUS** |
| 476 | DJedamski | user | 11 | -1 | `#cc241d` | **MINUS** |
| 477 | wasita | user | 29 | 0 | `#d3869b` | **ERGODIC** |
| 478 | kristinezheng | user | 0 | 1 | `#b8bb26` | **PLUS** |
| 479 | M1shaaa | user | 16 | -1 | `#cc241d` | **MINUS** |
| 480 | AustinCStone | user | 0 | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

> Note: kubeflow, TeglonLabs, zubyul, kristinezheng, AustinCStone returned 0 repos due to GitHub API rate limiting during this sweep window. Increments registered; repos will be populated on next sweep.

### Top Repos This Sweep (by Stars)

| Source | Repo | Language | Stars | Forks | Last Push |
|--------|------|----------|-------|-------|-----------|
| migalkin | NodePiece | Python | 143 | 21 | 2022-02-02 |
| migalkin | StarE | Python | 88 | 16 | 2023-12-01 |
| bmorphism | ocaml-mcp-sdk | OCaml | 60 | 2 | 2026-03-16 |
| migalkin | kgcourse2021 | HTML | 25 | 9 | 2025-08-04 |
| bmorphism | anti-bullshit-mcp-server | JavaScript | 23 | 7 | 2026-01-16 |
| plurigrid | asi | HTML | 16 | 5 | 2026-04-10 |
| migalkin | NBFNet_mlx | Python | 10 | 1 | 2024-03-02 |
| plurigrid | ontology | JavaScript | 7 | 9 | 2025-05-27 |
| migalkin | RWL | Python | 7 | 1 | 2022-12-01 |
| bmorphism | shitcoin | Python | 5 | 0 | 2026-04-08 |
| plurigrid | asi-skills | Julia | 3 | 0 | 2026-04-09 |
| bmorphism | open-location-code-zig | Zig | 3 | 0 | 2025-12-30 |
| plurigrid | zig-syrup | Zig | 2 | 2 | 2026-04-09 |

### Language Distribution (This Sweep)

| Language | Count |
|----------|-------|
| Python | 32 |
| Rust | 13 |
| HTML | 12 |
| Clojure | 8 |
| TypeScript | 7 |
| R | 7 |
| JavaScript | 6 |
| Jupyter Notebook | 6 |
| Go | 5 |
| Scheme | 4 |
| Zig | 4 |
| Julia | 4 |
| Svelte | 4 |

### Notable Repos

**bmorphism** (100 repos, most recently pushed 2026-04-08):
- `shitcoin` (Python, 5★) — CW20 IBC denom tool for permissionless degeneracy
- `ocaml-mcp-sdk` (OCaml, 60★) — MCP SDK via Jane Street oxcaml_effect library
- `anti-bullshit-mcp-server` (JavaScript, 23★) — epistemological claim validation MCP

**plurigrid** (100 repos, most recently pushed 2026-04-10):
- `gorj` (Clojure, 128 open issues) — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- `asi` (HTML, 16★) — everything is topological chemputer!
- `nanoclj-zig` (Zig, 20 open issues) — NaN-boxed Clojure interpreter in Zig 0.15

**migalkin** (30 repos):
- `NodePiece` (Python, 143★) — knowledge graph node representation
- `StarE` (Python, 88★) — EMNLP 2020 hyper-relational KG message passing

**wasita** (29 repos, neuroscience/HCI focus):
- Recent: `wm-cv` (Svelte, 2026-04-08), `wasita.github.io` (Svelte, 2026-03-24)

**DJedamski** (11 repos), **M1shaaa** (16 repos) — social graph nodes with recent activity.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...7b | 0.0 |
| bob | 0x0a3c...5d | 0.0 |
| A | 0x8699...7a | 0.0 |
| B | 0x3f89...13 | 0.0 |
| C | 0x38b9...5e | 0.0 |
| D | 0xf776...d1 | 0.0 |
| E | 0xdc1d...36 | 0.0 |
| F | 0x18a1...71 | 0.0 |
| G | 0x69a3...32 | 0.0 |
| H | 0xce67...0f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...54 | 0.0 |
| K | 0xa732...c4 | 0.0 |
| L | 0x7c2e...a9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...2c | 0.0 |
| O | 0x7325...9d | 0.0 |
| P | 0x6218...48 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...10 | 0.0 |
| S | 0xb875...86 | 0.0 |
| T | 0x3578...88 | 0.0 |
| U | 0x7586...56 | 0.0 |
| V | 0xb59d...c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...7d | 0.0 |
| Y | 0xd8e3...c4 | 0.0 |
| Z | 0x7af0...7c | 0.0 |

> All wallets report 0.0 APT. Accounts may not have initialized a CoinStore resource on Aptos mainnet, or balances are genuinely zero. Aptos fullnode API responded without errors for all queries.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...03 | 2 | ✅ |
| A-G | 0xf56c...96 | 2 | ✅ |
| Y-Z | 0xd3ff...83 | 2 | ✅ |
| S-T | 0x3b1c...83 | 2 | ✅ |
| V-W | 0x40fa...6d | 2 | ✅ |

**All 5 multisig contracts healthy** — each requires 2-of-N signatures. Configuration unchanged since last sweep.

### MNX Testnet Markets

`https://testnet.mnx.fi` — **unavailable**. The site returns an empty response (SPA with no server-side rendering). All probed API paths (`/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`) returned 404 or empty. Recorded as `unavailable` in `mnx_snapshots`.

---

## Database State

| Table | Rows |
|-------|------|
| world_increments | 514 |
| repo_snapshots | 895 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

**DuckDB path:** `packages/world-increment/ducklake/world-increments.duckdb`
