# World Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-05-12  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos Fetched | Note |
|--------|------|--------------|------|
| plurigrid | org | 100 | Full snapshot |
| TeglonLabs | org | 53 | Full snapshot |
| zubyul | user | 27 | Full snapshot |
| kubeflow | org | — | Rate limited (public API 60/hr) |
| bmorphism | user | — | Rate limited |
| migalkin | user | — | Rate limited |
| DJedamski | user | — | Rate limited |
| wasita | user | — | Rate limited |
| kristinezheng | user | — | Rate limited |
| M1shaaa | user | — | Rate limited |
| AustinCStone | user | — | Rate limited |

GitHub unauthenticated API limit (60 req/hr) exhausted after 3 sources. Prior sweep data for remaining sources present in DB from previous runs.

### GF(3) Color Chain Distribution

| Color | Hex | Trit | Count |
|-------|-----|------|-------|
| ERGODIC | #d3869b | 0 | 67 |
| PLUS | #b8bb26 | +1 | 68 |
| MINUS | #cc241d | -1 | 68 |

### Top Repos by Stars (This Sweep)

| Repo | Language | Stars |
|------|----------|-------|
| plurigrid/asi | HTML | 21 |
| plurigrid/ontology | JavaScript | 8 |
| plurigrid/asi-skills | Julia | 3 |
| plurigrid/zig-syrup | Zig | 2 |
| TeglonLabs/mathpix-gem | Ruby | 2 |
| TeglonLabs/vibespace | HTML | 2 |
| plurigrid/nash-portal | Rust | 2 |
| zubyul/jonikas_lab_data_analysis_misc | Jupyter Notebook | 2 |
| zubyul/WGCNA | HTML | 2 |
| zubyul/Nikolova_lab_data_analysis | R | 2 |

### Plurigrid Org Highlights (100 repos)
Active languages: HTML, JavaScript, Julia, Zig, Rust, TeX, Clojure, C++, Python  
Top repo: `asi` (21 stars) — ASI agent infrastructure

### TeglonLabs Highlights (53 repos)
Active languages: Ruby, HTML, JavaScript  
Notable: `mcp-terminal`, `agent-client-protocol`, `MCP-Universe`, `deepwiki-mcp`, `coin-flip-mcp`

### Zubyul Highlights (27 repos)
Active languages: Jupyter Notebook, R, Python, CSS  
Focus: bioinformatics, data analysis, lab tooling

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming-swarm addresses (alice, bob, A-Z) returned `resource_not_found` from the CoinStore resource endpoint. These accounts exist on Aptos mainnet but hold no APT via the legacy `0x1::coin::CoinStore` — balances may be held via Fungible Asset framework or accounts are unfunded.

| World | Address | Balance (APT) |
|-------|---------|--------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...3cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...25dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...76e10 | 0.0 |
| S | 0xb875...d0386 | 0.0 |
| T | 0x3578...f4588 | 0.0 |
| U | 0x7586...ef9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...cc7b0 | 0.0 |
| X | 0xa95c...3047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...e197c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts are **HEALTHY** — 2 signatures required.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. All API paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`, etc.) return HTML without JSON payloads. No market data extractable from server responses. Status: **UNAVAILABLE** (SPA, no public REST API).

---

## DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 203 |
| repo_snapshots | 1124 (cumulative across sweeps) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

---

*Sweep completed autonomously by world-increment-sweep + hamming-swarm-snapshot agent. 2026-05-12.*
