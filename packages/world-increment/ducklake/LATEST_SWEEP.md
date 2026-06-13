# World-Increment Sweep + Hamming Snapshot — 2026-06-13

## Sweep Metadata
- **Date:** 2026-06-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 271 |
| Total Repo Snapshots | 271 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 50 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social (zubyul graph) | 5 |
| wasita | social (zubyul graph) | 5 |
| AustinCStone | social (zubyul graph) | 3 |
| DJedamski | social (zubyul graph) | 2 |
| kristinezheng | social (zubyul graph) | 2 |
| M1shaaa | social (zubyul graph) | 2 |
| **Total** | | **271** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,720 | Jupyter Notebook |
| kubeflow/pipelines | 4,152 | Python |
| kubeflow/spark-operator | 3,127 | Go |
| kubeflow/trainer | 2,112 | Python |
| kubeflow/katib | 1,683 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 90 |
| 1 | `#b8bb26` | PLUS | 91 |
| -1 | `#cc241d` | MINUS | 90 |

Chain pattern per increment id: `id%3==0→ERGODIC, id%3==1→PLUS, id%3==2→MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-13)

All 28 addresses (alice, bob, A–Z) returned **0.0 APT** — accounts either inactive, unfunded, or CoinStore resource not registered at time of snapshot.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (see DB) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts responded with `sigs_required = 2`. Status: **ALL HEALTHY**.

| Pair | Contract Address | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — all API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets`) returned HTTP 401 (authentication required). No market data inserted.

---

## DuckDB Schema

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
- **kubeflow/kubeflow**: 15,720 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,152 stars — most popular Kubernetes ML pipeline (pushed 2026-06-13)
- **migalkin/NodePiece**: 144 stars — compositional knowledge graph embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs (TensorFlow)
- **TeglonLabs/jank-crane**: C++ converged-IR hub with GF3 convergence maps (pushed 2026-06-08)
- **All 5 multisigs**: sigs_required=2, live on Aptos mainnet
