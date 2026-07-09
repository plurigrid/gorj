# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-09

## Sweep Metadata
- **Date:** 2026-07-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 351 |
| Total Repo Snapshots | 1,272 |
| Aptos Snapshots | 28 |
| Multisig Probes | 5 |
| Sources Covered | 3 orgs + 8 users (11 total) |

---

## JOB 1: GitHub Social Graph Sweep

### Repos by Source (this sweep)
| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 49 | 102,057 |
| migalkin | user | 19 | 833 |
| bmorphism | user | 100+ | 509 |
| AustinCStone | user (social) | 30+ | 320 |
| plurigrid | org | 100+ | 162 |
| zubyul | user | 49 | 40 |
| DJedamski | user (social) | 6 | 16 |
| TeglonLabs | org | 5 | 14 |
| wasita | user (social) | 11 | 10 |
| kristinezheng | user (social) | 5 | 0 |
| M1shaaa | user (social) | 8 | 0 |

### Top Repos by Stars (all-time in DB)
| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,768 | — | 2026-07-08 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-09 |
| kubeflow/spark-operator | 3,135 | Python | 2026-07-08 |
| kubeflow/trainer | 2,134 | Go | 2026-07-08 |
| migalkin/NodePiece | 144 | Python | 2021-06-14 |
| AustinCStone/TextGAN | 92 | Python | 2016-09-19 |
| migalkin/StarE | 89 | Python | 2020-09-17 |
| migalkin/kgcourse2021 | 25 | HTML | — |
| AustinCStone/StereoVisionMRF | 11 | Python | — |

### Recently Active (pushed within last 7 days)
- **kubeflow/pipelines** — pushed 2026-07-09
- **kubeflow/kubeflow** — pushed 2026-07-08
- **kubeflow/trainer** — pushed 2026-07-08
- **wasita/wasita.github.io** — pushed 2026-07-06
- **kristinezheng/kristinezheng.github.io** — pushed 2026-07-01

### GF(3) Color Chain Distribution (world_increments)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 116 |
| +1 | `#b8bb26` | PLUS | 118 |
| -1 | `#cc241d` | MINUS | 117 |

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 total)
All 28 addresses queried against `fullnode.mainnet.aptoslabs.com`.

**Result: 0/28 addresses have active APT coin stores.**  
All returned `Resource not found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
These wallets are unfunded on Aptos mainnet as of 2026-07-09.

### Multisig Contract Probes (5 pairs via `0x1::multisig_account::num_signatures_required`)
| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...4987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...fbc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...e75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...ded7883` | 2 | ✓ |
| V-W | `0x40fad7b4...c80eb6d` | 2 | ✓ |

**All 5 multisigs healthy — 2-of-2 threshold confirmed.**

### MNX Markets (testnet.mnx.fi)
Probe result: SPA HTML (13 KB). No REST API responded at:
- `https://testnet.mnx.fi/api/markets`
- `https://testnet.mnx.fi/api/v1/markets`
- `https://testnet.mnx.fi/markets`
- `https://testnet.mnx.fi/api/tickers`

**Status: Frontend SPA only — no market data available via API probe. `mnx_snapshots` table empty.**

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
- **kubeflow/kubeflow**: 15,768 stars, pushed 2026-07-08 — active flagship ML platform
- **kubeflow/pipelines**: 4,169 stars, pushed 2026-07-09 — most recently updated
- **TeglonLabs/jank-crane**: C++, GF3 convergence maps, pushed 2026-06-08
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings (ICLR 2022)
- **bmorphism**: 100+ repos spanning OCaml MCP SDK, Zig, Clojure tooling
- **plurigrid**: 100+ repos; vivarium, gorj, ASI/topology work
- **All 5 Hamming multisigs respond** with 2-of-2 threshold — swarm intact
- **All 28 Hamming wallets unfunded** on Aptos mainnet
