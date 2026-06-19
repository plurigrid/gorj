# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-19

## Sweep Metadata
- **Date:** 2026-06-19
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 391 |
| Total Repo Snapshots | 391 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | UNAVAILABLE (Vercel auth) |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| AustinCStone | social-graph | 40 |
| zubyul | user | 49 |
| migalkin | social-graph | 19 |
| wasita | social-graph | 11 |
| M1shaaa | social-graph | 8 |
| DJedamski | social-graph | 6 |
| kristinezheng | social-graph | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **391** |

### Top Repos by Stars

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,736 | 2,680 |
| kubeflow/pipelines | Python | 4,154 | 2,009 |
| kubeflow/spark-operator | Python | 3,127 | 1,490 |
| kubeflow/trainer | Go | 2,116 | 970 |
| kubeflow/katib | Python | 1,683 | 528 |
| kubeflow/examples | Jsonnet | 1,460 | 756 |
| kubeflow/community-distribution | YAML | 1,025 | 1,065 |
| migalkin/NodePiece | Python | 144 | 21 |

### Language Breakdown (top 10)

| Language | Count |
|----------|-------|
| Python | 81 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| Go | 15 |
| HTML | 15 |
| Clojure | 14 |
| Jupyter Notebook | 14 |
| Julia | 9 |
| Zig | 7 |

### Most Recently Pushed (2026)

| Repo | Pushed At |
|------|-----------|
| kubeflow/notebooks | 2026-06-19T16:02:08Z |
| kubeflow/trainer | 2026-06-19T15:46:05Z |
| kubeflow/website | 2026-06-19T15:39:26Z |
| plurigrid/gorj | 2026-06-19T15:11:52Z |
| M1shaaa/M1shaaa | 2026-06-19T14:57:09Z |
| bmorphism/Gay.jl | 2026-06-19T00:48:59Z |

### GF(3) Color Chain

- `id mod 3 == 0` → trit=0, color=#d3869b, **ERGODIC** — 131 increments
- `id mod 3 == 1` → trit=1, color=#b8bb26, **PLUS** — 130 increments
- `id mod 3 == 2` → trit=-1, color=#cc241d, **MINUS** — 130 increments

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

All 28 Hamming swarm addresses (alice, bob, A–Z) queried against Aptos mainnet `fullnode.mainnet.aptoslabs.com`.

**Result: 0.0 APT on all 28 addresses** — no `CoinStore<AptosCoin>` resource found. Addresses exist on-chain but carry no native APT balance at this time.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B–Z | (24 more addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts responded successfully to `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All multisigs healthy — 2-of-N signature policy active on all 5 pairs.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active on all endpoints (`/`, `/api/markets`, `/api/v1/markets`). Requires visitor password or OIDC token. No market data could be extracted.

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
- **kubeflow/kubeflow**: 15,736 stars — flagship ML platform for Kubernetes (pushed today)
- **kubeflow/pipelines**: 4,154 stars — pushed today 2026-06-19
- **kubeflow/trainer**: 2,116 stars — pushed today 2026-06-19
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings
- **TeglonLabs/jank-crane**: GF3 convergence maps + simonw workflow (pushed 2026-06-08)
- **plurigrid/gorj**: This very repo — pushed today 2026-06-19
- **Hamming swarm**: All 28 addresses at 0 APT; all 5 multisigs responding with sigs=2
- **MNX testnet**: Locked behind Vercel auth — market data unavailable this sweep
