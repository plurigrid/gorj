# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-07  
**Branch:** world-increment sweep  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | ~100 |
| kubeflow | org | ~100 |
| TeglonLabs | org | 4 |
| bmorphism | user | 103 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 40 |

**Total world_increment events:** 201  
**Total repo_snapshots rows:** 1122

### GF(3) Trit Distribution

| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | `#d3869b` | 0 | 66 |
| PLUS | `#b8bb26` | +1 | 68 |
| MINUS | `#cc241d` | -1 | 67 |

### Top Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15706 | — |
| kubeflow | pipelines | 4153 | Python |
| kubeflow | spark-operator | 3126 | Python |
| kubeflow | trainer | 2112 | Go |
| kubeflow | katib | 1685 | Python |
| kubeflow | manifests | 1020 | YAML |
| AustinCStone | TextGAN | 92 | Python |
| migalkin | NodePiece | 144 | Python |
| migalkin | StarE | 89 | Python |
| bmorphism | ocaml-mcp-sdk | 61 | OCaml |

### Notable plurigrid repos
- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (420 open issues)
- `plurigrid/nanoclj-zig` — NaN-boxed Clojure interpreter in Zig 0.15, interaction nets, GF(3)
- `plurigrid/asi` — everything is topological chemputer! (25 stars)
- `plurigrid/nash-portal` — NASH token TUI in the browser — ratzilla WASM + GeckoTerminal OHLCV

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) queried on `fullnode.mainnet.aptoslabs.com`.  
**Result:** All 28 wallets have 0 APT balance (no CoinStore resource registered on mainnet).

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793... | 0.0 |
| bob | 0x0a3c... | 0.0 |
| A–Z | 0x8699...–0x7af0... | 0.0 each |

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4... | 2 | ✅ |
| A-G | 0xf56c... | 2 | ✅ |
| Y-Z | 0xd3ff... | 2 | ✅ |
| S-T | 0x3b1c... | 2 | ✅ |
| V-W | 0x40fa... | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-2 signature threshold.**

### MNX Markets (`testnet.mnx.fi`)

HTTP 401 Unauthorized on both `/` and `/api/markets`. MNX testnet requires authentication; no public market data available. `mnx_snapshots` table is empty.

---

## DuckDB Schema Summary

```
world_increments  — 201 rows (GF3-colored increment events)
repo_snapshots    — 1122 rows (GitHub repo metadata)
aptos_snapshots   — 28 rows  (A-Z + alice/bob wallet balances)
multisig_probes   — 5 rows   (2-of-2 multisig health)
mnx_snapshots     — 0 rows   (unavailable: auth required)
```

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent.*
