# World-Increment Sweep + Hamming Swarm Snapshot
**Sweep date:** 2026-06-11 09:13 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100+ |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 30+ |

### Notable Repos (by stars)
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,713 | Go |
| kubeflow/pipelines | 4,153 | Python |
| kubeflow/spark-operator | 3,126 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/say-mcp-server | 20 | JavaScript |
| bmorphism/babashka-mcp-server | 19 | JavaScript |
| bmorphism/manifold-mcp-server | 14 | JavaScript |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| bmorphism/penrose-mcp | 10 | JavaScript |

### Most Recently Active
- **bmorphism/satreadout** — Machine-checked saturating non-Riemannian perceptual readout (Lean 4, pushed 2026-06-10)
- **bmorphism/Gay.jl** — Wide-gamut color sampling (Julia, pushed 2026-06-10)
- **TeglonLabs/jank-crane** — crane-jank converged-IR hub with GF3 convergence maps (C++, pushed 2026-06-08)
- **kristinezheng/kristinezheng.github.io** — personal site (pushed 2026-06-07)
- **zubyul/voice-observatory** — passive macOS TUI observing voice-download pathways (pushed 2026-04-24)

### GF(3) Color Chain Distribution (this sweep: 204 increments)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | ~68 |
| +1 | #b8bb26 | PLUS | ~68 |
| -1 | #cc241d | MINUS | ~68 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)
All 28 Hamming swarm addresses queried via Aptos fullnode mainnet API.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...b3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

> All wallets returned 0.0 APT — CoinStore resource not initialized (unfunded or unclaimed addresses).

### Multisig Contract Probes (5 contracts)
All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

> All 5 multisig contracts healthy — 2-of-N threshold configured on each.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — testnet.mnx.fi returns HTTP 401 (Vercel authentication protection). Market data not accessible without Vercel bypass credentials. No mnx_snapshots inserted.

---

## DuckDB Ducklake Summary
- **File:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Tables:** world_increments, repo_snapshots, aptos_snapshots, multisig_probes, mnx_snapshots
- **world_increments:** 227 total rows (cumulative)
- **repo_snapshots:** 1148 total rows (cumulative)
- **aptos_snapshots:** 28 rows (this sweep)
- **multisig_probes:** 5 rows (this sweep)
