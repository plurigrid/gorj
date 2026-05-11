# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-11T10:10:09Z  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.1 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all sweeps) | 35 |
| Total Repo Snapshots (all sweeps) | 1,075 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 / 5 healthy |
| MNX Markets | unavailable (SPA) |

---

## GF(3) Color Chain — 2026-05-11 Sweep

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | 1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | 1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (social_graph) | user_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (social_graph) | user_snapshot | 1 | `#b8bb26` | **PLUS** |
| 8  | wasita (social_graph) | user_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (social_graph) | user_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (social_graph) | user_snapshot | 1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (social_graph) | user_snapshot | -1 | `#cc241d` | **MINUS** |
| 13 | 2026-05-11 (social_graph_sweep) | social_repo_snapshot | 1 | `#b8bb26` | **PLUS** |

GF(3) trit chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → PLUS`

---

## JOB 1: GitHub Social Graph Sweep

### Top Repos by Stars (2026-05-11 Snapshot)

| Repo | Language | Stars | Forks | Open Issues | Pushed |
|------|----------|-------|-------|-------------|--------|
| kubeflow/kubeflow | — | 15,630 | 2,648 | 2 | 2026-05-07 |
| kubeflow/pipelines | Python | 4,138 | 1,991 | 499 | 2026-05-08 |
| kubeflow/spark-operator | Python | 3,125 | 1,480 | 91 | 2026-05-08 |
| kubeflow/trainer | Go | 2,096 | 947 | 112 | 2026-05-09 |
| kubeflow/katib | Python | 1,683 | 522 | 124 | 2026-05-09 |
| kubeflow/examples | Jsonnet | 1,462 | 756 | 111 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,016 | 1,062 | 28 | 2026-05-08 |
| kubeflow/arena | Go | 810 | 190 | 57 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 5 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 21 | 0 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 16 | 1 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 0 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 1 | 2026-01-16 |
| plurigrid/asi | HTML | 21 | 5 | 4 | 2026-04-26 |
| bmorphism/Gay.jl | Julia | 1 | 0 | 188 | 2026-05-11 |
| plurigrid/gorj | Clojure | 0 | 0 | 146 | 2026-05-11 |

### Most Active Right Now (pushed 2026-05-11)

- `plurigrid/gorj` — Clojure — **146 open issues** — forj + Rama + GF(3) coloring
- `bmorphism/Gay.jl` — Julia — **188 open issues** — Wide-gamut color sampling
- `kubeflow/notebooks` — **189 open issues** — Kubeflow Notebooks

### Sources Snapshotted

| Source | Type | Distinct Repos | Cumulative Stars |
|--------|------|----------------|-----------------|
| kubeflow | org | 48 | 100,886 |
| migalkin | social_graph | 19 | 832 |
| bmorphism | user | 60+ | 418 |
| AustinCStone | social_graph | 40 | 319 |
| plurigrid | org | 60+ | 132 |
| zubyul | user | 18 (public) | 37 |
| DJedamski | social_graph | 6 | 16 |
| TeglonLabs | org | 4 | 14 |
| wasita | social_graph | 11 | 9 |
| M1shaaa | social_graph | 8 | 0 |
| kristinezheng | social_graph | 6 | 0 |

*Cumulative stars = sum across all snapshots (multiple sweeps included).*

### TeglonLabs (4 repos)

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| topoi | Python | 0 | 2025-01-24 |
| monad-mcp-server | — | 0 | 2025-05-14 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-05-11)

All 28 wallets queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
All return balance = **0 APT** (accounts exist on-chain; APT CoinStore resources are empty or uninitialized).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…4cc7b | 0.0 |
| bob | 0x0a3c…512d5d | 0.0 |
| A–Z (26 addresses) | — | 0.0 each |

### Multisig Probes — 5/5 HEALTHY

All 5 contracts respond to `0x1::multisig_account::num_signatures_required` and require 2 signatures.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | HEALTHY |
| A-G | 0xf56c…0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff…b883 | 2 | HEALTHY |
| S-T | 0x3b1c…7883 | 2 | HEALTHY |
| V-W | 0x40fa…eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` serves a Next.js SPA; neither `/api/markets` nor `/api/v1/markets` returned JSON. HTML page loads (~318 KB) but market data requires client-side JS execution. `mnx_snapshots` table has 0 rows.

---

## DuckDB Schema

```sql
world_increments  — 35 rows  (GF3 color-tagged sweep events, multi-sweep accumulation)
repo_snapshots    — 1,075 rows (11 sources: 3 orgs + 2 users + 6 social_graph)
aptos_snapshots   — 28 rows  (Hamming swarm: alice, bob, A–Z)
multisig_probes   — 5 rows   (all 2-of-N, all healthy)
mnx_snapshots     — 0 rows   (SPA, no REST API available)
```

## GF(3) Assignment Rule

```
id mod 3 == 0  →  trit=0,  color=#d3869b (rose),  name=ERGODIC
id mod 3 == 1  →  trit=1,  color=#b8bb26 (green), name=PLUS
id mod 3 == 2  →  trit=-1, color=#cc241d (red),   name=MINUS
```

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent — 2026-05-11*
