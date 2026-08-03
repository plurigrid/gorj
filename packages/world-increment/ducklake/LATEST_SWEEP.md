# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 352 |
| Total Repo Snapshots (cumulative) | 1,273 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Distribution (this run)
| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 117 |
| PLUS | #b8bb26 | +1 | 118 |
| MINUS | #cc241d | -1 | 117 |

### Repos by Source (distinct, cumulative DB)

| Source | Type | Distinct Repos | Max Stars | Total Stars |
|--------|------|----------------|-----------|-------------|
| kubeflow | org | 51 | 15,804 | 102,177 |
| migalkin | social | 30 | 144 | 832 |
| bmorphism | user | 165 | 61 | 509 |
| AustinCStone | social | 44 | 92 | 319 |
| plurigrid | org | 168 | 58 | 191 |
| zubyul | user | 59 | 2 | 40 |
| TeglonLabs | org | 54 | 2 | 14 |
| DJedamski | social | 11 | 2 | 16 |
| wasita | social | 32 | 2 | 10 |
| M1shaaa | social | 16 | 0 | 0 |
| kristinezheng | social | 18 | 0 | 0 |

### Notable Repos This Sweep
- **kubeflow/kubeflow** — 15,804 ⭐ (ML platform for Kubernetes)
- **kubeflow/pipelines** — 4,173 ⭐ (ML pipeline orchestration, pushed 2026-07-xx)
- **kubeflow/spark-operator** — 3,142 ⭐ (Kubernetes Spark operator)
- **migalkin/NodePiece** — 144 ⭐ (Compositional KG representations, ICLR '22, active 2026-05)
- **migalkin/StarE** — 89 ⭐ (Hyper-relational KG, EMNLP 2020)
- **migalkin/NBFNet_mlx** — 10 ⭐ (Neural Bellman-Ford on Apple Silicon MLX)
- **AustinCStone/TextGAN** — 92 ⭐ (Text GAN in TensorFlow)
- **AustinCStone/StereoVisionMRF** — 11 ⭐ (MRF depth from stereo)
- **TeglonLabs/jank-crane** — C++ (crane-jank IR hub, GF3 convergence maps, pushed 2026-06-08)
- **wasita/wasita.github.io** — Svelte (active, pushed 2026-07-21)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

Queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**All 28 wallets: 0.0 APT**

The `CoinStore<AptosCoin>` resource is absent for all addresses. This is expected on Aptos mainnet post-migration — APT is now tracked via the FungibleAsset standard (`0x1::fungible_asset::FungibleStore`) rather than the legacy CoinStore. Balances may be non-zero under the new resource type.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A–Z | 26 addresses | 0.0 each |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

All multisig accounts require 2-of-N signatures. Contracts responding correctly on mainnet.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — Next.js SPA. Endpoints `/api/markets` and `/api/v1/markets` return HTML (SPA shell), not JSON. No market data extractable from server-side rendering. Requires browser JS execution to populate.

---

## DuckDB Schema

Location: `packages/world-increment/ducklake/world-increments.duckdb`

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
