# World-Increment Sweep + Hamming Snapshot — 2026-05-12

## Sweep Metadata
- **Date:** 2026-05-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 100 | 72 |
| kubeflow | org | 48 | 34,040 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 100 | 248 |
| zubyul | user | 49 | 14 |
| migalkin | social (zubyul graph) | 5 | 275 |
| DJedamski | social (zubyul graph) | 2 | 1 |
| wasita | social (zubyul graph) | 3 | 3 |
| kristinezheng | social (zubyul graph) | 2 | 0 |
| M1shaaa | social (zubyul graph) | 2 | 0 |
| AustinCStone | social (zubyul graph) | 3 | 103 |
| **TOTAL** | | **318** | **34,758** |

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 106 |
| +1 | `#b8bb26` | PLUS | 106 |
| -1 | `#cc241d` | MINUS | 106 |

### Top 10 Repos by Stars
| Org/User | Repo | Language | Stars | Last Push |
|----------|------|----------|-------|-----------|
| kubeflow | kubeflow | — | 15,629 | 2026-05-07 |
| kubeflow | pipelines | Python | 4,139 | 2026-05-11 |
| kubeflow | spark-operator | Python | 3,125 | 2026-05-12 |
| kubeflow | trainer | Go | 2,097 | 2026-05-12 |
| kubeflow | katib | Python | 1,683 | 2026-05-09 |
| kubeflow | examples | Jsonnet | 1,462 | 2025-04-14 |
| kubeflow | manifests | YAML | 1,016 | 2026-05-08 |
| kubeflow | arena | Go | 810 | 2026-05-07 |
| kubeflow | kale | Python | 686 | 2026-05-11 |
| kubeflow | mpi-operator | Go | 526 | 2026-05-11 |

### Notable plurigrid Repos
- `gorj` (Clojure) — forj + Rama topology nREPL routing + GF(3) trit coloring, 156 open issues
- `zig-syrup` (Zig) — OCapN Syrup with CapTP optimizations, 2★
- `asi` (HTML) — everything is topological chemputer!, 21★
- `nash-portal` (Rust) — NASH token TUI in browser, 2★

### Notable Social Graph Repos
- `migalkin/NodePiece` — 144★ ICLR'22 knowledge graph embeddings
- `migalkin/StarE` — 89★ EMNLP 2020 hyper-relational KG
- `AustinCStone/TextGAN` — 92★ GAN for text generation (TensorFlow)
- `migalkin/NBFNet_mlx` — 10★ Neural Bellman-Ford on Apple Silicon (MLX)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Queried 28 addresses** (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`

**Result:** All 28 addresses returned `resource_not_found` — wallets have not initialized the `0x1::coin::CoinStore<AptosCoin>` resource on mainnet. These addresses are inactive or pre-funded test wallets not yet registered on mainnet.

| World | Status |
|-------|--------|
| alice, bob, A–Z (all 28) | `resource_not_found` (0 APT / uninitiated) |

### Multisig Contract Probes (Aptos Mainnet)
**All 5 multisig contracts healthy — require 2-of-N signatures.**

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...7883` | 2 | ✓ |
| V-W | `0x40fad7b4...eb6d` | 2 | ✓ |

### MNX Markets (`testnet.mnx.fi`)
**Status: Unavailable via API** — site is a Next.js SPA; all routes (`/api/markets`, `/api/v1/markets`, `/_next/data/...`) redirect to the client-side bundle with no extractable JSON market data. Noted as `ticker=N/A, category=SPA-no-API` in `mnx_snapshots`.

---

## DuckDB Schema Summary
```
world_increments  318 rows  (GF3-colored repo events, 1 per repo)
repo_snapshots    318 rows  (full metadata per repo)
aptos_snapshots    28 rows  (all resource_not_found on mainnet)
multisig_probes     5 rows  (all healthy, 2-of-N)
mnx_snapshots       1 row   (SPA unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
