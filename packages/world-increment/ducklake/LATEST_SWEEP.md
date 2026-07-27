# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Crawled

| Source | Type | Unique Repos | Max Stars |
|--------|------|-------------|-----------|
| plurigrid | org | 168 | 52 |
| bmorphism | user | 165 | 61 |
| kubeflow | org | 51 | 15,793 |
| TeglonLabs | org | 54 | 2 |
| zubyul | user | 59 | 2 |
| migalkin | social graph | 30 | 144 |
| AustinCStone | social graph | 44 | 92 |
| wasita | social graph | 31 | 2 |
| DJedamski | social graph | 11 | 2 |
| kristinezheng | social graph | 18 | 0 |
| M1shaaa | social graph | 16 | 0 |
| **Total** | | **647** | |

### Most Active Repos (2026-07-27)

| Repo | Pushed At |
|------|-----------|
| kubeflow/hub | 2026-07-27T18:24:01Z |
| plurigrid/gorj | 2026-07-27T18:15:25Z ← **this run** |
| kubeflow/pipelines | 2026-07-27T17:55:22Z |
| kubeflow/dashboard | 2026-07-27T15:59:25Z |
| kubeflow/mcp-server | 2026-07-27T14:47:39Z |
| kubeflow/community-distribution | 2026-07-27T14:14:00Z |
| kubeflow/mpi-operator | 2026-07-27T13:02:54Z |
| bmorphism/Gay.jl | 2026-07-27T02:46:40Z |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 107 |
| +1 | `#b8bb26` | PLUS | 107 |
| -1 | `#cc241d` | MINUS | 107 |

**321 world_increments** — balanced GF(3) color chain

### Notable Repos

- **kubeflow/kubeflow** — 15,793 ★ — Kubernetes ML platform
- **kubeflow/pipelines** — 4,171 ★ — ML Pipelines
- **kubeflow/spark-operator** — 3,142 ★ — Kubernetes Spark operator
- **migalkin/NodePiece** — 144 ★ — Knowledge Graph embeddings (ICLR'22)
- **migalkin/StarE** — 89 ★ — Hyper-Relational KG (EMNLP'20)
- **AustinCStone/TextGAN** — 92 ★ — TensorFlow text generation GAN
- **TeglonLabs/jank-crane** — GF3 convergence maps (pushed 2026-06-08)
- **plurigrid/gorj** — This repo — forj MCP + Hamming swarm

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 total)

**Status: All 28 wallets returned resource_not_found (HTTP 404)**

The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource is absent
at ledger version ~6,481,979,486 for all probed addresses. These accounts
likely use the FungibleAsset standard or have not been initialized with APT.

All balances recorded as `NULL` in `aptos_snapshots`.

### Multisig Contract Probes — 5/5 Healthy

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✓ |
| V-W | 0x40fad7b423a84365... | 2 | ✓ |

All 5 multisig contracts respond with `num_signatures_required = 2`.

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no REST API accessible**

`GET /api/markets` returns Next.js HTML (HTTP 200). The site is a
client-rendered SPA; market data is fetched client-side and not exposed
via public REST endpoints. `mnx_snapshots` table has 0 rows.

---

## DuckDB Tables

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 344 | GF3-tagged repo events |
| `repo_snapshots` | 1265 | Repo metadata with full provenance |
| `aptos_snapshots` | 28 | Wallet balance probes (all NULL — CoinStore absent) |
| `multisig_probes` | 5 | Multisig threshold probes (all 2-of-2, healthy) |
| `mnx_snapshots` | 0 | MNX markets (SPA, data unavailable) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
