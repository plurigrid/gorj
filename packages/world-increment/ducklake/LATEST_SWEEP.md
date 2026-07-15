# World-Increment Sweep — 2026-07-15

## Sweep Metadata
- **Date:** 2026-07-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment range this sweep:** 22–32 (world_increments table cumulative total: 43)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments | 11 |
| New Repo Snapshots | 383 |
| Cumulative Increments | 43 |
| Cumulative Repo Snapshots | 1,661 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Vercel auth required) |

---

## GF(3) Color Chain — This Sweep (Increments 22–32)

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 22 | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 23 | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 24 | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 25 | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 26 | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 27 | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 28 | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 29 | wasita | user | -1 | `#cc241d` | **MINUS** |
| 30 | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 31 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 32 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source (This Sweep)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| StochFlow | Python | 4 | 2024-03-20 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,776 | 2026-07-10 |
| pipelines | Python | 4,166 | 2026-07-15 |
| spark-operator | Python | 3,136 | 2026-07-14 |
| trainer | Go | 2,145 | 2026-07-14 |
| katib | Python | 1,690 | 2026-07-14 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| jank-crane | C++ | 0 | 2026-06-08 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2022-02-02 |
| StarE | Python | 89 | 2023-12-01 |
| kgcourse2021 | HTML | 24 | 2025-08-04 |
| NBFNet_mlx | Python | 10 | 2024-03-02 |
| RWL | Python | 8 | 2022-12-01 |

### AustinCStone (41 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2016-10-04 |
| StereoVisionMRF | Python | 11 | 2016-01-10 |
| SpectralClustering | Python | 3 | 2015-11-09 |

---

## Repo Counts by Source (This Sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **393** |

> Note: TeglonLabs dropped from 53 repos (Apr sweep) to 5 — likely visibility changes.
> kristinezheng down from 18 → 5. zubyul up from 24 → 49.

---

## Hamming Swarm — Aptos Snapshot (2026-07-15)

### Wallet Balances (alice, bob, A–Z)

All 28 wallets queried via Aptos Mainnet fullnode. All show **0.0 APT** in CoinStore at time of snapshot.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B–Z | (see DB) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts **healthy** — require 2 signatures.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

### MNX Markets

**Unavailable** — `https://testnet.mnx.fi` requires Vercel visitor authentication. No market data accessible without bypass token.

---

## Notable Highlights

- **kubeflow/pipelines** pushed today (2026-07-15) — 4,166 stars, active dev
- **M1shaaa/M1shaaa** profile repo pushed today (2026-07-15T02:04:27Z) — M1shaaa is active
- **plurigrid/asi** 30 stars (up from 16 in Apr sweep) — significant growth in ~3 months
- **TeglonLabs/jank-crane** — new since Apr sweep: crane-jank converged-IR hub with GF3 convergence maps
- **migalkin/NodePiece** still at 144★ — stable knowledge graph embedding leader
- **All Hamming swarm wallets at 0.0 APT** — no balance changes detected vs Apr sweep
- **All multisig contracts stable at 2-of-N** — no governance changes

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
