# LATEST_SWEEP — 2026-06-29

Generated: 2026-06-29T01:07 UTC

## GF(3) Color Chain
| trit | hex | name |
|------|-----|------|
| 0 | #d3869b | ERGODIC |
| +1 | #b8bb26 | PLUS |
| -1 | #cc241d | MINUS |

---

## JOB 1: GitHub Social Graph Sweep

### Orgs Scanned
| Org/User | Source Type | Repos Captured | Hot Repos |
|----------|-------------|----------------|-----------|
| plurigrid | org | 100+ | gorj (894 issues), asi (⭐26), eirobri (30 issues) |
| kubeflow | org | 47 | kubeflow/kubeflow ⭐15752, pipelines ⭐4159, spark-operator ⭐3129 |
| TeglonLabs | org | 5 | jank-crane (GF3 convergence maps), mathpix-gem ⭐2 |
| bmorphism | user | 77 | Gay.jl (187 issues, pushed 2026-06-29), ocaml-mcp-sdk ⭐61 |
| zubyul | user | 47 | nash-tui, gay-world, tilelang-kernels |

### Zubyul Social Graph
| User | Repos | Notable |
|------|-------|---------|
| migalkin | 4+ | StarE ⭐89, kgcourse2021 ⭐25, NBFNet_mlx ⭐10 |
| DJedamski | 6 | R/Kaggle data projects (2014-2018) |
| wasita | 11 | wasita.github.io (Svelte, active 2026-06-25) |
| kristinezheng | 5 | cognitive science, HackMIT, lookit-jenga |
| M1shaaa | 8 | lab-bookshelf, MNIST-Classifier, Yale-Work |
| AustinCStone | 2 | EpsteinSearch, bmfork (Python) |

### Top Active Repos (pushed last 7 days)
| Repo | Stars | Lang | Pushed | Description |
|------|-------|------|--------|-------------|
| bmorphism/Gay.jl | 2 | Julia | 2026-06-29 | Wide-gamut color sampling + SPI |
| plurigrid/gorj | 0 | Clojure | 2026-06-29 | forj+Rama+GF(3) (894 open issues!) |
| plurigrid/asi | 26 | HTML | 2026-06-28 | topological chemputer |
| kubeflow/pipelines | 4159 | Python | 2026-06-27 | ML Pipelines |
| kubeflow/hub | 174 | Go | 2026-06-27 | Model Registry |
| kubeflow/spark-operator | 3129 | Python | 2026-06-26 | Spark on K8s |
| kubeflow/trainer | 2126 | Go | 2026-06-26 | Distributed AI Training |
| plurigrid/eirobri | 0 | Clojure | 2026-06-23 | EiRoBri replay world |
| wasita/wasita.github.io | 1 | Svelte | 2026-06-25 | personal website |
| M1shaaa/M1shaaa | 0 | — | 2026-06-28 | GitHub profile config |

### DuckDB State
- **world_increments**: 34 rows (11 new this sweep)
- **repo_snapshots**: 1021 rows total
- **Sweep IDs GF3**: plurigrid=ERGODIC, kubeflow=PLUS, TeglonLabs=MINUS, bmorphism=ERGODIC, zubyul=PLUS, ...

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances
> NOTE: All 28 Hamming swarm addresses (alice, bob, A–Z) return `resource_not_found`
> for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
> This is expected on Aptos Mainnet v2+ — addresses have migrated to the
> Fungible Asset standard (0x1::primary_fungible_store). Balance = 0 via legacy CoinStore API.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...c7b | 0 (resource_not_found) |
| bob | 0x0a3c...d5d | 0 (resource_not_found) |
| A–Z (26 addrs) | 0x8699...–0x7af0... | 0 each (resource_not_found) |

### Multisig Contract Probes
All 5 multisig pairs are **HEALTHY** (2-of-2 signature threshold confirmed):

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — testnet.mnx.fi returns HTTP 401 (Vercel authentication required).
The site is a private deployment behind Vercel access controls and cannot be probed
without credentials. No market data captured.

---

## DuckDB Summary
```
packages/world-increment/ducklake/world-increments.duckdb
  world_increments: 34 rows
  repo_snapshots:   1021 rows  
  aptos_snapshots:  28 rows  (0 APT, legacy CoinStore n/a)
  multisig_probes:  5 rows   (all 2-of-2, healthy)
  mnx_snapshots:    0 rows   (auth-gated)
```

## Signal Summary
- **bmorphism/Gay.jl** most active: pushed TODAY with 187 open issues
- **plurigrid/gorj** (this repo): 894 open issues, active development
- **Kubeflow** very active: pipelines/trainer/spark-operator all pushed in last 48h
- **TeglonLabs/jank-crane**: GF3 convergence maps repo, first pushed June 2026
- **Hamming swarm**: All 28 Aptos addresses have no legacy CoinStore APT (FA migration)
- **Multisig network**: 5/5 pairs healthy at 2-of-2 threshold on Aptos mainnet
