# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-10  **Agent:** world-increment-sweep + hamming-swarm-snapshot
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.4)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Snapshotted | Top Stars |
|--------|------|-------------------|-----------|
| plurigrid | org | 100 | asi (30★), vcg-auction (7★), agent (5★) |
| kubeflow | org | 29 | kubeflow/kubeflow (15,772★), pipelines (4,169★), spark-operator (3,136★) |
| TeglonLabs | org | 5 | mathpix-gem (2★), jank-crane (0★) |
| bmorphism | user | 50 | ocaml-mcp-sdk (61★), anti-bullshit-mcp-server (23★) |
| zubyul | user | 49 | WGCNA (2★), jonikas_lab (2★), gay-world (1★) |
| migalkin | user | 19 | NodePiece (144★), StarE (89★), NBFNet_mlx (10★) |
| DJedamski | user | 6 | Getting-and-Cleaning-Data (1★), Kaggle (1★) |
| AustinCStone | user | 40 | TextGAN (92★), StereoVisionMRF (11★) |

**Total repos snapshotted this run:** 298

### Notable Activity (pushed 2026-07-10)
- **plurigrid/gorj**: forj + Rama topology nREPL routing + GF(3) gay trit coloring — 1,107 open issues
- **plurigrid/asi**: everything is topological chemputer! — 30★, pushed today
- **kubeflow/hub** (21:46Z): Model Registry for ML model developers — 177★
- **kubeflow/pipelines** (20:07Z): Machine Learning Pipelines — 4,169★
- **bmorphism/Gay.jl** (00:34Z): Wide-gamut color sampling with splittable determinism — 187 open issues

### Recent Highlights
- **kubeflow/kubeflow**: 15,772★ — flagship ML toolkit for Kubernetes
- **kubeflow/spark-operator**: 3,136★ — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 144★ — Compositional KG representations (ICLR'22)
- **AustinCStone/TextGAN**: 92★ — GAN-based text generation (TensorFlow)
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml MCP SDK via Jane Street oxcaml_effect
- **TeglonLabs/jank-crane** (2026-06-08): crane-jank converged-IR hub with GF3 convergence maps

### GF(3) Color Chain — This Run
| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1 | plurigrid (org) | 0 | `#d3869b` | ERGODIC |
| 2 | kubeflow (org) | 1 | `#b8bb26` | PLUS |
| 3 | TeglonLabs (org) | 2 | `#cc241d` | MINUS |
| 4 | bmorphism (user) | 0 | `#d3869b` | ERGODIC |
| 5 | zubyul (user) | 1 | `#b8bb26` | PLUS |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-10)
Queried via `fullnode.mainnet.aptoslabs.com` — all 28 wallets (alice, bob, A–Z).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|--------------|
| alice | 0xc793ac... | 0.00 |
| bob | 0x0a3c00... | 0.00 |
| A | 0x8699ed... | 0.00 |
| B–Z | (24 addrs) | 0.00 each |

**All 28 wallets: CoinStore resource not initialized (accounts unfunded)**
**Total APT across swarm: 0.00 APT**

### Multisig Contract Probes — 5/5 HEALTHY
| Pair | Contract Address (prefix) | Sigs Required | Status |
|------|--------------------------|--------------|--------|
| A-B | 0x0da4f4... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3a... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7... | 2 | ✓ HEALTHY |

All 5 multisig contracts respond with `num_signatures_required = 2`. **100% healthy.**

### MNX Markets (testnet.mnx.fi)
**Status: 401 Unauthorized** — Vercel-hosted SPA, auth required.
Endpoints probed: `/api/markets`, `/api/tickers`, `/api/v1/markets` — all 401.
No public market data available; `mnx_snapshots` table remains empty this run.

---

## DuckDB Table Counts (cumulative)
| Table | Rows |
|-------|------|
| world_increments | 28 |
| repo_snapshots | 999 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

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
