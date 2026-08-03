# World-Increment Sweep — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 35 |
| New World Increments (this sweep) | 12 |
| Total Repo Snapshots (cumulative) | 1045 |
| New Repo Snapshots (this sweep) | 101 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 (A-Z + alice + bob) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable |

---

## GF(3) Color Chain — This Sweep (IDs 13–24)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 24 | gorj (sweep) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source (This Sweep)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 58 | 2026-04-10 |
| gorj | Clojure | 1 | 2026-08-03 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| place | — | 0 | 2026-07 |
| eirobri | — | 0 | 2026-07 |

### kubeflow (50 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15804 | 2026-01-05 |
| pipelines | Python | 4173 | 2026-04-10 |
| spark-operator | Python | 3142 | 2026-04-10 |
| trainer | Go | 2165 | 2026-04-10 |
| katib | Python | 1694 | 2026-04-02 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | — | 0 |
| monad-mcp-server | — | 0 |
| topoi | — | 0 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| Gay.jl | Julia | 2 |
| open-location-code-zig | Zig | 3 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |

### AustinCStone (42 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| byteruckus | — | 0 |
| StereoVisionMRF | Python | 11 |

---

## Repo Counts by Source (This Sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 50 |
| AustinCStone | user | 42 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 12 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| **TOTAL (new)** | | **396** |

---

## Hamming Swarm Snapshot — Aptos Mainnet

### Balance Summary (all 28 addresses: 0.00 APT each)

All derived Hamming swarm addresses have zero APT balance on mainnet.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793acdec12b... | 0.00000000 |
| bob   | 0x0a3c00c58fdf... | 0.00000000 |
| A     | 0x8699edc09600... | 0.00000000 |
| B     | 0x3f892ebe6e45... | 0.00000000 |
| C     | 0x38b99e63ada9... | 0.00000000 |
| D     | 0xf77656248f64... | 0.00000000 |
| E     | 0xdc1d9d533bac... | 0.00000000 |
| F     | 0x18a14b5b4bec... | 0.00000000 |
| G     | 0x69a394c0b0ac... | 0.00000000 |
| H     | 0xce67c327a784... | 0.00000000 |
| I–Z   | (see DuckDB)        | 0.00000000 |

### Multisig Probes (5 pairs, all healthy)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4f428a0c0... | 2 | ✓ |
| A-G  | 0xf56c4a1c0906... | 2 | ✓ |
| Y-Z  | 0xd3ffe1812b2d... | 2 | ✓ |
| S-T  | 0x3b1c3ae905d4... | 2 | ✓ |
| V-W  | 0x40fad7b423a8... | 2 | ✓ |

All 5 multisig contracts are **healthy** (2-of-2 threshold).

### MNX Markets

MNX Markets (`testnet.mnx.fi`) is **unavailable** — SPA with no accessible REST API endpoint.

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
- **kubeflow/kubeflow**: 15,804 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,173 stars — most popular ML pipeline for Kubernetes
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 58 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **TeglonLabs/jank-crane**: New C++ repo (Jank CRANE integration)
- **Increment 24**: ERGODIC — sweep_complete closing the 8th full GF(3) cycle
- **Multisigs**: All 5 probed pairs healthy (2-of-2 threshold on Aptos mainnet)
- **MNX Markets**: Unavailable (SPA, no REST API exposed on testnet.mnx.fi)
