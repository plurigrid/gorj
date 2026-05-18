# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-05-03T (UTC)
**Branch:** world-increment/sweep-2026-05-03
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| # | Source | Type | GF(3) Trit | GF(3) Color | Hex |
|---|--------|------|-----------|-------------|-----|
| 1 | plurigrid | org | +1 (PLUS) | #b8bb26 | yellow-green |
| 2 | kubeflow | org | -1 (MINUS) | #cc241d | red |
| 3 | TeglonLabs | org | 0 (ERGODIC) | #d3869b | rose |
| 4 | bmorphism | user | +1 (PLUS) | #b8bb26 | yellow-green |
| 5 | zubyul | user | -1 (MINUS) | #cc241d | red |
| 6 | migalkin | user | 0 (ERGODIC) | #d3869b | rose |
| 7 | DJedamski | user | +1 (PLUS) | #b8bb26 | yellow-green |
| 8 | wasita | user | -1 (MINUS) | #cc241d | red |
| 9 | kristinezheng | user | 0 (ERGODIC) | #d3869b | rose |
| 10 | M1shaaa | user | +1 (PLUS) | #b8bb26 | yellow-green |
| 11 | AustinCStone | user | -1 (MINUS) | #cc241d | red |

### Repository Snapshot
**Total unique repos captured:** 561

| Source | Unique Repos |
|--------|-------------|
| plurigrid | 167 |
| bmorphism | 113 |
| TeglonLabs | 53 |
| kubeflow | 48 |
| AustinCStone | 43 |
| wasita | 31 |
| zubyul | 31 |
| migalkin | 30 |
| kristinezheng | 18 |
| M1shaaa | 16 |
| DJedamski | 11 |

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,617 | — |
| kubeflow/pipelines | 4,131 | Python |
| kubeflow/spark-operator | 3,122 | Python |
| kubeflow/trainer | 2,095 | Go |
| kubeflow/katib | 1,681 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| migalkin/NodePiece | 143 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |

### Language Distribution (top 12)
| Language | Unique Repos |
|----------|-------------|
| Python | 89 |
| TypeScript | 24 |
| JavaScript | 24 |
| Rust | 22 |
| HTML | 21 |
| Go | 19 |
| Jupyter Notebook | 15 |
| Clojure | 13 |
| R | 8 |
| Jsonnet | 8 |
| Julia | 8 |
| TeX | 6 |

### Notable Observations
- **bmorphism** social graph center: MCP-server ecosystem (babashka, say, anti-bullshit, penrose, nats, manifold, marginalia, slowtime, penumbra), Gay.jl color work, Zig tooling (nanoclj-zig, zig-syrup, open-location-code-zig), OCaml (ocaml-mcp-sdk: 60 stars)
- **zubyul** graph: world-builders (gay-world, cascade-world, hue-world, quantum-telephone), TileLang GPU kernels, Gay.jl fork, chromatic VRF
- **TeglonLabs**: topoi (Python), mathpix-gem (Ruby, 2 stars), monad-mcp-server, coin-flip-mcp (2 forks)
- **migalkin**: KG research (NodePiece 143 stars, StarE 89 stars), kgcourse2021 (25 stars), NBFNet_mlx
- Events API: bmorphism and zubyul event streams not publicly visible (rate-limited or private)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~5104274887.

**Result: All 28 addresses returned `resource_not_found`.**

The `CoinStore<AptosCoin>` resource was not registered for any of the Hamming swarm addresses. This indicates either:
1. Addresses have not registered/initialized an APT coin store on mainnet
2. Addresses hold assets through fungible assets v2 (not legacy CoinStore)
3. Addresses are test/dev addresses not funded on mainnet

| World | Address (truncated) | Balance APT |
|-------|---------------------|------------|
| alice | 0xc793ac...c7b | NULL |
| bob | 0x0a3c00...d5d | NULL |
| A–Z | (26 addresses) | NULL (all) |

### Multisig Contract Probes

Probed via `0x1::multisig_account::num_signatures_required` view function.

**All 5 multisig contracts are HEALTHY — require 2 signatures.**

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4f4...03 | 2 | YES |
| A-G | 0xf56c4a...96 | 2 | YES |
| Y-Z | 0xd3ffe1...83 | 2 | YES |
| S-T | 0x3b1c3a...83 | 2 | YES |
| V-W | 0x40fad7...6d | 2 | YES |

All pairs require 2-of-N threshold signatures. Contract state is consistent across the swarm.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi/api/markets` and `/api/tickers` return the Next.js SPA shell (HTML), not JSON. No REST API endpoint is publicly accessible without a session/auth token. **MNX market data: unavailable (SPA only, no public REST endpoints found).**

---

## DuckDB Schema Summary

```
world-increments.duckdb
├── world_increments     — GF(3) color-coded sweep events per source (11 sources)
├── repo_snapshots       — Full repo metadata (name, lang, stars, forks, issues, pushed_at)
├── aptos_snapshots      — Hamming swarm wallet balance readings (28 addresses, all NULL)
├── multisig_probes      — Multisig threshold probes (5 pairs, all 2-of-N healthy)
└── mnx_snapshots        — MNX market tickers (empty — SPA, no REST API)
```

### GF(3) Color Chain Legend
- **trit=0 ERGODIC** `#d3869b` (rose) — id%3==0
- **trit=+1 PLUS** `#b8bb26` (yellow-green) — id%3==1
- **trit=-1 MINUS** `#cc241d` (red) — id%3==2

---
*Generated by world-increment-sweep + hamming-swarm-snapshot agent — 2026-05-03*

---

## PREVIOUS SWEEP BELOW (2026-04-12)

## Sweep Metadata
- **Date:** 2026-04-12
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 471 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

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
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
