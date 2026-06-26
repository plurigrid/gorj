# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-26

## Sweep Metadata
- **Date:** 2026-06-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars |
|--------|------|------:|------------:|
| plurigrid | org | 100 | 77 |
| kubeflow | org | 48 | 34,256 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| migalkin | social-graph | 30 | 280 |
| wasita | social-graph | 30 | 6 |
| AustinCStone | social-graph | 30 | 108 |
| kristinezheng | social-graph | 18 | 0 |
| M1shaaa | social-graph | 16 | 0 |
| DJedamski | social-graph | 11 | 7 |
| **TOTAL** | | **437** | **35,997** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|------:|---------|
| kubeflow/kubeflow | 15,744 | — |
| kubeflow/pipelines | 4,156 | Python |
| kubeflow/spark-operator | 3,128 | Python |
| kubeflow/trainer | 2,122 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| kubeflow/community-distribution | 1,028 | YAML |
| kubeflow/arena | 813 | Go |
| kubeflow/kale | 694 | Python |
| kubeflow/mpi-operator | 528 | Go |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 88 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | ~60 | OCaml |

### GF(3) Color Chain Distribution

| Color Name | Trit | Hex | Count |
|-----------|-----:|-----|------:|
| ERGODIC | 0 | #d3869b | 145 |
| PLUS | +1 | #b8bb26 | 146 |
| MINUS | -1 | #cc241d | 146 |

GF(3) rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com`.
**All balances: 0.0 APT** — CoinStore resources not initialized (unfunded/new accounts).

| World | Address (truncated) | APT |
|-------|--------------------|----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.
**All healthy — 2-of-N threshold.**

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|:-------------:|:------:|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel Deployment Protection.
All API paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`) return 403 requiring
authentication bypass token. No market data extractable at this time.

---

## DuckDB Table Counts

| Table | Rows |
|-------|-----:|
| world_increments | 437 |
| repo_snapshots | 437 |
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

## Notable Highlights

- **kubeflow/kubeflow**: 15,744 stars — flagship ML platform for Kubernetes (up from 15,565 in Apr sweep)
- **kubeflow/pipelines**: 4,156 stars — most popular ML pipeline for Kubernetes
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **AustinCStone/TextGAN**: 92 stars — GAN-based text generation
- **TeglonLabs/jank-crane**: newest TeglonLabs repo (2026-06-08) — crane-jank converged-IR hub with GF3 convergence maps
- **Multisig swarm**: All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) active with 2-of-N threshold
- **Hamming wallets**: All 28 addresses at 0.0 APT — accounts not yet funded on mainnet
