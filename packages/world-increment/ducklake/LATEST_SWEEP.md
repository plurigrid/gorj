# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-13

## Sweep Metadata
- **Date:** 2026-07-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this sweep) | 129 |
| Sources Covered | 3 orgs + 8 users |
| GF(3) ERGODIC (#d3869b) | 42 |
| GF(3) PLUS (#b8bb26) | 44 |
| GF(3) MINUS (#cc241d) | 43 |

### Sources Swept

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 50 |
| kubeflow | org | 15 (top by activity) |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 (top public) |
| zubyul | user | 10 (top public) |
| migalkin | social graph | 4 |
| DJedamski | social graph | 2 |
| wasita | social graph | 3 |
| kristinezheng | social graph | 2 |
| M1shaaa | social graph | 2 |
| AustinCStone | social graph | 3 |

### Top Repos by Source

#### plurigrid (50 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-07 |
| place | TeX | 1 | 2026-06-27 |
| eirobri | Clojure | 0 | 2026-05-19 |
| shrimp | — | 0 | 2026-07-03 |

#### kubeflow (top 15 active 2026-07-13)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,773 | 2026-07-13 |
| pipelines | Python | 4,165 | 2026-07-13 |
| spark-operator | Python | 3,135 | 2026-07-13 |
| trainer | Go | 2,138 | 2026-07-13 |
| katib | Python | 1,690 | 2026-07-11 |
| mcp-server | Python | 26 | 2026-07-13 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |

#### bmorphism (top public)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 22 |
| Gay.jl | Julia | 2 |
| whale | MATLAB | 2 |
| shitcoin | Python | 5 |

#### zubyul (top public)
| Repo | Language | Stars |
|------|----------|-------|
| gay-world | Python | 1 |
| jonikas_lab_data_analysis_misc | Jupyter Notebook | 2 |
| Nikolova_lab_data_analysis | R | 2 |
| lastfm_analysis_copy | Jupyter Notebook | 1 |

#### Social graph highlights
| User | Repo | Stars |
|------|------|-------|
| migalkin | NodePiece | 144 |
| migalkin | StarE | 89 |
| AustinCStone | TextGAN | 92 |
| AustinCStone | StereoVisionMRF | 11 |
| wasita | magic-garden | 2 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-13)

All 28 hamming-swarm addresses queried against `fullnode.mainnet.aptoslabs.com`:

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | 26 addresses | 0.0 each |

**Interpretation:** All CoinStore resources returned 0 APT or resource-not-found. Swarm is dormant on mainnet — no APT flows detected across all 28 worlds.

### Multisig Contract Probes (5/5 HEALTHY)

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✅ HEALTHY |

All multisig accounts live on Aptos mainnet with canonical 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` behind Vercel deployment protection. Authentication required; no market data accessible.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights (2026-07-13 vs 2026-04-12 prior sweep)
- **kubeflow/kubeflow**: 15,773 stars (+208 since April)
- **kubeflow/mcp-server**: NEW — 26 ⭐ MCP Server for AI-Assisted Development
- **plurigrid/asi**: 30 stars (+14 since April)
- **bmorphism/ocaml-mcp-sdk**: 61 stars (+1)
- **bmorphism/anti-bullshit-mcp-server**: active 2026-07-12, 22 ⭐
- **kubeflow/docs-agent**: NEW (2025-07-19) — 39 ⭐ Kubeflow Documentation AI Agent
- **bmorphism/satreadout**: newest repo (2026-06-10) — Lean 4.28 saturating readout
- **zubyul/tilelang-kernels**: TileLang GPU kernels for GF(3) trit classification on NVIDIA GB10 Blackwell
- **All 5 multisig pairs**: 2-of-N threshold, all HEALTHY on Aptos mainnet
