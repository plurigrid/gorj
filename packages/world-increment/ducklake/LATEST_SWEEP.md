# World Increment Sweep + Hamming Swarm Snapshot

**Sweep Date**: 2026-06-16  
**Run Time**: UTC ~15:00–15:20  
**GF(3) Color Chain**: ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Orgs Snapshotted

| Org | Repos | Top Stars | Most Active (recent push) |
|-----|-------|-----------|--------------------------|
| plurigrid | 101 | asi (26★), ontology (8★) | gorj (today, 620 open issues), place (yesterday) |
| kubeflow | 48 | kubeflow/kubeflow (15,725★), pipelines (4,154★), trainer (2,115★), spark-operator (3,127★) | community, trainer, website, pipelines, katib |
| TeglonLabs | 5 | mathpix-gem (2★) | jank-crane (C++, 2026-06-08) |

### Users Snapshotted

| User | Repos | Notable |
|------|-------|---------|
| bmorphism | 104 | ocaml-mcp-sdk (61★), anti-bullshit-mcp-server (23★), Gay.jl (Julia), satreadout (Lean) |
| zubyul | 49 | voice-observatory, nash-tui (Rust), gay-terminal-colors (Clojure), Gay.jl fork |
| migalkin | 19 | Knowledge graph/GNN research repos |
| AustinCStone | 40 | ML/computer vision research |
| M1shaaa | 8 | lab-bookshelf- (TypeScript), pushed today (profile config) |
| DJedamski | 6 | kaggle_ncaa18 (Jupyter), EDA/Getting-and-Cleaning-Data (R) |
| wasita | 11 | wasita.github.io (Svelte, pushed yesterday), cognitive science repos |
| kristinezheng | 5 | kristinezheng.github.io (HTML, pushed 2026-06-07), lookit-jenga |

### DuckDB Final Counts

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1,335 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |

### Notable Plurigrid Activity (as of 2026-06-16)
- **gorj** (this repo): Clojure, 620 open issues, pushed today — GF(3)/REPL orchestration, forj+Rama topology
- **place**: TeX, pushed 2026-06-15 (8 open issues)
- **eirobri**: Clojure, EiRoBri replay world (29 open issues), pushed 2026-06-03
- **nash-portal**: Rust, NASH token TUI with GeckoTerminal OHLCV candlesticks (2★, 2026-05-19)
- **asi**: HTML, 26★, 8 forks — "everything is topological chemputer!" (2026-06-10)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-06-16 ~15:05 UTC)

All 28 Hamming swarm addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
**Result: All returned null** — accounts not initialized or no APT deposited via legacy coin module.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793acd... | 0.0 |
| bob | 0x0a3c00c... | 0.0 |
| A | 0x8699edc... | 0.0 |
| B | 0x3f892eb... | 0.0 |
| C | 0x38b99e6... | 0.0 |
| D | 0xf776562... | 0.0 |
| E | 0xdc1d9d5... | 0.0 |
| F | 0x18a14b5... | 0.0 |
| G | 0x69a394c... | 0.0 |
| H | 0xce67c32... | 0.0 |
| I | 0x070fe5d... | 0.0 |
| J | 0x4d964db... | 0.0 |
| K | 0xa732040... | 0.0 |
| L | 0x7c2eaea... | 0.0 |
| M | 0x6fed37a... | 0.0 |
| N | 0xe7dde6d... | 0.0 |
| O | 0x73252b6... | 0.0 |
| P | 0x6218792... | 0.0 |
| Q | 0xac40fa5... | 0.0 |
| R | 0x7ce605c... | 0.0 |
| S | 0xb875301... | 0.0 |
| T | 0x35781dc... | 0.0 |
| U | 0x75860da... | 0.0 |
| V | 0xb59dd81... | 0.0 |
| W | 0x5f32aef... | 0.0 |
| X | 0xa95cbbd... | 0.0 |
| Y | 0xd8e3284... | 0.0 |
| Z | 0x7af0ef6... | 0.0 |

### Multisig Probe Results — ALL HEALTHY ✅

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2/2 | ✅ healthy |
| A-G | 0xf56c4a1c... | 2/2 | ✅ healthy |
| Y-Z | 0xd3ffe181... | 2/2 | ✅ healthy |
| S-T | 0x3b1c3ae9... | 2/2 | ✅ healthy |
| V-W | 0x40fad7b4... | 2/2 | ✅ healthy |

All 5 multisig contracts on Aptos mainnet respond with 2-of-2 threshold.

### MNX Markets (testnet.mnx.fi)

**Status**: Unavailable — Vercel deployment protection (HTTP 401).  
`testnet.mnx.fi` returns authentication required page. No market data accessible without a visitor password or bypass token.  
`mnx_snapshots` table created but empty.

---

## GF(3) World Increment Chain

Each source assigned a GF(3) trit by increment ID:

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | 1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |

---

## DuckDB Location

`packages/world-increment/ducklake/world-increments.duckdb`

Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
