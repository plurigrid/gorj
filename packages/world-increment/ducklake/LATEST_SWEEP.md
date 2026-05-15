# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-15

## Sweep Metadata
- **Date:** 2026-05-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 182 (this sweep) |
| Total Repo Snapshots | 182 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy, 2-of-N) |
| MNX Markets | unavailable (Next.js SPA) |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 37 |
| bmorphism | user | 33 |
| kubeflow | org | 30 |
| zubyul | user (social graph) | 22 |
| migalkin | user (social graph) | 10 |
| wasita | user (social graph) | 10 |
| AustinCStone | user (social graph) | 10 |
| kristinezheng | user (social graph) | 8 |
| M1shaaa | user (social graph) | 8 |
| DJedamski | user (social graph) | 8 |
| TeglonLabs | org | 6 |
| **TOTAL** | | **182** |

### GF(3) Color Chain (first 12 increments)
| ID | Repo | GF3 Trit | Color | Name |
|----|------|-----------|-------|------|
| 1  | plurigrid/gorj | 0 | `#d3869b` | **ERGODIC** |
| 2  | plurigrid/zig-syrup | 1 | `#b8bb26` | **PLUS** |
| 3  | plurigrid/asi | -1 | `#cc241d` | **MINUS** |
| 4  | plurigrid/nash-portal | 0 | `#d3869b` | **ERGODIC** |
| 5  | plurigrid/horse | 1 | `#b8bb26` | **PLUS** |
| 6  | plurigrid/asi-skills | -1 | `#cc241d` | **MINUS** |
| 7  | plurigrid/bci-blue-share | 0 | `#d3869b` | **ERGODIC** |
| 8  | plurigrid/nanoclj-zig | 1 | `#b8bb26` | **PLUS** |
| 9  | plurigrid/spi-race | -1 | `#cc241d` | **MINUS** |
| 10 | plurigrid/reafference | 0 | `#d3869b` | **ERGODIC** |
| 11 | plurigrid/ontology | 1 | `#b8bb26` | **PLUS** |
| 12 | plurigrid/Plurigraph | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...` (182 total)

---

## Top Repos by Stars (this sweep)

| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/kubeflow | — | 15,632 | 2026-05-07 |
| kubeflow/pipelines | Python | 4,140 | 2026-05-15 |
| kubeflow/spark-operator | Python | 3,125 | 2026-05-15 |
| kubeflow/trainer | Go | 2,098 | 2026-05-15 |
| kubeflow/katib | Python | 1,682 | 2026-05-09 |
| kubeflow/examples | Jsonnet | 1,463 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,017 | 2026-05-13 |
| kubeflow/arena | Go | 810 | 2026-05-07 |
| kubeflow/kale | Python | 687 | 2026-05-15 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| plurigrid/vcg-auction | Rust | 7 | 2023-03-16 |
| plurigrid/ontology | JavaScript | 8 | 2025-05-27 |

### Hottest today (pushed 2026-05-15)
- `kubeflow/mlflow-integration`, `kubeflow/pipelines`, `kubeflow/kale`, `kubeflow/spark-operator`
- `kubeflow/notebooks`, `kubeflow/hub`, `kubeflow/trainer`
- `bmorphism/Gay.jl` (Julia, 188 open issues — heavy active development)
- `plurigrid/gorj` (Clojure, 205 open issues — **this repo**)
- `wasita/vocoder`, `wasita/wm-cv`, `kristinezheng/kristinezheng.github.io`

### Social Graph Highlights
- **migalkin**: Active KG researcher, NodePiece (144★ ICLR'22) updated this week
- **wasita**: Svelte developer, wm-cv and vocoder both active today
- **zubyul**: NASH TUI (Rust), Gay.jl, neuroscience genomics; deeply connected to plurigrid/bmorphism ecosystem
- **bmorphism**: 100 repos, heavy MCP server ecosystem (OCaml, Clojure, JS, Zig, Julia)
- **AustinCStone**: Python ML history, recent bmorf fork activity suggesting participation in Bittensor/bitmind work

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet — 28 Wallet Balances
All wallets returned `resource_not_found` for `CoinStore<AptosCoin>` — accounts not registered for native APT.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793acdec12b4a637... | 0.0 |
| bob | 0x0a3c00c58fdf9020b... | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Health — All 5 HEALTHY
| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df40622... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49... | 2 | ✓ |
| V-W | 0x40fad7b423a843650f... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Site is a Next.js SPA; `/api/markets` and `/api/v1/markets` return HTML shell only. No server-side JSON API found.

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

## DuckDB Table Summary
| Table | Rows |
|-------|------|
| world_increments | 182 |
| repo_snapshots | 182 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (placeholder) |

## Notable Highlights
- **kubeflow/kubeflow**: 15,632 stars — flagship ML platform for Kubernetes (up +67 from last sweep)
- **kubeflow/pipelines**: 4,140 stars — most active today (pushed 2026-05-15)
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22), updated this week
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **bmorphism/Gay.jl**: 188 open issues — heavy active development of wide-gamut GF(3) color sampling
- **plurigrid/gorj**: 205 open issues — this very repo, pushed today
- **All 5 multisig contracts**: healthy, 2-of-N threshold on Aptos mainnet
- **28 hamming wallets**: CoinStore not registered (unfunded for native APT)
