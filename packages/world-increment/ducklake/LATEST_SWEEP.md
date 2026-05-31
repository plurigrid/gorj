# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-05-31 UTC  
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d  
**DuckDB:** v1.5.3 (Variegata) · `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| kubeflow | org | 48 |
| plurigrid | org | 99 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| AustinCStone | user (social) | 40 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 6 |
| M1shaaa | user (social) | 8 |
| DJedamski | user (social) | 6 |
| TeglonLabs | org | 4 |
| migalkin | user (social) | 0 (no public repos found) |
| **TOTAL** | | **372** |

### Top Repos by Stars
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,693 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,149 | 2026-05-30 |
| kubeflow/spark-operator | Python | 3,124 | 2026-05-29 |
| kubeflow/trainer | Go | 2,107 | 2026-05-30 |
| kubeflow/katib | Python | 1,685 | 2026-05-29 |
| kubeflow/examples | Jsonnet | 1,463 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,019 | 2026-05-29 |
| kubeflow/arena | Go | 811 | 2026-05-07 |
| kubeflow/kale | Python | 691 | 2026-05-29 |
| kubeflow/mpi-operator | Go | 528 | 2026-05-29 |
| AustinCStone/TextGAN | Python | 92 | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| kubeflow/website | HTML | 184 | 2026-05-28 |
| kubeflow/community | Jupyter Notebook | 195 | 2026-05-29 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| plurigrid/asi | HTML | 23 | 2026-04-26 |

### Most Recently Active Repos
| Repo | Language | Last Push |
|------|----------|-----------|
| M1shaaa/M1shaaa | — | 2026-05-31 |
| plurigrid/gorj | Clojure | 2026-05-31 |
| bmorphism/Gay.jl | Julia | 2026-05-31 |
| kubeflow/pipelines | Python | 2026-05-30 |
| kubeflow/trainer | Go | 2026-05-30 |

### GF(3) Color Distribution (id mod 3)
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 124 |
| 1 | PLUS | #b8bb26 | 124 |
| -1 | MINUS | #cc241d | 124 |

### Notable Highlights
- **plurigrid/gorj** (this repo): Clojure, GF(3) trit coloring, 276 open issues — active
- **plurigrid/Gay.jl** / **bmorphism/Gay.jl**: Wide-gamut color sampling with SPI, pushed today (2026-05-31)
- **plurigrid/eirobri**: EiRoBri replay world (Clojure), 28 open issues
- **bmorphism/ocaml-mcp-sdk**: 61★ OCaml SDK for MCP using Jane Street's oxcaml_effect
- **kubeflow/mcp-apache-spark-history-server**: 173★ — Spark debugging for AI agents (new)
- **wasita/wasita.github.io**: Personal site in Svelte, pushed 2026-05-20

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet APT)
*Queried via `0x1::coin::balance` view function (FA standard accounts don't expose legacy CoinStore)*

| World | Address | Balance (APT) |
|-------|---------|---------------|
| bob | 0x0a3c...512d | **12.657007** |
| F | 0x18a1...cf71 | 1.960516 |
| L | 0x7c2e...eba9 | 1.927269 |
| J | 0x4d96...f54 | 1.895093 |
| alice | 0xc793...cc7b | 0.436434 |
| O | 0x7325...89d | 0.210136 |
| K | 0xa732...dc4 | 0.161961 |
| P | 0x6218...948 | 0.140136 |
| M | 0x6fed...2e9 | 0.112285 |
| N | 0xe7dd...b2c | 0.106121 |
| Q | 0xac40...89a | 0.103240 |
| S | 0xb875...386 | 0.091788 |
| R | 0x7ce6...e10 | 0.090217 |
| T | 0x3578...588 | 0.073713 |
| U | 0x7586...956 | 0.055773 |
| A | 0x8699...d7a | 0.051767 |
| V | 0xb59d...2c3 | 0.048833 |
| Y | 0xd8e3...4c4 | 0.044449 |
| X | 0xa95c...47d | 0.042577 |
| W | 0x5f32...7b0 | 0.040705 |
| B | 0x3f89...b13 | 0.036256 |
| Z | 0x7af0...97c | 0.024268 |
| D | 0xf776...dd1 | 0.011629 |
| C | 0x38b9...53e | 0.010185 |
| E | 0xdc1d...d36 | 0.009372 |
| H | 0xce67...00f | 0.001681 |
| G | 0x69a3...f32 | 0.000681 |
| I | 0x070f...fc9 | 0.000681 |

**Total swarm APT balance: ~22.15 APT**  
**Richest:** bob (12.66 APT) · F, L, J (~1.9 APT each) · alice (0.44 APT)

### Multisig Contract Health (5/5 ✓)
*Probed via `0x1::multisig_account::num_signatures_required`*

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ healthy |
| A-G | 0xf56c...096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ healthy |
| S-T | 0x3b1c...883 | 2 | ✓ healthy |
| V-W | 0x40fa...b6d | 2 | ✓ healthy |

All 5 multisig accounts are live, requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)
**Status: SPA-only — no REST API available.**  
`testnet.mnx.fi` is a Next.js SPA. Data loads via `wss://api.testnet.mnx.fi` WebSocket + Privy auth. REST paths (`/api/markets`, `/v1/markets`) return HTTP 404. No market tickers extractable without authenticated WebSocket session.

---

## DuckDB Schema & Row Counts
| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 372 | GF(3) annotated increment chain |
| `repo_snapshots` | 372 | GitHub repo metadata snapshot |
| `aptos_snapshots` | 28 | Hamming swarm APT balances |
| `multisig_probes` | 5 | Multisig health checks |
| `mnx_snapshots` | 0 | SPA-only, no data available |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
