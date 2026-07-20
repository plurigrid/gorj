# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-20

## Sweep Metadata
- **Date:** 2026-07-20 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 10 (top by stars) |
| TeglonLabs | org | 4 |
| zubyul | user (social) | 6 |
| migalkin | user (social) | 3 |
| AustinCStone | user (social) | 2 |
| wasita | user (social) | 2 |
| kristinezheng | user (social) | 1 |
| M1shaaa | user (social) | 1 |
| DJedamski | user (social) | 1 |
| **Total this sweep** | | **230 repos** |

### Top Repos by Stars (This Sweep)
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,785 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,169 | Python | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,140 | Python | Apache Spark on Kubernetes |
| kubeflow/trainer | 2,152 | Go | Distributed AI Training + LLM Fine-Tuning |
| kubeflow/katib | 1,691 | Python | Automated ML on Kubernetes |
| migalkin/NodePiece | 144 | Python | Representations for Large Knowledge Graphs (ICLR'22) |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| migalkin/StarE | 89 | Python | Message Passing for Hyper-Relational KGs (EMNLP 2020) |
| plurigrid/asi | 31 | HTML | everything is topological chemputer! |
| migalkin/kgcourse2021 | 24 | HTML | Knowledge Graphs course materials |
| bmorphism/Gay.jl | 2 | Julia | Wide-gamut color sampling with splittable determinism |

### Recently Active (pushed 2026-07)
| Repo | Pushed | Open Issues |
|------|--------|-------------|
| plurigrid/gorj | 2026-07-20 | 1,273 |
| kubeflow/kubeflow | 2026-07-20 | 0 |
| bmorphism/Gay.jl | 2026-07-20 | 187 |
| kubeflow/community-distribution | 2026-07-20 | 26 |
| wasita/wasita.github.io | 2026-07-16 | 8 |
| AustinCStone/byteruckus | 2026-07-15 | 0 |

### GF(3) Color Chain (IDs 24–253, this sweep)
- id%3==0 → trit=0 **ERGODIC** `#d3869b` (~77 increments)
- id%3==1 → trit=1 **PLUS** `#b8bb26` (~77 increments)
- id%3==2 → trit=-1 **MINUS** `#cc241d` (~76 increments)

### DuckDB State After Sweep
| Table | Total Rows | New This Sweep |
|-------|-----------|----------------|
| world_increments | 253 | 230 |
| repo_snapshots | 1,174 | 230 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 Hamming-world addresses (alice, bob, A–Z) queried via Aptos fullnode mainnet API.

**Result: All 28 addresses returned 0.0 APT balance.**

Balances are zero either because these addresses hold assets in other coin types / modules, or because the `CoinStore<AptosCoin>` resource is not registered for these accounts on mainnet.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...7b | 0.0 |
| bob | 0x0a3c...5d | 0.0 |
| A | 0x8699...7a | 0.0 |
| B | 0x3f89...13 | 0.0 |
| C | 0x38b9...5e | 0.0 |
| D | 0xf776...d1 | 0.0 |
| E | 0xdc1d...36 | 0.0 |
| F | 0x18a1...71 | 0.0 |
| G | 0x69a3...32 | 0.0 |
| H | 0xce67...0f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...54 | 0.0 |
| K | 0xa732...c4 | 0.0 |
| L | 0x7c2e...a9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...2c | 0.0 |
| O | 0x7325...9d | 0.0 |
| P | 0x6218...48 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...10 | 0.0 |
| S | 0xb875...86 | 0.0 |
| T | 0x3578...88 | 0.0 |
| U | 0x7586...56 | 0.0 |
| V | 0xb59d...c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...7d | 0.0 |
| Y | 0xd8e3...c4 | 0.0 |
| Z | 0x7af0...7c | 0.0 |

### Multisig Contract Probes
All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required` POST view call.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...03 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...96 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...83 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...83 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...6d | 2 | ✅ HEALTHY |

**All 5 multisig contracts: 2-of-N signatures required, all healthy.**

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel deployment protection enabled on `https://testnet.mnx.fi`. All API endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) blocked. No market data retrieved.

### DuckDB Aptos/Multisig State
| Table | Rows Inserted |
|-------|--------------|
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

---

## Schema Reference
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

*Generated by world-increment-sweep + hamming-swarm-snapshot agent · plurigrid/gorj · 2026-07-20*
