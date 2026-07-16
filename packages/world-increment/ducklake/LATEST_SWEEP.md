# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-16

## Sweep Metadata
- **Date:** 2026-07-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 405 |
| Total Repo Snapshots | 1,326 |
| Aptos Snapshots | 28 |
| Multisig Probes | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | ~100 |
| kubeflow | org | ~100 |
| TeglonLabs | org | 5 |
| bmorphism | user | ~100 |
| zubyul | user | ~100 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 11 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8+ |
| AustinCStone | social graph | 30 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,779 | — |
| kubeflow/pipelines | 4,167 | Python |
| kubeflow/spark-operator | 3,137 | Go |
| kubeflow/trainer | 2,150 | Python |
| kubeflow/katib | 1,690 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| TeglonLabs/mathpix-gem | 2 | Ruby |
| TeglonLabs/jank-crane | 0 | C++ |

### Language Distribution (top 10)

| Language | Repos |
|----------|-------|
| Python | 231 |
| Rust | 57 |
| HTML | 54 |
| JavaScript | 52 |
| Go | 51 |
| TypeScript | 46 |
| Jupyter Notebook | 40 |
| Clojure | 30 |
| Jsonnet | 23 |
| R | 22 |

### GF(3) World Increment Chain

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 135 |
| +1 | PLUS | #b8bb26 | 135 |
| -1 | MINUS | #cc241d | 135 |

GF(3) rule: `id mod 3 == 0` → ERGODIC | `id mod 3 == 1` → PLUS | `id mod 3 == 2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — 28 Addresses (alice, bob, A–Z)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`. Every account
returned `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>`.
Accounts are active (alice has sequence_number=72) but use the fungible asset
standard — no legacy CoinStore. Balances recorded as NULL.

| Address | World | Balance |
|---------|-------|---------|
| 0xc793...cc7b | alice | null (FA standard) |
| 0x0a3c...12d5 | bob | null (FA standard) |
| 0x8699...9d7a | A | null (FA standard) |
| 0x3f89...b13 | B | null (FA standard) |
| … (C–Z) | C–Z | null (FA standard) |

### Multisig Contract Probes — All Healthy

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 multisig contracts healthy — all require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

Status: **Authentication Required** — `https://testnet.mnx.fi/api/markets`
returns SPA HTML with auth gate. No market data accessible without credentials.
0 rows written to `mnx_snapshots`.

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
- **kubeflow/kubeflow**: 15,779 stars — flagship ML platform for Kubernetes
- **migalkin/NodePiece**: 144 stars — compositional knowledge graph representations (EMNLP)
- **AustinCStone/TextGAN**: 92 stars — TensorFlow GAN for text generation
- **TeglonLabs/jank-crane**: newest TeglonLabs repo (2026-06-08) — C++ crane-jank converged-IR hub with GF3 convergence maps
- **M1shaaa/M1shaaa**: pushed 2026-07-16T02:13 — most recently active social graph account
- **Aptos multisig**: all 5 contracts (A-B, A-G, Y-Z, S-T, V-W) healthy with 2-sig threshold
- **Aptos wallets**: all accounts active on mainnet but use fungible asset standard; legacy CoinStore not initialized
