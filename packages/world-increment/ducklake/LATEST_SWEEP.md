# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-09

## Sweep Metadata
- **Date:** 2026-06-09T01:11 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 32 |
| kubeflow | org | 17 |
| TeglonLabs | org | 5 |
| bmorphism | user | 15 |
| zubyul | user | 12 |
| migalkin | social (zubyul graph) | 5 |
| DJedamski | social (zubyul graph) | 3 |
| wasita | social (zubyul graph) | 4 |
| kristinezheng | social (zubyul graph) | 3 |
| M1shaaa | social (zubyul graph) | 2 |
| AustinCStone | social (zubyul graph) | 4 |
| **Total** | | **102** |

### Notable Repos

**plurigrid** — Active GF(3) / Clojure / Zig ecosystem (pushed 2026-06):
- `gorj` (447 open issues) — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- `eirobri` (29 open issues) — EiRoBri replay world
- `asi` (25 ⭐) — everything is topological chemputer!
- `nanoclj-zig` — NaN-boxed Clojure interpreter in Zig 0.15

**kubeflow** — Production ML on Kubernetes:
- `kubeflow` (15,709 ⭐, 2,673 forks) — canonical ML toolkit
- `pipelines` (4,153 ⭐) — last pushed 2026-06-08
- `spark-operator` (3,126 ⭐) + new `mcp-apache-spark-history-server` (174 ⭐)
- `trainer` (2,112 ⭐) — Distributed AI Model Training

**TeglonLabs** — 5 repos; `jank-crane` (C++, 2026-06-08) — crane-jank converged-IR hub with GF(3) convergence maps

**bmorphism** — Active:
- `Gay.jl` (189 open issues, pushed 2026-06-09) — Wide-gamut color sampling SPI
- `ocaml-mcp-sdk` (61 ⭐) — OCaml MCP SDK via Jane Street oxcaml_effect
- `anti-bullshit-mcp-server` (23 ⭐)

**zubyul** — Active:
- `tilelang-kernels` — TileLang GPU kernels for GF(3) trit classification (NVIDIA GB10 Blackwell)
- `plurigrid-site` (11 open issues)

**Social graph** — zubyul connections:
- `migalkin/NodePiece` (144 ⭐) — KG representation learning (ICLR 2022)
- `AustinCStone/TextGAN` (92 ⭐) — TF text generation GAN

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 34 |
| +1 | `#b8bb26` | PLUS | 34 |
| -1 | `#cc241d` | MINUS | 34 |

**Perfectly balanced** — 102 increments ≡ 0 (mod 3). GF(3) conservation holds.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, probed 2026-06-09T01:10 UTC)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. Accounts exist on-chain (e.g., alice has `sequence_number: 72`) but use the Fungible Asset (FA) standard post-migration. Legacy APT CoinStore balance = NULL for all 28 wallets.

### Multisig Contract Probes (5 pairs)

All 5 multisig accounts responded healthy with `num_signatures_required = 2`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|------------------|--------------|---------|
| A-B | `0x0da4f428...` | 2 | ✓ |
| A-G | `0xf56c4a1c...` | 2 | ✓ |
| Y-Z | `0xd3ffe181...` | 2 | ✓ |
| S-T | `0x3b1c3ae9...` | 2 | ✓ |
| V-W | `0x40fad7b4...` | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — Vercel deployment protection (HTTP 401). No market data captured; `mnx_snapshots` table empty.

---

## DuckDB Table Counts

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 102 | GF3-tagged repo snapshot events |
| repo_snapshots | 102 | full repo metadata |
| aptos_snapshots | 28 | hamming swarm wallets, balance_apt=NULL |
| multisig_probes | 5 | all healthy, sigs_required=2 |
| mnx_snapshots | 0 | unavailable (Vercel auth) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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

## Top Stars by Repo

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,709 | — | 2026-05-24 |
| kubeflow/pipelines | 4,153 | Python | 2026-06-08 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-08 |
| kubeflow/trainer | 2,112 | Go | 2026-06-08 |
| kubeflow/katib | 1,685 | Python | 2026-06-05 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| plurigrid/asi | 25 | HTML | 2026-04-26 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |
