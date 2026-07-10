# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 82 (29 new this sweep) |
| Total Repo Snapshots | 1003 (82 new this sweep) |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy 2-of-2) |
| MNX Markets | UNAVAILABLE (Vercel auth wall) |

---

## GF(3) Color Chain — This Sweep (IDs 54–82)

| ID range | Color | Trit | Name |
|----------|-------|------|------|
| 54, 57, 60, 63, 66, 69, 72, 75, 78, 81 | `#d3869b` | 0 | **ERGODIC** |
| 55, 58, 61, 64, 67, 70, 73, 76, 79, 82 | `#b8bb26` | +1 | **PLUS** |
| 56, 59, 62, 65, 68, 71, 74, 77, 80 | `#cc241d` | -1 | **MINUS** |

GF(3) chain continues from prior sweeps: cycle modulo 3 across all 82 increments.

---

## Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All addresses return `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>` —
wallets are registered on-chain but hold no native APT (balance = 0.0 APT each).

Representative addresses:
- alice: `0xc793...cc7b` → 0.0 APT
- bob: `0x0a3c...12d5` → 0.0 APT
- A–Z (26 wallets): all 0.0 APT

### Multisig Contract Probes (5 contracts)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4...7003` | 2 | ✅ HEALTHY |
| A-G | `0xf56c...0096` | 2 | ✅ HEALTHY |
| Y-Z | `0xd3ff...b883` | 2 | ✅ HEALTHY |
| S-T | `0x3b1c...7883` | 2 | ✅ HEALTHY |
| V-W | `0x40fa...eb6d` | 2 | ✅ HEALTHY |

All 5 multisig contracts operational with 2-of-2 threshold.

### MNX Markets (testnet.mnx.fi)

Unavailable — returns Vercel authentication wall. No market data accessible without auth token.

---

---

## Top Repos by Source (2026-07-10 Snapshot)

### plurigrid (103 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-07 |
| gorj | Clojure | 1 | 2026-07-07 |
| nash-portal | Rust | 2 | 2026-05-19 |
| ontology | JavaScript | 8 | 2026-05-09 |
| vcg-auction | Rust | 7 | 2025-12-16 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15770 | 2026-07-09 |
| pipelines | Python | 4169 | 2026-07-09 |
| spark-operator | Python | 3136 | 2026-07-09 |
| trainer | Go | 2134 | 2026-07-09 |
| katib | Python | 1689 | 2026-07-09 |
| mcp-apache-spark-history-server | Python | 182 | 2026-07-07 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |

### bmorphism (105 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| Gay.jl | Julia | 2 | 2026-06-20 |
| open-location-code-zig | Zig | 3 | 2026-03-24 |

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

### AustinCStone (40 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |

---

## Repo Counts by Source (2026-07-10)

| Source | Type | Repos |
|--------|------|-------|
| bmorphism | user | 105 |
| plurigrid | org | 103 |
| zubyul | user | 49 |
| kubeflow | org | 49 |
| AustinCStone | user | 40 |
| migalkin | social graph | 19 |
| wasita | social graph | 11 |
| M1shaaa | social graph | 8 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **400** |

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

## Notable Highlights (2026-07-10)
- **kubeflow/kubeflow**: 15,770 stars (+205 since Apr) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,169 stars (+50) — pushed actively 2026-07-09
- **kubeflow/mcp-apache-spark-history-server**: 182 stars — new MCP tool for Spark debugging (added since Apr)
- **migalkin/NodePiece**: 144 stars (+1) — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 61 stars (+1) — OCaml MCP SDK using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 30 stars (+14 since Apr) — topological chemputer, strong growth
- **plurigrid/gorj**: This repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring (1091 open issues)
- **bmorphism/Gay.jl**: 187 open issues — high-activity color sampling library
- **TeglonLabs/jank-crane**: NEW — crane-jank converged-IR hub with GF3 convergence maps (2026-06-08)
- **Hamming swarm**: All 28 wallets (alice, bob, A–Z) have 0 APT; all 5 multisig contracts 2-of-2 healthy
- **MNX testnet**: auth-walled, data unavailable
