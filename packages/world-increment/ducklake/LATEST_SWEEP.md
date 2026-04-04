# World-Increment Sweep — 2026-04-04

## Sweep Metadata
- **Date:** 2026-04-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 56 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA (no public API) |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## GitHub Social Graph — Repo Counts

| Source | Type | Total Repos | Top Repo (stars) |
|--------|------|-------------|------------------|
| plurigrid | org | 95 | asi (15★) |
| kubeflow | org | ~180 | pipelines (4112★) |
| TeglonLabs | org | 3 | mathpix-gem (2★) |
| bmorphism | user | 22+ | ocaml-mcp-sdk (60★) |
| zubyul | user | 44 | gay-world (1★) |
| migalkin | user | 19 | NodePiece (143★) |
| DJedamski | user | 6 | Kaggle (1★) |
| wasita | user | 9 | magic-garden (1★) |
| kristinezheng | user | 6 | (0★) |
| M1shaaa | user | 8 | (0★) |
| AustinCStone | user | 40 | TextGAN (92★) |

---

## Top Repos by Source

### plurigrid (95 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| asi | HTML | 15 | 2026-03-30 |
| asi-skills | Julia | 3 | 2026-04-04 |
| zig-syrup | Zig | 2 | 2026-04-04 |
| horse | TeX | 1 | 2026-04-04 |
| gorj | Clojure | 0 | 2026-04-04 |

### kubeflow (~180 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| pipelines | Python | 4112 | 2026-03-28 |
| spark-operator | Python | 3110 | 2026-03-27 |
| trainer | Go | 2068 | 2026-03-26 |
| mcp-apache-spark-history-server | Python | 144 | 2026-03-28 |
| kfctl | Go | 183 | 2023-08-15 |

### bmorphism
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| ocaml-mcp-sdk | OCaml | 60 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| shitcoin | HTML | 5 | 2026-03-09 |
| open-location-code-zig | Zig | 3 | 2025-12-30 |
| aella | Rascal | 1 | 2026-02-01 |

### zubyul
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| gay-world | Python | 1 | 2026-03-26 |
| zubyul.github.io | CSS | 1 | 2026-01-27 |
| Gay.jl | Julia | 0 | 2026-03-28 |
| plurigrid-site | Svelte | 0 | 2026-02-04 |
| tilelang-kernels | Python | 0 | 2026-03-16 |

### migalkin
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| NodePiece | Python | 143 | 2022-02-02 |
| StarE | Python | 88 | 2023-12-01 |
| kgcourse2021 | HTML | 25 | 2025-08-04 |
| NBFNet_mlx | Python | 10 | 2024-03-02 |

### AustinCStone
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| TextGAN | Python | 92 | 2016-10-04 |
| StructureFromMotion | Python | 1 | 2018-06-10 |
| EpsteinSearch | Python | 0 | 2026-02-11 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 addresses)

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26 addrs) | various | 0.0 each |

**Total APT across swarm: 0.00 APT**

> All 28 addresses show zero balance — uninitialized/empty accounts on Aptos mainnet.

---

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |

**All 5 multisig contracts healthy. All require 2-of-n signatures.**

---

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — `https://testnet.mnx.fi/api/markets` returns a Next.js SPA shell with no public JSON API endpoint. Market data is loaded client-side; no server-side JSON routes exposed.

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
- **kubeflow/pipelines**: 4,112★ — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,110★ — Kubernetes operator for Apache Spark
- **AustinCStone/TextGAN**: 92★ — GAN for text generation (TensorFlow, 2016)
- **migalkin/NodePiece**: 143★ — parameter-efficient KG representations
- **bmorphism/ocaml-mcp-sdk**: 60★ — OCaml MCP SDK using Jane Street's oxcaml_effect
- **plurigrid/asi**: 15★ — topological chemputer (most starred plurigrid repo)
- **plurigrid/gorj**: This repo — forj + Rama + GF(3) trit coloring (86 open issues!)
- **Hamming swarm**: All 28 APT addresses show 0 balance; all 5 multisigs are 2-of-n healthy
