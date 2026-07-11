# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-11

## Sweep Metadata
- **Date:** 2026-07-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 62 |
| Total Repo Snapshots (cumulative) | 983 |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — This Run (62 increments)

Distribution: ERGODIC=20 | PLUS=21 | MINUS=21 — balanced across three trits

### Top Repos by Source (2026-07-11 snapshot)

#### plurigrid org (103 total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | **30** | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-07 |
| ontology | JavaScript | 8 | 2026-05-09 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-05-19 |

#### bmorphism user (105 total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | **61** | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| Gay.jl | Julia | 2 | 2026-06-20 |
| satreadout | HTML | 0 | 2026-06-20 |
| whale | MATLAB | 2 | 2026-04-20 |

#### kubeflow org (49+)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | **15,771** | 2026-07-11 |
| pipelines | Python | 4,169 | 2026-07-11 |
| spark-operator | Python | 3,137 | 2026-07-11 |
| trainer | Go | 2,135 | 2026-07-11 |
| sdk | Python | 124 | 2026-07-11 |
| mcp-server | Python | 20 | 2026-07-10 |

#### migalkin user (19)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | **144** |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |

#### Other social graph
| User/Org | Top Repo | Stars |
|----------|----------|-------|
| wasita | magic-garden | 2 |
| zubyul | gay-world | 1 |
| TeglonLabs | mathpix-gem | 2 |
| AustinCStone | TextGAN | 92 |
| kristinezheng | kristinezheng.github.io | 0 |
| DJedamski | kaggle_ncaa18 | 0 |
| M1shaaa | lab-bookshelf- | 0 |

### Notable Delta Since Last Sweep (2026-04-12)

| Change | Detail |
|--------|--------|
| plurigrid/asi ⭐ 16→30 | +14 stars in ~3 months |
| kubeflow/kubeflow ⭐ 15565→15771 | +206 stars |
| kubeflow/pipelines ⭐ 4119→4169 | +50 stars |
| bmorphism/Gay.jl | 187 open issues (was < 100) |
| plurigrid/gorj | 1120 open issues (was ~0) — dramatic increase |
| kubeflow new: mcp-server | ⭐20 MCP server for AI-Assisted Development |
| kubeflow new: mcp-apache-spark-history-server | ⭐182 |
| TeglonLabs → now only 5 repos (was 53) | Org shrunk significantly |
| bmorphism/satreadout | New: Lean 4.28 machine-checked math |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — All 28 Addresses

**Status: resource_not_found at ledger v6,227,172,408**

The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource is not registered
for any of the 28 Hamming swarm addresses. This could indicate:
1. Addresses are freshly generated and never funded on mainnet
2. APT held via fungible asset store (v2) rather than legacy CoinStore (v1)
3. Addresses are testnet/devnet addresses queried against mainnet

All 28 entries recorded in `aptos_snapshots` with `balance_apt = NULL`.

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | **2-of-2** | ✅ HEALTHY |
| A-G | 0xf56c4a1c... | **2-of-2** | ✅ HEALTHY |
| Y-Z | 0xd3ffe181... | **2-of-2** | ✅ HEALTHY |
| S-T | 0x3b1c3ae9... | **2-of-2** | ✅ HEALTHY |
| V-W | 0x40fad7b4... | **2-of-2** | ✅ HEALTHY |

**All 5 multisig contracts healthy.** Consistent 2-of-2 threshold across all pairs.

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no REST API available**
`/api/markets` returns HTML shell. Data loaded client-side via JavaScript.
No market data extractable without browser execution. `mnx_snapshots` table is empty.

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

## Notable Highlights (2026-07-11)
- **kubeflow/kubeflow**: 15,771 ⭐ — active today (2026-07-11)
- **kubeflow/pipelines**: 4,169 ⭐ — active today
- **plurigrid/asi**: 30 ⭐ (+14 from April) — topological chemputer accelerating
- **bmorphism/ocaml-mcp-sdk**: 61 ⭐ — OCaml SDK for MCP using Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92 ⭐ — GAN text generation, still receiving traffic
- **plurigrid/gorj**: 1120 open issues — this repo is active hub for coordination
- **Multisig Hamming swarm**: 5/5 healthy, all 2-of-2 threshold
- **Aptos wallets**: 28 addresses probed, none funded on mainnet CoinStore v1
