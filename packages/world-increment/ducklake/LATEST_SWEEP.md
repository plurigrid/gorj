# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-19

## Sweep Metadata
- **Date:** 2026-06-19
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (2026-06-19)
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 10 |
| kubeflow | org | 10 |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 |
| zubyul | user | 9 |
| migalkin | user (social graph) | 5 |
| DJedamski | user (social graph) | 1 |
| wasita | user (social graph) | 2 |
| kristinezheng | user (social graph) | 1 |
| M1shaaa | user (social graph) | 1 |
| AustinCStone | user (social graph) | 2 |
| **TOTAL** | | **56** |

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 19 |
| +1 | #b8bb26 | PLUS | 19 |
| -1 | #cc241d | MINUS | 18 |

### Notable Repos by Source

#### plurigrid (most recently pushed 2026-06-19)
| Repo | Language | Stars | Open Issues | Pushed At |
|------|----------|-------|-------------|-----------|
| gorj | Clojure | 0 | 680 | 2026-06-19 |
| place | TeX | 1 | 8 | 2026-06-15 |
| asi | HTML | 26 | 4 | 2026-06-10 |
| eirobri | Clojure | 0 | 29 | 2026-06-03 |
| nash-portal | Rust | 2 | 1 | 2026-05-19 |
| zig-syrup | Zig | 2 | 0 | 2026-04-30 |
| asi-skills | Julia | 3 | 0 | 2026-04-26 |
| nanoclj-zig | Zig | 1 | 20 | 2026-04-25 |
| vivarium | Clojure | 1 | 0 | 2026-04-08 |

#### kubeflow (top by stars, active 2026-06-19)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,736 | 2026-06-18 |
| pipelines | Python | 4,154 | 2026-06-19 |
| spark-operator | Python | 3,127 | 2026-06-18 |
| trainer | Go | 2,117 | 2026-06-19 |
| katib | Python | 1,683 | 2026-06-15 |
| mcp-apache-spark-history-server | Python | 177 | 2026-06-19 |

#### TeglonLabs
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

#### bmorphism (active 2026-06-19)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 1 | 2026-06-19 |
| satreadout | Lean | 0 | 2026-06-15 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| world | Python | 0 | 2026-06-02 |
| oxgame | OCaml | 0 | 2026-05-15 |

#### zubyul
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| nash-tui | Rust | 0 | 2026-04-13 |
| nash-web | Rust | 0 | 2026-04-13 |
| gay-world | Python | 1 | 2026-03-26 |

#### Social Graph (zubyul connections)
| User | Repo | Language | Stars |
|------|------|----------|-------|
| migalkin | NodePiece | Python | 144 |
| migalkin | StarE | Python | 89 |
| migalkin | kgcourse2021 | HTML | 25 |
| migalkin | RWL | Python | 8 |
| wasita | wasita.github.io | Svelte | 1 |
| wasita | magic-garden | Python | 2 |
| AustinCStone | TextGAN | Python | 92 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances — 28 addresses (2026-06-19)
All 28 Hamming swarm addresses (alice, bob, A–Z) report **0.0 APT** balance.
The accounts exist on-chain but hold no native APT in their `0x1::coin::CoinStore`.

| Range | Addresses | Total APT |
|-------|-----------|-----------|
| Named (alice, bob) | 2 | 0.0 |
| A–M | 13 | 0.0 |
| N–Z | 13 | 0.0 |
| **TOTAL** | **28** | **0.0 APT** |

### Multisig Contract Probes — 5 pairs
All 5 multisig contracts respond healthy with **2-of-2 threshold** required.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...4987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — protected by Vercel deployment auth. Neither `/api/markets` nor `/api/v1/markets` return data. No market data captured.

---

## DuckDB Tables This Run
| Table | New Rows |
|-------|----------|
| `world_increments` | 56 |
| `repo_snapshots` | 56 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 (auth blocked) |

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

## Notable Highlights (2026-06-19 vs 2026-04-12)
- **kubeflow/kubeflow**: 15,736 stars (+171 since April sweep)
- **kubeflow/pipelines**: 4,154 stars (+35) — pushed 2026-06-19
- **kubeflow/spark-operator**: 3,127 stars (+16) — pushed 2026-06-19
- **kubeflow/mcp-apache-spark-history-server**: NEW — 177 stars, MCP server for Spark
- **bmorphism/Gay.jl**: 187 open issues (active development)
- **plurigrid/gorj**: 680 open issues (very active)
- **plurigrid/asi**: 26 stars (+10 since April)
- **All 5 Hamming multisigs**: healthy, 2-of-2 threshold
- **All 28 Hamming wallets**: 0.0 APT balance
