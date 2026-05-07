# World Increment Sweep + Hamming Snapshot

**Sweep timestamp:** 2026-05-07T17:30:00Z  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Unique Repos | Total Stars |
|--------|------|-------------|-------------|
| kubeflow | org | 47 | 98,880 |
| migalkin | user (zubyul social) | 30 | 832 |
| bmorphism | user | 108 | 419 |
| AustinCStone | user (zubyul social) | 43 | 323 |
| plurigrid | org | 103 | 124 |
| zubyul | user | 29 | 27 |
| DJedamski | user (zubyul social) | 11 | 17 |
| TeglonLabs | org | 53 | 14 |
| wasita | user (zubyul social) | 32 | 10 |
| M1shaaa | user (zubyul social) | 16 | 0 |
| kristinezheng | user (zubyul social) | 18 | 0 |

**Total unique repos captured:** 493 across 11 orgs/users

### Notable Repos (by stars)
- **kubeflow/kubeflow** — 15,625 ★ — Machine Learning Toolkit for Kubernetes
- **kubeflow/pipelines** — 4,136 ★ — Machine Learning Pipelines
- **kubeflow/spark-operator** — 3,124 ★ — Kubernetes operator for Apache Spark
- **migalkin/NodePiece** — 144 ★ — Compositional KG representations (ICLR'22)
- **AustinCStone/TextGAN** — 92 ★ — GAN for text generation in TensorFlow
- **migalkin/StarE** — 89 ★ — Message Passing for Hyper-Relational KGs (EMNLP'20)
- **bmorphism/ocaml-mcp-sdk** — 60 ★ — OCaml SDK for Model Context Protocol
- **plurigrid/asi** — 21 ★ — everything is topological chemputer!
- **bmorphism/say-mcp-server** — 20 ★ — MCP server for macOS text-to-speech
- **plurigrid/gorj** — 0 ★, 100 issues — forj + Rama + GF(3) gay trit coloring (this repo!)

### GF(3) Color Chain Distribution (this sweep)
| GF(3) Name | Trit | Color | Count |
|------------|------|-------|-------|
| ERGODIC | 0 | #d3869b | 34 |
| PLUS | +1 | #b8bb26 | 36 |
| MINUS | -1 | #cc241d | 36 |

### DuckDB Tables
- **world_increments**: 106 rows (this sweep: 83 repo events)
- **repo_snapshots**: 1,027 rows (cumulative across sweeps)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Hamming Swarm)
All 28 addresses (alice, bob, A-Z) returned **null** — no APT CoinStore resource found.
These accounts do not have an initialized APT CoinStore on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…cc7b | null |
| bob | 0x0a3c…512d | null |
| A | 0x8699…9d7a | null |
| B | 0x3f89…b13 | null |
| C | 0x38b9…35e | null |
| D | 0xf776…dd1 | null |
| E | 0xdc1d…d36 | null |
| F | 0x18a1…f71 | null |
| G | 0x69a3…f32 | null |
| H | 0xce67…00f | null |
| I | 0x070f…fc9 | null |
| J | 0x4d96…f54 | null |
| K | 0xa732…dc4 | null |
| L | 0x7c2e…ba9 | null |
| M | 0x6fed…e9 | null |
| N | 0xe7dd…b2c | null |
| O | 0x7325…89d | null |
| P | 0x6218…948 | null |
| Q | 0xac40…9a9 | null |
| R | 0x7ce6…e10 | null |
| S | 0xb875…386 | null |
| T | 0x3578…588 | null |
| U | 0x7586…956 | null |
| V | 0xb59d…2c3 | null |
| W | 0x5f32…b0 | null |
| X | 0xa95c…47d | null |
| Y | 0xd8e3…4c4 | null |
| Z | 0x7af0…97c | null |

### Multisig Contract Probes
All 5 multisig contracts are **healthy** — each requires **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…003 | 2 | true |
| A-G | 0xf56c…096 | 2 | true |
| Y-Z | 0xd3ff…883 | 2 | true |
| S-T | 0x3b1c…883 | 2 | true |
| V-W | 0x40fa…b6d | 2 | true |

### MNX Markets (testnet.mnx.fi)
**Status:** Unavailable — `testnet.mnx.fi` serves a Single Page Application (SPA).
API paths `/api/markets` and `/api/v1/markets` returned empty responses.
Market data not captured; recorded as unavailable in `mnx_snapshots` table.

---

## Storage
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Tables:** `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
- **Sequences:** `increment_seq`, `repo_seq`
