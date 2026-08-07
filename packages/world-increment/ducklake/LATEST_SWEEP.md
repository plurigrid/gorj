# World-Increment Sweep + Hamming Snapshot

**Run date:** 2026-08-07  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Summary

| Source | Type | Repos captured |
|--------|------|---------------|
| plurigrid | org | 50 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin (social) | user | 4 |
| wasita (social) | user | 2 |
| AustinCStone (social) | user | 2 |
| DJedamski (social) | user | 1 |
| M1shaaa (social) | user | 1 |
| kristinezheng (social) | user | 1 |
| **Total** | | **214** |

**world_increments rows:** 214  
**repo_snapshots rows:** 214  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

### Notable repos (most-starred, recently pushed)

| Repo | Stars | Lang | Pushed |
|------|-------|------|--------|
| kubeflow/pipelines | 4181 | Python | 2026-08-07 |
| kubeflow/spark-operator | 3145 | Python | 2026-08-06 |
| kubeflow/trainer | 2173 | Go | 2026-08-07 |
| kubeflow/kale | 699 | Python | 2026-08-05 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2016-09-19 |
| plurigrid/asi | 59 | HTML | 2026-07-10 |
| plurigrid/gorj | 1 | Clojure | 2026-08-07 |
| bmorphism/Gay.jl | 2 | Julia | 2026-08-07 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |

### Active frontier (pushed last 7 days as of 2026-08-07)

- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) (Clojure, 2026-08-07)
- `plurigrid/eirobri` — EiRoBri replay world (Clojure, 2026-08-04)
- `bmorphism/Gay.jl` — Wide-gamut color sampling (Julia, 2026-08-07)
- `kubeflow/trainer` / `kubeflow/pipelines` / `kubeflow/sdk` (all 2026-08-07)
- `wasita/xoxowasita-analysis` (Python, 2026-08-06)

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

Queried 28 addresses (alice, bob, A–Z) via Aptos fullnode mainnet.

**Result:** All 28 addresses returned **0.00000000 APT**.  
These accounts appear unregistered or have zero APT coin stores on mainnet.

| World | Address (truncated) | APT |
|-------|---------------------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| … (C–Z) | … | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts responded and reported **2 signatures required**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All multisigs are **healthy** (2-of-N threshold confirmed on-chain).

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a Next.js SPA. No REST API endpoints are exposed publicly:
- `/api/markets` → 200 HTML (SPA shell)
- `/api/ticker` → 404
- `/api/v2/markets` → 404

**Status: UNAVAILABLE** — market data not extractable without browser execution.

---

## DuckDB Schema

```
world_increments   — 214 rows (GF3-tagged repo snapshot events)
repo_snapshots     — 214 rows (org/user, language, stars, forks, pushed_at)
aptos_snapshots    — 28 rows  (alice/bob/A-Z balances)
multisig_probes    — 5 rows   (pair, address, sigs_required, healthy)
mnx_snapshots      — 1 row    (unavailable)
```
