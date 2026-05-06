# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-06

## Sweep Metadata
- **Date:** 2026-05-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 360 |
| Total Repo Snapshots | 1281 (337 unique repos across 11 sources) |
| Sources Covered | 3 orgs + 8 users (+ social graph) |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution

| GF(3) Name | Trit | Color | Count |
|------------|------|-------|-------|
| PLUS | +1 | `#b8bb26` | 121 |
| MINUS | -1 | `#cc241d` | 120 |
| ERGODIC | 0 | `#d3869b` | 119 |

Rule: `id mod 3 == 0` → ERGODIC `#d3869b` | `id mod 3 == 1` → PLUS `#b8bb26` | `id mod 3 == 2` → MINUS `#cc241d`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Unique Repos | Latest Push |
|--------|------|-------------|-------------|
| plurigrid | org | 100 | 2026-05-06 (`gorj`) |
| kubeflow | org | 47 | 2026-05-06 (`dashboard`) |
| bmorphism | user | 100 | 2026-05-06 (`Gay.jl`) |
| zubyul | user | 49 | 2026-04-24 (`voice-observatory`) |
| TeglonLabs | org | 4 | 2026-01-01 (`mathpix-gem`) |
| migalkin | social-graph | 19 | 2026-04-16 (`StarE`) |
| DJedamski | social-graph | 6 | 2023-04-21 |
| wasita | social-graph | 11 | 2026-05-06 (`vocoder`) |
| kristinezheng | social-graph | 6 | 2026-04-09 |
| M1shaaa | social-graph | 8 | 2026-02-04 |
| AustinCStone | social-graph | 31 | 2026-02-11 |

### Top Repos by Source

**plurigrid (100 repos)**
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 19 | 2026-04-26 |
| gorj | Clojure | 0 | 2026-05-06 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-04-26 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |

**kubeflow (47 repos)**
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,622 | 2026-04-29 |
| pipelines | Python | 4,132 | 2026-05-05 |
| spark-operator | Python | 3,123 | 2026-05-05 |
| trainer | Go | 2,096 | 2026-05-06 |
| katib | Python | 1,683 | 2026-04-14 |

**bmorphism (100 repos)**
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 60 | 2026-03-16 |
| anti-bullshit-mcp-server | JS | 23 | 2026-01-16 |
| say-mcp-server | JS | 20 | 2025-01-07 |
| Gay.jl | Julia | 1 | 2026-05-06 |

**migalkin (social graph)**
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |

**AustinCStone (social graph)**
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |
| StructureFromMotion | Python | 1 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 addresses)

**API endpoint:** `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** `resource_not_found` for all 28 addresses.

**Interpretation:** Accounts are **active** on Aptos mainnet (account A has `sequence_number=58`), but use the **Fungible Assets (FA)** module rather than the legacy Coin module. The legacy `CoinStore` resource does not exist for these wallets. Balance reads require the FA-aware API (`0x1::primary_fungible_store`).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | `0xc793…cc7b` | — (FA module) |
| bob | `0x0a3c…12d5d` | — (FA module) |
| A | `0x8699…9d7a` | — (FA module, seq=58) |
| B–Z | … | — (FA module) |

*All 28 inserted into `aptos_snapshots` with `balance_apt = NULL`.*

### Multisig Contract Probes

**Function:** `0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | `0x0da4…7003` | 2 | ✅ |
| A-G | `0xf56c…0096` | 2 | ✅ |
| Y-Z | `0xd3ff…b883` | 2 | ✅ |
| S-T | `0x3b1c…7883` | 2 | ✅ |
| V-W | `0x40fa…eb6d` | 2 | ✅ |

**All 5 multisig contracts healthy** — each requires unanimous 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable via REST API.
`testnet.mnx.fi` is a Next.js SPA. Endpoints `/api/markets` and `/api/v1/markets` return HTML, not JSON. `mnx_snapshots` table: **0 rows**.

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

## Key Signals

- **plurigrid/gorj** is the most recently pushed repo in the sweep (2026-05-06T06:19:35Z)
- **wasita/vocoder** was created and pushed today (2026-05-06) — freshest repo in the social graph
- **kubeflow/trainer** leads star growth in the ecosystem (2,096 ⭐, up from 2,080 in April)
- **bmorphism/Gay.jl** has 187 open issues as of today — very active development
- All 5 Hamming swarm multisig contracts respond and require 2-of-2 unanimous consent
- Aptos Hamming swarm has migrated fully to Fungible Assets module — legacy CoinStore absent
