# World-Increment Sweep — 2026-07-19

## Sweep Metadata
- **Date:** 2026-07-19
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (via pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 35 |
| New Increments This Sweep | 12 (ids 13–24) |
| Total Repo Snapshots | 1,338 |
| New Repo Snapshots | 394 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Vercel auth required) |

---

## GF(3) Color Chain — This Sweep (ids 13–24)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 24 | gorj (sweep_complete) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| StochFlow | Python | 4 | 2024-03-20 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,782 | 2026-07-10 |
| pipelines | Python | 4,169 | 2026-07-19 |
| spark-operator | Python | 3,139 | 2026-07-17 |
| trainer | Go | 2,152 | 2026-07-19 |
| katib | Python | 1,691 | 2026-07-16 |

### TeglonLabs (5 repos, down from 53 last sweep — org may have made repos private)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
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

### zubyul (49 repos, up from 24 last sweep)
Significant growth — 25 new repos since April sweep.

### migalkin (19 repos, down from 30 — some repos may be private now)
| Repo | Stars |
|------|-------|
| NodePiece | 143+ |
| StarE | 88+ |

### wasita (12 repos)
- `wasita.github.io` (Svelte): pushed 2026-07-16 — recently active personal site

### kristinezheng (5 repos)
- `kristinezheng.github.io` (HTML): pushed 2026-07-01 — recently updated

### M1shaaa (8 repos)
- `M1shaaa` profile: pushed **2026-07-19** — activity today

### AustinCStone (41 repos, down from 43)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92+ |
| StereoVisionMRF | Python | 11+ |

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
| wasita | user | 12 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **394** |

---

## Hamming Swarm Snapshot — Aptos Mainnet

**Date:** 2026-07-19  
**Method:** `CoinStore<AptosCoin>` resource query via fullnode.mainnet.aptoslabs.com

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Account existence confirmed (alice has `sequence_number=72` — active account). Accounts exist on-chain but have no APT coin store resource initialized; balance recorded as 0.0 APT for all.

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|--------------|--------|
| alice | 0xc793...cc7b | 0.0 | no_coin_store |
| bob | 0x0a3c...2d5d | 0.0 | no_coin_store |
| A | 0x8699...9d7a | 0.0 | no_coin_store |
| B–Z | (25 addresses) | 0.0 each | no_coin_store |

---

## Multisig Contract Probes — Aptos Mainnet

All 5 contracts healthy (2-of-2 signatures required):

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

---

## MNX Markets

**Status:** Unavailable — `testnet.mnx.fi` requires Vercel visitor password authentication. No market data extracted.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,782 stars (grew 217 since April) — flagship Kubernetes ML platform still active
- **kubeflow/pipelines**: 4,169 stars — pushed 2026-07-19 (today)
- **kubeflow/trainer**: 2,152 stars — distributed AI training, pushed today
- **kubeflow/mcp-server**: 28 stars — NEW since April: MCP Server for AI-Assisted Development with Kubeflow
- **plurigrid/asi**: 31 stars (was 16 in April — nearly doubled in 3 months)
- **TeglonLabs**: Dropped from 53 to 5 public repos — significant reduction (repos likely privated)
- **TeglonLabs/jank-crane**: NEW (created 2026-06-08) — crane-jank converged-IR hub with GF3 convergence maps
- **zubyul**: Grew from 24 to 49 public repos since April (+25 repos)
- **M1shaaa**: Active today (profile repo pushed 2026-07-19)
- **Multisig swarm**: All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) healthy at 2-of-2
- **Hamming swarm APT**: All 28 wallets show no coin store (alice account active, seq=72, but no APT balance)
- **Increment 24**: ERGODIC — sweep_complete closing the 8th full GF(3) cycle (ids 1–24)
