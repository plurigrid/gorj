# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-03  
**GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social-graph | 19 |
| DJedamski | social-graph | 6 |
| wasita | social-graph | 11 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |
| AustinCStone | social-graph | 40 |

**Total repo snapshots inserted this run:** 323  
**Total world_increments in DB:** 346  
**Total repo_snapshots in DB:** 1267

### Notable Repos

**plurigrid** (most active, pushed 2026-07-03):
- `plurigrid/gorj` — Clojure, 0★ (this repo, active today)
- `plurigrid/asi` — HTML, 28★ (pushed 2026-06-29)
- `plurigrid/eirobri` — Clojure, pushed 2026-06-30

**kubeflow** (active ML infra):
- `kubeflow/pipelines` — Python, 4167★ (pushed 2026-07-02)
- `kubeflow/mpi-operator` — Go, 529★
- `kubeflow/hub` — Go, 174★

**TeglonLabs**:
- `TeglonLabs/jank-crane` — C++, GF3 convergence maps + loopify pass spec (pushed 2026-06-08)
- `TeglonLabs/mathpix-gem` — Ruby, 2★, mathematical OCR

**bmorphism** (Gay.jl pushed 2026-07-03):
- `bmorphism/Gay.jl` — Julia, pushed 2026-07-03
- `bmorphism/satreadout` — HTML, pushed 2026-06-20

**Social graph highlights**:
- `migalkin/NodePiece` — Python, 144★ (compositional KG representations, ICLR'22)
- `migalkin/StarE` — Python, 89★ (hyper-relational KG, EMNLP 2020)
- `AustinCStone/TextGAN` — Python, 92★ (text generation GAN in TensorFlow)
- `wasita/wasita.github.io` — Svelte, pushed 2026-07-02

### DuckDB Schema

```
world_increments  — GF3-indexed event log
repo_snapshots    — full repo metadata per snapshot
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-07-03)

Queried Aptos mainnet via `https://fullnode.mainnet.aptoslabs.com/v1/`

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…cb13 | 0.0 |
| C | 0x38b9…535e | 0.0 |
| D | 0xf776…fdd1 | 0.0 |
| E | 0xdc1d…8d36 | 0.0 |
| F | 0x18a1…cf71 | 0.0 |
| G | 0x69a3…f32 | 0.0 |
| H | 0xce67…300f | 0.0 |
| I | 0x070f…1fc9 | 0.0 |
| J | 0x4d96…f54 | 0.0 |
| K | 0xa732…5dc4 | 0.0 |
| L | 0x7c2e…ba9 | 0.0 |
| M | 0x6fed…2e9 | 0.0 |
| N | 0xe7dd…1b2c | 0.0 |
| O | 0x7325…89d | 0.0 |
| P | 0x6218…948 | 0.0 |
| Q | 0xac40…89a9 | 0.0 |
| R | 0x7ce6…6e10 | 0.0 |
| S | 0xb875…386 | 0.0 |
| T | 0x3578…588 | 0.0 |
| U | 0x7586…956 | 0.0 |
| V | 0xb59d…2c3 | 0.0 |
| W | 0x5f32…7b0 | 0.0 |
| X | 0xa95c…047d | 0.0 |
| Y | 0xd8e3…44c4 | 0.0 |
| Z | 0x7af0…97c | 0.0 |

> All 28 addresses returned 0 APT — `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource not found (accounts unfunded or CoinStore not initialized on mainnet).

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…003 | 2 | ✅ |
| A-G | 0xf56c…096 | 2 | ✅ |
| Y-Z | 0xd3ff…883 | 2 | ✅ |
| S-T | 0x3b1c…883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

All 5 multisig contracts healthy, each requiring 2-of-N signatures (`0x1::multisig_account::num_signatures_required` returned `["2"]`).

### MNX Markets

`https://testnet.mnx.fi` returned **HTTP 401 — Vercel Authentication Required**.  
Market data unavailable without visitor password or bypass token. `mnx_snapshots` table empty.

---

## DuckDB Table Counts

```
DB: packages/world-increment/ducklake/world-increments.duckdb

Table             | Rows
------------------+------
world_increments  |  346
repo_snapshots    | 1267
aptos_snapshots   |   28
multisig_probes   |    5
mnx_snapshots     |    0
```

GF(3) distribution across 323 new increments (ids 24–346):
- ERGODIC (trit=0, #d3869b): ids ≡ 0 mod 3
- PLUS (trit=1, #b8bb26):    ids ≡ 1 mod 3
- MINUS (trit=-1, #cc241d):  ids ≡ 2 mod 3
