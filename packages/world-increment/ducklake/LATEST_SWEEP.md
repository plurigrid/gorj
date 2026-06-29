# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-29  
**GF(3) Color Chain:** ERGODIC #d3869b (trit=0, id%3==0)

---

## JOB 1: GitHub Social Graph Sweep

### Summary
Snapshotted **331 repos** across 11 sources (3 orgs + 2 primary users + 6 social graph users).

| Source | Type | Repos | Total Stars | Latest Push |
|---|---|---|---|---|
| bmorphism | user | 100 | 247 | 2026-06-29 |
| plurigrid | org | 100 | 78 | 2026-06-29 |
| zubyul | user | 49 | 14 | 2026-04-24 |
| kubeflow | org | 48 | 34,275 | 2026-06-27 |
| migalkin | social | 6 | 279 | 2026-05-28 |
| wasita | social | 6 | 4 | 2026-06-25 |
| TeglonLabs | org | 5 | 2 | 2026-06-08 |
| DJedamski | social | 5 | 3 | 2023-04-21 |
| AustinCStone | social | 5 | 103 | 2026-04-01 |
| kristinezheng | social | 4 | 0 | 2026-06-07 |
| M1shaaa | social | 3 | 0 | 2026-02-04 |

### Notable Active Repos (pushed 2026-06-29)
- **plurigrid/asi** (HTML, 27★) — "everything is topological chemputer!" — pushed 2026-06-29T03:15Z
- **plurigrid/place** (TeX, 1★, 10 issues) — pushed 2026-06-29T04:12Z
- **plurigrid/gorj** (Clojure, 898 issues) — "forj + Rama topology nREPL routing + GF(3) gay trit coloring" — pushed 2026-06-29T04:10Z
- **bmorphism/Gay.jl** (Julia, 2★, 187 issues) — "Wide-gamut color sampling with splittable determinism" — pushed 2026-06-29T00:40Z

### kubeflow Top Repos
| Repo | Language | Stars | Forks |
|---|---|---|---|
| kubeflow/kubeflow | - | 15,750 | 2,681 |
| kubeflow/pipelines | Python | 4,159 | 2,014 |
| kubeflow/spark-operator | Python | 3,129 | 1,492 |
| kubeflow/trainer | Go | 2,126 | 973 |
| kubeflow/katib | Python | 1,687 | 528 |

### TeglonLabs Repos
- **jank-crane** (C++) — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps
- **mathpix-gem** (Ruby, 2★) — mathematical image to LaTeX/SMILES OCR
- **coin-flip-mcp** (JS, 2 forks) — MCP server for randomness via random.org
- **monad-mcp-server** — Monad MCP Server
- **topoi** (Python) — (no description)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
Queried 28 addresses (alice, bob, A-Z) via Aptos fullnode mainnet.

**Result: All 28 wallets show 0.0 APT** — CoinStore resource not found or unfunded. These addresses exist on-chain but have no APT CoinStore balance registered.

| World | Address (prefix) | Balance APT |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...c4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes (Aptos Mainnet)
All 5 multisig contracts respond with **sigs_required=2** - all healthy.

| Pair | Address (prefix) | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable** - testnet.mnx.fi returns HTTP 401 (Vercel deployment protection). Authentication token required; no market data accessible from this environment.

---

## DuckDB Ducklake State
**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|---|---|
| world_increments | 24 |
| repo_snapshots | 1,275 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## GF(3) Chain
- id%3==0 -> trit=0, ERGODIC, color=#d3869b (rose)
- id%3==1 -> trit=1, PLUS, color=#b8bb26 (yellow-green)
- id%3==2 -> trit=-1, MINUS, color=#cc241d (red)

This sweep: **ERGODIC #d3869b**
