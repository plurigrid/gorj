# World Increment Sweep + Hamming Snapshot

**Sweep timestamp:** 2026-05-31T18:08Z  
**Branch:** world-increment/sweep-2026-05-31  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 48 | 34,159 |
| bmorphism | user | 100 | 247 |
| migalkin | user | 5 | 276 |
| plurigrid | org | 100 | 74 |
| AustinCStone | user | 4 | 103 |
| zubyul | user | 10 | 7 |
| wasita | user | 5 | 4 |
| TeglonLabs | org | 4 | 2 |
| DJedamski | user | 3 | 2 |
| M1shaaa | user | 3 | 0 |
| kristinezheng | user | 3 | 0 |
| **TOTAL** | | **285** | **34,874** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,695 | — |
| kubeflow/pipelines | 4,149 | Python |
| kubeflow/spark-operator | 3,124 | Python |
| kubeflow/trainer | 2,109 | Go |
| kubeflow/katib | 1,685 | Python |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| bmorphism/manifold-mcp-server | 14 | JavaScript |

### Notable Activity (zubyul social graph)

- **bmorphism/Gay.jl** — 189 open issues, Julia, wide-gamut color sampling (SplitMix64 + GF(3)) — most active repo
- **zubyul/tilelang-kernels** — GPU kernels for GF(3) trit classification, targeting NVIDIA GB10 Blackwell
- **zubyul/gay-world** — goblin world builder with MLX task decomposition
- **migalkin/RWL** — Weisfeiler-Leman Go Relational (LOG 2022), pushed 2026-05-28
- **TeglonLabs/mathpix-gem** — Ruby gem for mathematical OCR (LaTeX, SMILES)

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 95 |
| +1 | PLUS | `#b8bb26` | 95 |
| -1 | MINUS | `#cc241d` | 95 |

285 world increments minted. IDs sequenced 1→285, GF(3) balanced.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 Hamming swarm wallets (alice, bob, A–Z) returned **0 APT**.  
No `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource found on any address — accounts appear uninitialized or hold no APT coin store on Aptos mainnet.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes (5 pairs)

All 5 multisig accounts responded via `0x1::multisig_account::num_signatures_required`.  
All require **2-of-N** signatures. All **healthy**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | healthy |
| A-G | 0xf56c...096 | 2 | healthy |
| Y-Z | 0xd3ff...883 | 2 | healthy |
| S-T | 0x3b1c...883 | 2 | healthy |
| V-W | 0x40fa...b6d | 2 | healthy |

### MNX Testnet Markets

`https://testnet.mnx.fi` is a **Next.js SPA** — server returns rendered HTML only. No REST API endpoints (`/api/markets`, `/api/v1/markets`, `/api/v1/tickers`) responded with structured market data. Market data is loaded client-side via JavaScript bundles. Status: **unavailable via server-side probe**.

---

## DuckDB Schema

```
world_increments  — 285 rows (GF3 color chain)
repo_snapshots    — 285 rows (cross-org repo index)
aptos_snapshots   — 28 rows  (Hamming swarm wallet balances)
multisig_probes   — 5 rows   (2-of-N sig health)
mnx_snapshots     — 0 rows   (SPA, no API data)
```

DB path: `packages/world-increment/ducklake/world-increments.duckdb`
