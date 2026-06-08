# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-08  
**GF(3) Color Chain:** trit=-1 → MINUS #cc241d | trit=0 → ERGODIC #d3869b | trit=1 → PLUS #b8bb26

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Indexed |
|--------|------|--------------|
| plurigrid | org | 100+ (15 representative) |
| kubeflow | org | 51 (16 representative) |
| TeglonLabs | org | 5 |
| bmorphism | user | 100+ (15 representative) |
| zubyul | user | 51 (8 representative) |
| migalkin | zubyul-social | 19 (5 top) |
| DJedamski | zubyul-social | 6 (2 representative) |
| wasita | zubyul-social | 11 (3 top) |
| kristinezheng | zubyul-social | 5 (2 top) |
| M1shaaa | zubyul-social | 8 (2 representative) |
| AustinCStone | zubyul-social | 40 (4 top) |

### Top Repos by Stars (sampled)
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,708 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-08 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-04 |
| kubeflow/trainer | 2,112 | Go | 2026-06-05 |
| kubeflow/katib | 1,685 | Python | 2026-06-05 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 25 | HTML | 2026-04-26 |

### GF(3) Increment Distribution
| Trit | Label | Color | Count |
|------|-------|-------|-------|
| -1 | MINUS | #cc241d | 26 |
| 0 | ERGODIC | #d3869b | 25 |
| +1 | PLUS | #b8bb26 | 26 |

**Total world_increments:** 77  
**Total repo_snapshots:** 77

### Notable Activity
- **plurigrid/gorj** (this repo): 444 open issues — most active plurigrid repo  
- **bmorphism/Gay.jl**: 189 open issues, pushed 2026-06-08 — active color science work  
- **kubeflow/dashboard**: TypeScript, pushed 2026-06-08 — hot today  
- **TeglonLabs/jank-crane**: C++, pushed 2026-06-08 — crane-jank converged-IR hub with GF3 maps  
- **wasita** social graph: Svelte/TypeScript tilt, active personal site + magic-garden bot  
- **kristinezheng.github.io**: pushed 2026-06-07 — very recent activity  

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)
**Endpoint:** `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

All 28 addresses (alice, bob, A–Z) returned **null** balance — none have a registered `CoinStore<AptosCoin>` resource on Aptos mainnet. These addresses exist on-chain but hold no APT in the standard coin module (may use other token standards or are unfunded).

| World | Address (truncated) | Balance APT |
|-------|--------------------|----|
| alice | 0xc793...cc7b | null |
| bob | 0x0a3c...2d5d | null |
| A–Z | (26 addresses) | null |

### Multisig Contract Probes (5 pairs)
`POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|--------------------|----|---------|
| A-B | 0x0da4...7003 | **2** | ✓ |
| A-G | 0xf56c...0096 | **2** | ✓ |
| Y-Z | 0xd3ff...b883 | **2** | ✓ |
| S-T | 0x3b1c...7883 | **2** | ✓ |
| V-W | 0x40fa...eb6d | **2** | ✓ |

All 5 multisig accounts are live and require 2-of-N signatures. All healthy.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel authentication (deployment protection). All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return 401 Vercel auth gate. No market data could be extracted.

---

## DuckDB Schema Summary
**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 77 |
| repo_snapshots | 77 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth-gated) |

---
_Previous sweep data below (2026-04-12)_

---
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 471 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

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
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
