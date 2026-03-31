# World Increment Sweep + Hamming Snapshot — 2026-03-31

## Sweep Metadata
- **Date:** 2026-03-31T05:30:00Z
- **Agent:** world-increment-sweep (JOB 1 + JOB 2)
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 100 |
| Total Repo Snapshots | 100 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GitHub Repos by Org/User

| Org/User | Count |
|---|---|
| plurigrid | 22 |
| kubeflow | 16 |
| bmorphism | 12 |
| zubyul | 11 |
| TeglonLabs | 10 |
| AustinCStone | 6 |
| migalkin | 6 |
| wasita | 5 |
| kristinezheng | 4 |
| M1shaaa | 4 |
| DJedamski | 4 |
| **TOTAL** | **100** |

---

## Top Repos by Stars

| Repo | Stars | Language |
|---|---|---|
| kubeflow/kubeflow | 15547 | (config) |
| kubeflow/pipelines | 4114 | Python |
| kubeflow/spark-operator | 3110 | Python |
| kubeflow/trainer | 2070 | Go |
| kubeflow/katib | 1673 | Python |
| kubeflow/examples | 1459 | Jsonnet |
| kubeflow/manifests | 1006 | YAML |
| kubeflow/arena | 810 | Go |
| kubeflow/kale | 681 | Python |
| kubeflow/mpi-operator | 519 | Go |
| migalkin/NodePiece | 143 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 88 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |

---

## Notable Recent Activity (pushed March 2026)

- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (pushed 2026-03-31)
- `plurigrid/horse` — TeX (pushed 2026-03-31)
- `plurigrid/asi` — everything is topological chemputer! 13 stars (pushed 2026-03-30)
- `kubeflow/trainer` — Distributed AI Model Training + LLM Fine-Tuning on Kubernetes (pushed 2026-03-31)
- `kubeflow/pipelines` — 4114 stars (pushed 2026-03-31)
- `zubyul/Gay.jl` — Wide-gamut color sampling with splittable determinism (pushed 2026-03-28)
- `bmorphism/zig-syrup` — Embeddable OCapN Syrup encoder/decoder in Zig (pushed 2026-03-28)
- `M1shaaa/M1shaaa` — profile config (pushed 2026-03-31)

---

## Aptos Wallet Balances (Hamming Snapshot)

All 28 addresses returned 0 APT (CoinStore resource not funded/initialized on mainnet).

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (all 26 addresses) | 0.0 each |

---

## Multisig Contract Probes

All 5 contracts healthy (sigs_required = 2).

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

---

## MNX Market Data

**Status: Unavailable** — All MNX API endpoints (testnet.mnx.fi/api/markets, /api/tickers, /api/v1/markets) returned Next.js app HTML rather than JSON. No structured market data was accessible.

---

## GF(3) Color Chain Stats

100 repo snapshots tagged with GF(3) trit coloring (`id % 3`):

| GF(3) Name | Color | Trit | Count |
|---|---|---|---|
| ERGODIC | #d3869b (mauve) | 0 | 33 |
| PLUS | #b8bb26 (yellow-green) | 1 | 34 |
| MINUS | #cc241d (red) | -1 | 33 |

GF(3) Assignment Rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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
