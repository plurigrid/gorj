# World-Increment Sweep + Hamming Snapshot — 2026-07-30

## Sweep Metadata
- **Date:** 2026-07-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 352 |
| Total Repo Snapshots (cumulative) | 1,273 |
| New Repo Snapshots This Run | 329 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — This Run (329 increments)

| GF3 Name | Color | Trit | Count (this run) |
|----------|-------|:----:|:----------------:|
| ERGODIC | `#d3869b` | 0 | 109 |
| PLUS | `#b8bb26` | +1 | 110 |
| MINUS | `#cc241d` | -1 | 110 |

Assignment: `id mod 3 == 0 → ERGODIC, id mod 3 == 1 → PLUS, id mod 3 == 2 → MINUS`

---

## Top Repos by Stars (across ducklake)

| Repo | Stars | Language |
|------|------:|----------|
| kubeflow/kubeflow | 15,798 | — |
| kubeflow/pipelines | 4,171 | Python |
| kubeflow/spark-operator | 3,142 | Python |
| kubeflow/trainer | 2,163 | Go |
| kubeflow/katib | 1,694 | Python |
| kubeflow/examples | 1,461 | Jsonnet |
| kubeflow/community-distribution | 1,029 | YAML |
| kubeflow/manifests | 1,010 | YAML |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| kubeflow/arena | 815 | Go |
| migalkin/kgcourse2021 | 24 | HTML |
| AustinCStone/StereoVisionMRF | 11 | Python |
| migalkin/NBFNet_mlx | 10 | Python |

## Notable Updates (2026-07-30)
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"
- **wasita/wasita.github.io** (Svelte, pushed 2026-07-21): personal site most recently updated
- **AustinCStone/byteruckus** (HTML, pushed 2026-07-15): newest repo in AustinCStone graph
- **kristinezheng/kristinezheng.github.io** (HTML, pushed 2026-07-01): recent activity

## Repo Counts This Run (329 new snapshots)

| Source | Type | Repos |
|--------|------|-------|
| kubeflow | org | 49 |
| plurigrid | org | 100 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 12 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 25 |
| **TOTAL** | | **378 queried / 329 inserted** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 wallets probed via `fullnode.mainnet.aptoslabs.com`. Sleep 1s between calls.

| Result | Count |
|--------|------:|
| Balance = 0 APT | 28 |
| Balance > 0 APT | 0 |

All 28 addresses (alice, bob, A–Z) show 0 APT. The `0x1::coin::CoinStore<AptosCoin>` resource is not present on any address on mainnet — these appear to be unfunded identity/testnet addresses.

### Multisig Contract Probes
| Pair | Address | Sigs Required | Status |
|------|---------|:-------------:|--------|
| A-B | 0x0da4f428...4987003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9...d7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b4...0eb6d | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ healthy |

All 5 multisig accounts are 2-of-N, responding normally. **No unhealthy contracts.**

### MNX Markets (testnet.mnx.fi)
The site is a Next.js SPA. No REST `/api/markets` endpoint is accessible without browser JS execution. `mnx_snapshots` table: **0 rows** (data unavailable).

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## DuckDB Ducklake State
| Table | Rows (cumulative) |
|-------|:-----------------:|
| world_increments | 352 |
| repo_snapshots | 1,273 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

## Notable Highlights
- **kubeflow/kubeflow**: 15,798 stars (↑233 since 2026-04-12 sweep) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,171 stars (↑52) — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,142 stars (↑31) — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 144 stars (↑1) — scalable knowledge graph embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — TF text generation GAN, still active
- **TeglonLabs/jank-crane**: New C++ repo with GF3 convergence maps theme
- **All 5 multisig contracts**: healthy, sigs_required=2
- **All 28 Aptos wallets**: 0 APT on mainnet (unfunded identity addresses)
