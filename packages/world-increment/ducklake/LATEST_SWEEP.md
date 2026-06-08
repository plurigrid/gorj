# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-08  
**Branch:** world-increment/sweep  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Table

| GF3 ID | Trit | Color | Name | Source | Repos | Stars | Forks | Most Recent Push |
|--------|------|-------|------|--------|-------|-------|-------|-----------------|
| 1 | +1 | `#b8bb26` | PLUS | plurigrid | 100 | 76 | 47 | 2026-06-08 |
| 2 | -1 | `#cc241d` | MINUS | kubeflow | 48 | 34180 | 13523 | 2026-06-08 |
| 3 | 0 | `#d3869b` | ERGODIC | bmorphism | 100 | 247 | 72 | 2026-06-08 |
| 4 | +1 | `#b8bb26` | PLUS | zubyul | 49 | 14 | 2 | 2026-04-24 |
| 5 | -1 | `#cc241d` | MINUS | migalkin | 19 | 280 | 49 | 2025-08-04 |
| 6 | 0 | `#d3869b` | ERGODIC | AustinCStone | 40 | 108 | 38 | 2026-02-11 |
| 7 | +1 | `#b8bb26` | PLUS | wasita | 11 | 5 | 1 | 2026-06-01 |
| 8 | -1 | `#cc241d` | MINUS | TeglonLabs | 5 | 2 | 2 | 2026-06-08 |
| 9 | 0 | `#d3869b` | ERGODIC | DJedamski | 6 | 3 | 1 | 2018-03-07 |
| 10 | +1 | `#b8bb26` | PLUS | kristinezheng | 5 | 0 | 0 | 2026-06-07 |
| 11 | -1 | `#cc241d` | MINUS | M1shaaa | 8 | 0 | 0 | 2026-06-08 |

**Total repos snapshotted: 391**

### Notable Highlights

- **kubeflow/kubeflow**: 15,707 stars — most starred repo in sweep
- **kubeflow/pipelines**: 4,152 stars, 2,006 forks — active ML pipeline infra
- **kubeflow/spark-operator**: 3,126 stars — Kubernetes Spark lifecycle mgmt
- **kubeflow/trainer**: 2,112 stars — distributed AI training on Kubernetes
- **plurigrid/gorj**: 433 open issues — active forj/Rama nREPL routing project
- **bmorphism/Gay.jl**: 189 open issues — wide-gamut GF(3) color sampling
- **TeglonLabs/jank-crane**: pushed 2026-06-08 — crane-jank converged-IR hub
- **M1shaaa/M1shaaa**: pushed 2026-06-08 (same day)
- **kristinezheng/kristinezheng.github.io**: pushed 2026-06-07

### Most Active Today (2026-06-08)
- `kubeflow/dashboard` (TypeScript, 2026-06-08T00:34:15Z)
- `kubeflow/sdk` (Python, 2026-06-08T03:07:18Z)
- `plurigrid/gorj` (Clojure, 2026-06-08T03:14:34Z)
- `TeglonLabs/jank-crane` (C++, 2026-06-08T02:13:17Z)
- `bmorphism/Gay.jl` (Julia, 2026-06-08T00:42:52Z)
- `M1shaaa/M1shaaa` (config, 2026-06-08T03:38:51Z)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

All 28 Hamming swarm addresses queried against Aptos mainnet.  
**Result: All balances are 0.00000000 APT** — wallets exist on-chain (accounts queryable) but hold no APT coin balance at time of snapshot.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...512d | 0.00000000 |
| A–Z | (26 addresses) | 0.00000000 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

**All 5 multisig contracts are healthy with 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is protected by Vercel authentication (password-gated deployment). No public market data accessible without bypass token. Recorded as N/A in `mnx_snapshots` table.

---

## DuckDB Schema

```
world_increments  — 11 rows (one per source, GF3-colored)
repo_snapshots    — 391 rows (full GitHub social graph)
aptos_snapshots   — 28 rows (alice + bob + A-Z balances)
multisig_probes   — 5 rows (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots     — 1 row (unavailable marker)
```

## GF(3) Color Chain

- **ERGODIC** `#d3869b` (trit=0): bmorphism, AustinCStone, DJedamski
- **PLUS** `#b8bb26` (trit=+1): plurigrid, zubyul, wasita, kristinezheng
- **MINUS** `#cc241d` (trit=-1): kubeflow, migalkin, TeglonLabs, M1shaaa
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
