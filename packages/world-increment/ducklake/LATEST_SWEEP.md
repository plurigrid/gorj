# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-28T08:26 UTC  
**Branch:** `world-increment/sweep-2026-04-28-0826`  
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Total Repos |
|--------|------|-------------|
| plurigrid | Org | 100 |
| kubeflow | Org | 47 |
| TeglonLabs | Org | 4 |
| bmorphism | User | 101 |
| zubyul | User | 49 |
| migalkin | Social graph | 19 |
| DJedamski | Social graph | 6 |
| wasita | Social graph | 10 |
| kristinezheng | Social graph | 6 |
| M1shaaa | Social graph | 8 |
| AustinCStone | Social graph | 40 |

### Notable Activity (pushed within 48h of sweep)

| Repo | Lang | Stars | Pushed |
|------|------|-------|--------|
| kubeflow/trainer | Go | 2094 | 2026-04-28 |
| kubeflow/pipelines | Python | 4127 | 2026-04-28 |
| kubeflow/mcp-apache-spark-history-server | Python | 154 | 2026-04-28 |
| plurigrid/zig-syrup | Zig | 2 | 2026-04-26 |
| plurigrid/gorj | Clojure | 0 | 2026-04-28 |
| plurigrid/asi-skills | Julia | 3 | 2026-04-26 |
| bmorphism/Gay.jl | Julia | 1 | 2026-04-28 |
| wasita/wasita.github.io | Svelte | 1 | 2026-04-28 |
| M1shaaa/M1shaaa | — | 0 | 2026-04-28 |

### Top Repos by Stars

| Repo | Stars | Lang |
|------|-------|------|
| kubeflow/kubeflow | 15609 | — |
| kubeflow/pipelines | 4127 | Python |
| kubeflow/spark-operator | 3120 | Python |
| kubeflow/trainer | 2094 | Go |
| kubeflow/katib | 1681 | Python |
| kubeflow/examples | 1460 | Jsonnet |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |
| migalkin/NodePiece | 143 | Python |
| migalkin/StarE | 89 | Python |

### GF(3) Trit Distribution (this sweep — 37 new increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 19 |
| 1 | #b8bb26 | PLUS | 21 |
| -1 | #cc241d | MINUS | 20 |

GF(3) chain: `PLUS → MINUS → ERGODIC → …` cycling deterministically by increment id mod 3.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-28)

> Note: CoinStore resource absent (FA migration); balances retrieved via `0x1::coin::balance` view function.

| World | APT Balance | Address (prefix) |
|-------|-------------|-----------------|
| alice | 0.43643352 | 0xc793ace... |
| bob | **12.65700700** | 0x0a3c00c... |
| A | 0.05176700 | 0x8699edc... |
| B | 0.03625600 | 0x3f892eb... |
| C | 0.01018500 | 0x38b99e6... |
| D | 0.01162900 | 0xf776562... |
| E | 0.00937200 | 0xdc1d9d5... |
| **F** | **1.96051600** | 0x18a14b5... |
| G | 0.00068100 | 0x69a394c... |
| H | 0.00168100 | 0xce67c32... |
| I | 0.00068100 | 0x070fe5d... |
| **J** | **1.89509300** | 0x4d964db... |
| K | 0.16196100 | 0xa732040... |
| **L** | **1.92726900** | 0x7c2eaea... |
| M | 0.11228500 | 0x6fed37a... |
| N | 0.10612100 | 0xe7dde6d... |
| O | 0.21013600 | 0x73252b6... |
| P | 0.14013600 | 0x6218792... |
| Q | 0.10324000 | 0xac40fa5... |
| R | 0.09021700 | 0x7ce605c... |
| S | 0.09178800 | 0xb875301... |
| T | 0.07371300 | 0x35781dc... |
| U | 0.05577300 | 0x75860da... |
| V | 0.04883299 | 0xb59dd81... |
| W | 0.04070500 | 0x5f32aef... |
| X | 0.04257700 | 0xa95cbbd... |
| Y | 0.04444900 | 0xd8e3284... |
| Z | 0.02426800 | 0x7af0ef6... |

**Total swarm APT:** 20.34477251 APT  
**Largest holder:** bob (12.66 APT)  
**Active nodes (>1 APT):** bob, F, J, L  

### Multisig Contract Probes

All 5 probed multisig accounts are **healthy** (2-of-2 threshold):

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ healthy |
| A-G | 0xf56c4a1c... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✓ healthy |
| V-W | 0x40fad7b4... | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

Status: **SPA only** — Next.js frontend, no public REST API endpoints accessible (`/api/markets`, `/api/v1/markets` both return HTML shell). Market data unavailable for this snapshot.

---

## DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 60 |
| repo_snapshots | 981 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable marker) |

Database: `packages/world-increment/ducklake/world-increments.duckdb`

---

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
