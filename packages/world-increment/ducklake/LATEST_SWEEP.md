# World-Increment Sweep + Aptos Hamming Snapshot

**Timestamp:** 2026-05-15 (sweep executed)
**DuckDB:** v1.5.2 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Social Graph Sweep

### Repos by Source

| Source | Type | Repos Swept |
|--------|------|-------------|
| plurigrid | org | 20 |
| kubeflow | org | 20 |
| bmorphism | user | 20 |
| TeglonLabs | org | 4 |
| zubyul | user | 6 |
| migalkin | user | 8 |
| DJedamski | user | 6 |
| wasita | user | 5 |
| kristinezheng | user | 5 |
| M1shaaa | user | 4 |
| AustinCStone | user | 7 |
| **TOTAL** | | **105** |

### World Increments — GF(3) Color Chain Distribution

| GF(3) Trit | Name | Color | Count |
|------------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 35 |
| 1 | PLUS | `#b8bb26` | 35 |
| -1 | MINUS | `#cc241d` | 35 |
| **Total** | | | **105** |

GF(3) chain is perfectly balanced (modular arithmetic over 105 = 35 x 3).

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,632 | — |
| kubeflow/pipelines | 4,140 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,098 | Go |
| kubeflow/katib | 1,682 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 23 | HTML |

---

## Aptos Hamming Swarm Snapshot

All 28 addresses queried against Aptos mainnet fullnode (`fullnode.mainnet.aptoslabs.com`).
All wallets returned 0 APT balance (accounts uninitialized or no APT CoinStore resource on mainnet).

| World Label | Address (truncated) | APT Balance |
|-------------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...d7a | 0.0 |
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
| Q | 0xac40...9a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

---

## Multisig Contract Probes

All 5 multisig contracts responded successfully with 2 signatures required.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...b6d | 2 | true |

All multisig accounts are healthy (2-of-N threshold confirmed on mainnet).

---

## MNX Markets

Status: **Unavailable** — `https://testnet.mnx.fi/api/markets` returns HTML (Next.js frontend), not JSON API data. No market data recorded.

---

## DuckDB Record Summary

| Table | Records |
|-------|---------|
| world_increments | 105 |
| repo_snapshots | 105 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
| **Total** | **243** |

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,632 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,140 stars — most popular ML pipeline for Kubernetes
- **migalkin/NodePiece**: 144 stars — ICLR'22 compositional knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs (TensorFlow)
- **plurigrid/asi**: 23 stars — everything is topological chemputer
- **plurigrid/nanoclj-zig**: GF(3) trit conservation in Zig — directly on-theme for this sweep
- All 5 Hamming multisig contracts healthy with 2-of-N threshold on Aptos mainnet
