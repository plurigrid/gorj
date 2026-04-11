# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-04-11
**Agent:** world-increment-sweep + hamming-swarm-snapshot
**DuckDB version:** v1.5.1 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources
| Source | Type | Repos snapshotted | Stars |
|---|---|---|---|
| kubeflow | org | 11 | 28,577 |
| migalkin | social (zubyul graph) | 3 | 241 |
| bmorphism | user | 7 | 139 |
| AustinCStone | social (zubyul graph) | 2 | 103 |
| plurigrid | org | 20 | 54 |
| zubyul | user | 5 | 3 |
| TeglonLabs | org | 4 | 2 |
| wasita | social (zubyul graph) | 3 | 1 |
| DJedamski | social (zubyul graph) | 1 | 1 |
| kristinezheng | social (zubyul graph) | 1 | 0 |
| M1shaaa | social (zubyul graph) | 1 | 0 |
| **TOTAL** | | **58** | **29,121** |

### Most Recently Pushed (top 10)
| repo | stars | lang | pushed_at |
|---|---|---|---|
| plurigrid/horse | 1 | TeX | 2026-04-11T07:07Z |
| plurigrid/gorj | 0 | Clojure | 2026-04-11T06:41Z |
| kubeflow/pipelines | 4,119 | Python | 2026-04-11T04:43Z |
| kubeflow/model-registry | 172 | Go | 2026-04-10T22:07Z |
| kubeflow/spark-operator | 3,111 | Python | 2026-04-10T18:21Z |
| kubeflow/sdk | 102 | Python | 2026-04-10T16:34Z |
| kubeflow/notebooks | 70 | — | 2026-04-10T14:09Z |
| kubeflow/trainer | 2,080 | Go | 2026-04-10T13:35Z |
| plurigrid/web-browser | 0 | Rust | 2026-04-10T02:54Z |
| plurigrid/asi | 16 | HTML | 2026-04-10T02:37Z |

### GF(3) Trit Distribution (58 increments)
| trit | name | color | count |
|---|---|---|---|
| 0 | ERGODIC | #d3869b | 19 |
| +1 | PLUS | #b8bb26 | 20 |
| -1 | MINUS | #cc241d | 19 |

GF(3) chain balanced: 19 ERGODIC · 20 PLUS · 19 MINUS across 58 world increments.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z · 28 addresses)

All 28 addresses probed via `fullnode.mainnet.aptoslabs.com` with 1s sleep between calls.
All returned **0.0 APT** — `CoinStore` resource absent (accounts not funded on mainnet).

| world | address | balance APT |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D–Z | (see aptos_snapshots table) | 0.0 each |

### Multisig Contract Probes (5 pairs)

Probed via `0x1::multisig_account::num_signatures_required` on Aptos mainnet.

| pair | address | sigs_required | healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts healthy — 2-of-N threshold confirmed on-chain.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` returns a Next.js SPA shell at all probed API paths
(`/api/markets`, `/api/v1/markets`). No market data extractable without
JavaScript execution. Status: **unavailable / SPA**. Recorded in `mnx_snapshots`.

---

## DuckDB Tables
| table | rows |
|---|---|
| world_increments | 58 |
| repo_snapshots | 58 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/pipelines**: 4,119 stars — ML Pipelines for Kubernetes, pushed today
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes Spark operator
- **kubeflow/trainer**: 2,080 stars — Distributed AI Model Training
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street oxcaml_effect
- **migalkin/NodePiece**: 143 stars — Compositional KG representations (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — GAN for text generation in TensorFlow
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL + GF(3) trit coloring
- **plurigrid/nanoclj-zig**: NaN-boxed Clojure in Zig 0.15 with GF(3) trit conservation
- All 5 Hamming swarm multisig pairs: **healthy**, sigs_required=2
