# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| GitHub Repos Snapshotted (this run) | 327 (394 total unique) |
| World Increments Inserted | 327 |
| Cumulative DB Increments | 350+ |
| Cumulative Repo Snapshots | 1,271 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Healthy | 5/5 |
| MNX Markets | SPA — unavailable via API |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (this run)
| Source | Type | Repos captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 12 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 41 |
| **TOTAL** | | **394** |

### Top Repos by Stars
| Org/User | Repo | Stars | Language | Last Push |
|----------|------|-------|----------|-----------|
| kubeflow | kubeflow | 15,789 | — | 2026-07-10 |
| kubeflow | pipelines | 4,169 | Python | 2026-07-23 |
| kubeflow | spark-operator | 3,143 | Python | 2026-07-17 |
| kubeflow | trainer | 2,153 | Go | 2026-07-23 |
| kubeflow | katib | 1,692 | Python | 2026-07-22 |
| migalkin | NodePiece | 144 | Python | ICLR'22 |
| AustinCStone | TextGAN | 92 | Python | TF text GAN |
| migalkin | StarE | 89 | Python | EMNLP'20 |
| migalkin | kgcourse2021 | 24 | HTML | 2026-07-10 |
| migalkin | NBFNet_mlx | 10 | Python | 2024 |
| AustinCStone | StereoVisionMRF | 11 | Python | — |

### Notable Activity (2026 pushes)
- **TeglonLabs/jank-crane** (C++, 2026-06-08): crane-jank converged-IR hub, GF3 convergence maps
- **wasita/wasita.github.io** (Svelte, active July 2026): personal site, 8 open issues
- **AustinCStone/byteruckus** (HTML, 2026-07-15): brand new repo
- **migalkin/kgcourse2021** (HTML, 2026-07-10): KG course still receiving updates
- **kubeflow/{trainer,pipelines,katib}**: all pushed within 48h of this sweep

### GF(3) Color Chain (this run, IDs 24-350)
Assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)
| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793...cc7b | 0.0 | No coin store |
| bob | 0x0a3c...2d5d | 0.0 | No coin store |
| A–Z | (24 addresses) | 0.0 each | No coin store |

**Note:** All 28 addresses returned 0.0 APT. The `CoinStore<AptosCoin>` resource was absent on all probed accounts — these wallets are uninitialized or have no native APT balance. All API calls returned valid JSON (no timeouts or errors).

### Multisig Contract Probes — 5/5 HEALTHY
| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✅ HEALTHY |

All 5 multisig accounts require 2-of-N signatures. All returned `["2"]` from the view function — contracts live and responsive.

### MNX Markets (testnet.mnx.fi)
- **Status:** SPA (Next.js app) — no REST API exposed at `/api/markets` or `/api/tickers`
- Market data requires browser-side JS execution; unavailable via server fetch
- No `mnx_snapshots` rows inserted this run

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

## Notable Highlights (2026-07-24)
- **kubeflow/kubeflow**: 15,789 stars — up 224 since April 2026 sweep
- **kubeflow/trainer**: 2,153 stars — up 73 since April sweep (Go, very active)
- **migalkin/NodePiece**: 144 stars — knowledge graph composition ICLR'22
- **AustinCStone/TextGAN**: 92 stars — TF text GAN, still referenced
- **All 5 multisig contracts**: healthy, 2-of-N, responsive
- **Hamming swarm APT balances**: all 0.0 — no APT coin stores initialized on these addresses
