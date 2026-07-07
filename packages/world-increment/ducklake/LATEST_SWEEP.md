# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-07  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.4  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found | Top Star Repo |
|--------|------|-------------|---------------|
| plurigrid | org | 103 (100 fetched) | asi (28★) |
| kubeflow | org | 49 | kubeflow (15,769★) |
| TeglonLabs | org | 5 | mathpix-gem (2★) |
| bmorphism | user | 105 | ocaml-mcp-sdk (61★) |
| zubyul | user | 49 | gay-world (1★) |
| migalkin | user | 19 | NodePiece (144★) |
| wasita | user | 11 | magic-garden (2★) |
| AustinCStone | user | 40 | TextGAN (92★) |
| DJedamski | user | 6 | School (1★) |
| kristinezheng | user | 5 | Nikolova_lab_data_analysis (2★) |
| M1shaaa | user | 8 | — |

### Notable Repos (Recently Pushed — 2026)

- **plurigrid/gorj** — Clojure REPL MCP server, 1029 open issues, pushed 2026-07-07 (this repo)
- **plurigrid/place** — TeX forester, 12 open issues, pushed 2026-07-07
- **plurigrid/eirobri** — Clojure, pushed 2026-06-30
- **plurigrid/asi** — HTML, 28★ 8 forks, pushed 2026-06-29
- **kubeflow/pipelines** — Python, 4169★ 2026 forks, pushed 2026-07-07
- **kubeflow/trainer** — Go, 2129★, pushed 2026-07-06
- **kubeflow/spark-operator** — Python, 3132★ 1497 forks, pushed 2026-07-02
- **bmorphism/Gay.jl** — Julia wide-gamut color, 187 open issues, pushed 2026-06-20
- **bmorphism/penrose-mcp** — JS, 9★ 4 forks, pushed 2026-06-24
- **migalkin/NodePiece** — Python KG embeddings, 144★ 21 forks (ICLR'22), pushed 2026-05-07
- **wasita/wasita.github.io** — Svelte personal site, pushed 2026-07-06

### GF(3) Color Chain — This Run (New Increments)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1 | plurigrid (org) | 0 | `#d3869b` | ERGODIC |
| 2 | kubeflow (org) | 1 | `#b8bb26` | PLUS |
| 3 | TeglonLabs (org) | -1 | `#cc241d` | MINUS |
| 4 | bmorphism (user) | 0 | `#d3869b` | ERGODIC |
| 5 | zubyul (user) | 1 | `#b8bb26` | PLUS |
| 6 | migalkin (user) | -1 | `#cc241d` | MINUS |
| 7 | wasita (user) | 0 | `#d3869b` | ERGODIC |
| 8 | AustinCStone (user) | 1 | `#b8bb26` | PLUS |
| 9 | DJedamski (user) | -1 | `#cc241d` | MINUS |
| 10 | kristinezheng (user) | 0 | `#d3869b` | ERGODIC |
| 11 | M1shaaa (user) | 1 | `#b8bb26` | PLUS |

### DuckDB Ducklake State

```
world_increments:  34 rows  (GF3: 10 ERGODIC, 12 PLUS, 12 MINUS)
repo_snapshots:  1133 rows
aptos_snapshots:    28 rows (alice, bob, A–Z)
multisig_probes:     5 rows (all healthy)
mnx_snapshots:       0 rows (unavailable)
```

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balance Survey — 28 Addresses (alice, bob, A–Z)

**Result:** All 28 addresses returned HTTP 404 `resource_not_found` from Aptos mainnet fullnode at ledger version 6,152,766,293 (epoch 16445, block height 881,810,174).

The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource does not exist at any address. Hamming swarm wallets are unfunded / not yet on-chain.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | resource_not_found |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | resource_not_found |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a | resource_not_found |
| B | 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 | resource_not_found |
| C | 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e | resource_not_found |
| D | 0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1 | resource_not_found |
| E–Z | (see aptos_snapshots table) | resource_not_found |

### Multisig Contract Probes — 5 Pairs

All 5 multisig accounts are **live and healthy**. All require **2 signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — Vercel deployment requires visitor password authentication. No market data accessible without bypass token.

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

## Key Highlights

- **kubeflow/kubeflow**: 15,769 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,169 stars — most active repo (pushed 2026-07-07)
- **kubeflow/spark-operator**: 3,132 stars — K8s operator for Spark
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK with Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text GAN in TensorFlow
- **plurigrid/gorj**: 1029 open issues — this repo, very active
- **5 multisig contracts**: All live, all 2-of-N — swarm infrastructure intact
- **28 Hamming wallets**: All unfunded on Aptos mainnet at epoch 16445
