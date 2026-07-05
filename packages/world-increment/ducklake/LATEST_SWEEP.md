# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-05

## Sweep Metadata
- **Date:** 2026-07-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 111 |
| Total Repo Snapshots | 111 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Snapshotted | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy, 2-of-N) |
| MNX Markets | Unavailable (Vercel auth) |

---

## GF(3) Color Chain — 111 Increments (Sample)

| ID | Source | Repo | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | TeglonLabs | jank-crane | +1 | `#b8bb26` | **PLUS** |
| 2  | TeglonLabs | mathpix-gem | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | coin-flip-mcp | 0 | `#d3869b` | **ERGODIC** |
| 4  | TeglonLabs | monad-mcp-server | +1 | `#b8bb26` | **PLUS** |
| 5  | TeglonLabs | topoi | -1 | `#cc241d` | **MINUS** |
| 6  | plurigrid | shrimp | 0 | `#d3869b` | **ERGODIC** |
| 7  | plurigrid | asi | +1 | `#b8bb26` | **PLUS** |
| ... | ... | ... | ... | ... | ... |
| 111 | bmorphism | world | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain repeats: `PLUS → MINUS → ERGODIC → ...` (37 complete cycles over 111 increments)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet — 2026-07-05)

### Wallet Balances via `0x1::primary_fungible_store::balance` (FA method)

| World | APT Balance | Address (truncated) |
|-------|-------------|---------------------|
| alice | 0.43643352 | 0xc793...cc7b |
| bob | **12.657007** | 0x0a3c...2d5d |
| A | 0.051767 | 0x8699...9d7a |
| B | 0.036256 | 0x3f89...b13 |
| C | 0.010185 | 0x38b9...35e |
| D | 0.011629 | 0xf776...dd1 |
| E | 0.009372 | 0xdc1d...d36 |
| F | **1.960516** | 0x18a1...f71 |
| G | 0.000681 | 0x69a3...f32 |
| H | 0.001681 | 0xce67...00f |
| I | 0.000681 | 0x070f...fc9 |
| J | **1.895093** | 0x4d96...f54 |
| K | 0.161961 | 0xa732...dc4 |
| L | **1.927269** | 0x7c2e...ba9 |
| M | 0.112285 | 0x6fed...2e9 |
| N | 0.106121 | 0xe7dd...b2c |
| O | 0.210136 | 0x7325...89d |
| P | 0.140136 | 0x6218...948 |
| Q | 0.103240 | 0xac40...89a9 |
| R | 0.090217 | 0x7ce6...e10 |
| S | 0.091788 | 0xb875...386 |
| T | 0.073713 | 0x3578...588 |
| U | 0.055773 | 0x7586...956 |
| V | 0.048833 | 0xb59d...2c3 |
| W | 0.040705 | 0x5f32...7b0 |
| X | 0.042577 | 0xa95c...47d |
| Y | 0.044449 | 0xd8e3...4c4 |
| Z | 0.024268 | 0x7af0...97c |

**Key observations:** `bob` holds 12.66 APT (highest, 25× alice). `F`, `J`, `L` cluster near 2 APT. `G`, `I` nearly empty (0.0007 APT).

### Multisig Contract Probes (`0x1::multisig_account::num_signatures_required`)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ healthy |
| A-G | 0xf56c...096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✅ healthy |
| S-T | 0x3b1c...883 | 2 | ✅ healthy |
| V-W | 0x40fa...b6d | 2 | ✅ healthy |

All 5 multisig contracts live and returning valid signature threshold.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel deployment protection requires visitor password. No market data accessible.

---

## Top Repos by Source

### plurigrid (103 repos, 100 returned)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | **28** | 2026-06-29 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| StochFlow | Python | 4 | 2024-03-20 |
| gorj | Clojure | 0 | **2026-07-05** (992 issues) |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | **15,764** | 2026-06-18 |
| pipelines | Python | **4,169** | **2026-07-05** |
| spark-operator | Python | **3,132** | 2026-07-02 |
| trainer | Go | **2,129** | 2026-07-03 |
| katib | Python | **1,689** | 2026-07-01 |
| mcp-apache-spark-history-server | Python | 180 | 2026-06-25 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (105 repos, 100 returned)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | **61** | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |
| Gay.jl | Julia | 2 | **2026-07-05** (187 issues) |

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | **144** | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

### AustinCStone (40 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | **92** | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |
| SpectralClustering | Python | 3 | 2021-04-16 |

---

## Repo Counts by Source

| Source | Type | Total Repos | Returned |
|--------|------|-------------|----------|
| plurigrid | org | 103 | 100 |
| bmorphism | user | 105 | 100 |
| kubeflow | org | 49 | 49 |
| zubyul | user | 49 | 49 |
| AustinCStone | user | 40 | 40 |
| migalkin | user | 19 | 19 |
| wasita | user | 11 | 11 |
| M1shaaa | user | 8 | 8 |
| DJedamski | user | 6 | 6 |
| kristinezheng | user | 5 | 5 |
| TeglonLabs | org | 5 | 5 |
| **TOTAL** | | **~400** | **392** |

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

## Notable Highlights — 2026-07-05 Sweep
- **kubeflow/kubeflow**: 15,764 stars (+199 since Apr 12) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,169 stars (+50) — pushed 2026-07-05 (same day as this sweep)
- **plurigrid/asi**: 28 stars (+12) — topological chemputer, significantly growing
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK using Jane Street's oxcaml_effect
- **migalkin/NodePiece**: 144 stars (+1) — compositional representations for large KGs
- **AustinCStone/TextGAN**: 92 stars — text GAN still referenced years later
- **plurigrid/gorj**: 992 open issues (this repo, very active)
- **bmorphism/Gay.jl**: 187 open issues, pushed 2026-07-05 — active development
- **bob (Aptos)**: 12.66 APT — highest balance in the swarm
- **F, J, L (Aptos)**: ~2 APT each — cluster of medium holders
- **All 5 multisigs**: healthy with 2-of-N threshold
- **MNX testnet**: Vercel auth wall — data unavailable this run
