# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-11  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 25 |
| bmorphism | user | 16 |
| zubyul | user | 15 |
| kubeflow | org | 15 |
| AustinCStone | user (social) | 8 |
| M1shaaa | user (social) | 7 |
| migalkin | user (social) | 7 |
| wasita | user (social) | 7 |
| DJedamski | user (social) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (social) | 5 |
| **TOTAL** | | **116** |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC  | #d3869b | 0 | 38 |
| PLUS     | #b8bb26 | +1 | 39 |
| MINUS    | #cc241d | -1 | 39 |

### Notable Repos (by stars)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,714 | — | 2026-06-11 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-11 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-09 |
| kubeflow/trainer | 2,111 | Go | 2026-06-10 |
| kubeflow/katib | 1,683 | Python | 2026-06-05 |
| kubeflow/manifests | 1,022 | YAML | 2026-06-09 |
| kubeflow/arena | 812 | Go | 2026-05-07 |
| kubeflow/kale | 692 | Python | 2026-06-10 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/gorj | 0 | Clojure | 2026-06-11 (505 issues) |

### Hot Activity (pushed today 2026-06-11)

- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3)
- `kubeflow/kubeflow`, `kubeflow/dashboard`, `kubeflow/website`
- `bmorphism/Gay.jl` — Wide-gamut color sampling splittable determinism
- `M1shaaa/M1shaaa` — profile config updated

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-11)

All 28 Hamming swarm wallets queried against Aptos mainnet
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
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
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Result:** All wallets return 0.0 APT — accounts are either empty or CoinStore not registered on mainnet.

### Multisig Contract Probes

All 5 pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**Result:** All 5 multisig accounts healthy, all require 2-of-N signatures.

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE**: Vercel deployment protection active (authentication required). No API data extractable without bypass token.

---

## DuckDB Schema

```
world_increments  — 116 rows  (GF3 color chain, one per repo snapshot)
repo_snapshots    — 116 rows  (full metadata per repo)
aptos_snapshots   —  28 rows  (wallet balances)
multisig_probes   —   5 rows  (contract sigs_required)
mnx_snapshots     —   1 row   (availability note)
```
