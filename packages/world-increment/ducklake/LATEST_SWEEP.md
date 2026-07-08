# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-08

## Sweep Metadata
- **Date:** 2026-07-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 347 |
| Total Repo Snapshots | 1,268 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Healthy | 5/5 |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 115 |
| +1 | `#b8bb26` | PLUS | 116 |
| -1 | `#cc241d` | MINUS | 116 |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 49 | 102,058 |
| plurigrid | org | 103 | 162 |
| bmorphism | user | 105 | 509 |
| TeglonLabs | org | 5 | 14 |
| zubyul | user | 49 | 40 |
| AustinCStone | social | 40 | 309 |
| migalkin | social | 19 | 830 |
| wasita | social | 11 | 7 |
| M1shaaa | social | 8 | 0 |
| kristinezheng | social | 5 | 0 |
| DJedamski | social | 6 | 15 |
| **TOTAL** | | **400** | **104,000** |

### Top Repos by Source

#### plurigrid (103 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 1 | 2026-07-08 |
| asi | HTML | 30 | 2026-06-29 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| asi-skills | Julia | 3 | 2026-04-26 |

#### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,769 | 2026-07-06 |
| pipelines | Python | 4,169 | 2026-07-08 |
| spark-operator | Python | 3,134 | 2026-07-02 |
| trainer | Go | 2,132 | 2026-07-08 |
| katib | Python | 1,690 | 2026-07-08 |

#### bmorphism (105 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-07-08 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JS | 23 | 2026-01-16 |
| shitcoin | Python | 5 | 2026-04-08 |

#### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2022-02-02 |
| StarE | Python | 89 | 2023-12-01 |
| kgcourse2021 | HTML | 25 | 2025-08-04 |
| NBFNet_mlx | Python | 10 | 2024-03-02 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-07-08)

All 28 Hamming-swarm wallets probed on Aptos mainnet via fullnode.mainnet.aptoslabs.com.

**Result:** All wallets show 0 APT balance. Accounts exist on-chain but hold no coin at this snapshot time.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I–Z | various | 0.0 each |

### Multisig Contract Probes

All 5 contracts queried via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

**5/5 multisig contracts healthy** — all require exactly 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — testnet.mnx.fi returns HTTP 401 (Vercel deployment protection, visitor password required). No market data extractable without credentials.

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
- **kubeflow/kubeflow**: 15,769 stars — flagship ML platform for Kubernetes (pushed 2026-07-06)
- **kubeflow/pipelines**: 4,169 stars — ML Pipelines for Kubeflow (active 2026-07-08)
- **kubeflow/spark-operator**: 3,134 stars — Kubernetes Spark operator (active 2026-07-02)
- **kubeflow/trainer**: 2,132 stars — Distributed AI training (active 2026-07-08)
- **migalkin/NodePiece**: 144 stars — compositional KG representations
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs (2016)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP (Jane Street oxcaml_effect)
- **plurigrid/gorj**: This repo — forj + Rama topology nREPL routing + GF(3) coloring (pushed today)
- **plurigrid/asi**: 30 stars — topological chemputer, most-starred plurigrid repo
- **All 5 multisig contracts**: HEALTHY — 2-of-N quorum intact across A-B, A-G, Y-Z, S-T, V-W pairs
- **28 Hamming-swarm wallets**: 0 APT each — swarm quiescent at this snapshot
