# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 89 |
| Total Repo Snapshots | 1,010 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Top Repo by Stars |
|--------|------|---------------|-------------------|
| plurigrid | org | 99 | asi (31★), ontology (8★), vcg-auction (7★) |
| kubeflow | org | 49 | kubeflow/kubeflow (15,789★), pipelines (4,168★), spark-operator (3,142★) |
| TeglonLabs | org | 5 | mathpix-gem (2★) |
| bmorphism | user | 106 | ocaml-mcp-sdk (61★), risc0-cosmwasm-example (23★), say-mcp-server (20★) |
| zubyul | user | 49 | gay-world (1★), voice-observatory (0★) |
| migalkin | user | 19 | NodePiece (144★), StarE (89★), kgcourse2021 (24★) |
| DJedamski | social graph | 6 | Getting-and-Cleaning-Data (1★) |
| AustinCStone | social graph | 41 | TextGAN (92★), StereoVisionMRF (11★) |
| M1shaaa | social graph | 8 | lab-bookshelf (0★) |
| wasita | social graph | 12 | magic-garden (2★), wasita.github.io (1★) |
| kristinezheng | social graph | 5 | Green-Machine (0★) |

### GF(3) Color Chain — This Session (66 new increments)

| trit | color | name | count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 29 |
| 1 | #b8bb26 | PLUS | 30 |
| -1 | #cc241d | MINUS | 30 |

GF(3) chain: `PLUS → MINUS → ERGODIC` cycling, balanced across 89 total increments.

### Notable Recent Activity (pushed within 7 days of 2026-07-22)

- `plurigrid/gorj` — pushed 2026-07-22 (1,317 open issues — highly active)
- `plurigrid/eirobri` — pushed 2026-07-21 (EiRoBri replay world)
- `kubeflow/hub` — pushed 2026-07-22 (Model Registry, 178★)
- `kubeflow/pipelines` — pushed 2026-07-22 (4,168★)
- `bmorphism/Gay.jl` — pushed 2026-07-21 (187 open issues — very active)
- `bmorphism/anti-bullshit-mcp-server` — pushed 2026-07-12
- `bmorphism/gay-chat` — pushed 2026-07-14 (gay://chat over Spritely Brassica)
- `wasita/wasita.github.io` — pushed 2026-07-21
- `kristinezheng/kristinezheng.github.io` — pushed 2026-07-01

### Top Repos by Stars (Cross-Source)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,789 | — | 2026-07-21 |
| kubeflow/pipelines | 4,168 | Python | 2026-07-22 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-21 |
| kubeflow/trainer | 2,152 | Go | 2026-07-21 |
| kubeflow/katib | 1,692 | Python | 2026-07-20 |
| kubeflow/examples | 1,460 | Jsonnet | 2026-06-16 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| plurigrid/asi | 31 | HTML | 2026-07-10 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2026-03-19 |
| bmorphism/babashka-mcp-server | 19 | JavaScript | 2026-06-05 |
| migalkin/kgcourse2021 | 24 | HTML | 2026-07-10 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, ledger v6,398,007,773)

All 28 addresses (alice, bob, A–Z) probed via Aptos fullnode mainnet.  
All accounts are **on-chain active** (confirmed via sequence numbers: alice=72, bob=67, A–M range 23–62 txns).  
**All CoinStore resources returned `resource_not_found`** — wallets hold 0 APT in native `0x1::coin::CoinStore<AptosCoin>` at this ledger version.

> Accounts exist and are transacting — coins likely held as Fungible Assets (FA), staked, or custodial.

| World | Address (truncated) | Balance (APT) | Seq# |
|-------|---------------------|---------------|------|
| alice | 0xc793...cc7b | 0.0 | 72 |
| bob   | 0x0a3c...512d | 0.0 | 67 |
| A     | 0x8699...9d7a | 0.0 | 58 |
| B     | 0x3f89...b13  | 0.0 | 35 |
| C     | 0x38b9...35e  | 0.0 | 23 |
| D     | 0xf776...dd1  | 0.0 | 24 |
| E     | 0xdc1d...d36  | 0.0 | 24 |
| F     | 0x18a1...f71  | 0.0 | 62 |
| G     | 0x69a3...f32  | 0.0 | 31 |
| H     | 0xce67...00f  | 0.0 | 31 |
| I     | 0x070f...c9   | 0.0 | 31 |
| J     | 0x4d96...f54  | 0.0 | 32 |
| K     | 0xa732...dc4  | 0.0 | 41 |
| L     | 0x7c2e...ba9  | 0.0 | 49 |
| M     | 0x6fed...2e9  | 0.0 | 39 |
| N–Z   | (13 addresses) | 0.0 each | N/A |

### Multisig Contract Probes

All 5 multisig contracts responded **healthy** — `2` signatures required across all pairs.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...7003 | 2 | ✓ |
| A-G  | 0xf56c...0096 | 2 | ✓ |
| Y-Z  | 0xd3ff...b883 | 2 | ✓ |
| S-T  | 0x3b1c...7883 | 2 | ✓ |
| V-W  | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

Site is a **Next.js SPA** — no public REST API endpoints found at `/api/markets`, `/api/v1/markets`, or common paths. Market data is fetched client-side via JavaScript bundles. No market data captured; recorded as `N/A` in `mnx_snapshots` table.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)                  -- 89 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)                  -- 1,010 rows

aptos_snapshots(timestamp, world, address, balance_apt) -- 28 rows

multisig_probes(timestamp, pair, address, sigs_required, healthy) -- 5 rows

mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 1 row
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,789★ — flagship ML platform (up 224★ from April sweep)
- **kubeflow/pipelines**: 4,168★ — most active kubeflow repo (pushed today)
- **migalkin/NodePiece**: 144★ — scalable knowledge graph embeddings (up 1★)
- **bmorphism/Gay.jl**: 187 open issues — extremely active development
- **plurigrid/gorj**: 1,317 open issues — this very repo, pushed today
- **All 5 multisigs**: 2-of-N, all healthy — Hamming swarm intact
- **All 28 Aptos accounts**: on-chain active, 0 native APT in CoinStore
