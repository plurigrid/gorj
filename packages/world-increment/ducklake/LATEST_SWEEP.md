# World-Increment Sweep — 2026-07-19

## Sweep Metadata
- **Date:** 2026-07-19
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 35 |
| Total Repo Snapshots (cumulative) | 1021 |
| Aptos Worlds Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | 401 Unauthorized (unavailable) |

---

## GF(3) Color Chain — New Increments (IDs 13–24)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|----------|-------|------|
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
| 24 | plurigrid/gorj | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC` × 4 cycles (IDs 13–24)

---

## Top Repos by Source (2026-07-19 snapshot)

### plurigrid (103 repos total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 1 | 2026-07-19 (1256 open issues!) |
| place | TeX | 1 | 2026-07-14 |
| eirobri | Clojure | 0 | 2026-07-14 |
| shrimp | — | 0 | 2026-07-03 |
| asi | HTML | 31 ⭐ | 2026-07-10 |

**Notable changes since April**: `asi` stars: 16→31 (+15), `gorj` open issues exploded to 1256

### kubeflow (49 repos total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| notebooks | — | 74 | 2026-07-19 |
| mcp-server | Python | 29 ★ NEW | 2026-07-19 |
| sdk | Python | 126 ★ NEW | 2026-07-19 |
| pipelines | Python | 4167 | 2026-07-19 |
| kubeflow | — | 15781 | 2026-07-10 |
| trainer | Go | 2151 | 2026-07-18 |
| spark-operator | Python | 3139 | 2026-07-17 |
| mcp-apache-spark-history-server | Python | 183 ★ NEW | 2026-07-16 |

**Notable**: kubeflow grew from 47→49 repos; new `mcp-server` and `sdk` repos added; `kubeflow/kubeflow` now 15781 stars (+216)

### TeglonLabs (5 repos — was 53 in April, API now shows 5 public)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| **jank-crane** ★ NEW | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

**Notable**: `jank-crane` is new (C++) — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"

### bmorphism (106 repos total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| **gay-chat** ★ NEW | Scheme | 0 | 2026-07-14 |
| Gay.jl | Julia | 2 | 2026-07-14 (187 open issues) |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| ocaml-mcp-sdk | OCaml | 61 ⭐ | 2026-05-08 |
| penrose-mcp | JavaScript | 9 | 2026-06-24 |

**Notable**: `gay-chat` new — "gay://chat operationalization over Spritely Brassica Chat"; `ocaml-mcp-sdk` up to 61 stars

### zubyul (49 repos total, was 24 in April)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| big-bad-plurigrid-quiz | Emacs Lisp | 0 | 2026-04-09 |
| gay-world | Python | 1 | 2026-04-05 |

**Notable**: Significant repo growth 24→49 (many private repos now visible)

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 ⭐ | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 24 | 2026-07-10 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

### wasita (12 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| wasita.github.io | Svelte | 1 | 2026-07-16 |
| **pnas-typst-template** ★ NEW | — | 0 | 2026-07-16 |
| wm-cv | Svelte | 0 | 2026-07-14 |
| magic-garden | Python | 2 | 2026-04-22 |

### AustinCStone (41 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| **byteruckus** ★ NEW | HTML | 0 | 2026-07-15 |
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 103 |
| bmorphism | user | 106 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 12 |
| TeglonLabs | org | 5 (public) |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| **TOTAL** | | **403** |

---

## JOB 2: Hamming Swarm Snapshot (Aptos)

### Wallet Balances (alice, bob, A–Z)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
This indicates these wallets either have no APT or have not initialized their CoinStore resource.
All recorded as `balance_apt = 0.0` in `aptos_snapshots`.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0 (resource not found) |
| bob | 0x0a3c...12d5 | 0 (resource not found) |
| A–Z | (26 addresses) | 0 (resource not found) |

### Multisig Contracts (all healthy)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

All 5 multisig contracts require exactly 2 signatures. All responding correctly.

### MNX Markets

`https://testnet.mnx.fi/api/markets` → HTTP 401 Unauthorized. Market data unavailable this sweep.

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

---

## Notable Highlights This Sweep

- **TeglonLabs/jank-crane** (NEW, C++): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow" — GF3 convergence maps surfacing in the C++ layer
- **kubeflow/mcp-server** (NEW, Python, 29★): Kubeflow added MCP tooling; **kubeflow/sdk** (126★) for universal Python/K8s AI workloads
- **kubeflow/mcp-apache-spark-history-server** (NEW, 183★): MCP for Spark debugging growing fast
- **bmorphism/gay-chat** (NEW, Scheme): gay://chat protocol over Spritely Brassica — OCapN/Scheme comms layer
- **plurigrid/gorj** open issues: 1256 (this repo!) — very active
- **plurigrid/asi** stars: 16→31 (+15) since April sweep
- **bmorphism/ocaml-mcp-sdk** stars: 60→61 (steady growth)
- **zubyul** repo count: 24→49 (private repos now visible)
- **Hamming swarm**: All 5 multisig contracts alive, 2-of-N threshold, all healthy
- **APT wallets**: All 28 addresses have no CoinStore initialized on Aptos mainnet
