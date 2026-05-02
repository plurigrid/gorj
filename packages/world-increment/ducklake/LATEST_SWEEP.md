# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-02  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GF(3) Color Chain — This Sweep

```
id=13  PLUS     #b8bb26  github_sweep     plurigrid/org
id=14  MINUS    #cc241d  aptos_snapshot   aptos-mainnet
id=15  ERGODIC  #d3869b  sweep_complete   world-increment
```

GF(3) assignment: `id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d`

---

## JOB 1: GitHub Social Graph Sweep

> Note: GitHub REST API was rate-limited (unauthenticated IP quota exhausted).  
> All repo data collected via GitHub MCP search — full metadata available.

### Sources Swept

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 50 |
| kubeflow | org | 30 |
| bmorphism | user | 28 |
| zubyul | user | 20 |
| AustinCStone | user | 20 |
| migalkin | user | 19 |
| wasita | user | 10 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 6 |
| TeglonLabs | org | 4 |
| **TOTAL (new)** | | **201** |

**Cumulative repo_snapshots:** 1,145  
**Total world_increments:** 26

### Notable Repos (by stars)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,615 | — | 2026-05-02 |
| kubeflow/pipelines | 4,130 | Python | 2026-05-01 |
| kubeflow/spark-operator | 3,121 | Python | 2026-04-28 |
| kubeflow/trainer | 2,095 | Go | 2026-05-01 |
| kubeflow/katib | 1,681 | Python | 2026-04-27 |
| kubeflow/examples | 1,460 | Jsonnet | 2026-04-14 |
| kubeflow/manifests | 1,013 | YAML | 2026-04-30 |
| kubeflow/arena | 810 | Go | 2026-04-28 |
| kubeflow/kale | 684 | Python | 2026-04-29 |
| kubeflow/mpi-operator | 524 | Go | 2026-04-15 |
| migalkin/NodePiece | 143 | Python | 2026-03-02 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-28 |
| kubeflow/mcp-apache-spark-history-server | 163 | Python | 2026-04-30 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-02-05 |
| plurigrid/asi | 17 | HTML | 2026-04-26 |
| plurigrid/gorj | 0 ⚡ 45 issues | Clojure | 2026-05-02 |

### Social Graph Activity Highlights

- **bmorphism/magic-world-org** pushed 2026-05-01 (Python, MLX); boxxy (Move) pushed 2026-04-30
- **zubyul/voice-observatory** new 2026-04-23; ghostel-emacs-worlds 2026-04-24
- **plurigrid/gorj** 45 open issues, pushed today — active forj/GF(3) development
- **kubeflow/sdk** new repo (2025-04-23, 111★) — Universal Python SDK for AI on Kubernetes
- **kubeflow/mcp-server** added 2026-04-08 — AI-assisted Kubeflow development
- **TeglonLabs/mathpix-gem** (Ruby, 2★) — math OCR; coin-flip-mcp (JS, 2 forks)
- **migalkin:** StarE KG paper active (89★); NBFNet_mlx 10★ (Apple Silicon MLX)
- **wasita:** wasita.github.io pushed 2026-04-28; magic-garden bot active (2★)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 addresses unfunded — CoinStore resource not found on mainnet.**

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26 addrs) | 0x8699...→ 0x7af0... | 0.0 each |

**Total swarm APT: 0.0 / 28 addresses unfunded**

### Multisig Contract Probes

`POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**5/5 multisig contracts healthy — 2-of-N threshold confirmed on all pairs.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `/api/markets`, `/api/v1/markets`, `/api/tickers` all unreachable.  
SPA returns no extractable market data. No rows inserted into `mnx_snapshots`.

---

## DuckDB State (post-sweep)

| Table | Row Count |
|-------|-----------|
| world_increments | 26 |
| repo_snapshots | 1,145 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

## Full GF(3) Color Chain (ids 1–15)

| ID | Source | Event | GF3 | Color | Name |
|----|--------|-------|-----|-------|------|
| 1 | plurigrid | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 2 | kubeflow | repo_snapshot | -1 | `#cc241d` | MINUS |
| 3 | TeglonLabs | repo_snapshot | 0 | `#d3869b` | ERGODIC |
| 4 | bmorphism | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 5 | zubyul | repo_snapshot | -1 | `#cc241d` | MINUS |
| 6 | migalkin | repo_snapshot | 0 | `#d3869b` | ERGODIC |
| 7 | DJedamski | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 8 | wasita | repo_snapshot | -1 | `#cc241d` | MINUS |
| 9 | kristinezheng | repo_snapshot | 0 | `#d3869b` | ERGODIC |
| 10 | M1shaaa | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 11 | AustinCStone | repo_sweep | -1 | `#cc241d` | MINUS |
| 12 | bmorphism | sweep_complete | 0 | `#d3869b` | ERGODIC |
| **13** | **plurigrid** | **github_sweep** | **+1** | **`#b8bb26`** | **PLUS** |
| **14** | **aptos-mainnet** | **aptos_snapshot** | **-1** | **`#cc241d`** | **MINUS** |
| **15** | **world-increment** | **sweep_complete** | **0** | **`#d3869b`** | **ERGODIC** |
