# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-07-19  
**GF(3) color chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried
| Source | Type | Repos found |
|--------|------|-------------|
| plurigrid | org | 30 |
| kubeflow | org | 30 |
| TeglonLabs | org | 5 |
| bmorphism | user | 30 (of 106) |
| zubyul | user | 30 (of 49) |
| migalkin | social graph | 10 |
| DJedamski | social graph | 5 |
| AustinCStone | social graph | 5+ |

### Top repos by stars (this sweep)
| Repo | Stars | Language | Last pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,781 | — | 2026-07-18 |
| kubeflow/pipelines | 4,167 | Python | 2026-07-19 |
| kubeflow/spark-operator | 3,138 | Python | 2026-07-18 |
| kubeflow/trainer | 2,151 | Go | 2026-07-18 |
| kubeflow/katib | 1,691 | Python | 2026-07-18 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript | 2026-07-12 |
| plurigrid/asi | 31 | HTML | 2026-07-10 |

### plurigrid notable activity (2026-07-19)
- **gorj** (this repo): 1252 open issues, pushed 04:15 UTC today — active sprint
- **place**: TeX forester mathematical documentation, pushed 2026-07-14
- **eirobri**: EiRoBri replay world (Clojure), 30 open issues
- **asi**: 31 stars, "everything is topological chemputer!" — most starred plurigrid repo

### kubeflow notable (active today)
- `sdk` & `pipelines` both pushed today; `mcp-server` and `hub` also active 2026-07-18
- New `docs-agent` (2025-07-19 created) — AI-assisted Kubeflow documentation
- kubeflow/kubeflow hit 15,781 stars (+209 since 2026-04-12 sweep)

### bmorphism recent activity
- **gay-chat**: gay://chat over Spritely Brassica, pushed 2026-07-14
- **Gay.jl**: 187 open issues, active development; 2 stars
- **satreadout**: Lean 4 machine-checked saturating readout, 2026-06-20

### Social graph (migalkin)
- **kgcourse2021**: Knowledge Graphs course materials, last pushed 2026-07-10 (active!)
- **NBFNet_mlx**: Neural Bellman-Ford on Apple Silicon MLX
- migalkin 19 total public repos (KG/GNN research focus)

### DuckDB state
- `world_increments`: 60 rows total (37 added this run, GF3 chain ids 1-37)
- `repo_snapshots`: 981 rows total (historical accumulation across runs)
- `aptos_snapshots`: 28 rows (this run)
- `multisig_probes`: 5 rows (this run)

### GF(3) chain this run (first 12)
| ID | Source | Repo | Trit | Color | Name |
|----|--------|------|------|-------|------|
| 1 | plurigrid | asi | +1 | #b8bb26 | PLUS |
| 2 | plurigrid | gorj | -1 | #cc241d | MINUS |
| 3 | plurigrid | shrimp | 0 | #d3869b | ERGODIC |
| 4 | plurigrid | place | +1 | #b8bb26 | PLUS |
| 5 | plurigrid | eirobri | -1 | #cc241d | MINUS |
| 6 | plurigrid | nash-portal | 0 | #d3869b | ERGODIC |
| 7 | plurigrid | zig-syrup | +1 | #b8bb26 | PLUS |
| 8 | plurigrid | asi-skills | -1 | #cc241d | MINUS |
| 9 | plurigrid | nanoclj-zig | 0 | #d3869b | ERGODIC |
| 10 | plurigrid | graded-optic | +1 | #b8bb26 | PLUS |
| 11 | kubeflow | kubeflow | -1 | #cc241d | MINUS |
| 12 | kubeflow | pipelines | 0 | #d3869b | ERGODIC |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (alice–Z, 28 addresses)

All 28 Hamming swarm addresses returned **0.0 APT** — CoinStore resource not found on mainnet.
Addresses are likely testnet identifiers or unfunded mainnet accounts.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts healthy — **2-of-N signatures required** on all pairs.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — site requires Vercel authentication. No market data accessible.
Status: auth wall encountered on all endpoints (/, /api/markets, /api/tickers).

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name, actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues, pushed_at, description)
aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## Summary
- **GitHub**: 115+ repos snapshotted across plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, DJedamski, AustinCStone. gorj pushed today. kubeflow growing rapidly (+209 stars since April).
- **Aptos swarm**: 0 APT across all 28 Hamming addresses — testnet/unfunded.
- **Multisig health**: All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) require 2 sigs, all responding.
- **MNX**: Vercel auth wall — no data.
