# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-04

## Sweep Metadata
- **Date:** 2026-08-04T05:30Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 10 (top by activity) |
| TeglonLabs | org | 5 |
| bmorphism | user | 6 |
| zubyul | user | 4 |
| migalkin | user | 4 |
| wasita | user | 3 |
| AustinCStone | user | 3 |
| kristinezheng | user | 2 |
| M1shaaa | user | 2 |
| DJedamski | user | 2 |
| **TOTAL** | | **141** |

### GF(3) Color Distribution This Run

```
GF(3) trit=0 ERGODIC  #d3869b  → 47 increments
GF(3) trit=1 PLUS     #b8bb26  → 47 increments
GF(3) trit=-1 MINUS   #cc241d  → 47 increments
```

Chain rule: `id % 3 == 0 → ERGODIC | id % 3 == 1 → PLUS | id % 3 == 2 → MINUS`

### Notable Activity (2026-08-04)

**plurigrid (100 repos, org)**
- `plurigrid/gorj` — Clojure, pushed **2026-08-04** (this repo, active today)
- `plurigrid/eirobri` — Clojure, pushed **2026-08-04** (EiRoBri replay world)
- `plurigrid/place` — TeX, pushed 2026-08-02 (bci.place forester)
- `plurigrid/asi` — HTML, **58 stars** (top plurigrid repo), pushed 2026-07-10
- `plurigrid/zig-syrup` — Zig, pushed 2026-07-28 (OCapN Syrup impl)

**kubeflow (top 10 by activity)**
- `kubeflow/kubeflow` — **15,804 stars**, flagship ML platform for Kubernetes
- `kubeflow/pipelines` — **4,174 stars**, pushed 2026-08-04
- `kubeflow/spark-operator` — **3,143 stars**, pushed 2026-08-04
- `kubeflow/trainer` — 2,165 stars, Distributed AI Training
- `kubeflow/mcp-server` — 31 stars, new MCP integration

**TeglonLabs (5 repos)**
- `TeglonLabs/jank-crane` — C++, crane-jank converged-IR hub with GF(3)

**bmorphism (106 public repos, 6 sampled)**
- `bmorphism/anti-bullshit-mcp-server` — JS, **23 stars**, pushed 2026-08-02
- `bmorphism/ocaml-mcp-sdk` — OCaml, **61 stars**
- `bmorphism/Gay.jl` — Julia, GF(3) color core library, **188 open issues**
- `bmorphism/gay-chat` — Scheme, gay://chat over Spritely Brassica

**zubyul (49 repos, 4 sampled)**
- `zubyul/voice-observatory` — Python, passive macOS TUI, 2026-04-24
- `zubyul/tilelang-kernels` — Python, GPU kernels for GF(3) trit classification

**wasita (13 repos)**
- `wasita/joint-planning-lit` — created **2026-08-04** (brand new today)
- `wasita/wasita.github.io` — Svelte personal site, active 2026-07-21

**migalkin (19 repos)**
- `migalkin/kgcourse2021` — 24 stars, Knowledge Graphs course, updated 2026-07-10
- `migalkin/NodePiece` — **144 stars**, ICLR'22 KG embeddings

**AustinCStone (41 repos)**
- `AustinCStone/TextGAN` — **92 stars**, TensorFlow text GAN
- `AustinCStone/byteruckus` — HTML, created 2026-07-15

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Probed 28 addresses via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| Address Set | Addresses | Non-zero Balances |
|-------------|-----------|------------------|
| alice, bob | 2 | 0 |
| A–M | 13 | 0 |
| N–Z | 13 | 0 |
| **Total** | **28** | **0** |

All 28 Hamming swarm wallets returned 0.0 APT. Accounts either have never received APT or lack an initialized `CoinStore<AptosCoin>` resource on mainnet.

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | `0x0da4f428...987003` | 2 | ✅ HEALTHY |
| A-G | `0xf56c4a1c...c0096` | 2 | ✅ HEALTHY |
| Y-Z | `0xd3ffe181...5b883` | 2 | ✅ HEALTHY |
| S-T | `0x3b1c3ae9...d7883` | 2 | ✅ HEALTHY |
| V-W | `0x40fad7b4...0eb6d` | 2 | ✅ HEALTHY |

All 5 multisig contracts live on Aptos mainnet, all 2-of-2. **No anomalies detected.**

### MNX Markets (testnet.mnx.fi)

Status: **SPA-only — no REST API exposed.** The site is a Next.js single-page app. Endpoints `/api/markets`, `/api/tickers`, and `/api/v1/markets` all return the rendered HTML shell. Market data unavailable this sweep.

---

## DuckDB Table Status

| Table | Rows (total) | This Run |
|-------|-------------|----------|
| world_increments | 164 | 141 new |
| repo_snapshots | 1,085 | 141 new |
| aptos_snapshots | 28 | 28 new |
| multisig_probes | 5 | 5 new |
| mnx_snapshots | 0 | 0 (SPA) |

---

## Key Signals

1. **plurigrid/gorj** pushed today (2026-08-04) — this repo is actively developed
2. **wasita/joint-planning-lit** created today — new repo in the social graph
3. **All 5 multisig contracts healthy** — 2-of-2 sig requirements intact on mainnet
4. **28 Hamming wallets: 0 APT** — swarm wallets hold no APT on mainnet
5. **bmorphism/Gay.jl**: 188 open issues — high backlog, active community
6. **MNX testnet**: SPA-only, machine-readable data unavailable
7. **kubeflow/kubeflow**: 15,804 stars (+239 since April sweep)

## GF(3) Assignment Rule

```
id mod 3 == 0 → trit=0,  color=#d3869b, name=ERGODIC
id mod 3 == 1 → trit=1,  color=#b8bb26, name=PLUS
id mod 3 == 2 → trit=-1, color=#cc241d, name=MINUS
```
