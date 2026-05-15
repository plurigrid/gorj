# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-05-15  
**GF(3) Color Chain:** ERGODIC #d3869b (29) · PLUS #b8bb26 (31) · MINUS #cc241d (30)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 repos (top 17 indexed) |
| kubeflow | org | 48 repos (top 14 indexed) |
| TeglonLabs | org | 4 repos |
| bmorphism | user | 101 repos (top 14 indexed) |
| zubyul | user | 49 repos (top 8 indexed) |
| social graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) | network | 90 repos (top 10 indexed) |

### Top Repos by Stars (this sweep)
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,631 | — |
| kubeflow/pipelines | 4,140 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,098 | Go |
| kubeflow/katib | 1,682 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 22 | HTML |
| plurigrid/ontology | 8 | JavaScript |

### Recently Active (plurigrid orbit)
- **plurigrid/gorj** — forj + Rama topology nREPL routing + GF(3) gay trit coloring (pushed 2026-05-15)
- **plurigrid/zig-syrup** — OCapN Syrup in Zig (pushed 2026-04-30)
- **bmorphism/Gay.jl** — Wide-gamut color sampling with splittable determinism, 188 open issues (pushed 2026-05-15)
- **zubyul/voice-observatory** — Passive macOS TUI for voice-download pathways (pushed 2026-04-24)
- **TeglonLabs/mathpix-gem** — Math/chem OCR Ruby gem (pushed 2026-01-01)

### DuckDB Tables (cumulative across all sweeps)
```
world_increments: 90 rows
repo_snapshots:  1011 rows
```

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

> Note: CoinStore resource not found via `/v1/accounts/{addr}/resource/0x1::coin::CoinStore` (APT migrated to fungible assets). Balances retrieved via `0x1::coin::balance` view function.

### Wallet Balances (APT)
| World | Balance (APT) | Address |
|-------|--------------|---------|
| bob   | 12.6570 | 0x0a3c00c58fdf9020... |
| F     |  1.9605 | 0x18a14b5b4bec118c... |
| L     |  1.9273 | 0x7c2eaeafad972549... |
| J     |  1.8951 | 0x4d964db8f5383740... |
| alice |  0.4364 | 0xc793acdec12b4a63... |
| K     |  0.1620 | 0xa732040a6b0d5590... |
| O     |  0.2101 | 0x73252b6011a75115... |
| P     |  0.1401 | 0x6218792de4a9bc38... |
| M     |  0.1123 | 0x6fed37a7553ef16b... |
| N     |  0.1061 | 0xe7dde6da0a65f510... |
| Q     |  0.1032 | 0xac40fa50b81b4ca6... |
| S     |  0.0918 | 0xb8753014e4888ea4... |
| R     |  0.0902 | 0x7ce605cc8fda4f8e... |
| T     |  0.0737 | 0x35781dc0e42fef3f... |
| U     |  0.0558 | 0x75860da47565f650... |
| A     |  0.0518 | 0x8699edc0960dd5b9... |
| V     |  0.0488 | 0xb59dd8170321dfab... |
| X     |  0.0426 | 0xa95cbbd116548ac9... |
| Y     |  0.0444 | 0xd8e32848f1dffa81... |
| W     |  0.0407 | 0x5f32aef70f5ba530... |
| B     |  0.0363 | 0x3f892ebe6e45164e... |
| Z     |  0.0243 | 0x7af0ef6e1bd706f4... |
| Y     |  0.0444 | 0xd8e32848f1dffa81... |
| C     |  0.0102 | 0x38b99e63ada9b6fe... |
| D     |  0.0116 | 0xf77656248f64d5dd... |
| E     |  0.0094 | 0xdc1d9d533bac3507... |
| H     |  0.0017 | 0xce67c327a7844e54... |
| G     |  0.0007 | 0x69a394c0b0ac8421... |
| I     |  0.0007 | 0x070fe5d74e4eda30... |

**Total swarm APT:** ~20.56 APT

### Multisig Contract Probes (Aptos Mainnet)
All contracts require 2-of-2 signatures and are healthy:

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428a0c007da... | 2-of-2 | ✅ healthy |
| A-G | 0xf56c4a1c0906214f... | 2-of-2 | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df406... | 2-of-2 | ✅ healthy |
| S-T | 0x3b1c3ae905d44c3a... | 2-of-2 | ✅ healthy |
| V-W | 0x40fad7b423a84365... | 2-of-2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Next.js SPA; `/api/markets` returns HTML shell. No market data extractable without browser JS execution. `mnx_snapshots` table remains empty this sweep.

---

## DuckDB Schema
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

## GF(3) Color Distribution (this sweep's 90 increments)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 29 |
| 1 | #b8bb26 | PLUS | 31 |
| -1 | #cc241d | MINUS | 30 |
