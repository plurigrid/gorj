# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-09

## Sweep Metadata
- **Date:** 2026-06-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 37 |
| Total Repo Snapshots | 1,100 |
| New Repo Snapshots (this sweep) | ~156 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Orgs & Users Queried
| Source | Type | Repos This Sweep | Notable |
|--------|------|-----------------|---------|
| plurigrid | org | 50 | asi 25★, ontology 8★, gorj 454 open issues |
| kubeflow | org | 48 | kubeflow/kubeflow 15,710★, pipelines 4,153★, spark-operator 3,126★ |
| TeglonLabs | org | 5 | mathpix-gem, topoi, jank-crane, monad-mcp-server, coin-flip-mcp |
| bmorphism | user | 15 | ocaml-mcp-sdk 61★, anti-bullshit-mcp-server 23★, Gay.jl 189 open issues |
| zubyul | user | 10 | WGCNA 2★, gay-world 1★ |
| migalkin | user | 5 | NodePiece 144★, StarE 89★ |
| DJedamski | user | 4 | all ≤1★ |
| wasita | user | 6 | magic-garden 2★ |
| kristinezheng | user | 4 | all 0★ |
| M1shaaa | user | 4 | all 0★ |
| AustinCStone | user | 5 | TextGAN 92★, StereoVisionMRF 11★ |

### Repo Counts by Source (All Sweeps)
| Source | Type | Total Rows |
|--------|------|-----------|
| plurigrid | org | 250 |
| bmorphism | user | 215 |
| kubeflow | org | 142 |
| TeglonLabs | org | 111 |
| AustinCStone | user | 91 |
| wasita | user | 66 |
| migalkin | user | 65 |
| zubyul | user | 58 |
| kristinezheng | user | 40 |
| M1shaaa | user | 36 |
| DJedamski | user | 26 |
| **TOTAL** | | **1,100** |

---

## GF(3) Color Chain — This Sweep (IDs 13–26)

| ID | trit | Name | Color | Source | Event |
|----|------|------|-------|--------|-------|
| 13 | 1 | PLUS | `#b8bb26` | plurigrid | repo_sweep |
| 14 | -1 | MINUS | `#cc241d` | kubeflow | repo_sweep |
| 15 | 0 | ERGODIC | `#d3869b` | TeglonLabs | repo_sweep |
| 16 | 1 | PLUS | `#b8bb26` | bmorphism | repo_sweep |
| 17 | -1 | MINUS | `#cc241d` | zubyul | repo_sweep |
| 18 | 0 | ERGODIC | `#d3869b` | migalkin | repo_sweep |
| 19 | 1 | PLUS | `#b8bb26` | DJedamski | repo_sweep |
| 20 | -1 | MINUS | `#cc241d` | wasita | repo_sweep |
| 21 | 0 | ERGODIC | `#d3869b` | kristinezheng | repo_sweep |
| 22 | 1 | PLUS | `#b8bb26` | M1shaaa | repo_sweep |
| 23 | -1 | MINUS | `#cc241d` | AustinCStone | repo_sweep |
| 24 | 0 | ERGODIC | `#d3869b` | hamming_swarm | aptos_snapshot |
| 25 | 1 | PLUS | `#b8bb26` | multisig | multisig_probe |
| 26 | -1 | MINUS | `#cc241d` | mnx | mnx_probe |

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, ERGODIC #d3869b
- `id mod 3 == 1` → trit=1, PLUS #b8bb26
- `id mod 3 == 2` → trit=-1, MINUS #cc241d

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 addresses)
- **Network:** `https://fullnode.mainnet.aptoslabs.com/v1`
- **Result:** All 28 addresses — `resource_not_found` → balance_apt = 0.0
- Accounts: alice, bob, A–Z (Hamming swarm canonical set)
- Status: All accounts unfunded on mainnet as of 2026-06-09

**aptos_snapshots rows inserted:** 28

### Multisig Contract Probes (5 pairs)
- **Function:** `0x1::multisig_account::num_signatures_required`

| Pair | Sigs Required | Healthy |
|------|--------------|---------|
| A-B | 2 | ✓ |
| A-G | 2 | ✓ |
| S-T | 2 | ✓ |
| V-W | 2 | ✓ |
| Y-Z | 2 | ✓ |

**multisig_probes rows inserted:** 5

### MNX Market Data
- **Endpoint:** `https://testnet.mnx.fi`
- **Result:** Unavailable — Vercel authentication gate (403)
- **mnx_snapshots:** 0 rows inserted this sweep

---

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,710 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,153 stars — most active ML pipeline (pushed 2026-06-09)
- **kubeflow/spark-operator**: 3,126 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 25 stars — topological chemputer
- **plurigrid/gorj**: This very repo — MCP server + hooks for AI coding agents
- **Increment 26**: MINUS — sweep closing at GF(3) trit=-1 (mnx_probe)
