# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-09

## Sweep Metadata
- **Date:** 2026-05-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (cumulative after this sweep)

| Metric | Value |
|--------|-------|
| Total World Increments | 34 (+11 this sweep) |
| Total Repo Snapshots | 1120 (+176 this sweep) |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — This Sweep's Increments (IDs 24–34)

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 24 | plurigrid | org | 0 | `#d3869b` | **ERGODIC** |
| 25 | kubeflow | org | +1 | `#b8bb26` | **PLUS** |
| 26 | TeglonLabs | org | -1 | `#cc241d` | **MINUS** |
| 27 | bmorphism | user | 0 | `#d3869b` | **ERGODIC** |
| 28 | zubyul | user | +1 | `#b8bb26` | **PLUS** |
| 29 | migalkin | user | -1 | `#cc241d` | **MINUS** |
| 30 | DJedamski | user | 0 | `#d3869b` | **ERGODIC** |
| 31 | wasita | user | +1 | `#b8bb26` | **PLUS** |
| 32 | kristinezheng | user | -1 | `#cc241d` | **MINUS** |
| 33 | M1shaaa | user | 0 | `#d3869b` | **ERGODIC** |
| 34 | AustinCStone | user | +1 | `#b8bb26` | **PLUS** |

GF(3) assignment: `id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d`

---

## Top Repos by Source (this sweep)

### plurigrid (41 new snapshots)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 0 | 2026-05-09 |
| asi | HTML | 21 | 2026-04-26 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-04-26 |
| ontology | JavaScript | 8 | 2025-05-27 |

### kubeflow (30 new snapshots)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15628 | 2026-05-09 |
| pipelines | Python | 4137 | 2026-05-09 |
| spark-operator | Python | 3125 | 2026-05-09 |
| trainer | Go | 2096 | 2026-05-08 |
| katib | Python | 1683 | 2026-05-05 |
| arena | Go | 810 | 2026-05-07 |
| manifests | YAML | 1015 | 2026-05-08 |

### TeglonLabs (4 new snapshots)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| topoi | Python | 0 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (30 new snapshots)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| say-mcp-server | JavaScript | 20 | 2026-03-19 |
| babashka-mcp-server | JavaScript | 18 | 2026-03-26 |
| penrose-mcp | JavaScript | 10 | 2026-04-12 |
| Gay.jl | Julia | 1 | 2026-04-17 |

### migalkin (9 new snapshots)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |

### AustinCStone (14 new snapshots)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| bmfork | Python | 0 (pushed today 2026-05-09) |
| bmforkupdate | Python | 0 (pushed today 2026-05-09) |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

All 28 addresses queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<AptosCoin>`.

| World | Address (prefix) | Balance (APT) |
|-------|------------------|---------------|
| alice | 0xc793acd… | 0.00000000 |
| bob   | 0x0a3c00c… | 0.00000000 |
| A–Z   | various | 0.00000000 each |

**Summary:** All 28 addresses show 0 APT. The `CoinStore<AptosCoin>` resource is not registered on any of these addresses — they exist on-chain but have never received APT deposits. This is consistent with the prior sweep (2026-04-14).

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|------------------|---------------|--------|
| A-B  | 0x0da4f42… | **2** | ✓ Healthy |
| A-G  | 0xf56c4a1… | **2** | ✓ Healthy |
| Y-Z  | 0xd3ffe18… | **2** | ✓ Healthy |
| S-T  | 0x3b1c3ae… | **2** | ✓ Healthy |
| V-W  | 0x40fad7b… | **2** | ✓ Healthy |

All 5 multisig accounts operational with a 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)
**Status:** DATA UNAVAILABLE  
`testnet.mnx.fi` is a Next.js SPA. The `/markets` route responds HTTP 200 with client-side HTML. API endpoints `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/v1/markets` all return HTTP 404. No structured market data can be extracted. `mnx_snapshots` table remains empty.

---

## DuckDB Table Counts (cumulative)

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1120 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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
- **kubeflow/kubeflow**: 15,628 stars (+63 since Apr 14) — ML platform for Kubernetes
- **kubeflow/pipelines**: 4,137 stars (+18 since Apr 14)
- **migalkin/NodePiece**: 144 stars (+1) — ICLR'22 KG representation
- **bmorphism/ocaml-mcp-sdk**: 61 stars (+1) — OCaml SDK for MCP using Jane Street oxcaml_effect
- **AustinCStone/bmfork** + **bmforkupdate**: pushed today 2026-05-09
- **plurigrid/gorj**: pushed today — 120 open issues, active development
- All 5 Hamming-swarm multisigs remain healthy (2-of-N)
