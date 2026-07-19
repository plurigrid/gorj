# World-Increment Sweep + Hamming Snapshot — 2026-07-19

## Sweep Metadata
- **Date:** 2026-07-19T19:30 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 (new) + prior |
| Total Repo Snapshots | ~403 across 11 sources |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts | 5 (all healthy) |
| MNX Markets | unavailable (auth wall) |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Total Repos | Most Recent Push | Notable |
|--------|------|-------------|-----------------|---------|
| plurigrid | org | 103 | 2026-07-17 (asi ★31) | gorj (this repo, 1263 issues) |
| kubeflow | org | 49 | 2026-07-19 (4 repos) | kubeflow/kubeflow ★15782, pipelines ★4169 |
| TeglonLabs | org | 5 | 2026-06-08 (jank-crane) | mathpix-gem ★2 |
| bmorphism | user | 106 | 2026-07-14 (gay-chat) | ocaml-mcp-sdk ★61, anti-bullshit ★22 |
| zubyul | user | 49 | 2026-04-24 (voice-observatory) | gay-world ★1, tilelang-kernels |
| migalkin | user | 19 | 2026-07-10 (kgcourse2021) | NodePiece ★144, StarE ★89 |
| wasita | user | 12 | 2026-07-16 (wasita.github.io) | magic-garden ★2 |
| AustinCStone | user | 41 | 2026-07-15 (byteruckus) | TextGAN ★92, StereoVisionMRF ★11 |
| DJedamski | user | 6 | 2023-04-21 | Getting-and-Cleaning-Data |
| kristinezheng | user | 5 | 2026-07-01 (kristinezheng.github.io) | lookit-jenga |
| M1shaaa | user | 8 | 2026-02-04 (profile) | lab-bookshelf |
| **TOTAL** | | **~403** | | |

### GF(3) Color Chain — This Sweep's Increments

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 1 | plurigrid (org) | 0 | `#d3869b` | **ERGODIC** |
| 2 | kubeflow (org) | 1 | `#b8bb26` | **PLUS** |
| 3 | TeglonLabs (org) | -1 | `#cc241d` | **MINUS** |
| 4 | bmorphism (user) | 0 | `#d3869b` | **ERGODIC** |
| 5 | zubyul (user) | 1 | `#b8bb26` | **PLUS** |
| 6 | migalkin (user) | -1 | `#cc241d` | **MINUS** |
| 7 | wasita (user) | 0 | `#d3869b` | **ERGODIC** |
| 8 | AustinCStone (user) | 1 | `#b8bb26` | **PLUS** |
| 9 | DJedamski (user) | -1 | `#cc241d` | **MINUS** |
| 10 | kristinezheng (user) | 0 | `#d3869b` | **ERGODIC** |
| 11 | M1shaaa (user) | 1 | `#b8bb26` | **PLUS** |

### Highlights Since Last Sweep (2026-04-12)

- **kubeflow** extremely active on 2026-07-19: 4 repos pushed today including new `kubeflow/sdk` (★126) and `kubeflow/mcp-server` (★28)
- **plurigrid/asi** grew from ★16 → ★31 since April; gorj open issues 1263
- **bmorphism/Gay.jl** now has 187 open issues (was tracking actively)
- **bmorphism/gay-chat** new (2026-07-14) — Spritely Brassica Chat in Scheme
- **wasita** new repo `pnas-typst-template` (2026-07-16)
- **AustinCStone** new repo `byteruckus` (2026-07-15)
- **migalkin** revived kgcourse2021 knowledge graphs course (2026-07-10)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~6.36B. Accounts exist on-chain but have not been initialized with an APT CoinStore (no received/sent APT transactions).

| World | Address (prefix) | Balance APT |
|-------|-----------------|------------|
| alice | 0xc793acd… | 0.0 |
| bob | 0x0a3c00c… | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes — All Healthy ✓

| Pair | Address (prefix) | Sigs Required |
|------|-----------------|--------------|
| A-B | 0x0da4f428… | **2** |
| A-G | 0xf56c4a1c… | **2** |
| Y-Z | 0xd3ffe181… | **2** |
| S-T | 0x3b1c3ae9… | **2** |
| V-W | 0x40fad7b4… | **2** |

All 5 multisig contracts live and responsive on Aptos mainnet with 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)

**Status: Authentication Required** — testnet.mnx.fi returns an HTML auth wall on all probed endpoints (`/`, `/api/markets`, `/api/v1/markets`). No market data available without credentials. `mnx_snapshots` table is empty.

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

## DuckDB Tables Written

| Table | Rows |
|-------|------|
| world_increments | 34 (11 new + 23 from prior runs) |
| repo_snapshots | 991 (new inserts) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

## Notable Highlights

- **kubeflow/kubeflow**: ★15,782 — flagship ML platform for Kubernetes (active 2026-07-19)
- **kubeflow/pipelines**: ★4,169 — ML pipelines (pushed 2026-07-19)
- **kubeflow/spark-operator**: ★3,139 — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: ★144 — parameter-efficient KG embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: ★61 — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: ★92 — text generation with GANs
- **plurigrid/asi**: ★31 (up from 16 in April) — topological chemputer
- **plurigrid/gorj**: This repo — forj + Rama topology + GF(3) gay trit coloring
- **Multisig swarm**: All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) live with 2-sig threshold
- **Hamming wallets**: 28 addresses probed; all 0 APT (CoinStore not initialized on mainnet)
