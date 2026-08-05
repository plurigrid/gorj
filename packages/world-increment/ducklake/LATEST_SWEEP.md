# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-05  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.5 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 11 World Increments

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | plurigrid | org | 18 | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | 18 | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | 18 | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | 13 | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 7 | 0 | `#d3869b` | **ERGODIC** |
| 7  | wasita | user | 7 | +1 | `#b8bb26` | **PLUS** |
| 8  | DJedamski | user | 6 | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | 9 | -1 | `#cc241d` | **MINUS** |

**GF(3) chain:** `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Sources by Total Stars

| Source | Repos | Total Stars | Top Repo |
|--------|-------|-------------|----------|
| kubeflow | 18 | 32,517 | kubeflow/kubeflow 15,805★ |
| migalkin | 7 | 278 | NodePiece 144★ |
| bmorphism | 18 | 198 | risc0-cosmwasm-example 23★ |
| AustinCStone | 9 | 107 | TextGAN 92★ |
| plurigrid | 18 | 104 | plurigrid/asi 59★ |
| wasita | 7 | 4 | magic-garden 2★ |
| DJedamski | 6 | 3 | School/Kaggle 1★ each |
| TeglonLabs | 5 | 2 | mathpix-gem 2★ |
| zubyul | 13 | 1 | gay-world 1★ |
| kristinezheng | 5 | 0 | — |
| M1shaaa | 8 | 0 | — |
| **TOTAL** | **114** | **33,214** | |

### Notable Activity (2026-08-05)

**plurigrid (active today):**
- `gorj` — Clojure, 1655 open issues, pushed today (this repo!)
- `eirobri` — EiRoBri replay world, pushed today
- `place` — TeX, 15 open issues
- `asi` — 59★ topological chemputer

**kubeflow (very active today):**
- `trainer` — 2171★ Distributed AI Training/LLM Fine-Tuning
- `pipelines` — 4177★ ML Pipelines  
- `sdk` — 133★ Universal Python SDK
- `kubeflow` — 15,805★ flagship platform

**bmorphism (recent):**
- `Gay.jl` — 188 open issues, updated today
- `ocaml-mcp-sdk` — 61★ OCaml MCP SDK
- `nanoclj-zig` / `oxgame` — updated 2026-05

**wasita (updated today):**
- `xoxowasita-analysis` — Python, pushed 2026-08-05T15:35

**TeglonLabs:**
- `jank-crane` — C++, GF3 convergence maps, pushed 2026-06-08

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets probed)

All wallets queried via `fullnode.mainnet.aptoslabs.com/v1`. The `CoinStore<AptosCoin>` resource was **not found** for any of the 28 addresses. These addresses have not registered APT via the legacy CoinStore model — they may use the Fungible Asset model, be uninitialized, or exist only in the Hamming swarm configuration.

| Worlds | Addresses | Balance APT |
|--------|-----------|-------------|
| alice, bob | 2 legacy-named | — (no CoinStore) |
| A through Z | 26 Hamming-indexed | — (no CoinStore) |

### Multisig Probes (5 pairs)

Probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

**All 5 multisig contracts healthy — all require 2-of-2 signatures.**

### MNX Markets

`testnet.mnx.fi` serves an SPA with no accessible REST API. All endpoints returned HTML:
- `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets` — all **SPA HTML only**

Status: **UNAVAILABLE** — no market data extractable from this probe.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
-- 11 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
-- 114 rows

aptos_snapshots(timestamp, world, address, balance_apt)
-- 28 rows (all NULL balance)

multisig_probes(timestamp, pair, address, sigs_required, healthy)
-- 5 rows (all healthy, 2-of-2)

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
-- 0 rows (SPA, unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS  
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
